import streamlit as st
from streamlit_autorefresh import st_autorefresh
from dashboard_page import show_dashboard
import pandas as pd

st.set_page_config(page_title="Customer Analytics", layout="wide")


st.markdown("""
<h1 style='text-align: center; color: #1f77b4; font-size: 48px; font-family: "Arial Black", Gadget, sans-serif;'>
Customer Analytics Dashboard
</h1>
""", unsafe_allow_html=True)

st.divider()

tab1, tab2 = st.tabs(["Home", "Dashboard"])

count = st_autorefresh(interval=3000, limit=None, key="auto")


with tab1:
    st.markdown("<h3 style='text-align:center;'>Welcome to the Home Page!</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Your one-stop analytics portal for SaaS insights.</p>", unsafe_allow_html=True)

    images = [
        "https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg",
        "https://images.pexels.com/photos/3184295/pexels-photo-3184295.jpeg",
        "https://images.pexels.com/photos/3184465/pexels-photo-3184465.jpeg"
    ]

    img_index = count % len(images)
    st.image(images[img_index], width=1000, caption=f"Slide {img_index+1}")

with tab2:
    show_dashboard()