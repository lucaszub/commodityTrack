import streamlit as st
import pandas as pd
import altair as alt
from get_data import get_mart_production_data, get_snowflake_connection

def get_production_df():
    con = get_snowflake_connection()
    df = get_mart_production_data(con)
    return df

def show_wheat_production_histogram():
    # Palette de couleurs pour les barres
    palette = [
        "#FFFFFF", "#fffbd4", "#5EC9B3", "#4F8EF7", "#2BB3C0", "#4A90E2",
        "#6E9ECF", "#B2C6E2", "#B7D6B6", "#F9AFAE", "#F4B183", "#B4A7D6",
        "#A9D18E", "#FFD966", "#C9DAF8"
    ]
    
    df = get_production_df()
    # Renommage correct des colonnes pour correspondre au reste du code
    df = df.rename(columns={
        "COUNTRY_NAME": "area",
        "VALUE": "value",
        "TIME_YEAR": "year"
    })
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.dropna(subset=["value", "area", "year"])

    # Conversion des quantités en milliards
    df["value_billion"] = df["value"] / 1_000_000_000

    # Sélectionner l'année avec une option pour voir toutes les années
    years = sorted(df["year"].unique(), reverse=True)
    select_all = "Toutes"
    years_options = [select_all] + [str(y) for y in years]
    year_choice = st.selectbox("Année :", years_options, index=0)
    
    # Filtrer par année si un choix est fait
    if year_choice != select_all:
        filtered_df = df[df["year"] == int(year_choice)]
    else:
        filtered_df = df.copy()

    # Calcul du total mondial APRÈS filtrage (en milliards)
    total_world = filtered_df["value_billion"].sum()

    col1, col2 = st.columns(2)
    with col1:
        # Affichage du KPI production totale en petit (en milliards)
        if year_choice != select_all:
            kpi_label = f"Total wheat production in {year_choice}:"
        else:
            kpi_label = "Total wheat production (all years):"
        st.caption(f"{kpi_label} {total_world:,.2f} B tonnes")
    with col2:
        # Trouver le pays le plus producteur selon le filtre (en milliards)
        if not filtered_df.empty:
            top_producer_row = filtered_df.loc[filtered_df["value_billion"].idxmax()]
            top_country = top_producer_row["area"]
            top_value = top_producer_row["value_billion"]
            if year_choice != select_all:
                st.caption(f"🥇 {top_country} was the top producer in {year_choice} ({top_value:,.2f} B tonnes)")
            else:
                st.caption(f"🥇 {top_country} is the top producer (all years) ({top_value:,.2f} B tonnes)")
        else:
            st.caption("No data available for the selected year.")

    # Calculer les 20 pays producteurs de blé les plus importants
    top_areas = (
        filtered_df.groupby("area", as_index=False)["value_billion"]
        .sum()
        .sort_values("value_billion", ascending=False)
        .head(20)
    )
    filtered_df = filtered_df[filtered_df["area"].isin(top_areas["area"])]

    # Calculer la somme par pays (top 20)
    filtered_df = filtered_df.groupby("area", as_index=False)["value_billion"].sum()

    # Calcul du pourcentage sur la production mondiale filtrée
    filtered_df["percentage"] = filtered_df["value_billion"] / total_world
    filtered_df["percentage_label"] = (filtered_df["percentage"] * 100).map("{:.1f} %".format)

    # Ajoute cette ligne après le renommage des colonnes
    filtered_df["area_short"] = filtered_df["area"].str.slice(0, 8)

    bars = (
        alt.Chart(filtered_df)
        .mark_bar(cornerRadiusTopLeft=10, cornerRadiusBottomLeft=10)
        .encode(
            x=alt.X(
                "percentage:Q",
                title="", 
                sort=None,
                axis=alt.Axis(format="%", labels=False)
            ),
            y=alt.Y("area:N", title="Country", sort="-x"),
            color=alt.Color("area:N", scale=alt.Scale(range=palette), legend=None),
            tooltip=[
                alt.Tooltip("area:N", title="Country"),
                alt.Tooltip("percentage", title="Percentage", format=".1%"),
                alt.Tooltip("value_billion", title="Billion Tonnes", format=",.2f")
            ]
        )
    )

    text = (
        alt.Chart(filtered_df)
        .mark_text(
            align='left',
            baseline='middle',
            dx=5,
            fontSize=13,
            color='white'
        )
        .encode(
            y=alt.Y("area:N", sort="-x"),
            x=alt.X("percentage:Q"),
            text=alt.Text("percentage_label:N")
        )
    )

    chart = (
        (bars + text)
        .properties(height=650, width=500)
        .configure_view(strokeWidth=500, fill=None)
        .configure_axis(grid=False)
    )
    st.altair_chart(chart, use_container_width=True)