import streamlit as st

options = st.multiselect('Quais são seus esportes favoritos?', 
                         ['Futebol', 'Basquete', 'Vôlei', 'Tênis', 'Natação'])

st.write('Você selecionou:')
st.write('\n'.join([f'1. {option}' for option in options]))