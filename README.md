# Customer Segmentation Project

## Overview
This project focuses on customer segmentation using KMeans clustering and RFM (Recency, Frequency, Monetary) analysis. By dividing customers into distinct segments, businesses can better understand their customer base and target specific groups with personalized strategies.

---

## Objectives
- Segment customers into meaningful groups using KMeans clustering.
- Perform RFM analysis to understand customer behavior.
- Identify key customer segments such as Loyal Customers, Champions, Risk Customers, and New Customers.

---

## Project Workflow
1. **RFM Analysis**: 
   - Computed Recency, Frequency, and Monetary values for each customer.
   - Created 5 bins for each RFM metric based on quantiles.
2. **KMeans Clustering**:
   - Used the processed RFM data to create 4 clusters.
   - Determined the optimal number of clusters using methods like the elbow method or silhouette score.
3. **Data Analysis**:
   - Analyzed each cluster to identify patterns and insights.
   - Focused on understanding key customer groups:
     - **Loyal Customers**
     - **Champions**
     - **At Risk Customers**
     - **New Customers**

---

## Key Results
- Clear segmentation of customers into 4 clusters.
- Detailed insights into customer groups:
  - **Loyal Customers**: High frequency and monetary value, recent purchases.
  - **Champions**: Very high monetary value and frequency.
  - **At Risk Customers**: Low recency and frequency, indicating potential churn.
  - **New Customers**: Recently acquired, low frequency and monetary value.

---

## Technologies Used
- **Python**: Data analysis and clustering.
- **Libraries**:
  - `pandas`, `numpy` for data manipulation.
  - `matplotlib`, `seaborn` `plotly`for data visualization.
  - `sklearn` for KMeans clustering.

---
## Create a Virtual Environment
```
python -m venv venv
```
Activate the Virtual Environment in Windows
```
venv\Scripts\activate
```

## Install Dependencies
```
pip install -r requirements.txt
```

## Run the Project
```
streamlit run app.py
```
