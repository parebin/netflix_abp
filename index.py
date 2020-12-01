import pandas as pd
import numpy as np
import random
import streamlit as st
import time
import streamlit.components.v1 as components

url = "https://image.tmdb.org/t/p/w500/wwemzKWzjKYJFfCeiB57q3r4Bcm.png"

# embed streamlit docs in a streamlit app
components.iframe(url)

df_film = pd.read_csv('https://raw.githubusercontent.com/parebin/netflix_abp/main/top_200.csv')
liste_film = list(df_film['title'])

st.title('Recommandation Films')

#liste_film = [' ', 'titanic', 'The god Father', 'Film3', 'Film4']
film = st.selectbox('select_1erfilm', liste_film, 2)
film2 = st.selectbox('select_2ndfilm', liste_film, 2)
film3 = st.selectbox('select_3emefilm', liste_film, 2)


st.subheader('film choisi')
st.write(film)
st.write(film2)
st.write(film3)

data = pd.read_csv('https://raw.githubusercontent.com/parebin/netflix_abp/main/top_200.csv')
st.dataframe(data)
