# Tugas Kecil 2 IF2211

## Deskripsi Program

Program ini merupakan implementasi dari algoritma pembentukan kurva Bezier menggunakan dua metode berbeda: brute force dan divide and conquer. Kurva Bezier adalah jenis kurva parametrik yang sering digunakan dalam desain grafis dan animasi komputer.

Algoritma brute force bekerja dengan mencoba semua kemungkinan kombinasi titik kontrol untuk menghasilkan kurva Bezier, sedangkan algoritma divide and conquer membagi kurva menjadi segmen-segmen yang lebih kecil untuk kemudian menggabungkannya menjadi satu kurva Bezier.

## Fitur Program:

- Implementasi dua algoritma pembentukan kurva Bezier: brute force dan divide and conquer.
- Kemampuan untuk menentukan jumlah titik kontrol dan nilai kontrolnya.
- Visualisasi hasil kurva Bezier yang dihasilkan.

### Catatan:
Program ini ditulis untuk keperluan pembelajaran dan demonstrasi algoritma pembentukan kurva Bezier.

## Requirement dan Instalasi

1. tkinter
2. matplotlib

Dapat melakukan instalasi kedua module tersebut secara bersamaan dengan change directory ke folder project lalu menjalankan command:
`pip install -r requirements.txt`

## Cara Menjalankan Program

Jika program ini perlu dikompilasi, ikuti langkah-langkah berikut:

1. Buka terminal atau command prompt.
2. Pindah ke direktori folder project lalu lakukan
`cd bin`
untuk pindah direktori ke folder src
3. Jalankan perintah kompilasi berikut 
`./run-program`.
4. Tunggu sebentar dan GUI akan terbuka

## Cara Menggunakan Program

Untuk menghasilkan kurve bezier pada program ini, ikuti langkah-langkah berikut:

1. Pertama, dapat menekan tombol "how to use" untuk melihat cara menjalankan program.
2. Setelah itu dapat menekan tombol "create curve" untuk masuk ke laman create curve.
3. Lakukan penambahan titik dengan menekan tombol "add point" sebuah window akan muncul, anda dapat menambahkan titik sebanyak N kali dan juga dapat menghapus titik tersebut.
4. Jika semua titik sudah ditambahkan, tekan tombol submit untuk ditampilkan pada kurva (Jika ingin merubah list titik sebelumnya dapat membuka ulang window yang tertimpa oleh window utama)
5. Memilih metode antara "Divide and Conquer" atau "Brute Force".
6. Menentukan jumlah iterasi dengan mengisi pada bagian set iteration (Jika mengubah value jangan lupa untuk menekan 'Enter' pada keyboard agar teregister perubah pada program).
7. Terdapat opsi untuk melihat animasi pembetukan kurva, dapat menekan "on" untuk menampilkan animasi dan "off" untuk menampilkan kurvanya langsung.
8. Langkah terakhir menekan tombol "Start" untuk menjalankan program pembentukan kurva bezier.

### Note
Iterasi lebih dari 20 akan menyebabkan GUI untuk freeze jadi saran untuk menunggu program selesai dijalankan.  

## Author

Ahmad Thoriq Saputra
13522141
Rafif Ardhinto Ichwantoro
13522159