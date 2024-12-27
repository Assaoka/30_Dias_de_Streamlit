import streamlit as st

st.write(st.query_params)


st.write('Adicione: ?nome=SeuNome&idade=SuaIdade na URL para ver os parâmetros')

if 'nome' in st.query_params:
    st.write('Nome:', st.query_params['nome'])
if 'idade' in st.query_params:
    st.write('Idade:', st.query_params['idade'])

# Podemos adicionar parâmetros na URL também
st.query_params['AAAAA'] = 'BBBBB'


