import pandas as pd
import numpy as np
import random
import streamlit as st
import time
import streamlit.components.v1 as components




st.title('Recommandation Films')

liste_film = ['titanic', 'The god Father']
film = st.selectbox('select_film', liste_film, 1)


st.subheader('film choisi')
st.write(film)


url = "https://www.themoviedb.org/movie/597"

# embed streamlit docs in a streamlit app
components.iframe(url)
