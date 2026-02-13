import streamlit as st
import math, time 

st.title("_hitung _ is :blue[tabung] :rocket:")
r = st.number_input("masukan jari-jari (cm)): ",0)
t = st.number_input("masukan tinggi (cm): ",0)


if st.button("hitung jari-jari", type="primary"):
   loading = st.progress(0)
   for i in range(100):
    time.sleep(0.01)
    loading progress(i+1)
   v = math.pi*(r**2)*t
   st.success(f'tinggi tabung adalah{v:2f}')
