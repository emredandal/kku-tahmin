import streamlit as st
import random
import matplotlib.pyplot as plt

st.title("KKU Tahmin serap hoca icindir - Emredandal")

# MOD SEÇİMİ
mod = st.radio(
    "Oyun Modunu Seç:",
    ["1 - Normal Oyun", "2 - Simülasyon", "3 - Akıllı Bilgisayar"]
)

# ---------------------------
# 1️⃣ NORMAL OYUN
# ---------------------------
if mod == "1 - Normal Oyun":

    if "sayi" not in st.session_state:
        st.session_state.sayi = random.randint(1, 100)
        st.session_state.hak = 5

    tahmin = st.number_input("Tahminini gir:", min_value=1, max_value=100, step=1)

    if st.button("Tahmin Et"):

        if tahmin == st.session_state.sayi:
            st.success(" Tebrikler doğru tahmin!")
            st.session_state.clear()

        elif tahmin < st.session_state.sayi:
            st.warning("Daha büyük sayı gir.")

        else:
            st.warning("Daha küçük sayı gir.")

        st.session_state.hak -= 1

        if st.session_state.hak == 0:
            st.error(f" Hakkın bitti! Doğru sayı {st.session_state.sayi}")
            st.session_state.clear()


# ---------------------------
# 2️⃣ SİMÜLASYON
# ---------------------------
elif mod == "2 - Simülasyon":

    if st.button("Simülasyonu Başlat"):

        deneme_sayilari = []

        for _ in range(1000):
            sayi = random.randint(1, 100)
            alt = 1
            ust = 100
            deneme = 0

            while True:
                deneme += 1
                tahmin = (alt + ust) // 2

                if tahmin == sayi:
                    break
                elif tahmin < sayi:
                    alt = tahmin + 1
                else:
                    ust = tahmin - 1

            deneme_sayilari.append(deneme)

        plt.hist(deneme_sayilari)
        plt.xlabel("Tahmin Sayısı")
        plt.ylabel("Frekans")
        st.pyplot(plt)


# ---------------------------
# 3️⃣ AKILLI BİLGİSAYAR
# ---------------------------
elif mod == "3 - Akıllı Bilgisayar":

    if st.button("Bilgisayar Tahmin Etsin"):

        sayi = random.randint(1, 100)
        alt = 1
        ust = 100
        deneme = 0

        while True:
            deneme += 1
            tahmin = (alt + ust) // 2

            if tahmin == sayi:
                st.success(f"Bilgisayar {deneme} tahminde buldu!")
                break
            elif tahmin < sayi:
                alt = tahmin + 1
            else:
                ust = tahmin - 1
