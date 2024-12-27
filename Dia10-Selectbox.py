import streamlit as st

if "visibilidade" not in st.session_state:
    st.session_state.visibilidade = "Visível"
    st.session_state.disabilitado = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Desabilitar o widget de seleção", 
                key="desabilitado")
    st.radio("Visibilidade", 
             ["Visível", "Oculto", "Recolhido"]
                , key="visibilidade")

def visibilidade():
    match st.session_state.visibilidade:
        case "Visível":
            return "visible"
        case "Oculto":
            return "hidden"
        case "Recolhido":
            return "collapsed"

def disabilitado():
    if st.session_state.desabilitado:
        return True
    else:
        return False



with col2:
    option = st.selectbox(
                        'Como você gostaria de ser contatado?',
                        ('Email', 'WhatsApp', 'Telefone'),
                        label_visibility=visibilidade(),
                        disabled=disabilitado())


st.subheader(f"Você escolheu ser contatado por {option}")