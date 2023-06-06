# -*- coding: utf-8 -*-
"""Actividad Integradora UF6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TtPPsORi5eZdg_O5fuD2zuG8dwfn9p15
"""

import streamlit as st
import pandas as pd
import numpy as np

st.title('Police Incident Reports form 1028 to 2020 in San Francisco')

df = pd.read_csv('https://drive.google.com/file/d/11oLcKiW8SgCOp3tGiQCYuRG7pLL_J-Zf/view?usp=drive_link')

st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution')

mapa=pd.DataFrame(
    np.array([[latitude, longitude]]),
    columns=['lat', 'lon'])

mapa = mapa.dropna()
st.map(mapa.astype(float))
