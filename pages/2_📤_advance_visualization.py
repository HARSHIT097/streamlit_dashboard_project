import streamlit as st
import base64
import streamlit.components.v1 as components

st.set_page_config(page_title="CSV Analyzer", layout="wide")

st.title("📂 CSV Data Analyzer Dashboard")
st.markdown("""
Upload a CSV file to explore its structure, perform preprocessing, and generate insightful visualizations from its features.
""")

st.markdown("---")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Load default if nothing is uploaded
if uploaded_file is not None:
    import pandas as pd
    df = pd.read_csv(uploaded_file)
    st.success("Uploaded file successfully loaded.")
else:

    import pandas as pd
    import plotly.express as px
    import seaborn as sns
    import matplotlib.pyplot as plt
    import io
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import classification_report
    from ydata_profiling import ProfileReport

    df = pd.read_csv("WineQT.csv")
    st.info("Default file 'abc.csv' is loaded.")

    st.subheader("📄 Data Preview")
    st.dataframe(df.head())

    st.subheader("📊 Data Summary")
    st.write(df.describe())

    st.subheader("🧹 Select Preprocessing Options")
    if st.checkbox("Drop missing values"):
        df.dropna(inplace=True)
        st.info("Dropped missing values.")

    st.subheader("🔍 Automated Profiling (Pandas Profiling)")
    if st.checkbox("Run Pandas Profiling Report"):
        from ydata_profiling import ProfileReport
        profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
        components.html(profile.to_html(), height=1000, scrolling=True)

    st.subheader("🤖 Quick ML Model Preview")
    if st.checkbox("Run ML preview (classification)"):
        target_col = st.selectbox("Select target column", df.columns)
        if st.button("Train Model"):
            X = df.drop(columns=[target_col])
            y = df[target_col]
            X = pd.get_dummies(X, drop_first=True)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            st.text("Classification Report:")
            st.text(classification_report(y_test, y_pred,  zero_division=0))



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

