import pandas as pd
import numpy as np
import random
import streamlit as st
import time
import streamlit.components.v1 as components

url = "https://image.tmdb.org/t/p/w500/wwemzKWzjKYJFfCeiB57q3r4Bcm.png"

# embed streamlit docs in a streamlit app
components.iframe(url)


st.title('Recommandation Films')

liste_film = ['titanic', 'The god Father', 'Film3', 'Film4']
film = st.selectbox('select_film', liste_film, 2)


st.subheader('film choisi')
st.write(film)

_radio_button = components.declare_component(
    "radio_button", url="http://localhost:3001",
)


def custom_radio_button(label, options, default, key=None):
    return _radio_button(label=label, options=options, default=default, key=key)


result = custom_radio_button(
    "How many bats?",
    options=["one bat", "TWO bats", "THREE bats", "FOUR BATS! ah ah ah!"],
    default="one bat",
)
st.write("This many: %s" % result)
