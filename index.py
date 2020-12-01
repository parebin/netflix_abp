import pandas as pd
import numpy as np
import random
import streamlit as st
import time
from bs4 import BeautifulSoup
import requests


st.title('Recommandation Films')

liste_film = ['titanic', 'The god Father']
film = st.selectbox('select_film', liste_film, 1)


st.subheader('film choisi')
st.write(film)


url = "https://www.imdb.com/title/tt0120338/"

pageweb = requests.get(url)

scrap = BeautifulSoup(pageweb.text, "html.parser")

st.image(scrap.find_all("div", attrs="poster") [0].img)
