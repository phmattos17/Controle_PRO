import pandas as pd
import streamlit as st
import numpy as np


df = pd.read_csv('controle_alimentos_pro.csv',sep=',')

st.set_page_config(page_title="Entrada de Produtos")

st.markdown("Formulário para Entrada de Produtos")
st.sidebar.header("Entrada de Produtos")

st.markdown(
    '''
    Nesta aba você poderá adicionar produtos a lista.  
      
    Só aperte o botão de cadastro quando tiver preenchido todos os dados 🧐
    '''
)

with st.form(key='my_form_entrada'):
    produto = st.selectbox(
        'Por favor, selecione o produto',
        (np.sort(np.array(['Achocolatado 200 g', 'Açúcar', 'Amido de Milho 500 g', 'Arroz',
         'Aveia Yoki 170 gr', 'Azeite Extra Virgem', 'Batata Palha 500 gr',
         'Ervilha', 'Extrato de Tomate', 'Feijão Mulatinho', 'Ketchup 7 g',
         'Leite Condensado 395g', 'Leite Condensado 350 g',
         'Leite Condensado 200 g', 'Leite Caixa 1l', 'Leite de Coco 200 ml',
         'Macarrão Pene', 'Macarrão Parafuso', 'Macarrão Rigate',
         'Maionese 7 g', 'Margarina 250 g', 'Margarina 1 Kg',
         'Milharina Flocão', 'Óleo de Soja 1l',
         'Pipoca de Microondas', 'Queijo Ralado', 'Vinagre 500 ml',
         'Leite em Pó', 'Macarrão','Milharina','Sardinha','Fermento',
         'Sal', 'Feijão Preto','Água Sanitária','Sabonete','Pasta de Dente',
         'Vela','Biscoito Wafer Chocolate','Biscoito Wafer Limão','Biscoito Wafer Morango',
         'Biscoito Maizena Chocolate','Biscoito Maizena Leite','Biscoito Maria Chocolate',
         'Biscoito Maria Leite','Mistura Bolo Abacaxi','Mistura Bolo Limão','Mistura Bolo Milho',
         'Mistura Bolo Chocolate','Mistura Bolo Morango','Biscoito']))
         ), key='produto_entrada')

    marca = st.text_input(
        'Por favor, digite a marca do produto',
        key = 'marca_entrada'
    )

    quantidade = st.number_input(
        'Por favor, informe a quantidade',
        key = 'quantidade_entrada'
    )

    unidade_medida = st.selectbox(
        'Por favor, selecione o produto',
        ('Unidades','kg','Latas','Sachês'
         ), key='unidade_medida')


    data_validade = st.date_input(
        "Por favor, informe a data de validade",
        key = 'validade_entrada')

    tipo_entrada = st.selectbox(
        'Por favor, selecione o tipo de entrada',
        ('Compra', 'Doação'),
        key='tipo_entrada')

    add_button = st.form_submit_button('Adicionar')

    if add_button:
        df2 = pd.DataFrame({
            'PRODUTO':[st.session_state['produto_entrada']],
            'MARCA DO PRODUTO':[st.session_state['marca_entrada']],
            'QUANTIDADE':[st.session_state['quantidade_entrada']],
            'UNIDADE DE MEDIDA':[st.session_state['unidade_medida']],
            'DATA DE VALIDADE' :[st.session_state['validade_entrada']],
            'TIPO DE ENTRADA':[st.session_state['tipo_entrada']]
        })

        df = df.append(df2, ignore_index = True)

        df.to_csv('controle_alimentos_pro.csv',index=False)

        st.balloons()
