Tentu, saya telah merapikan dan menyusun teks deskripsi dataset Anda ke dalam format yang lebih terstruktur, profesional, dan mudah dibaca menggunakan tabel dan *heading* Markdown.

Informasi ini tampak seperti dokumentasi penting untuk proyek data, sehingga perapian difokuskan pada kejelasan, konsistensi, dan navigasi.

---

## Dokumentasi Dataset Operasional (Logistik & Pertambangan)

Dataset-dataset ini digunakan untuk tujuan prediksi dan analisis risiko yang terintegrasi di seluruh rantai operasional, mulai dari cuaca, kondisi jalan, performa alat berat, hingga jadwal kapal dan logistik.

**Akses Dataset:**
[Link Dataset (Google Drive)](https://drive.google.com/drive/folders/1_BJ2XarTcvJc1KAsoDAgfK1R-wXvAV0o?usp=sharing)

---

## 1. Weather Dataset

**Tujuan Utama:** Prediksi risiko cuaca dan pengaruhnya terhadap operasi, kapal, dan jalan.

| Atribut | Arti / Fungsi Singkat |
| :--- | :--- |
| **Date** | Waktu pencatatan cuaca (*time series*). |
| **Temperature\_C** | Suhu udara — memengaruhi performa mesin dan manusia. |
| **Humidity\_Percent** | Kelembapan udara — memengaruhi kenyamanan & visibilitas. |
| **Rainfall\_mm** | Curah hujan — indikator kondisi jalan & risiko banjir. |
| **Wind\_Speed\_mps** | Kecepatan angin — memengaruhi keamanan kapal. |
| **Wind\_Direction\_deg** | Arah angin — relevan untuk cuaca laut & pelayaran. |
| **Visibility\_km** | Jarak pandang — penting untuk navigasi kapal/kendaraan. |
| **Pressure\_hPa** | Tekanan atmosfer — sinyal cuaca ekstrem / badai. |
| **Sea\_State\_Level** | Skala keadaan laut (0–9) — kondisi gelombang laut. |
| **Wave\_Height\_m** | Tinggi gelombang — risiko keselamatan pelayaran. |
| **Tide\_Level\_m** | Ketinggian pasang surut laut — mempengaruhi pelabuhan. |
| **Storm\_Warning** | Indikator ada/tidaknya badai (0/1). |
| **Weather\_Condition** | Deskripsi cuaca (“Clear”, “Rainy”, “Storm”). |
| **Weather\_Risk\_Level** | Kategori risiko cuaca (“Safe”, “Caution”, “High Risk”). |

---

## 2. Road Condition Dataset

**Tujuan Utama:** Prediksi kondisi akses jalan dan risiko hambatan transportasi/logistik.

| Atribut | Arti / Fungsi Singkat |
| :--- | :--- |
| **Date** | Waktu pencatatan kondisi jalan. |
| **Surface\_Type** | Jenis permukaan jalan (Aspal, Tanah, dll). |
| **Surface\_Condition** | Kondisi permukaan (Kering, Basah, Licin). |
| **Pothole\_Density** | Jumlah lubang jalan — indikasi kerusakan. |
| **Slope\_Angle\_Degrees** | Derajat kemiringan — mempengaruhi beban kendaraan. |
| **Traffic\_Density** | Kepadatan lalu lintas per km. |
| **Flood\_Level\_m** | Kedalaman genangan air di jalan. |
| **Access\_Status** | Status akses (“Safe”, “Closed”, dll). |
| **Dust\_Level\_PPM** | Kadar debu di udara — berdampak pada alat berat. |
| **Ground\_Vibration\_mm\_s** | Getaran tanah — potensi kerusakan area kerja. |
| **Road\_Temperature\_C** | Suhu permukaan jalan. |
| **Rainfall\_mm** | Curah hujan — indikator kondisi jalan basah. |
| **Soil\_Moisture\_%** | Kelembapan tanah — relevan di jalan tanah/lumpur. |
| **Maintenance\_Activity** | Status perbaikan jalan. |
| **Accident\_Count** | Jumlah kecelakaan di lokasi. |
| **Road\_Condition\_Status** | Label akhir kondisi jalan (“Operational”, dll). |

---

## 3. Heavy Equipment Dataset

**Tujuan Utama:** Prediksi kerusakan mesin, efisiensi alat berat, dan *maintenance planning* (Pemeliharaan Prediktif).

| Atribut | Arti / Fungsi Singkat |
| :--- | :--- |
| **Timestamp** | Waktu pengukuran kondisi alat. |
| **Machine\_ID** | Identitas unik alat berat. |
| **Machine\_Type** | Jenis alat (Excavator, Dump Truck, dll). |
| **Engine\_Temperature\_C** | Suhu mesin — indikator *overheating*. |
| **Oil\_Pressure\_Bar** | Tekanan oli — indikator kesehatan mesin. |
| **Fuel\_Level\_Percent** | Sisa bahan bakar (%). |
| **Engine\_RPM** | Kecepatan putaran mesin. |
| **Vibration\_Level\_g** | Getaran alat — deteksi kerusakan komponen. |
| **Hydraulic\_Pressure\_Bar** | Tekanan sistem hidrolik. |
| **Working\_Hours** | Total jam kerja alat — umur operasional. |
| **Maintenance\_Status** | Status perawatan (“Normal”, “Need Service”). |
| **Fault\_Code** | Kode kesalahan sistem. |
| **Operational\_Mode** | Mode kerja alat (Idle, Load, Travel). |
| **Ambient\_Temperature\_C** | Suhu sekitar alat. |
| **Operator\_ID** | ID operator alat. |
| **Gear\_Position** | Posisi gigi transmisi. |
| **Fuel\_Consumption\_L\_h** | Konsumsi bahan bakar per jam. |
| **Torque\_Nm** | Torsi mesin — indikator beban kerja. |
| **Engine\_Load\_Percent** | Beban mesin relatif (%). |
| **Machine\_Failure** | Apakah alat mengalami kerusakan (0/1). |

---

## 4. Vessel Schedule Dataset

**Tujuan Utama:** Prediksi keterlambatan kapal dan efisiensi pelayaran.

| Atribut | Arti / Fungsi Singkat |
| :--- | :--- |
| **Record\_Timestamp** | Waktu pencatatan data kapal. |
| **Vessel\_ID** | Identitas kapal unik. |
| **Route\_Code** | Jalur pelayaran (R1–R5). |
| **Departure\_Time** | Waktu keberangkatan. |
| **Planned\_Arrival\_Time** | Waktu kedatangan terjadwal. |
| **Actual\_Arrival\_Time** | Waktu kedatangan aktual. |
| **Delay\_Minutes** | Selisih keterlambatan (menit). |
| **Cargo\_Type** | Jenis muatan kapal. |
| **Load\_Weight\_Tons** | Berat muatan (ton). |
| **Port\_Condition** | Kondisi pelabuhan (Normal, Padat, Tutup). |
| **Weather\_Impact\_Score** | Pengaruh cuaca terhadap pelayaran (0–1). |
| **Sea\_Condition\_Code** | Kondisi laut (Calm, Rough, Stormy). |
| **Crew\_Availability\_Percent** | Ketersediaan awak kapal (%). |
| **Vessel\_Status** | Status kapal (Sailing, Docked, Delayed). |
| **Fuel\_Consumption\_Tons** | Bahan bakar digunakan (ton). |
| **Engine\_RPM** | Putaran mesin kapal. |
| **Distance\_Traveled\_km** | Jarak tempuh kapal (km). |
| **Average\_Speed\_knots** | Kecepatan rata-rata (knot). |
| **Delay\_Risk** | Risiko keterlambatan (target prediksi). |

---

## 5. Logistics Dataset

**Tujuan Utama:** Prediksi efisiensi pengiriman, penggunaan bahan bakar, dan risiko keterlambatan logistik.

| Atribut | Arti / Fungsi Singkat |
| :--- | :--- |
| **Record\_Timestamp** | Waktu pencatatan data logistik. |
| **Logistics\_ID** | ID unik pengiriman. |
| **Date** | Tanggal pengiriman. |
| **Route\_Code** | Jalur logistik (sinkron dengan kapal). |
| **Origin\_Location** | Lokasi asal (tambang/gudang). |
| **Destination\_Location** | Tujuan pengiriman. |
| **Cargo\_Type** | Jenis muatan. |
| **Cargo\_Weight\_Tons** | Berat muatan (ton). |
| **Transport\_Mode** | Moda transportasi (Truck/Train/Vessel). |
| **Vessel\_ID** | Kapal terkait (jika mode Vessel). |
| **Machine\_ID** | Alat berat yang digunakan untuk *loading/unloading*. |
| **Distance\_km** | Jarak tempuh (km). |
| **Travel\_Time\_hr** | Waktu tempuh rencana (jam). |
| **Actual\_Travel\_Time\_hr** | Waktu tempuh aktual (jam). |
| **Fuel\_Used\_Liters** | Bahan bakar digunakan (liter). |
| **Fuel\_Cost\_USD** | Biaya bahan bakar. |
| **Delivery\_Status** | Status pengiriman (Delivered, Delayed, etc). |
| **Delay\_Cause** | Penyebab keterlambatan (Weather, Mechanical, etc). |
| **CO2\_Emission\_kg** | Emisi karbon transportasi (kg). |
| **Driver\_ID** | Identitas sopir. |
| **Delivery\_Risk\_Level** | Risiko pengiriman (“Low”, “Medium”, “High”). |

---

## 6. Production Dataset

**Tujuan Utama:** Analisis performa tambang dan prediksi produktivitas / risiko operasional.

| Atribut | Arti / Fungsi Singkat |
| :--- | :--- |
| **Record\_Timestamp** | Waktu pencatatan produksi. |
| **Production\_ID** | ID produksi unik. |
| **Date** | Tanggal produksi. |
| **Machine\_ID** | Alat berat yang digunakan. |
| **Shift** | Shift kerja (Morning, Afternoon, Night). |
| **Operator\_ID** | Operator alat. |
| **Material\_Type** | Jenis bahan tambang (Coal, Nickel, Iron Sand). |
| **Working\_Hours** | Lama jam kerja alat per *shift*. |
| **Production\_Tons** | Total hasil produksi (ton). |
| **Fuel\_Consumed\_Liters** | Bahan bakar digunakan (liter). |
| **Downtime\_Minutes** | Durasi gangguan operasional (menit). |
| **Weather\_Condition** | Cuaca saat operasi. |
| **Road\_Condition\_Status** | Kondisi akses jalan ke area produksi. |
| **Equipment\_Efficiency\_Percent** | Efisiensi alat terhadap target (%). |
| **Fuel\_Efficiency\_Tons\_per\_Liter** | Efisiensi bahan bakar per ton hasil. |
| **Incident\_Report** | Ada/tidak insiden keselamatan (0/1). |
| **Maintenance\_Required** | Kebutuhan servis alat (0/1). |
| **CO2\_Emission\_kg** | Emisi karbon dari operasi. |
| **Production\_Risk\_Level** | Risiko produksi (“Low”, “Medium”, “High”). |
| **Production\_Cost\_USD** | Biaya produksi per *shift*. |
| **Revenue\_USD** | Pendapatan dari hasil produksi. |

---

## Kesimpulan Fungsi Keseluruhan

| Dataset | Tujuan Utama / Fungsi Analitik |
| :--- | :--- |
| **Weather** | Prediksi risiko cuaca & dampak ke operasi. |
| **Road** | Prediksi kelayakan akses transportasi/logistik. |
| **Heavy Equipment** | Prediksi kerusakan mesin (*Predictive Maintenance*). |
| **Vessel** | Prediksi keterlambatan kapal & efisiensi pelayaran. |
| **Logistics** | Prediksi efisiensi dan risiko distribusi. |
| **Production** | Prediksi produktivitas, biaya, dan efisiensi energi. |