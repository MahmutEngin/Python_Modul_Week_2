# Python_Modul_Week_2
### Question1: Student Grades Processing
ogrenciler = {
    'Ahmet Yılmaz': [85, 90, 78], 
    'Mehmet Demir': [82, 86, 76], 
    'Ayşe Kaya': [78, 89, 95], 
    'Zeynep Çelik': [65, 70, 80], 
    'Ali Kara': [50, 60, 75], 
    'Fatma Yıldız': [88, 95, 80], 
    'Murat Aydın': [67, 68, 74], 
    'Elif Aksoy': [95, 90, 85], 
    'Hakan Öztürk': [45, 70, 54], 
    'Canan Taş': [80, 75, 82]
}
# 1-Her öğrencinin not ortalamasını hesapla ve sözlüğe ek
ortalamalar={}
for ogrenci in ogrenciler:
    notlar=ogrenciler[ogrenci]
    ort =sum(notlar) / len(notlar)
    ogrenciler[ogrenci].append(ort)
    ortalamalar[ogrenci] = ort
print(ogrenciler)
# 2-En yüksek not ortalamasına sahip öğrenciyi bul ve ekrana yazdır.
maximum =max(ortalamalar.values())
en_yuksek_ogrenci = max(ortalamalar, key=ortalamalar.get)
print(f' En yuksek ortalaya sahip ogrenci {en_yuksek_ogrenci} Notu: {maximum}')
# 3-Her öğrencinin adını soyadından ayır ve ayrı bir tuple'da sakla ve bir listeye ekle.
isim ={}
soyisim={}
for ogrenci in ogrenciler:
    ad, soyad =ogrenci.split()
    isim[ogrenci]= ad
    soyisim[ogrenci]=soyad
    adlar=tuple(isim.values())
    soyadlar=tuple(soyisim.values())

print(adlar)
print(soyadlar)
# 4-Adları alfabetik sıraya göre sırala ve sıralı listeyi ekrana yazdır.
alfabetik=sorted(ogrenciler.keys())
sirali_liste={sirali: ogrenciler[sirali] for sirali in alfabetik}
print(sirali_liste)
# 5-Not ortalaması 70'in altında olan öğrencileri bir kümede (kümede) tut.
dusuk =set()
for ogrenci in ogrenciler:
    notlar=ogrenciler[ogrenci]
    ort =sum(notlar) / len(notlar)
    if ort <70:
        dusuk.add(ogrenci)
print(dusuk)


#Question 2: Film Library Management System Project
# Film Kütüphanesi Yönetim Sistemi

film_koleksiyonu = []

def film_ekle():
    film = {}
    film['ad'] = input("Film adı: ")
    film['yönetmen'] = input("Yönetmen: ")
    film['yıl'] = input("Yayın yılı: ")
    film['tür'] = input("Tür: ")
    film_koleksiyonu.append(film)
    print(f"{film['ad']} filmi koleksiyona eklendi.")

def film_düzenle():
    film_adı = input("Düzenlemek istediğiniz filmin adını girin: ")
    for film in film_koleksiyonu:
        if film['ad'].lower() == film_adı.lower():
            film['yönetmen'] = input("Yeni yönetmen: ")
            film['yıl'] = input("Yeni yayın yılı: ")
            film['tür'] = input("Yeni tür: ")
            print(f"{film_adı} filmi güncellendi.")
            return
    print("Film bulunamadı.")

def film_sil():
    film_adı = input("Silmek istediğiniz filmin adını girin: ")
    for film in film_koleksiyonu:
        if film['ad'].lower() == film_adı.lower():
            film_koleksiyonu.remove(film)
            print(f"{film_adı} filmi silindi.")
            return
    print("Film bulunamadı.")

def koleksiyonu_görüntüle():
    if not film_koleksiyonu:
        print("Koleksiyon boş.")
        return
    for film in film_koleksiyonu:
        print(f"Film: {film['ad']}, Yönetmen: {film['yönetmen']}, Yıl: {film['yıl']}, Tür: {film['tür']}")

def ana_menu():
    while True:
        print("\n1. Film Ekle")
        print("2. Film Düzenle")
        print("3. Film Sil")
        print("4. Koleksiyonu Görüntüle")
        print("5. Çıkış")
        secim = input("Seçiminizi yapın: ")

        if secim == '1':
            film_ekle()
        elif secim == '2':
            film_düzenle()
        elif secim == '3':
            film_sil()
        elif secim == '4':
            koleksiyonu_görüntüle()
        elif secim == '5':
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")
ana_menu()



# Question 3: Customer Management System
musteriler = {}

while True:
    print("\nMüşteri Yönetim Sistemi")
    print("1. Yeni Müşteri Ekle")
    print("2. Müşteri Bilgilerini Güncelle")
    print("3. Müşteriyi Sil")
    print("4. Tüm Müşterileri Listele")
    print("5. Ödeme Yap")
    print("6. Çıkış")

    secim = input("Seçiminizi yapın: ")

    if secim == '1':
        id = input("Müşteri ID'sini girin: ")
        if id in musteriler:
            print("Bu ID zaten mevcut.")
        else:
            ad = input("Adı girin: ")
            soyad = input("Soyadı girin: ")
            email = input("E-posta adresini girin: ")
            telefon = input("Telefon numarasını girin: ")
            musteriler[id] = {
                'ad': ad,
                'soyad': soyad,
                'email': email,
                'telefon': telefon
            }
            print("Müşteri başarıyla eklendi.")

    elif secim == '2':
        id = input("Güncellemek istediğiniz müşteri ID'sini girin: ")
        if id not in musteriler:
            print("Müşteri bulunamadı.")
        else:
            print("Mevcut Bilgiler:", musteriler[id])
            ad = input("Yeni adı girin (boş bırakmak için Enter'a basın): ")
            soyad = input("Yeni soyadı girin (boş bırakmak için Enter'a basın): ")
            email = input("Yeni e-posta adresini girin (boş bırakmak için Enter'a basın): ")
            telefon = input("Yeni telefon numarasını girin (boş bırakmak için Enter'a basın): ")

            if ad:
                musteriler[id]['ad'] = ad
            if soyad:
                musteriler[id]['soyad'] = soyad
            if email:
                musteriler[id]['email'] = email
            if telefon:
                musteriler[id]['telefon'] = telefon
            print("Müşteri bilgileri güncellendi.")

    elif secim == '3':
        id = input("Silmek istediğiniz müşteri ID'sini girin: ")
        if id in musteriler:
            del musteriler[id]
            print("Müşteri silindi.")
        else:
            print("Müşteri bulunamadı.")

    elif secim == '4':
        if not musteriler:
            print("Hiç müşteri bulunmamaktadır.")
        else:
            for id, bilgiler in musteriler.items():
                print(f"ID: {id}, Ad: {bilgiler['ad']}, Soyad: {bilgiler['soyad']}, E-posta: {bilgiler['email']}, Telefon: {bilgiler['telefon']}")

    elif secim == '5':
        id = input("Ödeme yapmak istediğiniz müşteri ID'sini girin: ")
        if id in musteriler:
            print(f"{musteriler[id]['ad']} {musteriler[id]['soyad']} için ödeme işlemi gerçekleştirildi.")
        else:
            print("Müşteri bulunamadı.")

    elif secim == '6':
        print("Çıkış yapılıyor.")
        break

    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")