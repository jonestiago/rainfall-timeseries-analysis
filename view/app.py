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

df_filtrado = None

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

    classificacoes = ["Todas"] + sorted(df['Classificacao_Chuva'].unique())
    classificacao_selecionada = st.sidebar.selectbox(
        "Selecione a Classificação da Chuva",
        options=classificacoes,
        index=0
    )

    df_filtrado = df.copy()

    if ano_selecionado != "Todos":
        df_filtrado = df_filtrado[df_filtrado['Ano'] == int(ano_selecionado)]
    if estacao_selecionada != "Todas":
        df_filtrado = df_filtrado[df_filtrado['Estacao'] == estacao_selecionada]
    if classificacao_selecionada != "Todas":
        df_filtrado = df_filtrado[df_filtrado['Classificacao_Chuva'] == classificacao_selecionada]

# Métricas
st.subheader("Resumo dos Dados Filtrados")

if df_filtrado.empty:
    st.warning("Nenhum dado disponível para os filtros selecionados. Tente ajustar os filtros.")
else:
    col_1, col_2, col_3 = st.columns(3)

    media_total = df_filtrado['Total'].mean()
    col_1.metric(
        label="🌧️ Média mensal (mm)",
        value=f"{media_total:.1f} mm"
    )

    max_chuva = df_filtrado['Maxima'].max()
    col_2.metric(
        label="💧 Maior chuva diária (mm)",
        value=f"{max_chuva:.1f} mm"
    )

    media_dias_chuva = df_filtrado['NumDiasDeChuva'].mean()
    col_3.metric(
        label="📅 Média de Dias de Chuva",
        value=f"{media_dias_chuva:.1f} dias"
    )

# Abas / Tabs
abas = ["📈 Visão Geral", "📊 Análise Gráfica", "📋 Dados", "🧠 Interpretação"]
aba_1, aba_2, aba_3, aba_4 = st.tabs(abas)

with aba_1:
    st.subheader("Série Temporal da Precipitação")

    fig_1, ax_1 = plt.subplots(figsize=(12, 5))

    ax_1.plot(
        df_filtrado['Data'],
        df_filtrado['Total'],
        color='#1f77b4',
        linewidth=1.5,
        marker='o',
        markersize=3
    )

    ax_1.set_title("Precipitação Total Mensal ao Longo do Tempo")
    ax_1.set_xlabel("Data")
    ax_1.set_ylabel("Precipitação Total (mm)")
    ax_1.grid(True, alpha=0.3)

    st.pyplot(fig_1)
    st.markdown(
        '''
        "**Interpretação:** A série mostra a sazonalidade do regime de chuvas na região,
        com picos no verão e vales no inverno."
        '''
    )

with aba_2:
    st.subheader("Gráficos Detalhados")

    pass
