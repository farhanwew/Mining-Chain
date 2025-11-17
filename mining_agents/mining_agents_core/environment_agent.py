from agents import Agent, function_tool
from pydantic import BaseModel, Field
from typing import Literal, List, Optional, Optional
import joblib
import pandas as pd


# ================================
# 1. LOAD MODEL
# ================================
MODEL_WEATHER_PATH = "models/model_weather.pkl"
MODEL_ROAD_PATH = "models/model_road.pkl"

# Load the entire package saved by joblib
weather_package = joblib.load(MODEL_WEATHER_PATH)
road_package = joblib.load(MODEL_ROAD_PATH)

# Extract the actual model from the 'model' key
weather_model = weather_package['model']
road_model = road_package['model']


# ================================
# 2. PROMPT
# ================================
ENVIRONMENT_PROMPT = """
Anda adalah *Environment & Weather Analyst Agent* untuk operasi pertambangan batubara.

Tugas Anda:
1. Merangkum kondisi cuaca, prakiraan hujan, potensi badai, visibilitas, dan kecepatan angin.
2. Menganalisis kondisi jalan tambang (licin, tergenang, operable / tidak operable).
3. Mengidentifikasi risiko operasional yang dapat menunda atau menghentikan kegiatan tambang.
4. Berikan ringkasan sangat singkat dan hanya daftar risiko utama.
5. Lakukan analisis dengan cepat, di bawah 20 detik.

Output harus mengikuti schema yang telah ditentukan.
"""


# ================================
# 3. OUTPUT & INPUT SCHEMAS
# ================================
class WeatherRiskProbability(BaseModel):
    Safe: float
    Caution: float
    High_Risk: float = Field(..., alias="High Risk")

class RoadConditionProbability(BaseModel):
    Operational: float
    Severely_Damaged: float = Field(..., alias="Severely Damaged")
    Closed: float

class EnvironmentAgentOutput(BaseModel):
    weather_risk: Literal["Safe", "Caution", "High Risk"]
    weather_risk_probability: WeatherRiskProbability
    road_condition: Literal["Operational", "Severely Damaged", "Closed"]
    road_condition_probability: RoadConditionProbability
    environment_summary: str

# Define explicit input schemas for the tool function
class WeatherData(BaseModel):
    Date: Optional[str] = None
    Temperature_C: Optional[float] = None
    Humidity_Percent: Optional[float] = Field(None, alias='Humidity_%')
    Rainfall_mm: Optional[float] = None
    Wind_Speed_mps: Optional[float] = None
    Wind_Direction_deg: Optional[float] = None
    Visibility_km: Optional[float] = None
    Pressure_hPa: Optional[float] = None
    Sea_State_Level: Optional[int] = None
    Wave_Height_m: Optional[float] = None
    Tide_Level_m: Optional[float] = None
    Storm_Warning: Optional[int] = None
    Weather_Condition: Optional[str] = None
    Weather_Risk_Level: Optional[str] = None
    class Config:
        extra = 'forbid'

class RoadData(BaseModel):
    Date: Optional[str] = None
    Surface_Type: Optional[str] = None
    Surface_Condition: Optional[str] = None
    Pothole_Density: Optional[float] = None
    Slope_Angle_Degrees: Optional[float] = None
    Traffic_Density: Optional[float] = None
    Flood_Level_m: Optional[float] = None
    Access_Status: Optional[str] = None
    Dust_Level_PPM: Optional[float] = None
    Ground_Vibration_mm_s: Optional[float] = None
    Road_Temperature_C: Optional[float] = None
    Rainfall_mm: Optional[float] = None
    Soil_Moisture_Percent: Optional[float] = Field(None, alias='Soil_Moisture_%')
    Maintenance_Activity: Optional[str] = None
    Accident_Count: Optional[int] = None
    Road_Condition_Status: Optional[str] = None
    class Config:
        extra = 'forbid'


# ================================
# 4. FUNCTION TOOL
# ================================
@function_tool
def predict_environment_risk(weather_data: List[WeatherData], road_data: List[RoadData]) -> EnvironmentAgentOutput:
    """
    Prediksi risiko cuaca dan kondisi jalan tambang.
    """
    weather_data_dicts = [item.model_dump(by_alias=True) for item in weather_data]
    road_data_dicts = [item.model_dump(by_alias=True) for item in road_data]
    
    df_weather = pd.DataFrame(weather_data_dicts)
    df_road = pd.DataFrame(road_data_dicts)

    # --- WEATHER MODEL PREDICTION ---
    weather_feature_columns = [col for col in weather_package['feature_order'] if col in df_weather.columns]
    df_weather_features = df_weather[weather_feature_columns]
    predicted_class_weather = weather_model.predict(df_weather_features)[0]
    probs_weather = weather_model.predict_proba(df_weather_features)[0]
    weather_prob_dict = {cls: prob for cls, prob in zip(weather_model.classes_, probs_weather)}

    # --- ROAD CONDITION MODEL PREDICTION ---
    road_feature_columns = [col for col in road_package['feature_order'] if col in df_road.columns]
    df_road_features = df_road[road_feature_columns]
    predicted_class_road = road_model.predict(df_road_features)[0]
    probs_road = road_model.predict_proba(df_road_features)[0]
    road_prob_dict = {cls: prob for cls, prob in zip(road_model.classes_, probs_road)}

    # --- FINAL OUTPUT ---
    return EnvironmentAgentOutput(
        weather_risk=predicted_class_weather,
        weather_risk_probability=WeatherRiskProbability(**weather_prob_dict),
        road_condition=predicted_class_road,
        road_condition_probability=RoadConditionProbability(**road_prob_dict),
        environment_summary="",
    )


# ================================
# 5. AGENT
# ================================
environment_agent = Agent(
    name="EnvironmentAgent",
    instructions=ENVIRONMENT_PROMPT,
    output_type=EnvironmentAgentOutput,
    tools=[predict_environment_risk],
)
