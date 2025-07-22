# app.py (ou 🏠_Início.py)

import streamlit as st
from utils import setup_page

# Chama a função de setup, agora com apenas um argumento
setup_page(__file__)

# --- PÁGINA PRINCIPAL ---
st.title("Bem-vindo ao Assistente de Recrutamento da Decision!")
st.markdown("---")
st.markdown(
    """
    ### Navegue pelas páginas ao lado para conhecer o desafio e testar nossa solução.
    
    - **O Desafio:** Entenda o problema de negócio que motivou este projeto.
    - **Cadastro na Vaga:** Se candidate a uma vaga e veja a análise de compatibilidade em tempo real.
    
    *Use o menu na barra à esquerda para navegar entre as seções.*
    """
)