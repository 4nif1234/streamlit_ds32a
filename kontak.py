import streamlit as st
import pandas as pd
import numpy as np

def tampilkan_kontak():
    st.title("Kontak")
    st.write("Hubungi saya melalui tautan berikut:")

    # LinkedIn
    st.markdown(
        "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/username)"
    )

    # GitHub
    st.markdown(
        "[![GitHub](https://img.shields.io/badge/GitHub-Profile-black)](https://github.com/username)"
    )

    # Email
    st.write("📧 Email: your.email@example.com")

def tampilkan():
    data = pd.DataFrame(np.random.randn(50, 3), columns=['A', 'B', 'C'])
    st.line_chart(data)

    st.markdown("### Filter Data")
    range_slider = st.slider("Pilih range nilai:", 0, 100, (25, 75))
    st.write(f"Anda memilih range: {range_slider}")
