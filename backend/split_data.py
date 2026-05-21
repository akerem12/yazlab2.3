import os
import shutil
import random

# Klasör yolları ayarları
RAW_DATA_DIR = "raw_data"
DATASET_DIR = "dataset"
SPLIT_RATIO = 0.8  # %80 Train, %20 Val olacak şekilde böler

# İlk betikteki ile birebir aynı sınıf isimleri
siniflar = [
    "SUV",
    "VAN",
    "STATION_WAGON",
    "MICRO",
    "ACIK_TEKERLEKLI",
    "SEDAN",
    "HATCHBACK",
    "PICK_UP"
]

def verileri_dagit():
    print("Veri dağıtım işlemi başlıyor...\n")
    
    for sinif in siniflar:
        raw_sinif_yolu = os.path.join(RAW_DATA_DIR, sinif)
        train_sinif_yolu = os.path.join(DATASET_DIR, "train", sinif)
        val_sinif_yolu = os.path.join(DATASET_DIR, "val", sinif)
        
        # Eğer raw_data içinde bu sınıfın klasörü yoksa uyar ve atla
        if not os.path.exists(raw_sinif_yolu):
            print(f"⚠️ Uyarı: '{raw_sinif_yolu}' klasörü bulunamadı, atlanıyor.")
            continue
            
        # Klasördeki görselleri listele (sadece dosya olanları al)
        gorseller = [f for f in os.listdir(raw_sinif_yolu) if os.path.isfile(os.path.join(raw_sinif_yolu, f))]
        
        if len(gorseller) == 0:
            print(f"⚠️ Uyarı: '{sinif}' klasörü boş, atlanıyor.")
            continue
            
        # Görselleri rastgele karıştır (Modelin ezberlemesini önler)
        random.shuffle(gorseller)
        
        # Bölme noktasını (index) hesapla
        split_index = int(len(gorseller) * SPLIT_RATIO)
        train_gorseller = gorseller[:split_index]
        val_gorseller = gorseller[split_index:]
        
        # Train görsellerini kopyala
        for g in train_gorseller:
            kaynak = os.path.join(raw_sinif_yolu, g)
            hedef = os.path.join(train_sinif_yolu, g)
            shutil.copy(kaynak, hedef)
            
        # Validation görsellerini kopyala
        for g in val_gorseller:
            kaynak = os.path.join(raw_sinif_yolu, g)
            hedef = os.path.join(val_sinif_yolu, g)
            shutil.copy(kaynak, hedef)
            
        print(f"✅ {sinif}: Toplam {len(gorseller)} görsel -> {len(train_gorseller)} Train, {len(val_gorseller)} Val olarak ayrıldı.")

    print("\n🎉 Tüm veri dağıtımı başarıyla tamamlandı!")

if __name__ == "__main__":
    verileri_dagit()