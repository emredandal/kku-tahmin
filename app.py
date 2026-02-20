import streamlit as st
import random

st.title("KKU Tahmin-SerapHocaicindir-Emredandal")

# Mod seçimi
mod = st.radio(
    "Oyuncu Tipini Seç:",
    ["1 - İnsan Oyuncu", "2 - Random Bilgisyar", "3 - Akıllı Bilgisayar"]
)

# Session state ile sayı saklama
if "sayi" not in st.session_state:
    st.session_state.sayi = random.randint(1, 100)
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.hak = 5

# ==========================
# 1️⃣ İnsan Oyuncu
# ==========================
if mod == "1 - İnsan Oyuncu":

    tahmin = st.number_input("Tahminini gir:", 1, 100)

    if st.button("Tahmin Et"):
        if tahmin == st.session_state.sayi:
            st.success("Doğru Tahmin Hocamm :)")
            st.session_state.clear()

        elif tahmin < st.session_state.sayi:
            st.warning("Daha büyük sayı girin hocam.")

        else:
            st.warning("Daha küçük sayı girin hocam.")

        st.session_state.hak -= 1
        st.write("Kalan hak:", st.session_state.hak)

        if st.session_state.hak == 0:
            st.error(f" Bitti! Doğru sayı {st.session_state.sayi}")
            st.session_state.clear()


# ==========================
# 2️⃣ Random Bilgisayar
# ==========================
elif mod == "2 - Random Bilgisayar":

    if st.button("Bilgisayar Tahmin Etsin"):

        tahmin = random.randint(
            st.session_state.low,
            st.session_state.high
        )

        st.write("Random tahmin:", tahmin)

        if tahmin == st.session_state.sayi:
            st.success(" Bilgisayar buldu!")
            st.session_state.clear()

        elif tahmin < st.session_state.sayi:
            st.session_state.low = tahmin + 1
            st.warning("Daha büyük.")

        else:
            st.session_state.high = tahmin - 1
            st.warning("Daha küçük.")


# ==========================
# 3️⃣ Akıllı Bilgisayar
# ==========================
elif mod == "3 - Akıllı Bilgisayar":

    if st.button("Akıllı Tahmin Yap"):

        tahmin = (st.session_state.low + st.session_state.high) // 2

        st.write("Akıllı tahmin:", tahmin)

        if tahmin == st.session_state.sayi:
            st.success("Akıllı bilgisayar buldu!")
            st.session_state.clear()

        elif tahmin < st.session_state.sayi:
            st.session_state.low = tahmin + 1
            st.warning("Daha büyük.")

        else:
            st.session_state.high = tahmin - 1
            st.warning("Daha küçük.")
