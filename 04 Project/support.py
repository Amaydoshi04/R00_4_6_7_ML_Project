# Description: This file contains the code to support the main file.
# It contains the code to clean the data and create visualizations.\

# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the dataset
df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

# Create a copy of the dataset
df1 = df.copy()

# Drop the Person ID column
df1 = df1.drop(["Person ID"], axis=1)

# Split blood pressure into systolic and diastolic pressure
df1["Systolic Pressure"] = df1["Blood Pressure"].apply(lambda x: int(x.split("/")[0]))
df1["Diastolic Pressure"] = df1["Blood Pressure"].apply(lambda x: int(x.split("/")[1]))

# Drop the original blood pressure column
df1 = df1.drop(["Blood Pressure"], axis=1)

decription = pd.DataFrame(
    {
        "Gender": "The gender of the person (Male/Female).",
        "Age": "The age of the person in years.",
        "Occupation": "The occupation or profession of the person.",
        "Sleep Duration (hours)": "The number of hours the person sleeps per day.",
        "Quality of Sleep (scale: 1-10)": "A subjective rating of the quality of sleep, ranging from 1 to 10.",
        "Physical Activity Level (minutes/day)": "The number of minutes the person engages in physical activity daily.",
        "Stress Level (scale: 1-10)": "A subjective rating of the stress level experienced by the person, ranging from 1 to 10.",
        "BMI Category": "The BMI category of the person (e.g., Underweight, Normal, Overweight).",
        "Blood Pressure (systolic/diastolic)": "The blood pressure measurement of the person, indicated as systolic pressure over diastolic pressure.",
        "Heart Rate (bpm)": "The resting heart rate of the person in beats per minute.",
        "Daily Steps": "The number of steps the person takes per day.",
        "Sleep Disorder": "The presence or absence of a sleep disorder in the person (None, Insomnia, Sleep Apnea).",
    },
    index=["Description"],
)

le = LabelEncoder()
ss = StandardScaler()

df2 = df1.copy()

df2['Gender'] = le.fit_transform(df2['Gender'])
df2['Occupation'] = le.fit_transform(df2['Occupation'])
df2['BMI Category'] = le.fit_transform(df2['BMI Category'])
df2['Sleep Disorder'] = le.fit_transform(df2['Sleep Disorder'])
df2['Age'] = ss.fit_transform(df2[['Age']])
df2['Sleep Duration'] = ss.fit_transform(df2[['Sleep Duration']])
df2['Physical Activity Level'] = ss.fit_transform(df2[['Physical Activity Level']])
df2['Stress Level'] = ss.fit_transform(df2[['Stress Level']])
df2['Heart Rate'] = ss.fit_transform(df2[['Heart Rate']])
df2['Daily Steps'] = ss.fit_transform(df2[['Daily Steps']])
df2['Systolic Pressure'] = ss.fit_transform(df2[['Systolic Pressure']])
df2['Diastolic Pressure'] = ss.fit_transform(df2[['Diastolic Pressure']])
df2['Quality of Sleep'] = ss.fit_transform(df2[['Quality of Sleep']])

X = df2.drop(['Sleep Disorder'], axis=1)
y = df2['Sleep Disorder']

from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler

rus = RandomUnderSampler(random_state=42)
x_u, y_u = rus.fit_resample(X, y)

ros = RandomOverSampler(random_state=42)
x_o, y_o = ros.fit_resample(X, y)


data = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
data.head()
data.drop('Person ID', axis=1, inplace=True)
data['Systolic Pressure'] = data['Blood Pressure'].apply(lambda x: int(x.split('/')[0]))
data['Diastolic Pressure'] = data['Blood Pressure'].apply(lambda x: int(x.split('/')[1])) 
data.drop(['Blood Pressure'], axis=1, inplace=True)

data.head()
data['BMI Category'].unique()
data['BMI Category'] = data['BMI Category'].replace('Normal', 'Normal Weight')
data['BMI Category'].unique()
from sklearn.preprocessing import StandardScaler, LabelEncoder
le_gender = LabelEncoder()
le_gender.fit_transform(data['Gender'])
le_gender_mapping = dict(zip(le_gender.classes_, le_gender.transform(le_gender.classes_)))
print(le_gender_mapping)
ss_age = StandardScaler()
ss_age.fit_transform(data[['Age']])
ss_age.mean_, ss_age.scale_
le_occupation = LabelEncoder()
le_occupation.fit_transform(data['Occupation'])
le_occupation_mapping = dict(zip(le_occupation.classes_, le_occupation.transform(le_occupation.classes_)))
print(le_occupation_mapping)
ss_sleep_duration = StandardScaler()
ss_sleep_duration.fit_transform(data[['Sleep Duration']])
ss_sleep_duration.mean_, ss_sleep_duration.scale_
ss_quality_of_sleep = StandardScaler()
ss_quality_of_sleep.fit_transform(data[['Quality of Sleep']])
ss_quality_of_sleep.mean_, ss_quality_of_sleep.scale_
ss_physical_activity_level = StandardScaler()
ss_physical_activity_level.fit_transform(data[['Physical Activity Level']])
ss_physical_activity_level.mean_, ss_physical_activity_level.scale_
ss_stress_level = StandardScaler()
ss_stress_level.fit_transform(data[['Stress Level']])
ss_stress_level.mean_, ss_stress_level.scale_
le_bmi_category = LabelEncoder()
le_bmi_category.fit_transform(data['BMI Category'])
le_bmi_category_mapping = dict(zip(le_bmi_category.classes_, le_bmi_category.transform(le_bmi_category.classes_)))
print(le_bmi_category_mapping)
ss_heart_rate = StandardScaler()
ss_heart_rate.fit_transform(data[['Heart Rate']])
ss_heart_rate.mean_, ss_heart_rate.scale_
ss_daily_steps = StandardScaler()
ss_daily_steps.fit_transform(data[['Daily Steps']])
ss_daily_steps.mean_, ss_daily_steps.scale_
ss_systolic_pressure = StandardScaler()
ss_systolic_pressure.fit_transform(data[['Systolic Pressure']])
ss_systolic_pressure.mean_, ss_systolic_pressure.scale_
ss_diastolic_pressure = StandardScaler()
ss_diastolic_pressure.fit_transform(data[['Diastolic Pressure']])
ss_diastolic_pressure.mean_, ss_diastolic_pressure.scale_

def preprocessor(og_data, le_gender_mapping, le_occupation_mapping, le_bmi_category_mapping, ss_age, ss_sleep_duration, ss_quality_of_sleep, ss_physical_activity_level, ss_stress_level, ss_heart_rate, ss_daily_steps, ss_systolic_pressure, ss_diastolic_pressure):
    preprocessed_data = dict()

    preprocessed_data['gender'] = le_gender_mapping[og_data['gender']]
    preprocessed_data['age'] = ss_age.transform([[og_data['age']]])[0][0]
    preprocessed_data['occupation'] = le_occupation_mapping[og_data['occupation']]
    preprocessed_data['sleep_duration'] = ss_sleep_duration.transform([[og_data['sleep_duration']]])[0][0]
    preprocessed_data['sleep_quality'] = ss_quality_of_sleep.transform([[og_data['sleep_quality']]])[0][0]
    preprocessed_data['activity_level'] = ss_physical_activity_level.transform([[og_data['activity_level']]])[0][0]
    preprocessed_data['stress_level'] = ss_stress_level.transform([[og_data['stress_level']]])[0][0]
    preprocessed_data['bmi_category'] = le_bmi_category_mapping[og_data['bmi_category']]
    preprocessed_data['heart_rate'] = ss_heart_rate.transform([[og_data['heart_rate']]])[0][0]
    preprocessed_data['steps_per_day'] = ss_daily_steps.transform([[og_data['steps_per_day']]])[0][0]
    preprocessed_data['systolic_bp'] = ss_systolic_pressure.transform([[og_data['systolic_bp']]])[0][0]
    preprocessed_data['diastolic_bp'] = ss_diastolic_pressure.transform([[og_data['diastolic_bp']]])[0][0]

    return preprocessed_data

le_sleep_disorder_mapping = {'Insomnia': 0, 'None': 1, 'Sleep Apnea': 2}
le_sleep_disorder_mapping2 = {'0': 'Insomnia', '1': 'None', '2': 'Sleep Apnea'}