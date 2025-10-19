import streamlit as st
import random

st.title("🎯 Kelime Oyunu")


kelime_meyve = ["elma","armut","çilek","muz","kivi","portakal","mandalina","kavun","karpuz","erik"]
kelime_esya = ["kalem","silgi","askı","cüzdan","anahtar","telefon","masa","sandalye","yatak","bardak"]
kelime_renk = ["sarı","lacivert","mavi","kırmızı","turuncu","pembe","mor","siyah","beyaz","yeşil"]


if "kategori" not in st.session_state:
    st.session_state.kategori = None
if "kelime" not in st.session_state:
    st.session_state.kelime = ""
if "deneme" not in st.session_state:
    st.session_state.deneme = 0


kategori_sec = st.radio("Kategori Seçiniz:", ["Meyve", "Eşya", "Renk"])


if kategori_sec != st.session_state.kategori:
    st.session_state.kategori = kategori_sec
    st.session_state.deneme = 0
    if kategori_sec == "Meyve":
        st.session_state.kelime = random.choice(kelime_meyve)
        kelimeler = kelime_meyve
    elif kategori_sec == "Eşya":
        st.session_state.kelime = random.choice(kelime_esya)
        kelimeler = kelime_esya
    else:
        st.session_state.kelime = random.choice(kelime_renk)
        kelimeler = kelime_renk
else:
    if st.session_state.kategori == "Meyve":
        kelimeler = kelime_meyve
    elif st.session_state.kategori == "Eşya":
        kelimeler = kelime_esya
    else:
        kelimeler = kelime_renk


st.write("Bu kategorideki kelimeler:", ", ".join(kelimeler))
st.write(f"Kelimenin uzunluğu: {len(st.session_state.kelime)} harf")


tahmin = st.text_input("Tahmininizi giriniz:")


if st.button("Tahmin Et") and tahmin:
    st.session_state.deneme += 1
    if tahmin.lower() == st.session_state.kelime:
        st.success(f"Tebrikler! {st.session_state.deneme} denemede doğru bildiniz 🎉")
        st.balloons()
        
        if st.session_state.kategori == "Meyve":
            st.session_state.kelime = random.choice(kelime_meyve)
            kelimeler = kelime_meyve
        elif st.session_state.kategori == "Eşya":
            st.session_state.kelime = random.choice(kelime_esya)
            kelimeler = kelime_esya
        else:
            st.session_state.kelime = random.choice(kelime_renk)
            kelimeler = kelime_renk
        st.session_state.deneme = 0
        st.experimental_rerun()
    else:
        st.warning("Yanlış Cevap! Tekrar Deneyiniz!")
