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

# Carregamento de dados
@ st.cache_data
def carregar_dados():
    '''
    A definir
    '''
    caminho_arquivo = r"..\rainfall-timeseries-analysis\data\base_tratada.csv"

    if not os.path.exists(caminho_arquivo):
        st.error(f"Arquivo de dados não encontrado: {caminho_arquivo}")
        st.info("Certifique-se de que o arquivo 'base_tratada.csv' está na pasta 'data'.")
        return None

    try:
        df = pd.read_csv(caminho_arquivo)
        if 'Data' in df.columns and df['Data'].dtype == 'object':
            df['Data'] = pd.to_datetime(df['Data'])
        return df

    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return None

df = carregar_dados()

# Sidebar (Filtros)
st.sidebar.title("Filtros")

if df is not None and not df.empty:

    anos = sorted(df['Ano'].unique())
    ano_selecionado = st.sidebar.selectbox(
        "Selecione o Ano",
        options=["Todos"] + anos,
        index=0
    )

    estacoes = ["Todas"] + sorted(df['Estacao'].unique())
    estacao_selecionada = st.sidebar.selectbox(
        "Selecione a Estação",
        options=estacoes,
        index=0
    )
