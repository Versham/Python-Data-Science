
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import numpy as np
from datetime import datetime
from IPython.display import Video

plt.style.use("dark_background")
@st.cache
def load_data():
    df = pd.read_csv('covid_19_data.csv')
    return df

# The function plots the deaths and cases per day of a state and returns the lists 
# of cases/day and deaths/day
def plot_deaths_cases(data_original,place):
    data = data_original.reset_index()
    deaths = [0]
    j = 0
    for i in data['Deaths']:
        deaths.append(i-j)
        j = i
    deaths = deaths[2:]    
    confirmed = [0]
    j = 0
    for i in data['Confirmed']:
        confirmed.append(i-j)
        j = i 
    confirmed = confirmed[2:]
    fig,( p1,p2 )= plt.subplots(nrows=2,ncols=1,figsize=(20,10))    
    p1.plot(deaths[2:])
    p1.set_title('No of Deaths in '+place+' each day')
    p1.set_xlabel('Days')
    p1.set_ylabel('Deaths')
    p2.plot(confirmed[2:])
    p2.set_title('No of Cases in '+place+' each day')
    p2.set_xlabel('Days')
    p2.set_ylabel('Cases')
    return fig

df = load_data()


st.title('Covid 19 Data Analysis')

graph_list = ['Country/Region',
              'Total confirmed cases',
              'Covid confirmed cases in contry',
              'State wise Confirmed case',
              'State wise Death case',
              'confirmed/death cases each day in a state',
              ]


choice = st.sidebar.radio('Choose an Option', graph_list)

if choice == graph_list[0]:
    fig, ax = plt.subplots(figsize=(10, 7))
    df['Country/Region'].value_counts().head(25).plot(kind='bar')
    plt.title("Country/Region")
    st.pyplot(fig)


if choice == graph_list[1]:
    dfCon = df.groupby(
        'Country/Region')['Confirmed'].sum().reset_index().sort_values('Confirmed')
    fig, ax = plt.subplots(figsize=(10, 7))
    sns.boxplot(x='Country/Region', y='Confirmed', data=dfCon.tail())
    plt.title("Total Confirmed Cases")
    st.pyplot(fig)


if choice == graph_list[2]:
    data = df[df['Country/Region'] == 'India']
    data['Confirmed'].head(50)
    fig, ax = plt.subplots(figsize=(12, 7))
    plt.plot(data['Confirmed'])
    plt.title("Covid confirmed cases in country")
    st.pyplot(fig)

if choice == graph_list[3]:
    data = df[df['Country/Region'] == 'India']
    states = data['Province/State'].unique().tolist()
    statelist = st.sidebar.multiselect(
        'Select a Province/State', states,default=['West Bengal','Uttar Pradesh'])
    for state in statelist:
        state_df = data[data['Province/State'] == state]
        fig, ax = plt.subplots(figsize=(12, 7))
        plt.plot(state_df['Confirmed'])
        plt.title(f"{state} state wise confirmed covid cases")
        st.pyplot(fig)

if choice == graph_list[4]:
    data = df[df['Country/Region'] == 'India']
    states = data['Province/State'].unique().tolist()
    statelist = st.sidebar.multiselect(
        'Select a Province/State', states,default=['West Bengal','Uttar Pradesh'])
    for state in statelist:
        state_df = data[data['Province/State'] == state]
        fig, ax = plt.subplots(figsize=(12, 7))
        plt.plot(state_df['Deaths'])
        plt.title(f"{state} state wise deaths")
        st.pyplot(fig)


if choice == graph_list[5]:
    data = df[df['Country/Region'] == 'India']
    states = data['Province/State'].unique().tolist()
    statelist = st.sidebar.multiselect(
        'Select a Province/State', states,default=['West Bengal','Uttar Pradesh'])

    for state in statelist:
        state_df = data[data['Province/State'] == state]
        fig = plot_deaths_cases(state_df,state)
        st.pyplot(fig)
