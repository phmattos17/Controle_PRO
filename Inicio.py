import streamlit as st

st.set_page_config(
    page_title="Inicial"
)

st.sidebar.header("Página Inicial")

st.title(' Controle Almoxarifado Unidade Piedade')

st.markdown(
    '''
    Este aplicativo tem como principal objetivo garantir de forma **fácil e segura** o controle dos
    itens do almoxarifado do Movimento Pró Criança Unidade Piedade.  
      
      
    
    ### Você poderá fazer as seguintes ações 🤓:  
    - Cadastrar entradas e saídas de produtos
    - Visualizar produtos com data crítica
    - Visualizar prdutos e suas quantidades armazenadas
      
      
      
    ### Para o cadastro, tenha em mãos os seguintes dados ✏️:  
    - Produto
    - Marca do Produto
    - Quantidade
    - Data de Validade
    - Tipo de Entrada: Compra ou Doação
    
    '''
)
