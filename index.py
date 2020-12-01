import pandas as pd
import numpy as np
import random
import streamlit as st
import time
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app
components.iframe("https://lechaudron.io/tag/nantes/")


st.sidebar.slider("Choose a frame (index)", 0, len(selected_frames) - 1, 0)
