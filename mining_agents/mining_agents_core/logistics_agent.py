from agents import Agent, function_tool
from pydantic import BaseModel, Field
from typing import Literal, List, Optional, Optional
import joblib
import pandas as pd


# ================================
# 1. LOAD MODEL
# ================================
MODEL_VESSEL_PATH = "models/model_vessel.pkl"
MODEL_LOGISTICS_PATH = "models/model_logistics.pkl"

# Load the entire packages saved by joblib
vessel_package = joblib.load(MODEL_VESSEL_PATH)
logistics_package = joblib.load(MODEL_LOGISTICS_PATH)

# Extract the actual models from the 'model' key
vessel_model = vessel_package['model']
logistics_model = logistics_package['model']


# ================================
# 2. PROMPT
# ================================
LOGISTICS_PROMPT = """
Anda adalah *Logistics & Shipping Analyst Agent* untuk rantai pasok batubara.

Tugas Anda:
1. Menganalisis data jadwal kapal untuk memprediksi potensi keterlambatan (delay).
2. Menganalisis data logistik darat untuk memprediksi risiko pengiriman (delivery risk).
3. Mengidentifikasi constraint logistik yang berpotensi menghambat target pengiriman.
4. Memberikan ringkasan singkat dan hanya daftar risiko utama.
5. Lakukan analisis dengan cepat, di bawah 20 detik.

Output harus mengikuti schema yang telah ditentukan.
"""


# ================================
# 3. OUTPUT & INPUT SCHEMAS
# ================================
class VesselDelayProbability(BaseModel):
    On_Time: float = Field(..., alias="On Time")
    Late: float
    Weather_Delay: float = Field(..., alias="Weather Delay")

class DeliveryRiskProbability(BaseModel):
    Low: float
    Medium: float
    High: float

class LogisticsAgentOutput(BaseModel):
    vessel_delay: Literal["On Time", "Late", "Weather Delay"]
    vessel_delay_probability: VesselDelayProbability
    delivery_risk: Literal["Low", "Medium", "High"]
    delivery_risk_probability: DeliveryRiskProbability
    logistics_summary: str

# Define explicit input schemas for the tool function
class VesselData(BaseModel):
    Record_Timestamp: Optional[str] = None
    Vessel_ID: Optional[str] = None
    Route_Code: Optional[str] = None
    Departure_Time: Optional[str] = None
    Planned_Arrival_Time: Optional[str] = None
    Actual_Arrival_Time: Optional[str] = None
    Delay_Minutes: Optional[float] = None
    Cargo_Type: Optional[str] = None
    Load_Weight_Tons: Optional[float] = None
    Port_Condition: Optional[str] = None
    Weather_Impact_Score: Optional[float] = None
    Sea_Condition_Code: Optional[str] = None
    Crew_Availability_Percent: Optional[float] = Field(None, alias='Crew_Availability_%')
    Vessel_Status: Optional[str] = None
    Fuel_Consumption_Tons: Optional[float] = None
    Engine_RPM: Optional[float] = None
    Distance_Traveled_km: Optional[float] = None
    Average_Speed_knots: Optional[float] = None
    Delay_Risk: Optional[str] = None
    class Config:
        extra = 'forbid'

class LogisticsData(BaseModel):
    Record_Timestamp: Optional[str] = None
    Logistics_ID: Optional[str] = None
    Date: Optional[str] = None
    Route_Code: Optional[str] = None
    Origin_Location: Optional[str] = None
    Destination_Location: Optional[str] = None
    Cargo_Type: Optional[str] = None
    Cargo_Weight_Tons: Optional[float] = None
    Transport_Mode: Optional[str] = None
    Vessel_ID: Optional[str] = None
    Machine_ID: Optional[str] = None
    Distance_km: Optional[float] = None
    Travel_Time_hr: Optional[float] = None
    Actual_Travel_Time_hr: Optional[float] = None
    Fuel_Used_Liters: Optional[float] = None
    Fuel_Cost_USD: Optional[float] = None
    Delivery_Status: Optional[str] = None
    Delay_Cause: Optional[str] = None
    CO2_Emission_kg: Optional[float] = None
    Driver_ID: Optional[str] = None
    Delivery_Risk_Level: Optional[str] = None
    class Config:
        extra = 'forbid'


# ================================
# 4. FUNCTION TOOL
# ================================
@function_tool
def predict_logistics_risk(vessel_data: List[VesselData], logistics_data: List[LogisticsData]) -> LogisticsAgentOutput:
    """
    Prediksi risiko keterlambatan kapal dan risiko pengiriman logistik.
    """
    vessel_data_dicts = [item.model_dump(by_alias=True) for item in vessel_data]
    logistics_data_dicts = [item.model_dump(by_alias=True) for item in logistics_data]

    df_vessel = pd.DataFrame(vessel_data_dicts)
    df_logistics = pd.DataFrame(logistics_data_dicts)

    # --- VESSEL DELAY MODEL PREDICTION ---
    vessel_feature_columns = [col for col in vessel_package['feature_order'] if col in df_vessel.columns]
    df_vessel_features = df_vessel[vessel_feature_columns]
    predicted_class_vessel = vessel_model.predict(df_vessel_features)[0]
    probs_vessel = vessel_model.predict_proba(df_vessel_features)[0]
    vessel_prob_dict = {cls: prob for cls, prob in zip(vessel_model.classes_, probs_vessel)}

    # --- LOGISTICS DELIVERY RISK MODEL PREDICTION ---
    logistics_feature_columns = [col for col in logistics_package['feature_order'] if col in df_logistics.columns]
    df_logistics_features = df_logistics[logistics_feature_columns]
    predicted_class_logistics = logistics_model.predict(df_logistics_features)[0]
    probs_logistics = logistics_model.predict_proba(df_logistics_features)[0]
    logistics_prob_dict = {cls: prob for cls, prob in zip(logistics_model.classes_, probs_logistics)}

    # --- FINAL OUTPUT ---
    return LogisticsAgentOutput(
        vessel_delay=predicted_class_vessel,
        vessel_delay_probability=VesselDelayProbability(**vessel_prob_dict),
        delivery_risk=predicted_class_logistics,
        delivery_risk_probability=DeliveryRiskProbability(**logistics_prob_dict),
        logistics_summary="",
    )


# ================================
# 5. AGENT
# ================================
logistics_agent = Agent(
    name="LogisticsAgent",
    instructions=LOGISTICS_PROMPT,
    output_type=LogisticsAgentOutput,
    tools=[predict_logistics_risk],
)