# Importando bibliotecas necessárias
import streamlit as st
import pandas as pd
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
    Carrega a base de dados tratada a partir do arquivo CSV.
    Retorna um DataFrame ou None se houver erro.
    '''

    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(diretorio_atual, '..', 'data', 'base_tratada.csv')

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

if df is None:
    st.stop()

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

if df_filtrado.empty:
    st.sidebar.warning(
        '''
        A combinação de filtros selecionada não retornou nenhum dado.
        Tente ajustar os filtros.
        '''
    )
    st.stop()

# Métricas (Cards)
st.subheader("Resumo dos Dados Filtrados")

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

# Aba 1 - Visão Geral
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
        **Interpretação:** A série mostra a sazonalidade do regime de chuvas na região,
        com picos no verão e vales no inverno."
        '''
    )

# Aba 2 - Análise Gráfica
with aba_2:
    st.subheader("Gráficos Detalhados")

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("### Distribuição por Estação (Boxplot)")

        fig_2, ax_2 = plt.subplots(figsize=(8, 5))

        df_filtrado.boxplot(column='Total', by='Estacao', ax=ax_2)

        ax_2.set_title("Precipitação Total por Estação")
        ax_2.set_ylabel("Precipitação (mm)")

        st.pyplot(fig_2)
        st.markdown(
            '''
            **Interpretação:** O Verão e o Outono são as estações mais chuvosas,
            enquanto o Inverno é a mais seca.
            '''
        )

    with col_b:
        st.markdown("### Distribuição da Precipitação (Histograma)")

        fig_3, ax_3 = plt.subplots(figsize=(8, 5))

        sns.histplot(
            data=df_filtrado,
            x='Total',
            bins=20,
            kde=True,
            ax=ax_3,
            edgecolor='black',
            alpha=0.7
        )

        ax_3.set_title("Histograma da Precipitação Mensal")
        ax_3.set_xlabel("Precipitação Total (mm)")
        ax_3.set_ylabel("Frequência")

        st.pyplot(fig_3)
        st.markdown(
            '''
            **Interpretação:** A distribuição é assimétrica à direita,
            indicando uma longa cauda de eventos de chuva intensa.
            '''
        )

    st.markdown("### Relação entre Dias de Chuva e Total Mensal")

    fig_4, ax_4 = plt.subplots(figsize=(10, 5))

    scatter = ax_4.scatter(
        df_filtrado['NumDiasDeChuva'],
        df_filtrado['Total'],
        c=df_filtrado['NumDiasSemChuva'],
        cmap='coolwarm',
        alpha=0.7
    )

    ax_4.set_title("Dias de Chuva x Total Mensal")
    ax_4.set_xlabel("Número de Dias de Chuva")
    ax_4.set_ylabel("Precipitação Total (mm)")

    plt.colorbar(scatter, ax=ax_4, label='Dias Sem Chuva')

    st.pyplot(fig_4)
    st.markdown(
        '''
        **Interpretação:** A correlação positiva forte indica que meses 
        com mais dias de chuva tendem a ter um volume total maior.
        '''
    )

# Aba 3 - Dados
with aba_3:
    st.subheader("Tabela de Dados Filtrados")
    st.dataframe(df_filtrado)

    # Botão de Download
    csv = df_filtrado.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Baixar Dados Filtrados (CSV)",
        data=csv,
        file_name='dados_filtrados.csv',
        mime='text/csv'
    )

# Aba 4  - Interpretação
with aba_4:

    st.subheader("Interpretação dos Resultados")
    st.markdown(
        '''
          **Principais Achados:**
          *   **Sazonalidade:** O regime de chuvas em Tabatinga é fortemente sazonal, 
          com o Outono e o Verão sendo as estações mais chuvosas.
          *   **Distribuição:** A precipitação mensal não segue uma distribuição normal; 
          eventos de chuva intensa (>400mm) são menos frequentes, mas contribuem significativamente para o total anual.
          *   **Correlação:** Existe uma correlação positiva moderada a forte 
          entre o número de dias de chuva e o volume total mensal.
          
          **Limitações:**
          *   Os dados representam apenas uma estação pluviométrica, 
          não refletindo a variabilidade espacial da região.
          *   Há uma lacuna significativa de dados entre 1999 e 2015, 
          o que limita a análise de tendências de longo prazo.
          
          **Apoio à Decisão:**
          Este dashboard pode auxiliar na identificação de padrões históricos 
          e na previsão de safras agrícolas, no planejamento de recursos hídricos 
          e em estratégias de defesa civil, permitindo visualizar rapidamente 
          os meses e anos mais críticos em termos de chuva.
          '''
        )
