# pages/1_🎯_O_Desafio.py

import streamlit as st
from utils import setup_page

# Configura a página e a barra lateral
setup_page(__file__)

# --- TÍTULO DA PÁGINA ---
st.markdown("# O Desafio: IA no Recrutamento e Seleção")
st.markdown("---")

# --- NOVA SEÇÃO: SOBRE A DECISION ---
st.subheader("Sobre a Decision")
st.markdown(
    """
    Fundada em 1999, a Decision oferece serviços na área de Gestão de Recursos Humanos, 
    atuando em frentes de Tecnologia da Informação, Projetos e Consultorias. 
    Com escritórios em São Paulo, Campinas, Rio de Janeiro, Curitiba e Porto Alegre, 
    carregamos uma história de comprometimento, qualidade e confiança.
    
    A maneira como trabalhamos foge ao tradicional: o foco é resolver a necessidade 
    do cliente com agilidade, qualidade e inovação. As análises e recomendações são 
    baseadas em nossa ampla experiência, para garantir uma entrega eficiente e de alto padrão.
    """
)

# --- SERVIÇOS ---
st.markdown("#### Nossos Serviços:")
st.markdown(
    """
    - **Outsourcing:** Otimizamos a produtividade com nossos especialistas que contribuem com soluções ágeis de Tecnologia da Informação (TI).
        - Contratamos o profissional de acordo com a sua necessidade.
        - Analisamos os desafios da área de TI e validamos os custos atuais.
        - Conduzimos todo o processo de propostas, negociação e acompanhamos a fase de transição.

    - **Hunting:** Nossa equipe qualificada identifica o melhor talento para cada um de nossos clientes.
        - Entendemos a posição e o perfil desejado.
        - Avaliamos histórico, capacitações e aplicamos testes técnicos e psicológicos.
        - Cruzamos as necessidades do cliente com as expertises dos profissionais.

    - **BPO (Business Process Outsourcing):** Otimizamos o trabalho e a produtividade de processos com comprometimento em SLA, metas e cronogramas em diversas áreas.
        - Áreas atendidas: Administrativo, Almoxarifado, Arquivista, RH, Vendas, Compras, Engenharia, Produção, Financeiro, Jurídico, Customer Services, Suprimentos, BackOffice e Cargos executivos.
    """
)
st.markdown(
    """
    Fontes:
    
    - [Site Decision](https://www.decisionbr.com.br)
    
    - [LinkedIn Decision](https://www.linkedin.com/company/decisionbr-consultants/about)
    """
)
st.markdown("---")


# --- PROBLEMA CENTRAL ---
st.subheader("🎯 O Problema Central: Eficiência vs. Precisão no Recrutamento")
st.markdown(
    """
    No contexto de um portfólio de serviços tão amplo e especializado, o principal desafio era como otimizar a triagem inicial de currículos sem sacrificar a qualidade da análise. As dores do processo manual incluíam:

    - **Falta de Padronização:** Diferentes recrutadores podiam ter abordagens distintas.
    - **Dificuldade em Medir Engajamento:** Desafio de identificar o real interesse e compatibilidade técnica do candidato.
    - **Agilidade vs. Qualidade:** A pressão para preencher vagas rapidamente podia levar a um "match" de menor aderência.
    """
)

# --- OBSTÁCULOS ("PERCALÇOS") ---
st.subheader("🚧 Os Percalços do Desenvolvimento")
st.markdown(
    """
    Durante a construção da solução, enfrentamos alguns desafios técnicos significativos:

    1.  **Dados Heterogêneos:** Mistura de informações estruturadas (nível de experiência) com texto não estruturado (currículos, comentários).
    2.  **Engenharia de Features:** Necessidade de aplicar técnicas de Processamento de Linguagem Natural (NLP) para converter texto em features numéricas que um modelo pudesse entender.
    3.  **Definição do "Sucesso":** Usar o histórico de contratações para treinar o modelo a identificar o que define um "bom match".
    """
)

# --- A SOLUÇÃO E O MODELO ---
st.subheader("💡 Nossa Proposta e a Escolha do Modelo")
st.markdown(
    """
    Para solucionar essas dores, propomos um **MVP (Minimum Viable Product)** que utiliza Machine Learning para automatizar e otimizar a triagem inicial.

    A solução é um **modelo preditivo que calcula um "score" de compatibilidade** entre o perfil de um candidato e a descrição de uma vaga, utilizando um pipeline do `scikit-learn` com um modelo `XGBoost` no núcleo.
    """
)

# --- MÉTRICAS DE PERFORMANCE E DEFESA DOS RESULTADOS ---
st.subheader("📊 Resultados e Defesa da Solução")
st.code(
    """
--- MÉTRICAS DE PERFORMANCE (NO CONJUNTO DE TESTE) ---
  - Acurácia: 0.8221
  - F1-Score: 0.7910
----------------------------------------------------
""",
    language=None
)

st.markdown(
    """
    A **Acurácia de 82%** prova que o modelo foi eficaz em extrair o sinal correto do ruído dos dados complexos. O **F1-Score de 79%** demonstra que a ferramenta é confiável, equilibrando a recomendação de bons candidatos e minimizando o descarte de talentos. Além disso, cada aplicação é **salva em uma base de dados local** para rastreabilidade e melhoria contínua.
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