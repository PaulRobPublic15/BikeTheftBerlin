import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from folium.plugins import HeatMap
import geopandas as gpd
from pyproj import Proj, transform
from shapely.geometry import Point, Polygon
import json
import plotly.express as px
import streamlit as st
from data.get_data import read_data, get_geojson, round_up

def app():
    st.title('Bike Sharing 2')
    st.write("Bike sharing animation")
