import streamlit as st
import numpy as np

st.set_page_config(page_title="BFP - Bateria Fatorial de Personalidade", layout="wide")
st.title("Bateria Fatorial de Personalidade (BFP)")

st.markdown("""
<p style="font-size:16px">
Responda cada questão com um número de <strong>1 a 7</strong>, sendo:<br>
<strong>1 = Discordo totalmente</strong> &nbsp;&nbsp;&nbsp; <strong>7 = Concordo totalmente</strong>
</p>
""", unsafe_allow_html=True)

# Dicionário para guardar as respostas
respostas = {}

# Total de questões
total_questoes = 126
colunas = 4
questoes_por_coluna = total_questoes // colunas + 1

# Dividir a tela em 4 colunas
cols = st.columns(colunas)

# Inserir as questões distribuídas entre as colunas
for i in range(total_questoes):
    col = cols[i % colunas]
    with col:
        q_num = i + 1
        st.markdown(f"<span style='display:inline-block; width:60px'>Q{q_num}:</span>", unsafe_allow_html=True)
        resposta = st.number_input(
            label="",
            min_value=1,
            max_value=7,
            step=1,
            key=f"q_{q_num}",
            label_visibility="collapsed",
        )
        respostas[q_num] = resposta

# Botão de exemplo para mostrar algumas médias de facetas
if st.button("Calcular exemplo de facetas"):
    st.subheader("Exemplo de cálculo de facetas")

    facetas_exemplo = {
        "N1_Vulnerabilidade": [55, 60, 73, 75, 79, 82, 89, 110, 118],
        "E1_Comunicação": [17, 38, 66, 97, 105, 120]
    }

    for nome, itens in facetas_exemplo.items():
        valores = [respostas[i] for i in itens]
        media = np.mean(valores)
        st.write(f"{nome}: {media:.2f}")
