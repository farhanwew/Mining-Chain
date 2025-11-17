Ok saya sekarang mau membuat sebuah project bertema  Mining Value Chain Optimization . untuk projek descripton bisa dilihat di mining-agents/Project\   
  Description/readme.md . Dan sekarang saya berencana untuk implementasi dengan menggunakan OPEN AI AGENTS SDK . Dan sudah mencoba beberapa implemetasi di 
  mining-agents . Dan terdapat repo di pada repo openai-agents-python yang saya clone dari github agar kamu paham dan bisa melihat dokumentasi tentang open ai       
  agents sdk. Salah satu contoh implemntasi Ai agents bisa dilihat di  openai-agents-python/examples/financial_research_agent. Nah untuk sekarang saya    
  mau membuat system Ai agenys  di   mining-agents sesuai dengan mining-agents/Project\ Description/readme.md , yaitu untuk sementara bisa implemtasi    
  tool nya yaitu agent dapat mendapatkan insight dari data luar dari berbagi sumber , untuk contoh kasus ini saya menggunakn data dummy dari
  data/Dataset/Raw_Data/ berupa csv dengan deskripsi data/Dataset/Raw_Data/Readme.md dan agent bisa dapat justifikasi lagi dari Model ml yang dilatih    
  dengan dataset raw tadi yang file trainya  ada di models_ml/Train/train.py dan hasil model model  nya ada di models , jadi agent yang bertugas dapat   
  memprediksi dari data forecast (dummy)  misalnya unutk memmprediksi seminggu kedpannya sebagai alarm. Unutk implemtasi tool bisa dilihat di
  openai-agents-python/docs/tools.md , dan terkahir apakah memungkinan juga agent bisa Query SQL misal query dari CSV agar lebih spesfik seperti itu. Dan█
  jika kamu tidak tahu sebisa mungkin lihat dan cari tahu di folder openai-agents-python