# Call_Center_streamlit

- Use case 1: prévision du volume d'appels clients par jour depuis 2014

- Use case 2: prévision du volume d'appels abandonnés par jour

## Dataset utilisé : 311 Call Center data

Il s'agit de données de l'activité quotidienne d'un centre d'appels téléphonique (311). Ci-dessous, les liens vers les données : 

a) https://data.calgary.ca/w/hk5h-uv5k/6wv6-hjhs?cur=X75UG6BrhC1

b) https://data.calgary.ca/stories/s/Open-Calgary-Terms-of-Use/u45n-7awa

## Méthode de ML appliquée sur les deux use cases: méthode hybride

1) Décomposition de la série en composantes : tendence, saisonnalité,  bruit

- Tendance : orientation générale de la série (vers le haut ou vers le bas)
- Saisonnalité : tendances hebdomadaires, mensuelles, trismestrielles ou annuelles
- Bruit : ce qui reste après avoir extrait les composants précédents

2) Application des méthodes (Fbprophet, LSTM) sur la tendance pour réaliser les prévision

FBprophet: FbProphet est un puissant package d'analyse de séries chronologiques publié par l'équipe Core Data Science de Facebook. Il s'agit d'un package simple et facile à utiliser pour effectuer des analyses de séries chronologiques et des prévisions à grande échelle.

Prophet est une procédure de prévision des données de séries chronologiques basée sur un modèle additif où les tendances non linéaires sont adaptées à la saisonnalité annuelle, hebdomadaire et quotidienne, ainsi qu'aux effets des vacances. Cela fonctionne mieux avec des séries chronologiques qui ont de forts effets saisonniers et plusieurs saisons de données historiques. Prophet résiste aux données manquantes et aux changements de tendance, et gère généralement bien les valeurs aberrantes (https://facebook.github.io/prophet/)

LSTM : type de RNN