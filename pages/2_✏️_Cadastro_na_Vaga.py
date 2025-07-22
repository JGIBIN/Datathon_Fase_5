# ==============================================================================
# PÁGINA STREAMLIT: ANÁLISE DE COMPATIBILIDADE E APLICAÇÃO DE VAGA
# ==============================================================================

# --- SEÇÃO 0: IMPORTS ---
import streamlit as st
import pandas as pd
import joblib
import json
import os
from datetime import datetime
from utils import setup_page


# --- Configuração da Página ---
setup_page(__file__)


# --- Constante para o caminho da base de dados ---
DATABASE_PATH = "prospects_database.csv"

# ==============================================================================
# SEÇÃO 1: FUNÇÕES AUXILIARES
# ==============================================================================

@st.cache_resource
def carregar_artefatos():
    """Carrega os artefatos salvos (pipeline do modelo, lista de vagas e descrições)."""
    try:
        pipeline = joblib.load("models/decision_model.pkl")
        with open("models/vagas_disponiveis.json", 'r', encoding='utf-8') as f:
            lista_vagas = json.load(f)
        with open("models/descricoes_vagas.json", 'r', encoding='utf-8') as f:
            descricoes = json.load(f)
        return pipeline, lista_vagas, descricoes
    except FileNotFoundError as e:
        st.error(f"Erro ao carregar artefatos: {e}. Verifique se os arquivos estão na pasta 'models'.")
        return None, None, None

def salvar_aplicacao(data):
    """Salva os dados da aplicação do candidato em um arquivo CSV."""
    df_aplicacao = pd.DataFrame([data])
    if not os.path.exists(DATABASE_PATH):
        df_aplicacao.to_csv(DATABASE_PATH, index=False, sep=';', encoding='utf-8-sig')
    else:
        df_aplicacao.to_csv(DATABASE_PATH, mode='a', header=False, index=False, sep=';', encoding='utf-8-sig')

# ==============================================================================
# SEÇÃO 2: LAYOUT DA PÁGINA E INTERFACE DO USUÁRIO
# ==============================================================================

st.markdown("# 📝 Análise de Compatibilidade Candidato-Vaga")
st.markdown("---")

model_pipeline, vagas_disponiveis, descricoes_vagas = carregar_artefatos()

if model_pipeline and vagas_disponiveis and descricoes_vagas:
    st.info("Bem-vindo(a)! Primeiro, selecione uma vaga. Depois, preencha o formulário para ver sua compatibilidade.")
    st.write("")

    # --- PARTE 1: SELEÇÃO DA VAGA (FORA DO FORMULÁRIO) ---
    # Esta seção precisa ser interativa, por isso fica aqui fora.
    
    st.subheader("🎯 Vaga de Interesse")
    
    termo_pesquisa = st.text_input(
        "Pesquisar vaga por nome:",
        placeholder="Ex: Analista de Dados"
    )

    if termo_pesquisa:
        vagas_filtradas = [v for v in vagas_disponiveis if termo_pesquisa.lower() in v.lower()]
    else:
        vagas_filtradas = sorted(vagas_disponiveis)

    vaga_selecionada = st.selectbox(
        'Selecione a vaga para a qual deseja aplicar*',
        options=vagas_filtradas,
        index=0 if vagas_filtradas else None
    )
    
    if vaga_selecionada:
        with st.expander("Ver Descrição da Vaga", expanded=True):
            st.markdown(descricoes_vagas.get(vaga_selecionada, "Descrição não disponível."))
    elif termo_pesquisa:
         st.warning("Nenhuma vaga encontrada com este termo.")
    
    st.markdown("---")

    # --- PARTE 2: FORMULÁRIO DE DADOS DO CANDIDATO ---
    # Apenas os campos que devem ser submetidos juntos ficam aqui dentro.
    
    with st.form(key='application_form'):
        st.subheader("👤 Dados Pessoais")
        col_pessoal1, col_pessoal2 = st.columns(2)
        with col_pessoal1:
            nome_candidato = st.text_input("Nome Completo*")
        with col_pessoal2:
            email_candidato = st.text_input("E-mail*")
        linkedIn_candidato = st.text_input("Perfil do LinkedIn (opcional)")
        st.write("")

        st.subheader("📈 Perfil Profissional")
        col1, col2 = st.columns(2)
        with col1:
            nivel_profissional = st.selectbox('Nível Profissional*', ['Júnior', 'Pleno', 'Sênior', 'Especialista', 'Desconhecido'], index=1)
            nivel_academico = st.selectbox('Nível Acadêmico*', ['Ensino Médio', 'Técnico', 'Superior Incompleto', 'Superior Completo', 'Pós-graduação', 'Mestrado', 'Doutorado', 'Desconhecido'], index=3)
        with col2:
            nivel_ingles = st.selectbox('Nível de Inglês*', ['Básico', 'Intermediário', 'Avançado', 'Fluente', 'Desconhecido'], index=1)
            nivel_espanhol = st.selectbox('Nível de Espanhol*', ['Básico', 'Intermediário', 'Avançado', 'Fluente', 'Não possuo', 'Desconhecido'], index=4)

        conhecimentos_tecnicos = st.text_area(
            "Seus Conhecimentos Técnicos*",
            height=200,
            placeholder="Descreva suas experiências, tecnologias que domina (Python, SQL, Power BI, etc.)..."
        )
        certificacoes = st.text_area(
            "Suas Certificações",
            height=100,
            placeholder="Liste suas certificações relevantes para a vaga..."
        )
        comentario = st.text_area(
            "Comentário Adicional",
            placeholder="Adicione uma nota (opcional)."
        )

        st.caption("Campos com * são obrigatórios.")
        st.write("")
        
        submit_button = st.form_submit_button(label='✅ Enviar Aplicação e Ver Compatibilidade')

    # --- LÓGICA APÓS O ENVIO DO FORMULÁRIO ---
    if submit_button:
        if not all([nome_candidato, email_candidato, conhecimentos_tecnicos, vaga_selecionada]):
            st.warning("Por favor, preencha todos os campos obrigatórios (*).")
        else:
            with st.spinner('Processando sua aplicação...'):
                descricao_vaga_completa = descricoes_vagas.get(vaga_selecionada, "")
                texto_candidato_combinado = f"{conhecimentos_tecnicos} {certificacoes}"
                texto_completo_input = f"{descricao_vaga_completa} {texto_candidato_combinado}"

                input_data_model = {
                    'texto_completo': texto_completo_input,
                    'perfil_vaga.nivel profissional': nivel_profissional,
                    'perfil_vaga.nivel_academico': nivel_academico,
                    'perfil_vaga.nivel_ingles': nivel_ingles,
                    'formacao_e_idiomas.nivel_academico': nivel_academico,
                    'formacao_e_idiomas.nivel_ingles': nivel_ingles,
                    'formacao_e_idiomas.nivel_espanhol': nivel_espanhol,
                }
                input_df = pd.DataFrame([input_data_model])

                probabilidade = model_pipeline.predict_proba(input_df)[0][1]
                score_compatibilidade = int(probabilidade * 100)

                application_data_to_save = {
                    "data_aplicacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "nome_candidato": nome_candidato,
                    "email_candidato": email_candidato,
                    "linkedin_candidato": linkedIn_candidato,
                    "vaga_aplicada": vaga_selecionada,
                    "score_compatibilidade": score_compatibilidade,
                    "nivel_profissional": nivel_profissional,
                    "nivel_academico": nivel_academico,
                    "nivel_ingles": nivel_ingles,
                    "nivel_espanhol": nivel_espanhol,
                    "informacoes_profissionais.conhecimentos_tecnicos": conhecimentos_tecnicos,
                    "informacoes_profissionais.certificacoes": certificacoes,
                    "comentario": comentario
                }

                salvar_aplicacao(application_data_to_save)

                st.success(f"Obrigado, {nome_candidato}! Sua aplicação para a vaga '{vaga_selecionada}' foi recebida com sucesso.")
                st.metric(label="Seu percentual de Compatibilidade com a Vaga é:", value=f"{score_compatibilidade}%")
                st.progress(score_compatibilidade / 100.0)
                st.markdown("Boa sorte no processo! 🍀 Estamos na torcida por você.🎊")
                st.balloons()