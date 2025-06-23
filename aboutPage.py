import streamlit as st
import pandas as pd
import datetime
# from modules.formater import Title, Footer

def AboutPage():
    st.markdown("### 👨🏼‍💻 Goal")
    st.markdown("""
    This project is dedicated to analyzing **commodity production** and **price evolution** over time.  
    The main goal is to understand how global production volumes and market dynamics impact prices, using interactive data visualizations and analytics.  
    This dashboard is also my personal playground to experiment and learn about end-to-end data projects—from data ingestion to advanced analytics and deployment.  
    If you're interested in more advanced analyses or want to collaborate, feel free to contact me!
    """)

    st.markdown("### ⚙️ Infrastructure & Architecture")
    st.markdown("""
    The project is built on a modern data stack, leveraging:
    - **Azure Data Factory** for orchestration and scheduling of data pipelines.
    - **Azure Functions** for automated data collection and orchestration.
    - **Azure Blob Storage** for storing raw and intermediate data.
    - **Snowflake** as the central data warehouse for analytics and modeling.
    - **dbt** for data transformation, testing, and documentation directly within Snowflake.
    - **Azure Container App** for deploying dbt and streamlit
    - **Streamlit** for the interactive web dashboard and data exploration interface.
    """)

    st.markdown("### 📈 Data")
    st.markdown("""
    Price and production data are collected automatically and stored historically.
    The analysis covers multiple years and various commodities, enabling comparisons, trend detection, and calculation of key indicators (average price, annual changes, etc.).
    As the project evolves, new features and more advanced statistical analyses will be added to further enrich the insights.
    """)

    st.markdown("### 🌐 Data Sources")
    st.markdown("""
    The analysis relies on two main, reliable, and automated data sources:

    - **Commodity Prices: Alpha Vantage**  
      Price data for commodities is retrieved via the Alpha Vantage API, a recognized provider of financial and market data. This API delivers historical and up-to-date time series for many assets, including commodities, ensuring an accurate view of price evolution over several years.

    - **Production Data: FAO (FAOSTAT)**  
      Production data comes from the FAO (Food and Agriculture Organization of the United Nations), through their official FAOSTAT portal. FAOSTAT regularly publishes detailed datasets on global agricultural production, trade, development flows, and other key agri-food indicators. These datasets are recognized for their reliability and international coverage.

    Data from these sources is collected automatically using orchestrated pipelines (Azure Data Factory, Azure Functions), then stored and historized to enable comparative analyses, trend monitoring, and calculation of key indicators over the long term.

    **Why these sources?**  
    - *Alpha Vantage*: Fast, structured access to market data, with an API suitable for automation.  
    - *FAO/FAOSTAT*: The global reference for agricultural statistics, ensuring robust production analysis.

    This approach provides a comprehensive view: price evolution is put into perspective with production volumes to better understand global commodity market dynamics.
    """)

    st.markdown("### 🔗 Links")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### [🐙 GitHub](https://github.com/yourusername/yourproject)")
        st.write("Source code for the project")
    with col2:
        st.markdown("### [🗂️ Kaggle](https://www.kaggle.com/yourusername/yourdataset)")
        st.write("Dataset and further details")
