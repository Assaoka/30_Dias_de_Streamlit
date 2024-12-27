import streamlit as st

st.header('Botão Condicional')

if st.button('Clique aqui', help="Isso aparece quando você passa o mouse sobre o botão"):
    st.write('Você clicou')
else:
    st.write('Você não clicou')





r, m, l = st.columns(3)



if r.button('Direita', use_container_width=True):
    st.write('Direita')
if m.button('Meio', use_container_width=True):
    st.write('Meio')
if l.button('Esquerda', use_container_width=True):
    st.write('Esquerda')