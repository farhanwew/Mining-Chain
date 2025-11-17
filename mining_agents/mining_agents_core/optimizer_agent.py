from agents import Agent, function_tool
from pydantic import BaseModel, Field
from typing import List, Literal


# ================================
# 1. PROMPT
# ================================
OPTIMIZER_PROMPT = """
Anda adalah *Final Optimization & Weekly Plan Agent* di sebuah perusahaan tambang.

Anda menerima informasi ringkas dari tiga agent spesialis:
1.  **EnvironmentAgent**: Memberikan data risiko cuaca dan kondisi jalan.
2.  **EquipmentAgent**: Memberikan data prediksi kegagalan alat berat.
3.  **LogisticsAgent**: Memberikan data prediksi keterlambatan kapal dan risiko pengiriman.

Tugas Anda:
1.  Sintesis semua informasi yang masuk untuk mendapatkan gambaran operasional yang utuh.
2.  Buat minimal 2 skenario rekomendasi untuk mengoptimalkan produksi dan pengiriman. Fokus pada tindakan konkret yang merespons risiko yang teridentifikasi. Contoh:
    - Penyesuaian jadwal hauling karena jalan licin.
    - Prioritas maintenance untuk alat berat yang berisiko gagal.
    - Perubahan urutan loading kapal untuk menghindari keterlambatan.
3.  Berikan prioritas (High, Medium, Low) untuk setiap tindakan yang direkomendasikan.
4.  Sertakan justifikasi yang komprehensif untuk setiap rekomendasi, dengan mengacu langsung pada data dari agent-agent spesialis.
5.  Rangkum semua rekomendasi menjadi sebuah draf email "Rencana Operasional Mingguan".

Output harus mengikuti schema yang telah ditentukan.
"""


# ================================
# 2. OUTPUT SCHEMA
# ================================
class Recommendation(BaseModel):
    scenario: str = Field(..., description="Deskripsi skenario optimasi atau tindakan yang direkomendasikan.")
    priority: Literal["High", "Medium", "Low"] = Field(..., description="Prioritas tindakan yang direkomendasikan.")
    justification: str = Field(..., description="Justifikasi komprehensif berdasarkan data dari agent lain.")

class OptimizerAgentOutput(BaseModel):
    recommendations: List[Recommendation]
    """Daftar skenario dan rekomendasi yang dioptimalkan."""

    weekly_email_plan: str = Field(..., description="Draf email berisi rangkuman rencana operasional mingguan.")


# ================================
# 3. FUNCTION TOOL
# ================================
@function_tool
def generate_recommendations(
    environment_summary: str,
    equipment_summary: str,
    logistics_summary: str
) -> OptimizerAgentOutput:
    """
    Menggabungkan analisis dari berbagai agent untuk menghasilkan rekomendasi teroptimasi.

    Fungsi ini tidak melakukan kalkulasi, namun berfungsi sebagai struktur data
    untuk memastikan output dari LLM sesuai dengan format yang diharapkan. LLM akan
    mengisi konten berdasarkan prompt dan data input yang diberikan.

    Parameters
    ----------
    environment_summary : str
        Ringkasan dari EnvironmentAgent.
    equipment_summary : str
        Ringkasan dari EquipmentAgent.
    logistics_summary : str
        Ringkasan dari LogisticsAgent.

    Returns
    -------
    OptimizerAgentOutput
        Objek terstruktur yang berisi rekomendasi dan draf email.
    """
    # LLM will generate the actual content for these fields based on the prompt.
    # This function just defines the structure.
    return OptimizerAgentOutput(
        recommendations=[],
        weekly_email_plan=""
    )


# ================================
# 4. AGENT
# ================================
optimizer_agent = Agent(
    name="OptimizerAgent",
    instructions=OPTIMIZER_PROMPT,
    output_type=OptimizerAgentOutput,
)