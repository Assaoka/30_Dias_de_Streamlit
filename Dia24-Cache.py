import streamlit as st
import numpy as np
import time

# Essa é um decorator que faz com que a função seja cacheada, dessa forma ela só é executada uma vez com os mesmos parâmetros. Isso é útil para funções que demoram para ser executadas. Existem 2 formas, a primeira é o cache_data (para coisas que voce pode armazenar em um banco de dados) e o cache_resource para coisas que não podem ser armazenadas em um banco de dados.


@st.cache_data
def fibonacci(n):
    time.sleep(0.5)
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Funciona como um fibonacci com backtracking

n = st.slider('Escolha um número:', 0, 40, 20)
st.write('Fibonacci de', n, 'é', fibonacci(n))