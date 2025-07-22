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

    1.  **Dados Heterogêneos:** Os dados dos candidatos vinham de fontes diversas, misturando informações estruturadas (nível de experiência, formação) com uma grande massa de texto não estruturado (currículos, descrições de atividades, comentários). Tratar e padronizar essa variedade foi o primeiro grande obstáculo.

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
    """
)

# --- MÉTRICAS DE PERFORMANCE E DEFESA DOS RESULTADOS ---
st.subheader("📊 Resultados e Defesa da Solução")
st.markdown(
    """
    Para validar a eficácia do nosso modelo, ele foi rigorosamente avaliado em um conjunto de dados de teste. Os resultados não são apenas números, mas uma resposta direta aos desafios que enfrentamos.
    """
)
st.code(
    """
--- MÉTRICAS DE PERFORMANCE (NO CONJUNTO DE TESTE) ---
  - Acurácia: 0.8221 (82.21%)
  - F1-Score: 0.7910 (79.10%)
----------------------------------------------------
""",
    language=None
)

st.markdown("#### Por que essas métricas são boas para o nosso problema?")

st.markdown(
    """
    1.  **Superando a Complexidade dos Dados (Acurácia de 82%)**:
        Nosso principal obstáculo era a bagunça e a falta de padrão nos dados. Uma **acurácia de 82.21%** em dados de teste significa que, mesmo com toda a complexidade de currículos e descrições de vagas, o modelo acerta a previsão de compatibilidade em mais de 8 a cada 10 casos.

    2.  **Resolvendo o Conflito Agilidade vs. Qualidade (F1-Score de 79%)**:
        No recrutamento, o erro mais caro é descartar um bom candidato. O **F1-Score de 79.10%** demonstra que nossa ferramenta é confiável, pois ela busca um equilíbrio entre recomendar bons candidatos e minimizar as chances de deixar talentos valiosos escaparem.

    3.  **Rastreabilidade e Melhoria Contínua**:
        Além da análise, cada aplicação é **salva em uma base de dados local (arquivo CSV)**, criando um registro histórico para auditorias e futuro re-treinamento do modelo.

    Em suma, as métricas validam que a solução proposta ataca diretamente as dores do processo de R&S, oferecendo uma triagem inicial automatizada, rápida, confiável e rastreável.
    """
)

# --- MEMBROS DO GRUPO ---
st.markdown("---")
st.subheader("👥 Membros do Grupo")
st.markdown(
    """
    - **Isaura Lima de Oliveira** - RM358471
    - **Jorge Diego Guarda Gibin** - RM359181
    - **Thiago de Mendonça Modesto** - RM358841
    """
)

st.markdown(
    """
    > **Agora, navegue até a página 'Cadastro na Vaga' para ver a solução em ação!**
    """
)