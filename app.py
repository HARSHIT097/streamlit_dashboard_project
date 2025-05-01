# main.py
import streamlit as st

st.set_page_config(page_title="📊 Streamlit Dashboard", layout="wide")

with st.sidebar:
    st.title("📚 Navigation")
    st.markdown("Use the menu to explore features.")

st.title("🎯 Welcome to the Smart CSV Analyzer")
st.markdown("Select a page from the sidebar to begin.")
