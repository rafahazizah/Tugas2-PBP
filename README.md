Link aplikasi : https://app-pacilmart-pbp.adaptable.app/main/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
<!-- MEMBUAT PROJEK DJANGO -->
- pertama membuat direktori utama di dalam Lokal
- Kemudian, membuat virtual environment menggunakan perintah      (python -m venv env)
- Setelah itu membaut dependencies yang dimana dependencies itu disimpan dalam file bernama requirements.txt, kemudian install dependencies dengan perintah (pip install -r requirements.txt), lalu membaut nama proyek django pacil_mart mengguankan perintah (django-admin startproject shopping_list .)
- Setelah direktoi pacil_mart berada di lokal, tambahkan "*" pada bagian ALLOWED_HOST dalam file settings.py. Kemudian jalankan perintah (python manage.py runserver), cek link yang tersedia jika ada animasi roket beararti Django berhasil dibuat
- Buat .gitignore 
- Kemudian buar repositori dan lakukan git remote, git add . , git commit, dan git push.
<!-- Membuat aplikasi dengan nama main pada proyek tersebut. -->
- buka file proyek django --> pacil_mart , kemudiaN buka cmdnya dan aktifkan virtual environment nya dengan perintah (env\Scripts\activate.bat)
- buat aplikasi baru (main) dengan perintah (python manage.py startapp main)
- kemudian buka settings.py dalam pacil_mart lalu tambahkan main dalam variabel INSTALLED_APPS
- buat folder templates dalam folder main kemudian buat main.html dalam folder templates, isi main.html dengan nama,amount,decription.
<!-- MODEL APLIKASI MAIN DENGAN NAMA ITEM -->
- buka models.py dalam folder main
- isi file models.py dengan ;
    from django.db import models
    class Product(models.Model):
        name = models.CharField(max_length=255)
        date_added = models.DateField(auto_now_add=True)
        Category = models.TextField()
        amount = models.IntegerField()
        price = models.IntegerField()
        description = models.TextField()
- lakukan migrasi dengan perintah python manage.py makemigrations kemudian perintah ini python manage.py migrate
- buka file views.py yang ada di main, lalu tambahkan perintah import (from django.shortcuts import render), agar bisa merender tampilan HTML sesuai dengan data yang diberikan
- tambahkan fungsi show_main dalam file main
- lalu pada file main.html lakukan update sesuai dengan tugas  
<!-- ROUTING URL -->
- Dalam folder main buka file urls.py kemudian diadalamnya isi dengan kode ini ;
    from django.urls import path
    from main.views import show_main
    app_name = 'main'
    urlpatterns = [
        path('', show_main, name='show_main'),]
- kemudian pada folder pacil_mart buka file urls.py dan tambahkan fungsi impor include (from django.urls import path,include) dan juga tambahkan (path('main/', include('main.urls')),) pada bagian urlpatterns
- Jalankan perintah python manage.py runserver
- Kemudian buka link yang ada pada terminal atau pada http://localhost:8000/main/
<!-- DEPLOYMENT KE ADAPTABLE -->
- Sign in menggunakan akun githuh 
- Kemudian pilih repo yang menampung proyek django disini nama reponya adalah Tugas2-PBP
- Lalu, pilih python template kemudian pilih PostgreSQL
- pilih versi dari python yang sesuai dengan yang ada di laptop dan pada bagian start command ketik (python manage.py migrate && gunicorn pacil_mart.wsgi)
- Masukkan nama app sesuai keinginan
- Centang bagian HTTP Listener on PORT dan tekan depoly app dan tunggu samapai selesai.

2. Bagan : ristek.link/Bagan-PBP  
<!-- PENJELASAN BAGAN -->
- Pertama-tama request dari user pertama kali akan diterima dari URL
- Setelah menemukan kecocokan URL dengan pola yang ada dalam urls.py, maka request akan diteruskan ke views.py
- fungsi dalam view akan meminta data daro models.py
- Selanjutnya data akan disajikan dalam bentuk HTML
- dan terakhir HTML akan memberikan respon yang akan dikirimkan kepada user untuk ditampilkan di browser. 

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Karena tanpa menggunakan virtual environment maka dalam proses pembuatan atau pengembangan aplikasi web yang mengguanakan Django maka akan mengalami masalah atau error seperti konflik antar versi dari python, konflik terhadap sistem operasi utama, dan lain-lain.
Ya, kita masih tetap bisa membuat aplikasi web barbasis django tanpa menggunakan virtual environmnet, akan tetapi dianjurkan untuk tetap mengguanakan virtual environment agar tidak terjadi konflik.


4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

-MVC , adalah Model-View-Controller yang artinya MVC merupakan pola desain dalam pengembangan Software yang dimana MVC ini berguna untuk memisahkan komponen-komponen utama dalam sebuah aplikasi. 
    Model , yang berfungsi untuk mengelola data dan logikanya
    View , Yang berfungsi untuk mengtur tampilan untuk user
    Controller , yang berfungsi untuk mengatur interaksi antara model denga view (menerima input dari user lalu memprosesnya)

-MVT, adalah Model-View-Template yang merupakan salah satu komponen dari django yang berbasis pyhton, MVT merupakan versi dari MVC yang sdah diadaptasi untuk django
    Model, berfungsi untuk mengelola data dan logikanya
    View, interface user yang dimana view itu mengambil data dari Model
    Template, adalah komponen yang memisahkan tampilan HTML dari logika sebuah aplikasi

-MVVM, adalah Model-View-ViewModel pola dari software yyang digunakan untuk mengembangkan aplikasi khususnya apliaksi yang berbasis interface (UI)
    Model, berfungsi untuk mengelola data dan logika
    View, Interface untuk user
    ViewModel, ViewModel berfungsi sebagai jembatan bagi Model dan View, yang dimana ViewModel akan mengubah data dari Model ke dalam format yang dapat ditampilkan oleh View.

Perbadaan dari tiga model tersebut adalah sebagai berikut;
    - Data binding
        - MVC, tidak mempunyai data bawaan
        - MVT, punya data bawaan yaitu django
        - MVVM, punya pengikat data yang otomatis apabila ada perubahan
    - Fungsi umum ;
        - MVC, diguanakn dalam berbagai jenis aplikasi termasuk aplikasi web,mobile,dekstop
        - MVT, Secara khusu digunakan untuk mengembangkan web dengan django
        - MVVM, pengembangan aplikasi dengan antar interface yang kompleks
    - Antar Komponen ; 
        - MVC, pada MVC controller berfungsi untuk menghubungkan Model dan View, View kirim input ke Controller lalau diproses kemudian Model dan View diperbarui sesuai dengan kebutuhan dari user.
        - MVT, View mengambil dari MOdel dan mengirimkannya ke Template untuk menampilkan ke tampilan untuk user.
        - MVVM, Perantara anatar View dan Model adalah ViewModel, data dari model diambil oleh ViewModel dan dihubungkan ke View dan diubah kedalam format yang sesuai dengan format View

