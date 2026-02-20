import random
import streamlit as st
import matplotlib.pyplot as plt

# Sayı aralığı
MIN = 1
MAX = 1_000_000

st.title("Algoritma Performans Karşılaştırması")
st.write("1 milyon ihtimal arasında Random vs Smart tahmin karşılaştırması")

# --------------------------
# RANDOM OYUNCU
# --------------------------
def random_player(secret):
    low = MIN
    high = MAX
    attempts = 0

    while True:
        guess = random.randint(low, high)
        attempts += 1

        if guess == secret:
            return attempts
        elif guess < secret:
            low = guess + 1
        else:
            high = guess - 1


# --------------------------
# SMART OYUNCU (Binary Search)
# --------------------------
def smart_player(secret):
    low = MIN
    high = MAX
    attempts = 0

    while True:
        guess = (low + high) // 2
        attempts += 1

        if guess == secret:
            return attempts
        elif guess < secret:
            low = guess + 1
        else:
            high = guess - 1


# --------------------------
# SİMÜLASYON
# --------------------------
def simulate(player_func, games=200):
    total = 0
    for _ in range(games):
        secret = random.randint(MIN, MAX)
        total += player_func(secret)
    return total / games


# --------------------------
# BUTON
# --------------------------
if st.button("Simülasyonu Başlat"):

    st.write("Simülasyon çalışıyor...")

    random_avg = simulate(random_player)
    smart_avg = simulate(smart_player)

    st.success("Simülasyon tamamlandı!")

    st.write("Random Ortalama Deneme:", round(random_avg, 2))
    st.write("Smart Ortalama Deneme:", round(smart_avg, 2))

    players = ["Random", "Smart"]
    averages = [random_avg, smart_avg]

    fig, ax = plt.subplots()
    ax.bar(players, averages)
    ax.set_ylabel("Ortalama Deneme Sayısı")
    ax.set_title("1.000.000 Arasında Tahmin Performansı")

    st.pyplot(fig)

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Basit Simülasyon")

n = st.slider("Kaç kez denensin?", 10, 10000, 1000)

data = np.random.normal(0, 1, n)

fig, ax = plt.subplots()
ax.hist(data, bins=30)

st.pyplot(fig)
