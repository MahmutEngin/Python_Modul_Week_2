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



### Question 3: Customer Management System
def menu():
    print("""
        1) Yemi musteri eklemek icin "1" e basiniz.
        2) Musteri bilgilerini duzenlemek icin "2" e basiniz.
        3) Musteri bil;gilerini silmek icin "3" e basiniz.
        4) Musterileri listelemek icin "4" e basiniz.
        4) Cikmak icin "q" e basiniz.
        """) 
musteriler={}
while True:
    menu()
    secim = input("Seciminizi yapiniz: ")
    if secim in  ["1","2","3","4","q"]:
        if secim=="q":
           break
        if secim=="1": # musteri Ekleme
           ide = input("Musteri idesini giriniz:")          
           ad= input("Musteri adini giriniz:")
           soyad= input("Musteri soyadini giriniz:")
           e_posta = input("Musteri mail adresini giriniz:")
           telefon = input("Musteri telefon numarasini giriniz:")
           musteriler[ide]=[ad,soyad,e_posta,telefon]
           print(musteriler)
        if secim=="2":
           ide = input("Musteri idesini giriniz:")    
           if ide in musteriler:
                ad = input("Yeni ad (degisiklik olmayacaksa enter'a basiniz) ")
                soyad = input("Yeni soyad (degisiklik olmayacaksa enter'a basiniz) : ")
                e_posta = input("Yeni e-posta (degisiklik olmayacaksa enter'a basiniz)  : ")
                telefon = input("Yeni telefon (degisiklik olmayacaksa enter'a basiniz) : ")
                if ad:
                    musteriler[ide][0]=ad
                if soyad:
                    musteriler[ide][1]=soyad
                if e_posta:
                    musteriler[ide][2]=e_posta
                if  telefon:
                    musteriler[ide][3]= telefon
                print(musteriler)
