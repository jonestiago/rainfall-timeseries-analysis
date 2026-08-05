# Importando bibliotecas necessárias
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configurações da página
st.set_page_config(
    page_title="Dashboard Pluviométrico - Tabatinga/AM (1982-2025)",
    page_icon="🌧️",
    layout="wide"
)

# Título do dashboard
st.title("Análise Pluviométrica - Tabatinga/AM (1982-2025)")
st.markdown(
    '''
    Este dashboard apresenta uma análise exploratória 
    dos dados de precipitação da estação 469001,
    localizada em Tabatinga - AM, no período de 1982 a 2025.
    '''
)

