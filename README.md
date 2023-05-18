# TUGAS PRAKTIKUM
1. Silakan selesaikan praktikum tersebut sesuai langkah-langkah sebelumnya, lalu laporkan hasilnya berupa link repository GitHub dengan nama spark-sql-big-data disertai dengan screenshot hasilnya.
2. Jelaskan masing-masing maksud kode berikut sesuai nomor kodenya pada laporan praktikum Anda!

<img width="330" alt="image" src="https://user-images.githubusercontent.com/95727437/232962857-ae2e62ae-e00e-444c-a6d0-e66b603a5bd0.png">

| Nomor Kode | Jawaban |
| --- | --- |
| 1 | Mendefinisikan variabel mylist untuk data, myschema untuk mendefinisikan skema/struktur |
| 2 | Membuat Dataframe |
| 3 | Parallelize untuk membuat RDD, sedangkan toDF untuk mengkonversi RDD menjadi dataframe |
| 4 | hadoop untuk menjalankan perintah hadoop, fs untuk operasi file seperti baca/tulis/hapus, put untuk upload/mengunggah file |
| 5 | pyspark.sql untuk akses modul pyspark, SQLContext objek untuk interaksi dengan data, createOrReplaceTempView untuk membuat tampilan tabel sementara, show untuk menampilkan |
| 6 | textfile untuk membaca file txt, map untuk menerapkan fungsi, strip untuk menghapus spasi, StructField untuk menentukan skema/struktur dataframe, StringType untuk menentukan tipedata String |
| 7 | spark.read.format untuk membaca format file misalnya .csv, jdbc untuk membaca data menggunakan JDBC, option untuk konfigurasi data, load untuk membaca data  |
| 8 | Untuk menampilkan data  |
| 9 | collect untuk mengambil semua baris dan dikembalikan dalam bentuk array, rdd untuk konversi dataframe ke RDD, take untuk mengambil elemen RDD |
| 10 | makeRDD untuk membuat RDD, Seq untuk sequence, createDataset untuk membuat dataset |
| 11 | filter untuk memfilter baris sesuai kondisi tertentu |
| 12 | as untuk memberi nama alias, toDF untuk mengkonversi RDD menjadi dataframe, first untuk mengambil nilai/elemen pertama dari dataframe/RDD |
| 13 | listDatabase untuk menampilkan daftar database, listTable untuk menampilkan daftar tabel, listFunction untuk menampilkan daftar fungsi, isCached untuk memeriksa dataframe sudah dicache atau belum, select untuk memilih sesuatu pada data dalam tabel(query) |
| 14 | Read utuk membaca file, text untuk file .txt |
| 15 | load untuk membaca data yang sudah di format, json adalah format dari data, format untuk menentukan format, printSchema untuk menampilkan skema/struktur dari dataframe |
| 16 | write untuk menulis data, save untuk menyimpan data |
| 17 | parquet adalah format dalam big data, jika di spark untuk membaca format parquet |
| 18 | Options untuk konfigurasi pada data, inferSchema untuk menginfer schema secara otomatis, csv adalah format file, header untuk menggunakan baris pertama pada csv sebagai nama kolom dataframe, codec untuk mengonversi data dari satu format encoding ke format encoding lainnya |

## SCREENSHOT
<img width="331" alt="00_runningspark" src="https://github.com/irbaadika/spark-sql-big-data/assets/95727437/a580d4dc-9b00-4395-ab1d-5f7464210f41">

### 1. Analitik dengan DataFrame
<img width="324" alt="01_AnalitikDenganDataframe" src="https://github.com/irbaadika/spark-sql-big-data/assets/95727437/60f21de1-529b-4403-ae41-0b8e9a918cc0">
<img width="318" alt="01_AnalitikDenganDataframe_2" src="https://github.com/irbaadika/spark-sql-big-data/assets/95727437/1057196f-a36f-4025-889a-60b3514093c0">

### 2. Membuat DataFrame dari Database Eksternal
<img width="323" alt="02_MembuatDataFramedariDatabaseEksternal" src="https://github.com/irbaadika/spark-sql-big-data/assets/95727437/c36b7fc3-34ba-4560-8001-8d316584f529">
<img width="323" alt="02_MembuatDataFramedariDatabaseEksternal_2" src="https://github.com/irbaadika/spark-sql-big-data/assets/95727437/124f98fe-1606-4187-a359-7778d126a0cc">

### 3. Mengkonversi DataFrame ke RDDs
<img width="272" alt="03_MengonversiDataFramekeRDDs" src="https://github.com/irbaadika/spark-sql-big-data/assets/95727437/60c5bcce-e9c5-433f-9eb9-c4bf4afaee79">

### 4. Membuat Datasets
<img width="322" alt="04_MembuatDatasets" src="https://github.com/irbaadika/spark-sql-big-data/assets/95727437/99459f31-9edd-4861-8289-b3c8da7ae81b">

### 5. Mengkonversi DataFrame ke Datasets dan Sebaliknya
<img width="321" alt="05_MengonversiDataFramekeDatasetsdanSebaliknya" src="https://github.com/irbaadika/spark-sql-big-data/assets/95727437/72c0b44f-09ea-46f1-8303-d9e7bb5c1945">

### 6. Mengakses Metadata Menggunakan Catalog
<img width="322" alt="06_MengaksesMetadataMenggunakanCatalog" src="https://github.com/irbaadika/spark-sql-big-data/assets/95727437/ec444684-c1a1-436a-b5cb-589d68846f35">
<img width="311" alt="06_MengaksesMetadataMenggunakanCatalog_2" src="https://github.com/irbaadika/spark-sql-big-data/assets/95727437/0e5428ed-a9bb-4fa6-9323-8f51109e2076">

### 7. Bekerja dengan Berkas Teks
<img width="322" alt="07_BekerjadenganBerkasTeks" src="https://github.com/irbaadika/spark-sql-big-data/assets/95727437/fde60408-86a3-45d1-9d61-c997a2ce9123">

### 8. Bekerja dengan Berkas JSON
<img width="321" alt="08_BekerjadenganBerkasJson" src="https://github.com/irbaadika/spark-sql-big-data/assets/95727437/b91d169c-697d-4693-a96e-14a8ab28bdee">

### 9. Bekerja dengan Berkas CSV
<img width="321" alt="09_BekerjadenganBerkasCSV" src="https://github.com/irbaadika/spark-sql-big-data/assets/95727437/01333e99-026a-4be3-b3f1-67fa3ee941fd">
<img width="322" alt="09_BekerjadenganBerkasCSV_2" src="https://github.com/irbaadika/spark-sql-big-data/assets/95727437/35e0d684-84f7-4136-8977-ffaee1345c6d">
