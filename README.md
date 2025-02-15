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
```
locations = {
    "Lokasyon_A": {
        "coordinates": [enlem1, boylam1],  # [Enlem, Boylam]
        "scores": {
            "nufus": 90,
            "ulasim": 70,
            "maliyet": 50,
            "cevre": 75,
            "sosyal": 75
        }
    },
    "Lokasyon_B": {
        "coordinates": [enlem2, boylam2],
        "scores": {
            "nufus": 75,
            "ulasim": 80,
            "maliyet": 55,
            "cevre": 65,
            "sosyal": 70
        }
    }
}
```
## Çalıştırma
_Python'da softmax.py dosyasını çalıştırın._

### Kullanım Alanları

1. Şehir içi toplu taşıma optimizasyonu
2. Lojistik dağıtım rotaları planlama
3. Acil durum hizmetleri için en hızlı erişim rotası

## _Katkıda bulunmak için Issue açabilir veya Pull Request gönderebilirsiniz._
