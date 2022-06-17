import pandas as pd
import numpy as np
import streamlit as st

df = pd.read_csv('controle_alimentos_pro.csv',sep=',')
df_retirada = pd.read_csv('retiradas.csv',sep=',')

st.set_page_config(page_title="Retirada de Produtos")

st.markdown("Formulário para Retirada de Produtos")
st.sidebar.header("Retirada de Produtos")

st.markdown(
    '''
    Nesta aba você poderá retirar produtos da lista.  
      
    Você só precisa informar três dados do produto 😁:
    - Produto
    - Data de Validade
    - Quantidade Retirada
    
    
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
         ), key='produto_saida')

    quantidade = st.number_input(
        'Por favor, informe a quantidade',
        key = 'quantidade_saida'
    )

    data_validade = st.date_input(
        "Por favor, informe a data de validade",
        key = 'validade_saida')

    responsavel = st.selectbox(
        'Por favor, indique o setor responsável pela retirada',
        (np.sort(np.array(['GESTÃO',"ADMINISTRATIVO","PSICOSSOCIAL","LIMPEZA","COZINHA"]))),
                 key = 'responsavel_retirada')

    retirar_button = st.form_submit_button('Retirar')

    if retirar_button:
        df2 = pd.DataFrame({
            'PRODUTO':[st.session_state['produto_saida']],
            'QUANTIDADE':[st.session_state['quantidade_saida']],
            'DATA DE RETIRADA' :pd.to_datetime('today').normalize(),
            'RESPONSÁVEL':[st.session_state['responsavel_retirada']]
        })

        df_retirada = df_retirada.append(df2, ignore_index = True)

        df_retirada.to_csv('retiradas.csv',index=False)

        try:

            df.loc[(df['PRODUTO']==st.session_state['produto_saida'])|
                   (df['DATA DE VALIDADE']==st.session_state['validade_saida']),'QUANTIDADE']-=st.session_state['quantidade_saida']

            df.to_csv('controle_alimentos_pro.csv',index=False)

            st.balloons()
        except:

            st.write('Não foi possível completar a retirada. Por favor, verifique os dados')