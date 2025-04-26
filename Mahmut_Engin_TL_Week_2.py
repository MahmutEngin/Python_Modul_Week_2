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