# program-multi-thread

![Screenshot (300)](https://github.com/user-attachments/assets/be712d6d-ceae-4e7d-a6ac-869320c84375)

**Grafik Kiri Atas: Cache Hits**

Tanpa Koherensi (warna oranye): Jumlah cache hits relatif lebih rendah untuk kedua thread (Thread 0 dan Thread 1).
Dengan Koherensi (warna biru): Jumlah cache hits meningkat signifikan untuk kedua thread.
Interpretasi: Penggunaan koherensi cache meningkatkan jumlah cache hits. Ini berarti bahwa lebih banyak permintaan data dapat dipenuhi dari cache lokal masing-masing thread, mengurangi kebutuhan untuk mengakses memori utama yang lebih lambat.

**Grafik Kanan Atas: Akses Memori**

Tanpa Koherensi (bagian bawah, warna oranye): Jumlah akses memori relatif lebih tinggi untuk kedua thread.
Dengan Koherensi (bagian atas, warna biru): Jumlah akses memori berkurang secara signifikan dibandingkan dengan tanpa koherensi.
Interpretasi: Dengan adanya koherensi cache, kebutuhan untuk mengakses memori utama menjadi lebih sedikit. Hal ini karena data yang sering digunakan cenderung tetap konsisten di cache lokal masing-masing thread.

**Grafik Kiri Bawah: Jumlah Pesan Koherensi**

Grafik ini hanya menampilkan satu batang berwarna oranye dengan label "Koherensi". Batang ini menunjukkan adanya sejumlah pesan koherensi (sekitar 100).
Interpretasi: Ketika koherensi cache diimplementasikan, sistem perlu mengirimkan pesan-pesan koherensi antar cache untuk memastikan konsistensi data. Grafik ini menunjukkan aktivitas komunikasi koherensi yang terjadi.

**Grafik Kanan Bawah: Waktu Eksekusi (detik)**

Tanpa Koherensi (batang hijau): Waktu eksekusi tampak lebih tinggi.
Dengan Koherensi (batang merah): Waktu eksekusi terlihat jauh lebih rendah.
Interpretasi: Penggunaan koherensi cache secara signifikan mengurangi waktu eksekusi keseluruhan simulasi. Hal ini disebabkan oleh peningkatan cache hits dan penurunan akses memori utama, meskipun ada overhead komunikasi koherensi.

**Kesimpulan Umum:**

Secara keseluruhan, simulasi dengan koherensi cache menunjukkan performa yang lebih baik dibandingkan dengan simulasi tanpa koherensi cache. Hal ini ditunjukkan oleh:

Peningkatan jumlah cache hits.
Penurunan jumlah akses memori.
Pengurangan waktu eksekusi secara keseluruhan.
Meskipun ada overhead berupa pesan-pesan koherensi, manfaat dari menjaga konsistensi data di cache dan mengurangi akses ke memori utama lebih dominan dalam kasus ini, menghasilkan peningkatan kinerja.
