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

koleksiyon = []

while True:
    print("\n1. Film Ekle")
    print("2. Film Düzenle")
    print("3. Film Sil")
    print("4. Koleksiyonu Görüntüle")
    print("5. Çıkış")
    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        film_adı = input("Film adı: ")
        yonetmen = input("Yönetmen: ")
        yayin_yili = input("Yayın yılı: ")
        tur = input("Tür: ")
        koleksiyon.append({
            "film_adı": film_adı,
            "yonetmen": yonetmen,
            "yayin_yili": yayin_yili,
            "tur": tur
        })
        print(f"{film_adı} eklendi!")

    elif secim == "2":
        film_adı = input("Düzenlemek istediğiniz filmin adı: ")
        for film in koleksiyon:
            if film["film_adı"] == film_adı:
                yeni_ad = input("Yeni film adı (boş bırakmak için Enter'a basın): ")
                yeni_yonetmen = input("Yeni yönetmen (boş bırakmak için Enter'a basın): ")
                yeni_yayin_yili = input("Yeni yayın yılı (boş bırakmak için Enter'a basın): ")
                yeni_tur = input("Yeni tür (boş bırakmak için Enter'a basın): ")
                
                if yeni_ad:
                    film["film_adı"] = yeni_ad
                if yeni_yonetmen:
                    film["yonetmen"] = yeni_yonetmen
                if yeni_yayin_yili:
                    film["yayin_yılı"] = yeni_yayin_yılı
                if yeni_tur:
                    film["tur"] = yeni_tur

                print(f"{film_adı} düzenlendi!")
                break
        else:
            print(f"{film_adı} bulunamadı.")

    elif secim == "3":
        film_adı = input("Silmek istediğiniz filmin adı: ")
        for film in koleksiyon:
            if film["film_adı"] == film_adı:
                koleksiyon.remove(film)
                print(f"{film_adı} silindi!")
                break
        else:
            print(f"{film_adı} bulunamadı.")

    elif secim == "4":
        if not koleksiyon:
            print("Koleksiyon boş.")
        else:
            for film in koleksiyon:
                print(f"Film Adı: {film['film_adı']}, Yönetmen: {film['yonetmen']}, Yayın Yılı: {film['yayin_yılı']}, Tür: {film['tur']}")

    elif secim == "5":
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")


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
