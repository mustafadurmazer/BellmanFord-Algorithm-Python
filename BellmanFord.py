def bellman_ford(dugum_sayisi, kenar_uzunlukları,kaynak_noktası):
    # Graftaki kaynak noktası hariç diğer bütün düğümlerin ağırlıkları infinitive(sonsuz) olarak belirlenir.
    agırlık = [float('inf')] * dugum_sayisi
    agırlık[kaynak_noktası] = 0
    # Kaynak noktasının ağırlıgı 0 olarak belirlenir.
    
    for _ in range(dugum_sayisi - 1):
    # dugum_sayisi N ile N-1 tane iterasyon olmalıdır.
        for kaynak, hedef , uzaklık in kenar_uzunlukları:
            if agırlık[kaynak] + uzaklık < agırlık[hedef]:
                agırlık[hedef] = agırlık[kaynak] + uzaklık
                # Her iterasyonda düğümlerin ağırlıkları yeniden değerlendirilir. 
                
    
    
    for kaynak, hedef,uzaklık in kenar_uzunlukları:
        #Eğer (dugum_sayisi-1) tane işlemden sonra hala ağırlık + uzaklık hedefın agırlıgından küçük çıkıyorsa negatif döngü vardır
        if agırlık[kaynak] + uzaklık < agırlık[hedef]:
            print("Negatif ağırlıklı döngü tespit edildi")   
            return
            # Negatif ağırlıklı döngü tespit edilirse Bellman-Ford algoritması çalışmaz.Bu yüzden fonksiyon NONE döndürür.           

    for dugum_numarası in range (1,dugum_sayisi):
        print(f"Kaynak Noktasının {dugum_numarası}. düğüme olan uzaklığı: {agırlık[dugum_numarası]}")

        
    #Eğer negatif ağırlıklı döngü yoksa fonksiyon ağırlıkları döndürür.

if __name__ == "__main__":
    dugum_sayisi = 6
    # Kenarlar ve aralarındaki mesafeler liste halinde verilmelidir.ÖRN: 0 ile 1. düğüm arasındaki mesafe 6 birimdir.
    kenarlar = [
        (0,1,6),
        (0,2,4),
        (0,3,5),
        (1,4,-1),
        (2,1,-2),
        (2,4,3),
        (3,2,-2),
        (3,5,-1),
        (4,5,3)
    ]
    
    #Kaynak noktasının hangi nokta olduğu belirtilmelidir.0 olarak belirledik.
    baslangic_dugumu = 0
    #Fonksiyon istenen parametrelerle çağırıldı.
    bellman_ford(dugum_sayisi,kenarlar,baslangic_dugumu)
    #Kaynak düğümünün diğer düğümlere olan uzaklığı yazdırıldı.
    
    
    