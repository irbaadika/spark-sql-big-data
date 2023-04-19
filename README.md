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
