import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


df = pd.read_csv('controle_alimentos_pro.csv',sep=',')
df_retirada = pd.read_csv('retiradas.csv',sep=',')

st.set_page_config(page_title="Resumo de Produtos")

st.sidebar.header("Resumo de Produtos")

st.markdown(
    '''
    Nesta aba você terá duas importantes funções deste app:  
    - Identificar produtos com data crítica de validade
    - Obter um resumo dos itens em estoque
    
    '''
)

st.markdown('### Produtos com data de validade crítica 🚨')

df['DATA DE VALIDADE'] = pd.to_datetime(df['DATA DE VALIDADE'],format='%Y-%m-%d')

df['HOJE'] =pd.to_datetime('today').normalize()

df['DIAS PARA VENCIMENTO'] = (df['HOJE']-df['DATA DE VALIDADE'])/np.timedelta64(1,'D')

st.write(df[df['DIAS PARA VENCIMENTO']<=15][['PRODUTO','MARCA DO PRODUTO','QUANTIDADE','UNIDADE DE MEDIDA',
                                   'DATA DE VALIDADE' ,'TIPO DE ENTRADA']])

st.markdown('### Produtos de Compras em Estoque  ')

st.dataframe(df[df['TIPO DE ENTRADA']=='Compra'])

st.markdown('### Produtos de Doações em Estoque  ')

st.dataframe(df[df['TIPO DE ENTRADA']=='Doação'])

st.markdown('### Histórico Retirada ')

st.dataframe(df_retirada)



if st. button('Baixar Itens em Estoque'):

    df_sorted = df.sort_values('PRODUTO')
    fig, ax =plt.subplots(figsize=(12,4))
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=df_sorted.values,colLabels=df_sorted.columns,loc='center')

    pp = PdfPages("table.pdf")
    pp.savefig(fig, bbox_inches='tight')
    pp.close()