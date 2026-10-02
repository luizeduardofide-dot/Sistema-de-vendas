import streamlit as st
import pandas as pd
import plotly.express as px

 
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas ")


st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"]) 
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor",)
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

if botao_cadastrar:
    if quantidade <=0:
        st.error("A quantidade deve ser maior que zero.")
    elif valor <=0:
        st.error("O valor deve ser maior que zero.")
    else:
        nova_venda = [str(data), vendedor, produto, quantidade, valor]
        ultima_linha = len(tabela_vendas)
        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv("vendas.csv", index=False)
        st.success("Venda cadastrada com sucesso!")




st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)


st.write("## Dashboard")
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento total", f"R$ {faturamento}")

grafico_faturamento = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto", title="Faturamento por Produto")
st.plotly_chart(grafico_faturamento)

grafico_quantidade = px.pie(tabela_vendas, names="produto", values="valor", color="produto", title="Quantidade Vendida por Produto", hole = 0.5)
st.plotly_chart(grafico_quantidade)

