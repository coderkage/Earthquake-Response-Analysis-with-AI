import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.write("Polayaadi Mone")

x = st.text_input("hello guys chai pi lo")

st.write(x)

st.write("mewing?")
y = st.button("🤫🧏‍♀️")
z = st.button("what's mewing?")
a = st.button("clear")
if a:
    pass
elif y:
    st.write("bye bye")

elif z:
    st.write("It's over for you")