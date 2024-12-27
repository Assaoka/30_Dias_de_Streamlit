import streamlit as st

st.header("Crie sua conta")
barra = st.progress(0)

nome = st.text_input("Username")
email = st.text_input("Email")
senha = st.text_input("Senha", type="password")
confirmar_senha = st.text_input("Confirmar senha", type="password")

if senha != confirmar_senha:
    st.error("As senhas não coincidem")

if st.button("Criar conta", disabled=(senha != confirmar_senha)):
    st.success("Conta criada com sucesso")


def progresso():
    n = 33 if (nome) else 0
    n += 33 if (email) else 0
    n += 34 if (senha == confirmar_senha) and (senha) else 0
    return n

barra.progress(progresso())


