import pandas as pd
import numpy as np
import random
import streamlit as st


import streamlit.components.v1 as components
# from sklearn.preprocessing import StandardScaler
# from sklearn.neighbors import NearestNeighbors


# image Netflix
url = "https://image.tmdb.org/t/p/w500/wwemzKWzjKYJFfCeiB57q3r4Bcm.png"
components.iframe(url)


# sidebar
# filtre nombre de film à choisir
nb_film_vu = st.sidebar.slider("Nombre de film déjà vu :", 5, 10, 5)

# décocher les genres non désirés // toutes les genres sont cochés par défaut
st.sidebar.write('Décochez les genres que vous n aimez pas')
condition = [0, 1, 2, 3, 4, 6]
cls0 = st.sidebar.checkbox("Drame", value=True)
if cls0 == False : 
  condition.remove(0)
cls1 = st.sidebar.checkbox("Science Fiction", value=True)
if cls1 == False : 
  condition.remove(1)
cls2 = st.sidebar.checkbox("Comedy", value=True)
if cls2 == False : 
  condition.remove(2)
cls3 = st.sidebar.checkbox("Documentaire", value=True)
if cls3 == False : 
  condition.remove(3)
cls4 = st.sidebar.checkbox("Mistère", value=True)
if cls4 == False : 
  condition.remove(4)
cls6 = st.sidebar.checkbox("Thriler", value=True)
if cls6 == False : 
  condition.remove(6)




# filtre sur le nombre de film à proposé
nb_film_reco=st.sidebar.slider("Nombre de film préconisés :", 3, 10, 5)



#import de la base de film à présenter
df_film = pd.read_csv('https://raw.githubusercontent.com/parebin/netflix_abp/main/top_200.csv')
film_propo = [' ']
liste_film = list(df_film['title'][df_film['cls'].apply(lambda x : x in condition)])
film_propo = film_propo + liste_film


# titre prinsipale
st.title('Renseignez vos films déja vu')



# if apparation selectbox avec nb_film

if nb_film_vu == 5 : 
  film1 = st.selectbox('select 1er film', film_propo, 0)
  film2 = st.selectbox('select 2eme film', film_propo, 0)
  film3 = st.selectbox('select 3eme film', film_propo, 0)
  film4 = st.selectbox('select 4eme film', film_propo, 0)
  film5 = st.selectbox('select 5eme film', film_propo, 0)
  liste_film = [film1, film2, film3, film4, film5]
elif nb_film_vu == 6 :
  film1 = st.selectbox('select 1er film', film_propo, 0)
  film2 = st.selectbox('select 2eme film', film_propo, 0)
  film3 = st.selectbox('select 3eme film', film_propo, 0)
  film4 = st.selectbox('select 4eme film', film_propo, 0)
  film5 = st.selectbox('select 5eme film', film_propo, 0)
  film6 = st.selectbox('select 6eme film', film_propo, 0)
  liste_film = [film1, film2, film3, film4, film5, film6]
elif nb_film_vu == 7 :
  film1 = st.selectbox('select 1er film', film_propo, 0)
  film2 = st.selectbox('select 2eme film', film_propo, 0)
  film3 = st.selectbox('select 3eme film', film_propo, 0)
  film4 = st.selectbox('select 4eme film', film_propo, 0)
  film5 = st.selectbox('select 5eme film', film_propo, 0)
  film6 = st.selectbox('select 6eme film', film_propo, 0)
  film7 = st.selectbox('select 7eme film', film_propo, 0)
  liste_film = [film1, film2, film3, film4, film5, film6, film7]
elif nb_film_vu == 8 :
  film1 = st.selectbox('select 1er film', film_propo, 0)
  film2 = st.selectbox('select 2eme film', film_propo, 0)
  film3 = st.selectbox('select 3eme film', film_propo, 0)
  film4 = st.selectbox('select 4eme film', film_propo, 0)
  film5 = st.selectbox('select 5eme film', film_propo, 0)
  film6 = st.selectbox('select 6eme film', film_propo, 0)
  film7 = st.selectbox('select 7eme film', film_propo, 0)
  film8 = st.selectbox('select 8eme film', film_propo, 0)
  liste_film = [film1, film2, film3, film4, film5, film6, film7, film8]
elif nb_film_vu == 9 :
  film1 = st.selectbox('select 1er film', film_propo, 0)
  film2 = st.selectbox('select 2eme film', film_propo, 0)
  film3 = st.selectbox('select 3eme film', film_propo, 0)
  film4 = st.selectbox('select 4eme film', film_propo, 0)
  film5 = st.selectbox('select 5eme film', film_propo, 0)
  film6 = st.selectbox('select 6eme film', film_propo, 0)
  film7 = st.selectbox('select 7eme film', film_propo, 0)
  film8 = st.selectbox('select 8eme film', film_propo, 0)
  film9 = st.selectbox('select 9eme film', film_propo, 0)
  liste_film = [film1, film2, film3, film4, film5, film6, film7, film8, film9]
elif nb_film_vu == 10 :
  film1 = st.selectbox('select 1er film', film_propo, 0)
  film2 = st.selectbox('select 2eme film', film_propo, 0)
  film3 = st.selectbox('select 3eme film', film_propo, 0)
  film4 = st.selectbox('select 4eme film', film_propo, 0)
  film5 = st.selectbox('select 5eme film', film_propo, 0)
  film6 = st.selectbox('select 6eme film', film_propo, 0)
  film7 = st.selectbox('select 7eme film', film_propo, 0)
  film8 = st.selectbox('select 8eme film', film_propo, 0)
  film9 = st.selectbox('select 9eme film', film_propo, 0)
  film10 = st.selectbox('select 10eme film', film_propo, 0)
  liste_film = [film1, film2, film3, film4, film5, film6, film7, film8, film9, film10]




st.write(liste_film)


# permet de retirer les id des films choisis
def list_id(liste_titre):
  liste_id = []
  for i in liste_titre :
    film = i
    liste_id.append(int(df_film['movieId'][df_film['title'] == film]))
  return liste_id


#liste des id des films choisis

if ' ' in liste_film :
  st.write('Compléter tous les choix')
else :

  liste_id = list_id(liste_film)
  st.write(liste_id)










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

