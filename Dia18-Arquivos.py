import streamlit as st
import pandas as pd

arquivo = st.file_uploader("Escolha um arquivo CSV", type='csv')

if arquivo is not None:
    df = pd.read_csv(arquivo)
    st.write("Planilha:")
    st.write(df)

    st.write("Estatísticas:")
    st.write(df.describe())
else:
    st.write("Aguardando upload de arquivo...")


