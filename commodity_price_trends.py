import streamlit as st
import pandas as pd
import altair as alt
from get_data import get_snowflake_connection, get_mart_price_data

def get_price_df():
    con = get_snowflake_connection()
    df = get_mart_price_data(con)
    return df

def show_commodity_price_trends():
    df = get_price_df()
    df["PRICE_DATE"] = pd.to_datetime(df["PRICE_DATE"])
    df["YEAR"] = df["PRICE_DATE"].dt.year
    df["MONTH"] = df["PRICE_DATE"].dt.strftime("%b")
    df["MONTH_NUM"] = df["PRICE_DATE"].dt.month
    df["YEAR_MONTH"] = df["PRICE_DATE"].dt.to_period("M").astype(str)

    # KPIs globaux dans des colonnes (format petit, style wheat_production_chart)
    col1, col2 = st.columns(2)
    with col1:
        st.caption(f"Total Records: {len(df):,}")
    with col2:
        st.caption(f"Average Price (all commodities): {df['VALUE'].mean():,.2f}")

    # Sélection de la matière première
    st.subheader("Price Evolution")
    commodities = df["COMMODITY_NAME"].unique()
    commodity_choice = st.selectbox("Select Commodity:", commodities)

    # Filtres sous le selectbox
    filter_option = st.radio(
        "Select period:",
        ("All", "Last 10 years", "Last 5 years", "Last 36 months", "Last 12 months"),
        horizontal=True
    )

    filtered_df = df[df["COMMODITY_NAME"] == commodity_choice].sort_values("PRICE_DATE")

    if filter_option == "Last 12 months":
        plot_df = filtered_df.tail(12)
        chart = (
            alt.Chart(plot_df)
            .mark_area(point=True)
            .encode(
                x=alt.X("YEAR_MONTH:N", title="Month"),
                y=alt.Y("VALUE:Q", title="Average Price (per t)"),
                tooltip=[
                    alt.Tooltip("YEAR_MONTH:N", title="Year-Month"),
                    alt.Tooltip("VALUE:Q", title="Average Price (per tonne)")
                ]
            )
            .properties(
                height=350,
                title=f"{commodity_choice} Price - Last 12 Months"
            )
        )
    elif filter_option == "Last 36 months":
        plot_df = filtered_df.tail(36)
        chart = (
            alt.Chart(plot_df)
            .mark_area(point=True)
            .encode(
                x=alt.X("YEAR_MONTH:N", title="Month"),
                y=alt.Y("VALUE:Q", title="Average Price (per t)"),
                tooltip=[
                    alt.Tooltip("YEAR_MONTH:N", title="Year-Month"),
                    alt.Tooltip("VALUE:Q", title="Average Price (per tonne)")
                ]
            )
            .properties(
                height=350,
                title=f"{commodity_choice} Price - Last 36 Months"
            )
        )
    else:
        if filter_option == "Last 5 years":
            min_year = filtered_df["YEAR"].max() - 4
        elif filter_option == "Last 10 years":
            min_year = filtered_df["YEAR"].max() - 9
        else:
            min_year = filtered_df["YEAR"].min()
        plot_df = filtered_df[filtered_df["YEAR"] >= min_year]
        grouped = plot_df.groupby("YEAR", as_index=False)["VALUE"].mean()
        chart = (
            alt.Chart(grouped)
            .mark_area(point=True)
            .encode(
                x=alt.X("YEAR:O", title="Year"),
                y=alt.Y("VALUE:Q", title="Average Price (per t)"),
                tooltip=[
                    alt.Tooltip("YEAR:O", title="Year"),
                    alt.Tooltip("VALUE:Q", title="Average Price (per tonne)")
                ]
            )
            .properties(
                height=350,
                title=f"{commodity_choice} Price - {filter_option}"
            )
        )

    st.altair_chart(chart, use_container_width=True)