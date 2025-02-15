# Genel Rota Optimizasyon Sistemi

Bu proje, herhangi bir şehir veya bölgedeki lokasyonlar için **çok kriterli optimizasyon** ile en verimli toplu taşıma rotasını belirlemek üzere tasarlanmıştır. Nüfus, ulaşım, maliyet gibi dinamik faktörler dikkate alınarak matematiksel modelleme yapar ve interaktif harita çıktısı üretir.

 
## Temel Özellikler
- **Esnek Veri Yapısı**: Lokasyon sayısı ve kriterler özelleştirilebilir.
- **Bilimsel Hesaplama**: 
  - Softmax ile kriter normalizasyonu
  - Haversine formülü ile gerçek mesafe analizi
- **Dinamik Optimizasyon**: Fayda/maliyet dengesine göre rota seçimi
- **Rota Görselleştirme**: Folium ile interaktif harita entegrasyonu

##  Hızlı Başlangıç
### Gereksinimler

```bash
pip install numpy pandas folium math itertools
```

## Veri Yapılandırma

_softmax.py dosyasında lokasyon bilgilerini tanımlayınız._ 

# Lokasyonlar ve kriterler (Örnek)

Öncelikle istediğiniz sayıdaki lokasyonların adlarını ve kriter değerlerini giriniz.
```
veri_sozlugu = {
    'Lokasyon': ['Lokasyon 1', 'Lokasyon 2', 'Lokasyon 3'],
    'Kriter 1': [90, 75, 85],
    'Kriter 2': [70, 80, 65],
    'Kriter 3': [50, 55, 65],
    'Kriter 4': [75, 65, 85],
    'Kriter 5': [75, 70, 80]
}
```


Kriterlerin önemine göre kriter ağırlıklarını belirleyiniz.
```
kriter_agirliklari = {
    'Nufus': 0.2,
    'Ulasim': 0.2,
    'Maliyet': 0.2,
    'Cevre': 0.2,
    'Sosyal': 0.2
}
```



Girdiğiniz lokasyonların enlem ve boylamlarını giriniz.
```
lokasyon_koordinatlari = {
    'Lokasyon 1': [Enlem1, Boylam1],
    'Lokasyon 2': [Enlem2, Boylam2],
    'Lokasyon 3': [Enlem3, Boylam3]
}
```

## Çalıştırma
_Python'da softmax.py dosyasını çalıştırın._

### Kullanım Alanları

1. Şehir içi toplu taşıma optimizasyonu
2. Lojistik dağıtım rotaları planlama
3. Acil durum hizmetleri için en hızlı erişim rotası

## _Katkıda bulunmak için Issue açabilir veya Pull Request gönderebilirsiniz._
