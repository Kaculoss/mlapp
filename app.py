import streamlit as st

from explore_page import show_explore_page
from predict_page import show_predict_page

page = st.sidebar.selectbox("Expore Or Predict", ("Predict", "Explore"))

if page == "Explore":
    show_explore_page()
else:
    show_predict_page()
