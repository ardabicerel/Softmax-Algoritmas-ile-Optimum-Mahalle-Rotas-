import numpy
import pandas
import folium
import math
import itertools


veri_sozlugu = {
    'Mahalle': ['Karakaş', 'Karacaibrahim', 'İstasyon'],
    'Nufus': [90, 75, 85],
    'Ulasim': [70, 80, 65],
    'Maliyet': [50, 55, 65],
    'Cevre': [75, 65, 85],
    'Sosyal': [75, 70, 80]
}


veri_tablosu = pandas.DataFrame(veri_sozlugu)


def softmax(girdi_degerleri):

    maksimum_deger = numpy.max(girdi_degerleri)
    us_degerleri = numpy.exp(girdi_degerleri - maksimum_deger)
    return us_degerleri / us_degerleri.sum()


kriter_listesi = ['Nufus', 'Ulasim', 'Maliyet', 'Cevre', 'Sosyal']
for kriter in kriter_listesi:
    yeni_sutun_adi = kriter + '_softmax'
    veri_tablosu[yeni_sutun_adi] = softmax(veri_tablosu[kriter])

print("\nNormalize Edilmiş Puanlar:")
print(
    veri_tablosu[['Mahalle', 'Nufus_softmax', 'Ulasim_softmax', 'Maliyet_softmax', 'Cevre_softmax', 'Sosyal_softmax']])

kriter_agirliklari = {
    'Nufus': 0.2,
    'Ulasim': 0.2,
    'Maliyet': 0.2,
    'Cevre': 0.2,
    'Sosyal': 0.2
}


veri_tablosu['weighted_score'] = (
        veri_tablosu['Nufus_softmax'] * kriter_agirliklari['Nufus'] +
        veri_tablosu['Ulasim_softmax'] * kriter_agirliklari['Ulasim'] +
        veri_tablosu['Maliyet_softmax'] * kriter_agirliklari['Maliyet'] +
        veri_tablosu['Cevre_softmax'] * kriter_agirliklari['Cevre'] +
        veri_tablosu['Sosyal_softmax'] * kriter_agirliklari['Sosyal']
)


print("\nAğırlıklı Toplam Skorlar:")
print(veri_tablosu[['Mahalle', 'weighted_score']])


mahalle_koordinatlari = {
    'Karakaş': [41.73302948404126, 27.218009451827083],
    'Karacaibrahim': [41.73088203719272, 27.228799510116346],
    'İstasyon': [41.72995148710946, 27.205695939172912]
}


def haversine_distance(lat1, lon1, lat2, lon2):

    earth_radius = 6371.0
    lat_difference = math.radians(lat2 - lat1)
    lon_difference = math.radians(lon2 - lon1)
    a = (math.sin(lat_difference / 2) ** 2 + math.cos(math.radians(lat1)) *
         math.cos(math.radians(lat2)) * math.sin(lon_difference / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    mesafe = earth_radius * c
    return mesafe

tum_rotalar = list(itertools.permutations(mahalle_koordinatlari.keys(), 3))

en_iyi_rota = None
en_iyi_rota_orani = -1
rota_detaylari = {}

for rota in tum_rotalar:
    toplam_mesafe = 0.0
    toplam_fayda = 0.0

    onceki_mahalle = rota[0]
    fayda_ilk = veri_tablosu.loc[veri_tablosu['Mahalle'] == onceki_mahalle, 'weighted_score'].values[0]
    toplam_fayda += fayda_ilk

    for mahalle in rota[1:]:

        onceki_koordinatlar = mahalle_koordinatlari[onceki_mahalle]
        simdiki_koordinatlar = mahalle_koordinatlari[mahalle]
        mesafe = haversine_distance(onceki_koordinatlar[0], onceki_koordinatlar[1],
                                    simdiki_koordinatlar[0], simdiki_koordinatlar[1])
        toplam_mesafe += mesafe

        fayda_mevcut = veri_tablosu.loc[veri_tablosu['Mahalle'] == mahalle, 'weighted_score'].values[0]
        toplam_fayda += fayda_mevcut

        onceki_mahalle = mahalle

    if toplam_mesafe > 0:
        fayda_maliyet_orani = toplam_fayda / toplam_mesafe
    else:
        fayda_maliyet_orani = toplam_fayda

    rota_detaylari[rota] = {
        'toplam_mesafe': toplam_mesafe,
        'toplam_fayda': toplam_fayda,
        'fayda_maliyet_orani': fayda_maliyet_orani
    }

    if fayda_maliyet_orani > en_iyi_rota_orani:
        en_iyi_rota_orani = fayda_maliyet_orani
        en_iyi_rota = rota

print("\nOTOBÜS ROTA MALİYET-FAYDA ANALİZİ SONUÇLARI:")
for rota, detay in rota_detaylari.items():
    print(
        f"Rota: {rota} | Toplam Mesafe: {detay['toplam_mesafe']:.2f} km | Toplam Fayda: {detay['toplam_fayda']:.4f} | Fayda/Maliyet Oranı: {detay['fayda_maliyet_orani']:.4f}")

print(f"\nEn uygun otobüs rotası: {en_iyi_rota} (Fayda/Maliyet Oranı: {en_iyi_rota_orani:.4f})")

merkez_koordinatlari = [41.73532175834693, 27.22482472265881]
harita_objesi = folium.Map(location=merkez_koordinatlari, zoom_start=13)


for mahalle_adi, koordinatlar in mahalle_koordinatlari.items():
    marker = folium.Marker(
        location=koordinatlar,
        popup=f"{mahalle_adi} bilgisi",
        tooltip=f"{mahalle_adi}"
    )
    marker.add_to(harita_objesi)

rota_koordinat_listesi = [mahalle_koordinatlari[mahalle_adi] for mahalle_adi in en_iyi_rota]
folium.PolyLine(rota_koordinat_listesi, color="blue", weight=5, opacity=0.8).add_to(harita_objesi)

harita_objesi.save("harita.html")
