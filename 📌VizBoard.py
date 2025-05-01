import io
import base64
import streamlit as st

st.set_page_config(page_title="📊 Streamlit Dashboard", layout="wide")

with st.sidebar:
    st.title("📚 Navigation")
    st.markdown("Use the menu to explore features.")

st.title("🎯 Welcome to the Smart CSV Analyzer")
st.markdown("Select a page from the sidebar to begin.")



# --- Sidebar Footer Section ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 🌐 Connect & Download")

# LinkedIn button
linkedin_url = "https://www.linkedin.com/in/harshitsingh097/"
st.sidebar.markdown(
    f"""
    <a href="{linkedin_url}" target="_blank" style="
        display: inline-block;
        background-color: #0077b5;
        color: white;
        padding: 10px 16px;
        margin: 4px 0;
        text-align: center;
        text-decoration: none;
        border-radius: 8px;
        font-weight: bold;
        font-size: 16px;
        width: 100%;
        ">
        💼 Connect on LinkedIn
    </a>
    """,
    unsafe_allow_html=True
)

# Resume download button
with open("resume.pdf", "rb") as f:
    resume_data = f.read()
b64_resume = base64.b64encode(resume_data).decode()
download_link = f"""
    <a href="data:application/pdf;base64,{b64_resume}" download="resume.pdf" style="
        display: inline-block;
        background-color: #28a745;
        color: white;
        padding: 10px 16px;
        margin: 4px 0;
        text-align: center;
        text-decoration: none;
        border-radius: 8px;
        font-weight: bold;
        font-size: 16px;
        width: 100%;
        ">
        📄 Download Resume
    </a>
"""
st.sidebar.markdown(download_link, unsafe_allow_html=True)

# Copyright
st.sidebar.markdown(
    """
    <div style="text-align: center; margin-top: 20px; color: gray; font-size: 12px;">
        © 2025 Harshit Singh
    </div>
    """,
    unsafe_allow_html=True
)

