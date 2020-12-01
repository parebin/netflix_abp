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


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

icon("search")
selected = st.text_input("", "Search...")
button_clicked = st.button("OK")
