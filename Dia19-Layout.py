import streamlit as st
import time

st.header("Layout")
st.subheader("Colunas")
col1, col2 = st.columns(2)
col1.write("Coluna 1")
col2.write("Coluna 2")

st.subheader("Container")
with st.container(border=True):
    st.write("Este texto está dentro de um container")
    st.write("Este também")


col1, col2 = st.columns(2)
with col1:
    with st.container(border=True, height=200):
        st.write("Este texto está dentro de um container que está dentro de uma coluna")
        st.write("Este também")
with col2:
    with st.container(border=True, height=200):
        st.write("Este texto também está dentro de um container que está dentro de uma coluna")

st.subheader("Caixa de diálogo")
@st.dialog("Sign up")
def signup_dialog():
    name = st.text_input("Name")
    email = st.text_input("Email")

    if st.button("Sign up"):
        st.write(f"Signing up {name} with email {email}")
st.button("Sign up", on_click=signup_dialog, key="signup")

st.subheader("Empty")
# Este é um conteiner que só armazena um unico elemento. Isso é util para atualizar o conteudo de um elemento sem ter que recarregar a pagina
with st.empty():
    if st.button("Rode o contador de 10 segundos"):
        for seconds in range(10):
            st.write(f"⏳ {seconds} seconds have passed")
            time.sleep(1)
        st.write("✅ 10 segundos se passaram")

st.subheader("Expandir")
with st.expander("Expander", icon="🔍"):
    st.write("Este texto está dentro de um expander")

st.subheader("Popover")
# Conteiner de varios elementos que é exibido quando o usuario clica em um botão
with st.popover("Popover"):
    st.write("Este texto está dentro de um popover")

with st.sidebar:
    st.header("Sidebar")
    st.write("Este texto está dentro da sidebar")

st.subheader("Tabs")
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("Esse é o conteúdo da Tab 1")
with tab2:
    st.write("já esse é o conteúdo da Tab 2")
