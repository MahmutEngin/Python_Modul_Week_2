#Q1

student={
    "FErnando Muslera":[85,90,78],
    "Davinson Sanchez":[92,88,76],
    "Abdulkerim Bardakci":[78,89,95],
    "Eren Elmali":[65,70,80],
    "Gabriel Sara":[50,60,55],
    "Lucas Toreira":[88,85,90],
    "Baris Alper":[72,68,74],
    "Dries Mertens":[95,90,88],
    "emanuel Icardi":[45,50,55],
    "Victor Osimhen":[80,75,82]
    }
i=0
for isim,notlar in student.items():
    ortalama=sum(notlar)/len(notlar)
    student[isim]=notlar+[int(ortalama)]

for isim,deger in student.items():
    print(f"{isim}:{deger}")

en_isim=""
en_yuksek_ort=0
          
for isim,notlar in student.items():
    
    ortalama=notlar[-1]
    if ortalama>en_yuksek_ort:
          en_yuksek_ort=ortalama
          en_isim=isim

print(f"En yuksek not ortalamasina sahip ogrenci:{en_isim} {en_yuksek_ort}")
#print("En yüksek not ortalamasına sahip öğrenci: {} {}".format(en_isim, en_yuksek_ort))
isimler=[]
for isim,notlar in student.items():
    
    a=isim.split()[0]
    my_tuple=(a,)
    isimler.append(my_tuple)

isimler.sort()
print(isimler)


yetmis_alti=[]
for isim,notlar in student.items():
    if notlar[-1]<70:        
        yetmis_alti.append(isim)
        sete_cevir=set(yetmis_alti)

print(sete_cevir)




#Q2
#Film rehberi uygulamasi
filmler={}
print("Film rehberine hos geldiniz")
print("Bu rehberde filmlerle ilgili tum islemleri yapabilirsiniz")  
print("cikmak icin 'q' tusuna basiniz")
secenek=int(input("""ne yapmak istiyorsunuz:\n1-Film ekleme\n2-Film cikarma
3-film duzenleme(hangiverileri)\n4-Filmleri goruntuleme
5-Filtreleme\nSeceneginizi girin: """))

#film ekleme
if secenek==1:
    film_adedi=int(input("Kac adet film gireceksiniz:"))
    for i in range(0,film_adedi):
        isim=input("Filmin ismi:")
        yonetmen=input("Yonetmen adi:")
        yili=input("yayin yili:")
        tur=input("Filmin Turu nedir:")
        filmler[isim]={
            'yonetmen':yonetmen,
            'yili':yili,
            'tur':tur,
        }
    print("Filmler eklendi.",filmler)

#Film silme
elif secenek==2:
    silme=input("silmek istediginiz filmin ismini girin:")
    if silme in filmler:
        filmler.pop(silme)
        print("film silindi. kalan liste:", filmler)
    else:
        print("Bu isimde film yok")


#Film duzeltme
elif secenek==3:
    degisik=input("hangi filmi degistirmek istiyorsun:")
    if degisik in filmler:
        sec=int(input("bu filmin hangi ozelligini degistirmek istersin:\n1-ismi\n2-yonetmen\n3-yili\n4-tur:"))
        if sec==1:
            yeni_isim=input("girmek istedginiz yeni isim:")
            filmler[yeni_isim]=filmler.pop(degisik)
        elif sec==2:
            yeni_yonetmen=input("yeni yonetmen ismi:")
            filmler[degisik]['yonetmen']=yeni_yonetmen
        elif sec==3:
            yeni_yil=input("yeni yili giriniz:")
            filmler[degisik]['yili']=yeni_yil
        elif sec==4:
            yeni_tur=input("yeni turu giriniz:")
            filmler[degisik]['tur']=yeni_tur
        else:
            print("gecersiz secim")
        print("Guncel filmler:", filmler)
    else:
        print("Bu isimde film yok.")

#Film Goruntuleme        
elif secenek==4:
    print("Film Listesi")
    for isim,bilgiler in filmler.items():
        print(f"{isim}| Yonetmen:{bilgiler['yonetmen']}| Yil:{bilgiler['yili']}| Tur:{bilgiler['tur']}")

#Filtreleme

elif secenek==5:
    filtrele=int(input("Hangi ozellige gore filtreleme istersin:\n1-tur\n2-yayinyili"))
    if filtrele==1:
        tur_sec=input("Hangi tur istersin:")
        tur_film=[]
        for keys,values in filmler.values():
            if values['tur']==tur_sec:
                tur_film.append(keys)
        print("Turlere gore filmler", tur_film)
                 
    elif filtrele==2:
        yil_sec=int(input("hangi yildaki filmleri istersin:"))
        yil_film=[]
        for keys,values in filmler.items():
            if values['yili']==yil_sec:
                yil_film.append(keys)
        print("Yillara gore filmler", yil_film)
    else:
        print("Gecersiz secim")
        
        

#Q3

print("Musteri yonetim sistemine hos geldiniz.")

musteriler = {}  # DIŞARIDA TANIMLANMALI

musteri_id = 0    # Otomatik artan ID

while True:
    secenek=int(input("""
    Ne yapmak istiyorsunuz:
    1-Musteri ekleme
    2-Musteri bilgilerini guncelleme
    3-Musteri silme(Musteri ID ile)
    4-Musteri bilgileri listeleme
    5-Cikis
    Seceneginizi girin: """))
    
    if secenek==1:
        kac_musteri=int(input("Kac musteri gireceksiniz:"))
        for i in range(kac_musteri):
            musteri_id+=1
            isim=input("Musteri ismi:")
            adres=input("Adres::")
            telefon=input("Telefon:")
            email=input("Email:")
            
            musteriler[musteri_id]={
                'isim':isim,
                'adres':adres,
                'telefon':telefon,
                'email':email,
            }
        print("Musteriler eklendi", musteriler)

    elif secenek==2:
        degisecek_musteri_id=int(input("Bilgileri degisecek musterinin ID sini giriniz:"))
        if degisecek_musteri_id in musteriler:
            sec=int(input("""Musteri bilgilerinden hangisini degistirmek istedginizi secin:
                             1-isim
                             2-Adres
                             3-Telefon
                             4-Email
                          """))
            if sec==1:
                yeni_isim=input("Yeni ismi giriniz:")
                musteriler[degisecek_musteri_id]['isim']=yeni_isim
            elif sec==2:
                yeni_adres=input("Yeni adresi giriniz:")
                musteriler[degisecek_musteri_id]['adres']=yeni_adres    
            elif sec==3:
                yeni_tel=input("Yeni telefonu giriniz:")
                musteriler[degisecek_musteri_id]['telefon']=yeni_tel
            elif sec==4:
                yeni_email=input("Yeni email giriniz:")
                musteriler[degisecek_musteri_id]['email']=yeni_email
            else:
                print("Gecersiz secim")
        else:
            print("Bu ID no lu musteri bulunamadi.")


    elif secenek==3:
        sil=int(input("Silmek istediginiz musterinin ID nosunu giriniz:"))
        if sil in musteriler:
            musteriler.pop(sil)
            print(f"Musteri {sil} silindi. KAlan liste:", musteriler)
        else:
            print("Bu ID no lu musteri bulunamadi.")


    elif secenek==4:
        print("Guncel musteri listesi")
        for isim,bilgiler in musteriler.items():
            print(f"{musteri_id} | Isim:{bilgiler['isim']} | Adres:{bilgiler['adres']} | Telefon:{bilgiler['telefon']} | Email:{bilgiler['email']}")
    elif secenek==5:
        print("Cikis yapiliyor...")
        break
    else:
        print("gecersiz secim")
        




