import streamlit as st

st.title('Customizando o tema de aplicações Streamlit')

st.write('Conteúdo do arquivo `.streamlit/config.toml` desta aplicação')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Selecione um número:', 0, 10, 5)
st.write('O número selecionado no controle deslizante é:', number)

st.markdown("Podemos fazer pequenas alterações em temas já existentes usando o parametro base='light' ou base='dark'")

