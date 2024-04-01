# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

# Load the dataset from support.py
from support import df1, decription

# Set the page configuration
st.set_page_config(
    page_title="Statistical Analysis", page_icon=":zzz:", layout="centered"
)

# Set page title
st.title("Statistical Analysis")

# ----- Overview ----- #
# Create a subsection for the overview
st.subheader("Overview")

# Display a simple summary of the dataset
st.write("The dataset contains the following columns:")
st.table(decription)

# Show some basic descriptive statistics
st.write("Descriptive Statistics")
st.table(df1.describe())
# ----- End ----- #

# ----- Sleep Duration Analysis ----- #
st.markdown("## Sleep Duration Analysis")

# Create a histogram of sleep duration
st.plotly_chart(
    px.histogram(
        df1,
        x="Sleep Duration",
        title="Distribution of Sleep Duration",
        labels={"x": "Sleep Duration", "y": "Count"},
        marginal="",
    )
)

# Create a box plot of sleep duration
st.plotly_chart(
    px.box(
        df1,
        x="Sleep Duration",
        title="Box Plot of Sleep Duration",
        labels={"x": "Sleep Duration"},
    )
)
# ----- End ----- #


# ----- Gender-based Analysis ----- #
st.subheader("Gender-based Analysis")

# Bar plot showing number of males vs. females
st.plotly_chart(
    px.bar(
        df1,
        x=["Male", "Female"],
        y=df1["Gender"].value_counts(),
        title="Number of Males vs. Females",
        labels={"x": " Gender", "y": "Count"},
    )
)

# Violin plot showing the age distribution of males and females
df_gender = df1.copy()
df_gender = df_gender.groupby(["Gender"])
st.plotly_chart(px.violin(df1, x="Age", y="Gender"))

# Box plot showing the distribution of sleep duration by Gender
st.plotly_chart(
    px.histogram(
        df1[df1["Gender"] == "Male"],
        x="Sleep Duration",
        title="Sleep Duration Distribution for Males",
        labels={"x": "Sleep Duration", "y": "Count"},
    )
)

st.plotly_chart(
    px.histogram(
        df1[df1["Gender"] == "Female"],
        x="Sleep Duration",
        title="Sleep Duration Distribution for Females",
        labels={"x": "Sleep Duration", "y": "Count"},
    )
)

# Box plot showing the distribution of sleep quality by Gender
st.plotly_chart(px.box(df1.groupby(["Gender"]), x=0, y=["Males", "Females"])) 
# ----- End ----- #

# ----- Occupation-based Analysis ----- #
