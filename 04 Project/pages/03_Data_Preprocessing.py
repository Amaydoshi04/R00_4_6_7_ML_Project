# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

# Load the dataset from support.py
from support import df, df1, decription, x_u, y_u, x_o, y_o

# Set the page configuration
st.set_page_config(
    page_title="Data Preprocessing", page_icon=":zzz:", layout="centered"
)

# Set page title
st.title("Data Preprocessing")

# Display the first 5 rows of the dataset
st.markdown("### Dataset Preview")

with st.expander("Click here to view the dataset"):
    st.write(df)

# Basic information about the dataset
st.markdown("### Basic Information")

# Shape
st.markdown("#### Shape of the Dataset")
st.write(f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

# Columns
st.markdown("#### Features in the Dataset")
st.write(decription)

# Data types
st.markdown("#### Data Types")
st.table(df.dtypes)

# Data cleaning
st.markdown("### Data Cleaning")
st.markdown("#### Dropping Columns")
st.write("We will drop the 'Person ID' column as it is not required for our analysis.")
st.code("df1 = df.drop(['Person ID'], axis=1)")

# Splitting the 'Blood Pressure' column
st.markdown("#### Splitting and Dropping the 'Blood Pressure' Column")
st.write(
    "We will split the 'Blood Pressure' column into 'Systolic Pressure' and 'Diastolic Pressure' as the original attribute is unusable."
)
st.code(
    "df1['Systolic Pressure'] = df1['Blood Pressure'].apply(lambda x: int(x.split('/')[0]))"
)
st.code(
    "df1['Diastolic Pressure'] = df1['Blood Pressure'].apply(lambda x: int(x.split('/')[1]))"
)
st.code("df1 = df1.drop(['Blood Pressure'], axis=1)")

# Checking Null Values
st.markdown("#### Checking for Null Values")
st.table(df1.isnull().sum())

# Checking Size of Classes
st.markdown("### Checking the Size of Classes")
st.plotly_chart(
    px.pie(
        df,
        names="Sleep Disorder",
        title="Sleep Disorder Distribution",
        hole=0.5,
        labels=["None", "Sleep Apnea", "Insomnia"],
    )
)

# Descriptive Statistics
st.markdown("### Descriptive Statistics")
st.table(df1.describe())

# Unique Values for each categorical column
st.markdown("#### Unique Values for Categorical Columns")
for col in df1.select_dtypes(include=["object"]).columns:
    st.write(f"**{col}** : {df1[col].unique()}")


st.write(
    "Since the classes are imbalanced, we have two approaches to handle this:\n\n 1.Under-sampling and \n\n 2.Over-sampling."
)

# Under-sampling
st.markdown("#### Under-sampling")
st.write(
    "Under-sampling involves removing samples from the majority class to balance the dataset."
)
st.write(
    "First, we will split the features and labels into two separate variables.\nWe will use X for our features and y for our labels."
)
st.code("X = df.drop(['Sleep Disorder'], axis=1)\ny = df['Sleep Disorder']")


st.code(
    "from imblearn.under_sampling import RandomUnderSampler\nrus = RandomUnderSampler(random_state=42)\nx_res, y_res = rus.fit_resample(X, y)"
)

# substitute values in y_u
y_u = pd.Series(y_u)
y_u = y_u.replace(0, "None")
y_u = y_u.replace(1, "Sleep Apnea")
y_u = y_u.replace(2, "Insomnia")
st.plotly_chart(
    px.pie(y_u, names="Sleep Disorder", title="Sleep Disorder Distribution", hole=0.5)
)
st.write("Each class is of size 77")

# Over-sampling
st.markdown("#### Over-sampling")
st.write(
    "Over-sampling involves adding more copies of the minority class to balance the dataset."
)
st.write("We have used the default SMOTE technique.")

st.code(
    "from imblearn.over_sampling import RandomOverSampler\nros = RandomOverSampler(random_state=42)\nx_res, y_res = ros.fit_resample(X, y)"
)

# substitute values in y_o
y_o = pd.Series(y_o)
y_o = y_o.replace(0, "None")
y_o = y_o.replace(1, "Sleep Apnea")
y_o = y_o.replace(2, "Insomnia")

st.plotly_chart(
    px.pie(y_o, names="Sleep Disorder", title="Sleep Disorder Distribution", hole=0.5)
)

st.write("Each class is of size 219")
