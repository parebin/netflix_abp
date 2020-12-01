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


url = "https://image.tmdb.org/t/p/w500/wwemzKWzjKYJFfCeiB57q3r4Bcm.png"

# embed streamlit docs in a streamlit app
components.iframe(url)
