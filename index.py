import pandas as pd
import numpy as np
import random
import streamlit as st
import time

liste_film = ['titanic', 'The god Father']
film = st.selectbox('select_film', liste_film, 1)


st.subheader('film choisi')
st.write(film)
