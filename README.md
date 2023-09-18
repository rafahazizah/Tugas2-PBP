# TUGAS 2 #
Link aplikasi : https://app-pacilmart-pbp.adaptable.app/main/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
# MEMBUAT PROJEK DJANGO 
- pertama membuat direktori utama di dalam Lokal
- Kemudian, membuat virtual environment menggunakan perintah      (python -m venv env)
- Setelah itu membaut dependencies yang dimana dependencies itu disimpan dalam file bernama requirements.txt, kemudian install dependencies dengan perintah (pip install -r requirements.txt), lalu membaut nama proyek django pacil_mart mengguankan perintah (django-admin startproject shopping_list .)
- Setelah direktoi pacil_mart berada di lokal, tambahkan "*" pada bagian ALLOWED_HOST dalam file settings.py. Kemudian jalankan perintah (python manage.py runserver), cek link yang tersedia jika ada animasi roket beararti Django berhasil dibuat
- Buat .gitignore 
- Kemudian buar repositori dan lakukan git remote, git add . , git commit, dan git push.
# Membuat aplikasi dengan nama main pada proyek tersebut
- buka file proyek django --> pacil_mart , kemudiaN buka cmdnya dan aktifkan virtual environment nya dengan perintah (env\Scripts\activate.bat)
- buat aplikasi baru (main) dengan perintah (python manage.py startapp main)
- kemudian buka settings.py dalam pacil_mart lalu tambahkan main dalam variabel INSTALLED_APPS
- buat folder templates dalam folder main kemudian buat main.html dalam folder templates, isi main.html dengan nama,amount,decription.
# MODEL APLIKASI MAIN DENGAN NAMA ITEM 
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
# ROUTING URL 
- Dalam folder main buka file urls.py kemudian diadalamnya isi dengan kode ini ;
    from django.urls import path
    from main.views import show_main
    app_name = 'main'
    urlpatterns = [
        path('', show_main, name='show_main'),]
- kemudian pada folder pacil_mart buka file urls.py dan tambahkan fungsi impor include (from django.urls import path,include) dan juga tambahkan (path('main/', include('main.urls')),) pada bagian urlpatterns
- Jalankan perintah python manage.py runserver
- Kemudian buka link yang ada pada terminal atau pada http://localhost:8000/main/
# DEPLOYMENT KE ADAPTABLE 
- Sign in menggunakan akun githuh 
- Kemudian pilih repo yang menampung proyek django disini nama reponya adalah Tugas2-PBP
- Lalu, pilih python template kemudian pilih PostgreSQL
- pilih versi dari python yang sesuai dengan yang ada di laptop dan pada bagian start command ketik (python manage.py migrate && gunicorn pacil_mart.wsgi)
- Masukkan nama app sesuai keinginan
- Centang bagian HTTP Listener on PORT dan tekan depoly app dan tunggu samapai selesai.

2. Bagan : ristek.link/Bagan-PBP  
# PENJELASAN BAGAN -->
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


# TUGAS 3 #
1. Apa perbedaan antara form POST dan form GET dalam Django?
Dalam Django ada yang namanya HTTP POST dan HTTP GET yang diaman dua hal tersebut mempunyai fungsi yang sama yaitu untuk mengirimmkan data dari HTML ke Django.
# PERBEDAAN
- Tujuan Utama
    - POST, Untuk mengirimkan data yang bersifat sensitif, pada umumnya POST digunakan untuk mengirim data seperti kata sandi, formulir, dan permintaan untuk upgrade, menghapus sumder daya server.
    - GET, Berfungsi untuk mengambil data dari server tanpa melakukan perubahan pada sumber, biasanya digunakan untuk mengambil data dari server tanpa mengubah datanya. 
- SECURITY
    - POST, metode ini maka datanya tidak akan ditampilkan di URL , hal ini memnbuat penggunaan POST lebih aman apabila mengirimkan data yang sensitif.
    - GET, Data akan muncul di URL sehingga tidak aman a[abila mengirimkan data yang bersifat sensitif.]
- Kapasitas Data
    - POST, tidak ada batasan kapasitas data yang akan dikirimkan sesuai untk mengirmkan data yang berkapasitas besar.
    - GET, Memiliki batasan tentang panjang URL pada browser dan server, jadi kurangs esuai untuk mengirimkan data yang besar.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML,JSON,HTML merupakan format-format dalam mengirimkan data 
# Perbedaan 
- Tujuan utama 
    - XML, XML dibangun atau dirancang dengan fungsi untuk menggambarkan data dan juga struktur sebuah dokumen, digunakan untuk melakukan pertukaran data anatr aplikasi, dan lain-lain
    - JSON, memiliki fungsi untuk menggamabarkan data yang berfoks pada objek dan array. JSON merupakan format yang paling umum dalam melakukan data pada pertukaran data aplikasi web.
    - HTML, memilki fungsi untuk membuat suatu halaman web untuk menampilkan sebuah konten dalam sebuah web. HTML tidak digunakan untuk pertukaran seperti XML dan JSON.
- Struktur Data
    - XML, memilki struktur data yang fleksibel, yang sangat sesuai untuk data yang kompleks 
    - JSON, memiliki struktur yang data lebih sederhana dari XML, struktur yang seperti ini lebih sesuai untuk data yang berbentuk objek seperti data yang digunakan dalam aplikasi web.
    - HTML, memiliki struktur yang terbatas daripada XML dan juga JSON
- Fungsi umum
    - XML, berfungsi untuk konfigurasi file, pertukaran data antar aplikasi, dan lain-lain
    - JSON, Digunakan untuk mengembangkan web dan pertukaran data yang simple
    - HTML, Berfungsi untuk menampilkan konten pada web browser.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    - Format yang digunakan oleh JSON memilki format yang ringkasi dibandingkan dengan XML, yang dimana format tersebut dapat lebih mudah dipahami dan juga di-debug
    - JSON dapat dibaca dengan mudah oleh berbagai bahasa pemrograman seperti Python, JavaScript, Java, dan lain-lain. 
    - JSON menggunakan tipe data yang biasa digunakan dalam pengembangan web seperti angka,string,boolean,array,null,dan objek.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
# Membuat input form
- Membuat file baru dengan nama forms.py di dalam folder main
- Masukkan kode ini ;
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "amount", "description"]
    sesuaikan bagian fields sesuai dengan models yang ada 
- pada file views.py yang ada di folder main dan tambahkan beberapa import seprti ini ;
    - from django.http import HttpResponseRedirect
    - from main.forms import ProductForm
    - from django.urls import reverse
- Kemudian buat fungsi baru (create_product) pada views.py yang berfungsi untuk menerima request dari user.
    def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
- Lalu pada fungsi def show_main tambahkan kode Product.objects.all() yang berfungsi untuk mengambil seleuruh objek yang ada pada database . Pada fungsi ini juga tambahkan 'products': products pada bagian context.
- tambahkan import (create_product) pada urls.py pada main dan juga tambahkan path url baru pada bagian urlpatterns
- Buat file baru pada folder templates pada main dengan nama create_product.html 
- Pada main.html tambahkan kode block content dengan fungsi menampilkan produk dengan bentuk table dan tombol 

5. Screenshot Hasil URL Postman
    Link Screenshot : ristek.link/Screenshot-URL-PBP

