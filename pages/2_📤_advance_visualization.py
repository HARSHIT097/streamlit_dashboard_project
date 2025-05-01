import streamlit as st
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


