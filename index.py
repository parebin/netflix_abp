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

# box pour présenter les 200 films
film = st.selectbox('select 1er film', liste_film, 2)
film2 = st.selectbox('select 2eme film', liste_film, 2)
film3 = st.selectbox('select 3eme film', liste_film, 2)
film4 = st.selectbox('select 4eme film', liste_film, 2)
film5 = st.selectbox('select 5eme film', liste_film, 2)

# ecrire les 5 films choisis
st.subheader('film choisi')
st.write(film)
st.write(film2)
st.write(film3)
st.write(film4)
st.write(film5)

liste_film = [film, film2, film3, film4, film5]

# permet de retirer les id des films choisis
def list_id(liste_titre):
  liste_id = []
  for i in liste_titre :
    film = i
    liste_id.append(int(df_film['movieId'][df_film['title'] == film]))
  return liste_id

#liste des id des films choisis

liste_id = list_id(liste_film)

st.write(liste_id)


tab_size=st.sidebar.slider("Tab size", 1900, 2018, 1960)
st.sidebar.write('Décochez les genres que vous n aimez pas')
cls0=st.sidebar.checkbox("Drame", value=True)
cls1=st.sidebar.checkbox("Science Fiction", value=True)
cls2=st.sidebar.checkbox("Comedy", value=True)
cls3=st.sidebar.checkbox("Documentaire", value=True)
cls4=st.sidebar.checkbox("Mistère", value=True)
cls6=st.sidebar.checkbox("Thriler", value=True)
#cls7=st.sidebar.checkbox("Amour", value=True)

st.write(tab_size)

#test d'affichage de 
# data = pd.read_csv('https://raw.githubusercontent.com/parebin/netflix_abp/main/top_200.csv')
# st.dataframe(data)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')





#icon("search")
#selected = st.text_input("", "Search...")
button_clicked = st.button("OK")

