import streamlit as st
import pandas as pd
import plotly.express as px
import io

st.set_page_config(page_title="Interactive Session Dashboard", layout="wide")

# Sidebar Inputs
st.sidebar.title("Input Session Data")

aom_input = st.sidebar.text_input("Enter AOMs (comma-separated)", "W,S,A,C,D")
total_input = st.sidebar.text_input("Enter Total Sessions", "1200,600,800,1600,500")
current_input = st.sidebar.text_input("Enter Current Sessions", "860,450,300,1250,267")

try:
    aoms = [x.strip() for x in aom_input.split(",")]
    total_sessions = list(map(int, total_input.split(",")))
    current_sessions = list(map(int, current_input.split(",")))

    if len(aoms) != len(total_sessions) or len(aoms) != len(current_sessions):
        st.error("All input lists must have the same length.")
    else:
        # Create DataFrame
        df = pd.DataFrame({
            "AOM": aoms,
            "Total Sessions": total_sessions,
            "Current Sessions": current_sessions
        })
        df["Utilization (%)"] = (df["Current Sessions"] / df["Total Sessions"]) * 100

        st.title("📊 Session Utilization Dashboard")

        # Display Table
        st.subheader("📋 Session Data")
        st.dataframe(df, use_container_width=True)

        # Chart Selection
        st.subheader("📈 Visualization")
        chart_type = st.selectbox(
            "Select a chart to display:",
            ["Total vs Current Sessions", "Utilization Percentage", "Utilization Pie Chart"]
        )

        fig = None  # Declare upfront for download block

        if chart_type == "Total vs Current Sessions":
            fig = px.bar(df, x="AOM", y=["Total Sessions", "Current Sessions"],
                         barmode="group", title="Total vs Current Sessions")

        elif chart_type == "Utilization Percentage":
            fig = px.bar(df, x="AOM", y="Utilization (%)",
                         title="Utilization Percentage by AOM",
                         color="Utilization (%)", text="Utilization (%)")
            fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
            fig.update_layout(yaxis=dict(range=[0, 100]))

        elif chart_type == "Utilization Pie Chart":
            fig = px.pie(df, names="AOM", values="Utilization (%)",
                         title="Utilization Distribution (Percentage)",
                         hole=0.3)

        if fig:
            st.plotly_chart(fig, use_container_width=True)
            img_bytes = fig.to_image(format="png")
            st.download_button(
                label="📥 Download Chart as PNG",
                data=img_bytes,
                file_name=f"{chart_type.replace(' ', '_').lower()}.png",
                mime="image/png"
            )

except Exception as e:
    st.error(f"Input Error: {e}")
