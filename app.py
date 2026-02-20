import random

# ======================
# OYUN MOTORU
# ======================

def play_game(player_type):
    print("\nKKU tahmin- serap hoca icindir- emredandal")

    sayı = random.randint(1, 100)
    tahmin_hakkı = 10

    low = 1
    high = 100

    while tahmin_hakkı > 0:

        # İnsan oyuncu
        if player_type == "human":
            tahmin = int(input("Tahmininizi girin: "))

        # Random bilgisayar
        elif player_type == "random":
            tahmin = random.randint(1, 100)
            print("Bilgisayar tahmini:", tahmin)

        # Akıllı bilgisayar (binary search)
        elif player_type == "smart":
            tahmin = (low + high) // 2
            print("Akıllı tahmin:", tahmin)

        else:
            print("Geçersiz oyuncu tipi.")
            return

        # Kontrol
        if tahmin == sayı:
            print("🎉 Doğru tahmin!")
            return

        elif tahmin < sayı:
            print("Daha büyük bir sayı girin.")
            low = tahmin + 1

        else:
            print("Daha küçük bir sayı girin.")
            high = tahmin - 1

        tahmin_hakkı -= 1

    print("❌ Tahmin hakkı bitti! Doğru sayı:", sayı)


# ======================
# SEÇİM MENÜSÜ
# ======================

print("1 - İnsan Oyuncu")
print("2 - Random Bilgisayar")
print("3 - Akıllı Bilgisayar")

secim = input("Seçiminiz: ")

if secim == "1":
    play_game("human")
elif secim == "2":
    play_game("random")
elif secim == "3":
    play_game("smart")
else:
    print("Hatalı seçim.")
