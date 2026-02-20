import streamlit as st
import random
import time

st.title("KKU-Tahmin-Serap hocam icindir-Emredandal")

# =========================
# MOD SEÇİMİ
# =========================
mod = st.radio(
    "Oyuncu Tipini Seç:",
    ["1 - İnsan Oyuncu", "2 - Random Bilgisayar", "3 - Akıllı Bilgisayar"]
)

# =========================
# 1️⃣ İNSAN OYUNCU
# =========================
if mod == "1 - İnsan Oyuncu":

    if "sayi" not in st.session_state:
        st.session_state.sayi = random.randint(1, 100)
        st.session_state.hak = 5

    tahmin = st.number_input("Tahminini gir:", 1, 100, step=1)

    if st.button("Tahmin Et"):

        if tahmin == st.session_state.sayi:
            st.success("Doğru tahmin oldu serap hocam :)")
            st.session_state.clear()

        elif tahmin < st.session_state.sayi:
            st.warning("hocam daha büyük sayı girin.")

        else:
            st.warning("hocam daha küçük sayı girin.")

        st.session_state.hak -= 1
        st.write("Kalan hak:", st.session_state.hak)

        if st.session_state.hak == 0:
            st.error(f"Maalesef tahmin hakkı bitti hocam, Doğru sayı {st.session_state.sayi}")
            st.session_state.clear()


# =========================
# 2️⃣ RANDOM BİLGİSAYAR
# =========================
elif mod == "2 - Random Bilgisayar":

    if st.button("Başlat"):

        sayi = random.randint(1, 100)
        output = ""
        low = 1
        high = 100

        for _ in range(5):
            tahmin = random.randint(low, high)
            output += f"Random tahmin: {tahmin}\n"

            if tahmin == sayi:
                output += "Doğru tahmin!\n"
                break
            elif tahmin < sayi:
                output += "Daha büyük bir sayı.\n"
                low = tahmin + 1
            else:
                output += "Daha küçük bir sayı.\n"
                high = tahmin - 1

        else:
            output += f"Bulamadı! Doğru sayı {sayi}\n"

        st.text(output)


# =========================
# 3️⃣ AKILLI BİLGİSAYAR
# =========================
elif mod == "3 - Akıllı Bilgisayar":

    if st.button("Başlat"):

        sayi = random.randint(1, 100)
        low = 1
        high = 100
        output = ""

        while True:
            tahmin = (low + high) // 2
            output += f"Akıllı tahmin: {tahmin}\n"

            if tahmin == sayi:
                output += "Doğru tahmin!\n"
                break
            elif tahmin < sayi:
                output += "Daha büyük bir sayı.\n"
                low = tahmin + 1
            else:
                output += "Daha küçük bir sayı.\n"
                high = tahmin - 1

        st.text(output)
