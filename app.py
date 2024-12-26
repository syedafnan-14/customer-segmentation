import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Customer Segmentation Using RFM")

kmeans = joblib.load("customer_segmentation_model.pkl")
rfm = pd.read_csv("Customer_Segmentation.csv")

def predict_rfm(num1,num2,num3):
    data = pd.DataFrame(data=[[num1,num2,num3]],columns=["Recency_Score","Frequency_Score","Monetary_Score"])
    pred = kmeans.predict(data)
    label = ['Loyal Customer','Champion','At Risk','New Customer']
    return label[pred[0]]
    


col1,col2,col3 = st.columns(3)
num1 = col1.number_input("Recency_Score (1-5):", min_value=1, max_value=5, step=1, value=1)
num2 = col2.number_input("Frequency_Score (1-5):", min_value=1, max_value=5, step=1, value=1)
num3 = col3.number_input("Monetary_Score (1-5):", min_value=1, max_value=5, step=1, value=1)

value = ""
if st.button(label="Predict"):
    value = predict_rfm(num1,num2,num3)

st.markdown(f"<span style='font-size:20px; font-weight:bold; font-style:italic'>{value}</span>",unsafe_allow_html=True)


custom_colors = {
    'Loyal Customers': '#99ff99',  
    'Champions': '#66b3ff',        
    'At Risk Customers': '#ff9999',  
    'New Customers': '#ffcc99'     
}

figpx = px.scatter_3d(
    rfm,
    x='log_Recency',
    y='log_Frequency',
    z='log_Monetary',
    color='Cluster Labels',  
    color_discrete_map=custom_colors,  
    labels={'log_Recency': 'Recency', 'log_Frequency': 'Frequency', 'log_Monetary': 'Monetary'},
    title='Customer Segmentation Visualization'
)
st.plotly_chart(figpx)



customers = rfm.shape[0]
labels = ['Loyal Customers','Champions','At Risk Customers','New Customers']
sizes = (rfm["Clusters"].value_counts()/customers)*100
colors = ['#99ff99', '#66b3ff', '#ff9999', '#ffcc99']

fig,ax = plt.subplots(figsize=(8,6))

ax.pie(
    sizes, labels=labels, colors=colors, autopct='%1.1f%%',
    startangle=120, wedgeprops={'edgecolor': 'black'}
)

ax.set_title('Customer Segmentation', fontsize=14)
ax.legend([0,1,2,3],title='Clusters',loc='best',)
st.pyplot(fig)