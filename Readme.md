# CommodiTrack

Website : https://commoditrack.lzubdev.com/

CommodiTrack is a Streamlit application for analyzing and visualizing commodity prices and production volumes.  
It connects to APIs such as Alpha Vantage to collect data, then provides interactive dashboards to track market trends and production volumes.

Website : https://commoditrack.lzubdev.com/

## 👨🏼‍💻 Goal

The goal of this project is to understand how global production volumes and market dynamics influence commodity prices, using interactive visualizations and advanced analytics.  
It also serves as a personal playground to explore end-to-end data projects: ingestion, transformation, analysis, and deployment.

## ⚙️ Infrastructure & Architecture

The app is built on a modern data stack:

- **Azure Data Factory**: Orchestration and scheduling of data pipelines
- **Azure Functions**: Automated data collection and orchestration
- **Azure Blob Storage**: Storage for raw and intermediate data
- **Snowflake**: Central data warehouse for analytics
- **dbt**: Data transformation, testing, and documentation in Snowflake
- **Azure Container App**: Deployment of dbt and Streamlit
- **Streamlit**: Interactive web dashboard for data exploration

## 📈 Data

Price and production data are collected and historized automatically.  
The analysis covers multiple years and various commodities, enabling:

- Product comparisons
- Trend detection
- Calculation of key indicators (average price, annual variations, etc.)

## 🌐 Data Sources

- **Commodity Prices: Alpha Vantage**  
  Price data is retrieved via the Alpha Vantage API, known for its high-quality financial and market time series.

- **Production: FAO (FAOSTAT)**  
  Production data comes from the FAO (Food and Agriculture Organization), via FAOSTAT, the global reference for agricultural statistics.

Pipelines (Azure Data Factory, Azure Functions) ensure automatic collection and historization, enabling comparative analysis and long-term trend monitoring.

## 🔗 Links

- **Streamlit code** :
  [🐙 GitHub dbt](https://github.com/lucaszub/commodityTrack-dbt)

---

_This project puts commodity price evolution into perspective with production volumes to better understand global market dynamics._
