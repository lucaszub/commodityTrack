import streamlit as st
from wheat_production_chart import show_wheat_production_histogram
from aboutPage import AboutPage as about_page
from commodity_price_trends import show_commodity_price_trends


st.sidebar.markdown("## 👋 Hey, I’m Lucas.")
st.sidebar.markdown("""
Data engineer passionate about building reliable data pipelines and BI solutions with Azure, Python, Snowflake, and Power BI.    
I enjoy creating end-to-end Azure projects, working with dbt for data transformation, and exploring new data technologies.
""")

def Price_Production_Analytics():
    st.title("🌾 Wheat Production Analytics")
    show_wheat_production_histogram()

def Commodity_Price_Trends():
    st.title("📈 Commodity Price Trends")
    show_commodity_price_trends()

def About_Page():
    st.title("ℹ️ About")
    about_page()

# Navigation avec st.navigation (personnalisée)
pages = [Price_Production_Analytics, Commodity_Price_Trends, About_Page]
pg = st.navigation(pages)
pg.run()