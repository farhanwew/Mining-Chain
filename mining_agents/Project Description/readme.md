# Latar Belakang

Industri pertambangan batubara pada umumnya selalu menghadapi tantangan operasional di lapangan yang membuat perencanaan produksi dan distribusi kerap meleset dari target, contohnya:
1. Curah hujan tinggi yang dapat menghentikan kegiatan pertambangan di tambang
2. Keterlambatan pengiriman akibat ombak tinggi di pelabuhan
3. Alat berat yang sering bermasalah/rusak
4. Kekurangan operator yang terampil
Penggunaan Artificial Intelligence (AI) dapat menawarkan solusi analisis real-time untuk memantau kondisi lapangan dan merekomendasikan optimasi berbasis data sehingga risiko keterlambatan dan penurunan produksi dapat diminimalkan.

# Latar Belakang Masalah

Industri pertambangan batubara menghadapi banyak tantangan operasional yang kompleks. Variabel di lapangan sering berubah dan sulit diprediksi. Misalnya, ketika hujan deras aktivitas penambangan harus berhenti karena jalan tambang licin. Ombak tinggi membuat kapal tidak bisa bersandar di pelabuhan sehingga pengiriman batubara tertunda.
Di sisi lain, armada alat berat seperti truk dan excavator sering mengalami kerusakan, sementara jumlah operator dan mekanik yang benar-benar kompeten masih terbatas. Kondisi ini membuat perencanaan produksi dan distribusi sering kali tidak berjalan sesuai target. Perusahaan membutuhkan alat bantu yang mampu menganalisis kondisi lapangan secara real-time sekaligus memberikan rekomendasi optimasi.
Kehadiran Artificial Intelligence (AI), khususnya berbasis agentic AI, membuka peluang baru untuk meningkatkan ketahanan operasional tambang. Dengan memanfaatkan data cuaca, kondisi jalan, jadwal peralatan, hingga ketersediaan kapal, AI dapat melakukan simulasi berbagai skenario dan mengusulkan opsi terbaik untuk meminimalkan risiko keterlambatan atau penurunan produksi.

# Ruang Lingkup Proyek & Tujuan Ruang Lingkup:

1. Membangun portal aplikasi (web-based) yang dapat mengubah input berupa kondisi operasional lapangan (misalnya: prakiraan cuaca, status jalan tambang, ketersediaan kapal, jadwal peralatan).
2. Menggunakan model AI dengan pendekatan Agentic AI untuk melakukan simulasi berbagai skenario operasional serta menghasilkan rekomendasi optimisasi produksi dan distribusi batubara.
3. Menyediakan fitur chat box interaktif yang memungkinkan user bertanya langsung terkait kondisi terbaru di lapangan dan opsi optimasi yang diajukan AI.
4. Portal juga menampilkan justifikasi singkat dari setiap rekomendasi, sehingga user dapat memahami alasan di balik keputusan AI.

# Tujuan

1. Memberikan pengalaman praktis dalam merancang sistem berbasis Agentic AI untuk menangani tantangan nyata di industri pertambangan batubara.
2. Mengintegrasikan kemampuan data engineering, data science, dan software development untuk membangun solusi operasional tambang yang adaptif.
3. Menyediakan alat bantu yang dapat meningkatkan efisiensi, mengurangi risiko keterlambatan, dan menekan biaya operasional akibat variabilitas lapangan.
Hasil yang Diharapkan
1. Portal aplikasi prototipe dengan kapabilitas berikut: a. Menerima input kondisi operasional dari user atau sistem (data cuaca, kondisi jalan, status armada, jadwal kapal). b. Menyediakan simulasi skenario produksi dan distribusi berdasarkan data terkini. c. Menghasilkan rekomendasi optimisasi yang dapat langsung ditindaklanjuti di lapangan. d. Menyediakan chat box untuk Q&A interaktif terkait kondisi lapangan dan rekomendasi AI. e. Menampilkan justifikasi setiap rekomendasi dengan visualisasi data pendukung.
2. Dokumentasi proyek yang menjelaskan: a. Arsitektur sistem portal aplikasi. b. Model AI dan pendekatan Agentic AI yang digunakan. c. Dataset (cuaca, peralatan, logistik, produksi) yang dipakai. d. Keterbatasan sistem serta peluang pengembangan lebih lanjut.

# TO-BE Process Flow

 **process optimization** or **digital transformation** using **AI Agents** in a **mining/shipping** context.

Here's a breakdown of the key elements 

---

## ⚙️ TO-BE Process Flow


This image is a clearer, dark-mode version of the same **TO-BE Process Flow** chart that was in your previous image, focusing specifically on the steps involving **AI Agents**, the **Mine Planner**, and the **Shipping Planner**.

The yellow boxes provide more specific details on the sub-tasks for the **AI Agents**.

-----

## ⚙️ TO-BE Process Flow Breakdown (Enhanced Details)



| AI Agent Step | Sub-Tasks (Yellow Box Details) |
| :--- | :--- |
| **1. Summarize external situation and recent changes on internal operational** | \* **Collect information from identified sources** (Weather forecast, production system, etc.)<br>\* **Summarize information** |
| **2. Optimize Plan and provide key justification** | \* **Create narration on the potential impact** (This is the "key justification" provided to the planners for review) |
| **3. Create Summary Email Plan** | \* **Collect review from each persona** (Collect approval/feedback from Planners)<br>\* **Summarizes and create email draft to be sent to responsible parties** (Automate external communication) |

### **II. Planner Roles (Middle & Bottom Rows)**

The planners interact with the AI-generated information and recommendations:

  * **Mine Planner:**

      * **Action 1:** **Review Information and change the mining weekly plan** (Initial planning based on AI summary).
      * **Action 2:** **Review** (Decision on the optimized plan and justification). If **NO**, the process loops back to *Optimize Plan*. If **YES**, it proceeds to the Shipping Planner's review.
      * **Action 3:** **Receive Summary Email Plan** (Receives the final communication).

  * **Shipping Planner:**

      * **Action 1:** **Receive mining plan changes** (Initial planning based on the Mine Planner's update).
      * **Action 2:** **Review** (Decision on the optimized plan and justification). If **NO**, the process loops back to *Optimize Plan*. If **YES**, the process proceeds to the final step.
      * **Action 3:** **Receive Summary Email Plan** (Receives the final communication).

The flow clearly demonstrates a continuous loop where the **AI Agents** continuously refine the plan and justification until both the **Mine Planner** and the **Shipping Planner** approve the optimization.

---

## 🤖 AI Agent Recommendations Example (Illustrative)

This section shows a screenshot of what an AI agent interface might look like, providing a **"Revised Agent Output"** which includes:

- Summary of changes.
- Justification for the changes.
- A generated email ready for the planner to send.

---

# Indikator Penilaian Teknis

1. Prototype aplikasi bisa berfungsi untuk: a. Chat Agent bisa menjawab query dengan menampilkan konteks yang relevant dan menampilkan response yang masih dalam batas normal, yaitu kurang dari 2 detik. b. Dapat menerima input dari user. c. Menghasilkan lebih dari 1 rekomendasi rencana optimasi yang sesuai dengan kriteria. d. Dapat melakukan prioritisasi dari usulan rekomendasi yang ditampilkan. e. Menyediakan justifikasi untuk rekomendasi yang diusulkan.
2. Dokumentasi proyek, yang menjelaskan arsitektur sistem, model AI yang digunakan, dataset yang digunakan, serta limitasi sistem.

# Tambahan rangkuman

- Data dummy data tidak ada, bisa riset dan minta llm buat untuk generate.
- Coba liat tools untuk agentic AI. Buat agent untuk chat. Explore untuk buat agent , integrasikan ke web App ini . Kasih ke agent konteks . Boleh hit llm API
- Buat Dokumentasi lengkap
- Ai summarize situation misal cuaca, jumlah / target produksi pokoknay goals ya dapat
- ada mine planner dia bisa ngedit/ngubah hasil dari AI (ada form) dan lain lain (tbh ga paham) dan dibalikan ke Ai agents (nnti dia optimize) jadi keknya ga semata mata AI agents aja, ada feedback dari manusia ini juga yaitu mine planner. Jadi keknya fitur buatr ngubah /column tersedia
- optimasi sekenario (kemuginana yang bisa dilakukan) dan justification nya tidak hanya satu saja,
- buat summary email diikirm ke user ?
- dan juga ada shipping planer juga . Jadi ada 2 role login sebagan mine planner dan shipping planer , mungkin login beda
- jadi Ketika login sudah ada summary nya untuk tiap masing masing role. yang mana memberikan sesuai porsinya, chatbot ini lebih ke tambahannya saja agar dapat berinteraksi dengan agent , jadi bisa dibaut sebagai penanya jika ada insight yang memang tidak ditampilkan sebelumnya.
- referensi kasus yang mirip / simiilar (capacity plaaning)
- Weekly plan hasilnya