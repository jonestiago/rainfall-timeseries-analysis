# **🌧️ Dashboard Pluviométrico - Tabatinga/AM (1982-2025)**

**Objetivo**\
Este dashboard interativo foi desenvolvido com Streamlit para analisar os dados de precipitação da estação 469001, localizada em Tabatinga - AM, cobrindo o período de 1982 a 2025.

O público-alvo são estudantes de engenharia ambiental e profissionais da área de recursos hídricos. O dashboard apoia decisões relacionadas ao planejamento agrícola, gestão de reservatórios e análise de eventos climáticos extremos.

## **Bibliotecas Utilizadas**
- `streamlit`: Para a criação da interface web interativa.
- `pandas`: Para manipulação e análise dos dados.
- `matplotlib`: Para a geração dos gráficos.
- `seaborn`: Para visualizações estatísticas (opcional, mas usado no histograma).

## **Instalação e Execução (Windows)**
Siga os passos abaixo para executar o dashboard no seu computador.

### **1. Abra a pasta do projeto:**
Abra o diretório  `rainfall-timeseries-analysis`

### **2. Abra o Prompt de comando na pasta do projeto:**
Na barra de endereços, digite `cmd` e pressione **Enter**.\
Uma janela do Prompt de comando será aberta automaticamente já posicionada dentro da pasta `rainfall-timeseries-analysis`.

### **3. Acesse a pasta do dashboard:**
O arquivo principal `app.py` está dentro da pasta `view`. No Prompt de Comando que você acabou de abrir, execute o comando abaixo para entrar nela:
```bash
cd view
```

### **4. Instale as Dependências:**
O arquivo requirements.txt contém a lista de bibliotecas que o dashboard precisa para funcionar. Execute o comando abaixo:
```bash
pip install -r requirements.txt
```

### **5. Execute o Dashboard:**
Para executar o dashboard, execute o comando abaixo:
```bash
streamlit run app.py
```

### **6. Acesse o Dashboard:**
Abra o navegador e navegue para o link: `http://localhost:8501/`

## **Componentes do Dashboard**

### **Filtros (Sidebar):**
- **Ano:** Filtra os dados por um ano específico.
- **Estação:** Filtra por estação do ano (Verão, Outono, Inverno, Primavera).
- **Classificação da Chuva:** Filtra por classificações como "Muito Chuvoso", "Normal" ou "Muito Seco".

### **Métricas (Cards):**
- **Média Mensal (mm):** A média da precipitação total nos meses filtrados.
- **Maior Chuva Diária (mm):** O maior valor de precipitação em um único dia.
- **Média de Dias de Chuva:** A média de dias com chuva por mês.

### **Gráficos:**
- **Série Temporal:** Evolução da precipitação total mensal ao longo do tempo.
- **Distribuição por Estação (Boxplot):** Comparação da precipitação entre as estações do ano.
- **Distribuição da Precipitação (Histograma):** Frequência dos volumes de chuva.
- **Relação Dias de Chuva x Total:** Dispersão mostrando a correlação entre o número de dias chuvosos e o volume total.

### **Dados**
- Tabela: Exibe os dados filtrados
- Permite o download em formato CSV.

### **Interpretação**
- Seção com os principais achados, limitações e aplicações práticas do dashboard.