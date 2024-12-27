import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


chart_data = pd.DataFrame(np.random.randn(100, 3), columns=["a", "b", "c"])

tab1, tab2, tab3 = st.tabs(["Gráfico de Linhas", "Gráfico de Barras", "Gráfico de Dispersão"])

with tab1:
    st.write("# Gráfico de Linhas")
    st.line_chart(chart_data)

with tab2:
    st.write("# Gráfico de Barras")
    st.bar_chart(chart_data)

with tab3:
    st.write("# Gráfico de Dispersão")
    c = (
        alt.Chart(chart_data)
        .mark_circle()
        .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
    )
    st.altair_chart(c, use_container_width=True)


