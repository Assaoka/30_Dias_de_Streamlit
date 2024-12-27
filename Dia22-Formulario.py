import streamlit as st

st.header('Formulario')
with st.form(key='my_form'):
    st.subheader("Monte seu sanduíche")
    tamanho = st.selectbox('Tamanho', ['Pequeno', 'Médio', 'Grande'])
    molho = st.multiselect('Molhos', ['Maionese', 'Ketchup', 'Mostarda', 'Barbecue'])
    proteinas = st.selectbox('Proteínas', ['Peito de frango', 'Hambúrguer', 'Carne de soja'])
    queijo = st.checkbox('Queijo')
    salada = st.checkbox('Salada')
    obs = st.text_input('Observações')


    # TODAS AS INFORMAÇÕES SÓ SERÃO ENVIADAS QUANDO O BOTÃO FOR CLICADO
    submit_button = st.form_submit_button(label='Enviar')

if submit_button:
    st.write('Seu sanduíche foi montado com sucesso!')
    st.write(f'Tamanho: {tamanho}')
    st.write(f'Molhos: {molho}')
    st.write(f'Proteínas: {proteinas}')
    st.write(f'Queijo: {queijo}')
    st.write(f'Salada: {salada}')
    st.write(f'Observações: {obs}')
else:
    st.write('Faça seu pedido!')