from pydantic import BaseModel, Field
from typing import Literal, List, Optional, Optional
import joblib
import pandas as pd
from agents import Agent, function_tool

# ================================
# 1. LOAD MODEL
# ================================
MODEL_EQUIPMENT_PATH = "models/model_equipment.pkl"

# Load the entire package saved by joblib
equipment_package = joblib.load(MODEL_EQUIPMENT_PATH)

# Extract the actual model from the 'model' key
equipment_model = equipment_package['model']


# ================================
# 2. PROMPT
# ================================
EQUIPMENT_PROMPT = """
Anda adalah *Equipment Analyst Agent* untuk operasi tambang batubara.

Tugas Anda:
1. Menganalisis data sensor dari alat berat untuk memprediksi potensi kegagalan (failure).
2. Mengidentifikasi risiko berdasarkan data seperti suhu mesin, tekanan oli, dan getaran.
3. Memberikan ringkasan singkat tentang status alat berat dan hanya daftar risiko utama.
4. Lakukan analisis dengan cepat, di bawah 20 detik.

Output harus mengikuti schema yang telah ditentukan.
"""


# ================================
# 3. OUTPUT & INPUT SCHEMAS
# ================================
class FailureProbability(BaseModel):
    Failure: float
    No_Failure: float = Field(..., alias="No Failure")

class EquipmentAgentOutput(BaseModel):
    machine_failure: Literal["Failure", "No Failure"]
    """Prediksi apakah alat berat akan mengalami kegagalan (failure) atau tidak."""

    failure_probability: FailureProbability
    """Probabilitas untuk setiap kelas prediksi (Failure vs. No Failure)."""

    equipment_summary: str
    """Ringkasan status alat berat dan potensi risiko kegagalan berdasarkan data."""

# Define input schema for the tool function
class EquipmentData(BaseModel):
    Timestamp: Optional[str] = None
    Machine_ID: Optional[str] = None
    Machine_Type: Optional[str] = None
    Engine_Temperature_C: Optional[float] = None
    Oil_Pressure_Bar: Optional[float] = None
    Fuel_Level_Percent: Optional[float] = Field(None, alias='Fuel_Level_%')
    Engine_RPM: Optional[float] = None
    Vibration_Level_g: Optional[float] = None
    Hydraulic_Pressure_Bar: Optional[float] = None
    Working_Hours: Optional[float] = None
    Maintenance_Status: Optional[str] = None
    Fault_Code: Optional[str] = None
    Operational_Mode: Optional[str] = None
    Ambient_Temperature_C: Optional[float] = None
    Operator_ID: Optional[str] = None
    Gear_Position: Optional[int] = None
    Fuel_Consumption_L_h: Optional[float] = None
    Torque_Nm: Optional[float] = None
    Engine_Load_Percent: Optional[float] = Field(None, alias='Engine_Load_%')
    Machine_Failure: Optional[int] = None
    class Config:
        extra = 'forbid'


# ================================
# 4. FUNCTION TOOL
# ================================
@function_tool
def predict_equipment_failure(equipment_data: List[EquipmentData]) -> EquipmentAgentOutput:
    """
    Prediksi risiko kegagalan (failure) pada alat berat.

    Parameters
    ----------
    equipment_data : List[EquipmentData]
        Data telemetri dari alat berat.

    Returns
    -------
    EquipmentAgentOutput
        Hasil prediksi kegagalan alat berat, termasuk probabilitasnya.
        Summary akan diisi oleh LLM.
    """
    equipment_data_dicts = [item.model_dump() for item in equipment_data]
    df_equipment = pd.DataFrame(equipment_data_dicts)
    
    # --- EQUIPMENT MODEL PREDICTION ---
    feature_columns = [col for col in equipment_package['feature_order'] if col in df_equipment.columns]
    df_features = df_equipment[feature_columns]

    predicted_class_int = equipment_model.predict(df_features)[0]
    probs = equipment_model.predict_proba(df_features)[0]

    class_labels = {1: "Failure", 0: "No Failure"}
    predicted_class_label = class_labels[predicted_class_int]

    prob_dict = {class_labels[cls]: prob for cls, prob in zip(equipment_model.classes_, probs)}

    # --- FINAL OUTPUT ---
    return EquipmentAgentOutput(
        machine_failure=predicted_class_label,
        failure_probability=FailureProbability(**prob_dict),
        equipment_summary="",  # This will be filled in by the LLM
    )


# ================================
# 5. AGENT
# ================================
equipment_agent = Agent(
    name="EquipmentAgent",
    instructions=EQUIPMENT_PROMPT,
    output_type=EquipmentAgentOutput,
    tools=[predict_equipment_failure],
)