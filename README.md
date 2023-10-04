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
    class item(models.Model):
        name = models.CharField(max_length=255)
        date_added = models.DateField(auto_now_add=True)
        amount = models.IntegerField()
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
# Perbedaan
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
    from main.models import item
    class itemForm(ModelForm):
        class Meta:
            model = item
            fields = ["name", "amount", "description"]
    sesuaikan bagian fields sesuai dengan models yang ada 
- pada file views.py yang ada di folder main dan tambahkan beberapa import seprti ini ;
    - from django.http import HttpResponseRedirect
    - from main.forms import itemForm
    - from django.urls import reverse
- Kemudian buat fungsi baru (create_item) pada views.py yang berfungsi untuk menerima request dari user.
    def create_item(request):
    form = itemForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "create_item.html", context)
- Lalu pada fungsi def show_main tambahkan kode item.objects.all() yang berfungsi untuk mengambil seleuruh objek yang ada pada database . Pada fungsi ini juga tambahkan 'items': items pada bagian context.
- tambahkan import (create_item) pada urls.py pada main dan juga tambahkan path url baru pada bagian urlpatterns
- Buat file baru pada folder templates pada main dengan nama create_item.html 
- Pada main.html tambahkan kode block content dengan fungsi menampilkan produk dengan bentuk table dan tombol
 # format HTML, XML, JSON #
 - Pada views.py pada folder main tambahkan import 
    from django.http import HttpResponse
    from django.core import serializers
- Kemudian membuat fungsi show_xml dan fungsi show_json seperti dibawah ini 
    - XML
    def show_xml(request):
    data = item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    - JSON
    def show_json(request):
    data = item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
- kemudian tambahkan import show_xml dan show_json pada urls.py pada folder main .
- terakhir tambahkan path url (XML, path('xml/', show_xml, name='show_xml'),JSON, path('json/', show_json name='show_json'),) pada bagian urlpatterns.
# XML by ID, dan JSON by ID #
- buat fungsi baru untuk xml dan json
    - XML
        def show_xml_by_id(request, id):
        data = item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    - JSON
        def show_json_by_id(request, id):
        data = item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
- Tambakan perintah import show_xml_by_id, show_json_by_id pada urls.py pada main
- dan yang terakhir tambahkan kode path baru (path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), )pada bagian urlpatterns 

# ROUTING #
- Dalam routing XML dan json routing dapat dilakukan dengan cara berikut yaitu dengan menambahkan path url pada bagian urlpatterns seperti ini 
    - XML, path('xml/', show_xml, name='show_xml'),
    - JSON, path('json/', show_json, name='show_json'), 
- Dalam routing XML ID dan JSON ID routing dapat dilakuan dengan cara berikut yaitu  dengan manambahkan path url pada bagian urlpatterns seperti ini;
    - XML, 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    - JSON
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 


5. Screenshot Hasil URL Postman
    Link Screenshot : ristek.link/Screenshot-URL-PBP


# TUGAS 4 

### Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreation merupakan salah satu fitu bawaan yang disediaka oleh django dalam modul django.contrib.auth.forms. Fitur ini berfungsi untuk membuat registration form dalam aplikasi web. Fitur ini dapat mempermudah untuk mengumplkan data seperti nama , password dan juga konfimasi password.
Adapun beberapa kekurangan dari menggunakan Django UserCreation Form, anatara lain;
- Desain Terbatas
UserCreationForm dari djnago memiliki fitur ayang cukup sederhana oleh karena itu apbila aplkasi memerlkan form registration yang lebih kompleks maka harus membuat custom sendiri.
- Custom 
Apabila inigin menambahkan fitur lain diluar default dari UserCreationForm maka haus dilakukan pengimplementasian secara terpisah.
- Tampilan Default
Tampilan defauls dari UserCreationForm mungkin tidaks esuai dengan keinginan maka harus diatur secara manual.
    
### Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
- Autentikasi
Merupakan sebuah proses verifikasi (menegecek apakah user merupakan user yang legal atau bukan) user saat akan melakukan log in atau mengakses aplikasi. Autentikasi sendiri melibatkan username dan password sebagai langkahnya. Dalam Django autentikasi secara default akan mengelola informasi login,logout,otentikasi user.
- Otorisasi
Merupakan proses dalam pemutusan apa saja yang dapat dilakukan oleh user yang sudah terautentikasi dalam penggunaan aplikasi, otorisasi berguna untuk memberikan roles kepada user sesuai dengan peran mereka. Dalam django sistem ini memperbolehkan para pengembang untuk mendefinisikan roles dari pengguna dan kontrol akses terhadap views,model, dan lain-lain.

### Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna
Cookies merupakan informasi yang berbentuk nama dan nilai yang tersimpan dalam komputer user yang berisikan data dari klien yang berguna auntuk mengidentifikasi dan juga melacak user saat mereka menggunakan web. 
- Cara Django mengelola cookies;
Django membuat ID sesi unik untuk pengguna yang mengunjungi situs web. Data sesi, seperti preferensi atau login, disimpan di server Django, bukan di cookie pengguna. Saat pengguna melakukan permintaan berikutnya, ID sesi disertakan dalam permintaan HTTP untuk mengidentifikasi sesi dan mengambil data sesi dari server. Cookie ID sesi dienkripsi untuk keamanan, dan Django mengontrol berapa lama sesi berlangsung serta menghapus sesi yang sudah berakhir.

### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies secar default mempunyai resiko potensial yang harus diwaspadain anatara lain;
- Keamanan Data: Cookies dapat menyimpan informasi yang sensitif, dan jika tidak dienkripsi atau diatur dengan benar, data tersebut dapat rentan terhadap upaya pencurian.
- Pelacakan Pengguna: Cookies digunakan untuk memantau aktivitas pengguna di situs web, namun harus dikelola dengan hati-hati untuk menghindari pelanggaran privasi.
- Cross-Site Scripting (XSS): Serangan XSS dapat memanipulasi cookies dan mengakses informasi pengguna jika data tidak diverifikasi sebelum dimasukkan ke dalam cookies.
- Cross-Site Request Forgery (CSRF): Cookies yang tidak aman dapat dimanfaatkan dalam serangan CSRF untuk mengirimkan permintaan yang tidak diinginkan atas nama pengguna yang telah diautentikasi.
- Masa Kadaluwarsa: Cookies memiliki jangka waktu kadaluwarsa yang perlu diatur dengan benar agar tidak menimbulkan risiko keamanan jika melebihi batas waktu yang sesuai.
- HTTPS: Untuk meningkatkan keamanan, sangat disarankan menggunakan HTTPS saat mengirim cookies agar komunikasi antara server dan klien terenkripsi.
- Pencurian Cookies: Penjahat siber dapat mencuri cookies pengguna melalui metode seperti man-in-the-middle atau pencurian cookie.
- Kepatuhan: Saat mengumpulkan data pribadi, penting untuk mematuhi peraturan privasi dan regulasi data seperti GDPR atau CCPA demi menjaga privasi dan keamanan data pengguna.


### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

##### Mengimplementasikan fungsi registrasi, login, dan logout
###### LOGIN
- Membuat fungsi login yang isinya seperti ini;
```python
def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:show_main')
            else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
        context = {}
        return render(request, 'login.html', context)
```

- Kemudian tambahkan perintah import authenticate dan log in yang berfungsi untuk autentikasidan juga login
- Buat file login.html di folder templates yang ada di main, yang isinya seperti ini;
```python
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```
- Kemudian pada folder urls.py di main tambahkan fungsi import yaitu login_user dan pada bagian urlpatterns tambahkan path baru yaitu ;
```python
path('login/', login_user, name='login'),
``` 
###### LOGOUT
- Buat fungsi logout yang isinya seperti ini
```python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
- Kemudian tambahkan fungsi import (logout) pada pada file views.py pada folder main
- Pada main.html tambahkan kode baru divawah abgian add new item seperti ini;
```python
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...
```
- dan pada urls.py pada folder main tambhak fungsi import baru yaitu (logout_user), dan pada bagian urlpatterns nyabtambahkan kode ini 
```python
path('logout/', logout_user, name='logout'),
```

##### Membuat dua akun pengguna dengan masing-masing tiga dummy data
Link = ristek.link/accoun-dummy-data

##### Menghubungkan model Item dengan User.
- Pada models.py pada tambahkan fungsi import yaitu (from django.contrib.auth.models import User)
- tambahkan kod abru pada class item pada models.py
```python
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```
- Kemudian pada fungsi create_item ganti kodennya menjadi seperti ini 
```python
if form.is_valid() and request.method == "POST":
    item = form.save(commit=False)
    item.user = request.user
    item.save()
    return HttpResponseRedirect(reverse('main:show_main'))
```
- dan pada fungsi show_main ganti menjadi seperti ini 
```python
def show_main(request):
    item = Iteam.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
    ...
```
- dan yang terajhir lakukan migrasi dengan perintah python manage makemigration.py dan ketikkan 1 lal ketikkan 1 lagi dan kemudian masukkan python manage.py migrate

##### Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
- Pada views.py yanga da pada folder main tambahkan fungsi import baru yaitu 
```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
- lalu, pada fungsi last_user pada file views.py ganti kode yang awalnya if user is not None menjadi seperti ini ;
```python
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```
- dan pada fungsi show_main di file views.py di bagian context tambahkan kode ini 
```python
'last_login': request.COOKIES['last_login'],
```
- lalu pada fungsi logout_user ganti kodenya dengan ini
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
- dan yang terakhir pada file main.html tambahkan kode berikut diantara tabel dan tombol logout
```python
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```

# TUGAS 5
### Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
##### Tag Selector
berguna untuk memilih semua elemen dengan tag yang sama dan untuk memberikan gaya secara umum pada elemen-elemen dengan tag tertentu.
Digunakan disaat akan mengaplikasikan style yang sama ke elemen yang banyak dengan tag yang sama seperti mengatur style teks pada paragraf '<p>'
##### Class Selector
Berguna untuk memilih elemen berdasarkan kelas yang ada pada elemen tersebut, selector ini memberikan fleksibilitas dalam pengaturan gayanya
Digunakan saat ingin memberikan style yang khusus kepada pada elemen yang mempunyai class tertentu, seperti mengubah warna teks dengan class "highlight"
##### Id Selector
berguna untuk memilih elemen berdasarkan ID uniknya dan mengaplikasikan gaya pada satu elemen tertentu.
Digunakan saat ngin memberikan gaya khusus pada satu elemen tertentu dalam halaman, seperti mengatur warna latar belakang header dengan ID "header".
##### Attribute Selector ('*')
Berguna untuk memilih elemen berdasarkan nilai atribut tertentu yang dimiliki oleh elemen tersebut.
Digunakan saat ingin memilih elemen dengan atribut khusus, misalnya memilih semua tautan <a> dengan atribut target="_blank"
##### Universal Selector
Berguna untuk mengatur gaya global atau mereset gaya pada semua elemen.
Digunakan saat ingin mengatur gaya dasar pada semua elemen, seperti menghapus margin dan padding bawaan.
##### Pseudo Selector
Berguna untuk  memilih elemen berdasarkan keadaan atau karakteristik tertentu yang tidak dapat diwakili oleh selector lainnya. Ini memungkinkan Anda membuat efek dan gaya yang dinamis.
Digunakan saat ngin mengaplikasikan gaya atau efek berdasarkan keadaan elemen, seperti mengubah tampilan tombol saat digerakkan mouse (:hover) atau memilih elemen setiap beberapa elemen (:nth-child(odd)).


### Jelaskan HTML5 Tag yang kamu ketahui.
HTML5 adalah versi terbaru dari HTML yang diresmikan oleh W3C pada tahun 2014. Adapun beberapa teg yang HTML5 sediakan antara lain;
- header, berguna untuk menjelaskan bagian paling atas halaman yang biasanya berisi logo, Judul, dan lain-lain
- footer, berguna untuk mendifinisikan bagian bawah dari sebuah halaman pada web yang biasanya berisi info kontak,sosial mesia, ataupun hak cipta.
- nav, untuk menandai navigasi dalam halaman web yang biasanya berisi tautan menu
- main, Berisi konten utama dari web, dalam satu halaman hanya boleh 1 elemen main saja
- Video, berguna untuk memasukkan sebuah video didalam web 
- form, untuk membuat formulir untuk dikirimkan ke server , berisi input, tombol, dan action yang akan dilakukan oleh user
- input, berguna untuk membuat elemen input/masukkan seperti tombol,kotak teks,dan lain-lain


### Jelaskan perbedaan antara margin dan padding.
##### Margin 
Merupakan suatu area yang berada di sekeliling elemen dan terletak di luar batas elemen itu sendiri yang berfungsi untuk mengatur jarak antara elemen tersebut dengan elemen-elemen lain yang ada di sekitarnya.
###### Perbedaan
- Area yang berada disekitar HTML dan diluar batas elemen
- Menagtur jarak diantara elemen dengan elemen lain disekitarnya
- Pada margin tidak mempunyai warna atau latar belakang
##### Padding
Merupakan area yang mengelilingi konten elemen dan berada di dalam batas elemen itu sendiri yang berfungsi adalah untuk mengatur jarak antara konten elemen dan batas elemen tersebut.
###### Perbedaan 
- Padding berada di dalam batas elemen HTML, diantara konten elemen dan batas elemen.
- Mengatur jarak diantara konten dan juga batas elemen.
- Pada padding mempunyai warna atau latar belakang wrna.


### Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
##### Bootstrap
Framework CSS yang dari sananya sudah mempunyai komponen dan gaya yang sudah disiapkan dan siap untuk langsung digunakan. 
##### Tailwind CSS
Framework yang berfokus pada utility yang dimana kita menambahkan , membangun tampilannya dengan menggabungkan kelas-kelas utilitas di dalam HTML.
###### Waktu Kegunaan
Penggunanan dari Bootstrap sebaiknya digunakan ketika kita ingin membuat sebuah web dengan cepat dan instan tanpa harus merancang atau mendesain tampilannya dari awal.
Sedangkan Tailwind CSS digunakan apabila kita ingin membuat web yang ingin mempunyai rancangan yang lebih kompleks dan khusus.


### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
#### Menambahkan Bootstrap 
- Pada base.html yang ada pada pacil_mart tambhakan kode meta 
```python
<head>
    {% block meta %}
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
    {% endblock meta %}
</head>
```
- Kemudian pada blok tersebut jga tambahkan bootstrap CSS dan JS
###### CSS
```python
<head>
    {% block meta %}
        ...
    {% endblock meta %}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
```
###### JS
```python
<head>
    ...
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
</head>
```

#### Tambahkan Navbar
- pada main.html tambhaknkode yang ada pada web bootstrp yang berfungsi untuk menampilkan nama, tombol logout pada navbarnya

#### Menambahkan Edit dan Delete pada Aplikasi
- Pada Views.py yang ada pada main buat fungsi baru dengan nama edit_item dan delete_item
###### Edit
```python
def edit_item(request, id):
    # Get item berdasarkan ID
    item = item.objects.get(pk = id)

    # Set item sebagai instance dari form
    form = itemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)
```
###### Delete
```python
def delete_item(request, id):
    # Get data berdasarkan ID
    item = Item.objects.get(pk = id)
    # Hapus data
    item.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))
```
- Kemudian buat file baru pada folder templates pada main yaitu edit_item.html
###### edit_item.html
```python
{% extends 'base.html' %}
{% load static %}

{% block content %}
<div style="background-color: rgb(171, 172, 177); text-transform: uppercase; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; padding: 10px;">
    <h1>Edit Item</h1>
</div>

<div style="background-color: rgb(192, 185, 185); padding: 20px; border-radius: 20px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); text-align: center;">
    <form method="POST">
        {% csrf_token %}
        <table style="margin: 0 auto;">
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Edit Item" style="background-color: rgb(63, 57, 178); color: aliceblue; border: none; padding: 10px 20px; border-radius: 7px; cursor: pointer;">
                </td>
            </tr>
        </table>
    </form>
</div>
{% endblock %}

```
- tambahkan fungsi import pada urls.py
###### edit_item
```python
from main.views import edit_item
```
###### delete_item
```pyhton
from main.views import delete_item
```
- Tambahkan path edit dan delete pada bagian urlpatterns 
###### edit_item
```python
path('edit-item/<int:id>', edit_item,name='edit_item'),
```
###### delete_item
```python
path('delete/<int:id>', delete_item,name='delete_item'), 
```
- Setelah itu untuk tambhakan kode seperti ini pada main.html, yang berguna untuk memunculkan button edit dan deletenya
```python

<tr>
    ...
    <td>
        <a href="{% url 'main:edit_product' product.pk %}">
            <button>
                Edit
            </button>
        </a>
        <a href="{% url 'main:delete_product' product.pk %}">
              <button>
                  Delete
              </button>
          </a>
    </td>
</tr>
...
```
