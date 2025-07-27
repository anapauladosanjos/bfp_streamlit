import streamlit as st
import pandas as pd
import plotly.express as px
import random

# ---------- MAPAS DAS FACETAS ----------
mapa = {
    'E1 – Comunicação': {'itens': [17, 38, 66, 97, 105, 120], 'inversos': [17, 38, 66]},
    'E2 – Altivez': {'itens': [3,5,14,78,93,99,111], 'inversos': []},
    'E3 – Dinamismo': {'itens': [21,26,32,108,117], 'inversos': []},
    'E4 – Interações sociais': {'itens': [8,11,47,50,52,71,90], 'inversos': []},
    'S1 – Amabilidade': {'itens': [2,4,12,15,20,43,46,61,92,96,104,125], 'inversos': []},
    'S2 – Pró‑sociabilidade': {'itens': [18,24,27,63,76,87,107,109], 'inversos': [18,24,27,87,107]},
    'S3 – Confiança nas pessoas': {'itens': [7,10,30,39,57,68,98,119], 'inversos': [10,30,39,57,98,119]},
    'R1 – Competência': {'itens': [28,41,58,64,67,72,83,85,91,122], 'inversos': []},
    'R2 – Ponderação/prudência': {'itens': [9,19,45,101], 'inversos': [19]},
    'R3 – Empenho/comprometimento': {'itens': [34,54,80,103,112,114,116], 'inversos': []},
    'A1 – Abertura a ideias': {'itens': [23,33,36,42,53,56,62,81,88,115], 'inversos': [23,33,42,56,62,115]},
    'A2 – Liberalismo': {'itens': [1,31,59,69,74,123,126], 'inversos': [1]},
    'A3 – Busca por novidades': {'itens': [6,44,49,84,94,113], 'inversos': [84]},
    'N1 – Vulnerabilidade': {'itens': [55,60,73,75,79,82,89,110,118], 'inversos': []},
    'N2 – Instabilidade emocional': {'itens': [25,51,65,77,86,102], 'inversos': []},
    'N3 – Passividade/falta de energia': {'itens': [13,22,35,37,95,100], 'inversos': []},
    'N4 – Depressão': {'itens': [16,29,40,48,70,106,121,124], 'inversos': [16]},
}

fatores = {
    'Extroversão': ['E1 – Comunicação', 'E2 – Altivez', 'E3 – Dinamismo', 'E4 – Interações sociais'],
    'Socialização': ['S1 – Amabilidade', 'S2 – Pró‑sociabilidade', 'S3 – Confiança nas pessoas'],
    'Realização': ['R1 – Competência', 'R2 – Ponderação/prudência', 'R3 – Empenho/comprometimento'],
    'Abertura': ['A1 – Abertura a ideias', 'A2 – Liberalismo', 'A3 – Busca por novidades'],
    'Neuroticismo': ['N1 – Vulnerabilidade', 'N2 – Instabilidade emocional', 'N3 – Passividade/falta de energia', 'N4 – Depressão'],
}

st.set_page_config(layout="wide")
st.title("BFP – Teste de Facetas com 126 Itens")

st.markdown("### Preenchimento dos itens (valores de 1 a 7)")
st.markdown("*(Valores aleatórios gerados para teste)*")

# ---------- ENTRADA DOS 126 ITENS EM 6 COLUNAS ----------
respostas = {}
cols = st.columns(6)
for i in range(1, 127):
    col = cols[(i - 1) % 6]
    with col:
        respostas[i] = st.number_input(f"Item {i}", 1, 7, random.randint(1, 7), key=f"item_{i}")

# ---------- CÁLCULO DAS FACETAS ----------
resultados = []
for faceta, info in mapa.items():
    valores = []
    for i in info['itens']:
        r = respostas[i]
        if i in info['inversos']:
            valores.append(8 - r)
        else:
            valores.append(r)
    EB = round(sum(valores) / len(valores), 2)
    resultados.append({'Faceta': faceta, 'EB': EB})

df = pd.DataFrame(resultados)

# ---------- CÁLCULO DOS FATORES ----------
fator_scores = []
for fator, facs in fatores.items():
    es = round(df[df['Faceta'].isin(facs)]['EB'].mean(), 2)
    fator_scores.append({'Fator': fator, 'Escore Geral': es})
df_fat = pd.DataFrame(fator_scores)

# ---------- EXIBIÇÃO DOS RESULTADOS ----------
st.markdown("## Resultados")
st.subheader("Escores Brutos por Faceta (1 a 7)")
st.dataframe(df.set_index('Faceta'))

st.subheader("Escore Geral por Fator (1 a 7)")
st.table(df_fat.set_index('Fator'))

# ---------- GRÁFICO RADAR ----------
fig = px.line_polar(df, r='EB', theta='Faceta', line_close=True)
fig.update_traces(fill='toself')
fig.update_layout(height=600)
st.plotly_chart(fig)
