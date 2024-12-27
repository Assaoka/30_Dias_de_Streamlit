"""
O comando write() é um canivete suíço para escrever qualquer tipo de dado no Streamlit. 
Ele se adapta automaticamente ao tipo de dado que você passa para ele.
https://docs.streamlit.io/develop/api-reference/write-magic/st.write 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.write("# Exemplo 1")
st.write("*Texto em itálico*, **Texto em negrito**, :+1:, :green[Texto em verde]:")

st.write("# Exemplo 2")
st.write(123)

st.write("# Exemplo 3")
st.write({"Nome": "João", "Idade": 30})

st.write("# Exemplo 4")
df = pd.DataFrame({"A": np.linspace(-10, 10, 100)})
df["B"] = df["A"].apply(lambda x: x**3 + x**2 + x + 1)
st.write(df)

st.write("# Exemplo 5")
fig, ax = plt.subplots()
ax.plot(df["A"], df["B"])
st.write(fig)



# Outras opções que podemos explorar
st.header("Exemplo de header", divider="blue", anchor="top") # Cria um cabeçalho
st.markdown("Texto em Markdown") # Escreve um texto em markdown
st.caption("Exemplo de caption (:rainbow[aceita markdown])") # Adiciona uma legenda
st.text("Texto simples, :red[NÃO ACEITA MARKDOWN]") # Escreve um texto simples
st.latex(r"\int_{a}^{b} x^2 dx") # Escreve uma expressão matemática em LaTeX, o markdown já renderiza latex também
st.code("""nome = input("Qual é o seu nome?")
        print(f"Olá, {nome}")""",
        language="python", # Define a linguagem do código
        line_numbers=True) # Adiciona um bloco de código

