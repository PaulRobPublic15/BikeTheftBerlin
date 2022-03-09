#imports
import streamlit as st
import pandas as pd
import folium
import geopandas as gpd
from streamlit_folium import folium_static
import pickle
import geopandas

def app():
    #@st.cache(suppress_st_warning=True)
    st.title('1.1 Bike Accident')
    st.write("Bike accidents by area.")
