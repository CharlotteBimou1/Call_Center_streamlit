# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 17:34:46 2021

@author: Charlotte BIMOU
"""
import streamlit as st
import pandas as pd
import numpy as np
from fbprophet import Prophet
from fbprophet.diagnostics import performance_metrics
from fbprophet.diagnostics import cross_validation
from fbprophet.plot import plot_cross_validation_metric
import base64

st.title('Prévision journalière du Volume des Appels client')

st.write("IMPORT DES DONNEES")
st.write("Import des données au format csv. La base de données doit avoir deux colonnes nommées comme suit 'ds' et 'y'.La colonne 'ds' doit être au format date. La colonne 'y' doit être numerique représentant les données à prévoire.")

#data = pd.read_csv('C://Users//lenoa//TS_streamlit//Call_Center_streamlit//call_abandoned_trend.csv')
data = pd.read_csv("call_volume_trend.csv")

if data is not None:
    appdata = pd.read_csv("call_volume_trend.csv")
    appdata['ds'] = pd.to_datetime(appdata['ds'],errors='coerce') 
    
    st.write(data)
    
    max_date = appdata['ds'].max()

st.write("SELECTION DE LA PERIODE DE PREVISION")

periods_input = st.number_input('Combien de jours de prévision voulez-vous ?',
min_value = 1, max_value = 365)

if data is not None:
    obj = Prophet()
    obj.fit(appdata)

st.write("VISUALISATION DES DONNEES PREDITES")
st.write("Le graphique suivant montre les futures valeurs prédites. 'yhat' est la valeur prédire; upper et lower sont les bornes de l'intervalle de confiance par défaut 80%")

if data is not None:
    future = obj.make_future_dataframe(periods=periods_input)
    
    fcst = obj.predict(future)
    forecast = fcst[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

    forecast_filtered =  forecast[forecast['ds'] > max_date]    
    st.write(forecast_filtered)

    
    st.write("Le visuel suivant montre les valeurs réelles (points noirs) et prédites (ligne bleue) dans le temps..")    

    figure1 = obj.plot(fcst)
    st.write(figure1)
 
    st.write("Les quelques visuels suivants montrent une tendance de haut niveau des valeurs prédites, des tendances par jour de la semaine et des tendances annuelles (si l'ensemble de données couvre plusieurs années). La zone ombrée en bleu représente les intervalles de confiance supérieur et inférieur.")
      

    figure2 = obj.plot_components(fcst)
    st.write(figure2)
    
