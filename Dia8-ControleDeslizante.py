import streamlit as st
from datetime import datetime, time

age = st.slider("Quantos anos você tem?", 0, 130, 25)
st.write(f"Você tem {age} anos")


values = st.slider("Selecione um intervalo de valores", 
                   0.0, 100.0, (25.0, 75.0))
st.write(f"Você selecionou o intervalo de valores: {values}")

compromisso = st.slider("Selecione um horário para o compromisso",
                        value=(time(8, 0), time(12, 0)))
st.write(f"Seu compromisso está marcado para as {compromisso[0]} e termina às {compromisso[1]}")


data = st.slider("Quando você vai começar?",
                 value=datetime(2020, 1, 1, 9, 30),
                 format="MM/DD/YY - hh:mm")
st.write("Início:", data)


cor = st.select_slider("Selecione uma cor",
        options=[
                "red",
                "orange",
                "green",
                "blue",
                "violet",
                "rainbow"])
st.write(f":{cor}[Texto]")