# pages/1_🎯_O_Desafio.py

import streamlit as st
from utils import setup_page

# Configura a página e a barra lateral
setup_page(__file__)

# --- TÍTULO DA PÁGINA ---
st.markdown("# O Desafio: IA no Recrutamento e Seleção")
st.markdown("---")

# --- CONTEXTO INICIAL ---
st.markdown(
    """
    A **Decision**, como empresa especializada em alocação de talentos de TI (bodyshop), 
    enfrenta o desafio constante de encontrar o candidato ideal para cada vaga de forma 
    rápida e precisa. O processo de "match" entre um profissional e uma oportunidade é complexo e envolve múltiplas variáveis.
    """
)

# --- PROBLEMA CENTRAL ---
st.subheader("🎯 O Problema Central: Eficiência vs. Precisão")
st.markdown(
    """
    O principal desafio era como otimizar a triagem inicial de currículos sem sacrificar a qualidade da análise. As dores do processo manual incluíam:

    - **Falta de Padronização:** Diferentes recrutadores podiam ter abordagens distintas, levando à perda de informações valiosas sobre os candidatos.
    - **Dificuldade em Medir Engajamento:** Era um desafio identificar o real interesse e a compatibilidade técnica do candidato nas primeiras etapas.
    - **Agilidade vs. Qualidade:** A pressão para preencher vagas rapidamente podia levar a saltar etapas cruciais, resultando em um "match" de menor aderência e potencial retrabalho.
    """
)

# --- OBSTÁCULOS ("PERCALÇOS") ---
st.subheader("🚧 Os Percalços do Desenvolvimento")
st.markdown(
    """
    Durante a construção da solução, enfrentamos alguns desafios técnicos significativos:

    1.  **Dados Heterogêneos:** Os dados dos candidatos não estão em uma forma consistente, misturando informações estruturadas (nível de experiência, formação) com uma grande massa de texto não estruturado (currículos, descrições de atividades, comentários). Tratar e padronizar essa variedade foi o primeiro grande obstáculo.

    2.  **Engenharia de Features:** Como transformar texto livre — com seus jargões, abreviações e semântica complexa — em features numéricas que um modelo de Machine Learning pudesse entender? Foi necessário aplicar técnicas de Processamento de Linguagem Natural (NLP), como a vetorização TF-IDF, para converter palavras em vetores que representam sua importância.

    3.  **Definição do "Sucesso":** O que define um "bom match"? Foi preciso usar o histórico de contratações da Decision para treinar o modelo. O alvo da previsão se tornou a probabilidade de um candidato ser considerado aderente à vaga, com base nos padrões de perfis que tiveram sucesso no passado.
    """
)

# --- A SOLUÇÃO E O MODELO ---
st.subheader("💡 Nossa Proposta e a Escolha do Modelo")
st.markdown(
    """
    Para solucionar essas dores, propomos um **MVP (Minimum Viable Product)** que utiliza Machine Learning para automatizar e otimizar a triagem inicial.

    A solução é um **modelo preditivo que calcula um "score" de compatibilidade** entre o perfil de um candidato e a descrição de uma vaga.

    **Por que adotamos este modelo?**
    - **Combinação de Dados:** A abordagem escolhida, utilizando um pipeline do `scikit-learn`, nos permitiu combinar de forma eficaz tanto os dados estruturados (níveis, formação) quanto o texto não estruturado (habilidades, experiências).
    - **Performance com XGBoost:** O coração do nosso modelo é o `XGBoost`, um algoritmo de Gradient Boosting. Ele foi escolhido por sua alta performance em dados tabulares e heterogêneos (como os nossos, após a engenharia de features), sua robustez e capacidade de capturar interações complexas entre as variáveis.
    - **Interpretabilidade e Eficiência:** O modelo não só oferece uma predição precisa, mas também é eficiente, permitindo uma análise em tempo real. Isso cria uma ferramenta poderosa para auxiliar a equipe de recrutamento a focar nos candidatos com maior potencial.

    > **Navegue até a página 'Análise de Compatibilidade' para ver a solução em ação!**
    """
)