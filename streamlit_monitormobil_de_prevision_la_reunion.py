import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Monito Réunion", layout="wide", initial_sidebar_state="expanded")
st.title("📊 Monito de Prévision des Réunions")

st.sidebar.header("Filtres de données")
selected_date = st.sidebar.date_input("Sélectionner une date")
mobile_list = ["Mobile A", "Mobile B", "Mobile C"]
selected_mobile = st.sidebar.selectbox("Choisir un mobile", mobile_list)

@st.cache_data
def load_data():
    data = pd.DataFrame({
        "Date": pd.date_range(start="2025-01-01", periods=10).tolist()*3,
        "Valeur": [10, 15, 12, 18, 20, 25, 22, 30, 28, 35]*3,
        "Mobile": ["Mobile A"]*10 + ["Mobile B"]*10 + ["Mobile C"]*10
    })
    return data

data = load_data()
filtered_data = data[(data["Date"] == pd.Timestamp(selected_date)) & (data["Mobile"] == selected_mobile)]

st.subheader(f"Prévision pour {selected_mobile} le {selected_date}")
col1, col2 = st.columns(2)

with col1:
    st.write("### Données brutes")
    if not filtered_data.empty:
        st.dataframe(filtered_data)
    else:
        st.write("Aucune donnée disponible pour cette sélection.")

with col2:
    st.write("### Graphique")
    if not filtered_data.empty:
        fig = px.line(filtered_data, x="Date", y="Valeur", title="Prévision")
        fig.update_layout(width=None, height=400)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("Aucun graphique à afficher.")

with st.expander("Détails supplémentaires"):
    st.write("Ajouter ici des analyses ou commentaires complémentaires.")
