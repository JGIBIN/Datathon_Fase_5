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
# Configura a página e a barra lateral
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
        st.error(f"Erro ao carregar artefatos: {e}. Certifique-se de que os arquivos 'decision_model.pkl', 'vagas_disponiveis.json' e 'descricoes_vagas.json' estão na pasta 'models'.")
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

st.markdown("# Cadastro e Análise de Compatibilidade Candidato vs Vaga")
st.markdown("---")

model_pipeline, vagas_disponiveis, descricoes_vagas = carregar_artefatos()

if model_pipeline and vagas_disponiveis and descricoes_vagas:
    st.info("Bem-vindo(a)! Preencha o formulário abaixo para aplicar para uma de nossas vagas e veja sua compatibilidade instantaneamente.")

    with st.form(key='application_form'):
        
        
        # --- SEÇÃO 1: VAGA DE INTERESSE (MANTIDA) ---
        st.subheader("1. Vaga de Interesse")
        vaga_selecionada = st.selectbox(
            'Para qual vaga você deseja aplicar?*',
            options=sorted(vagas_disponiveis)
        )
        if vaga_selecionada:
            with st.expander("📝Ver Descrição da Vaga", expanded=False):
                st.markdown(descricoes_vagas.get(vaga_selecionada, "Descrição não disponível."))

        st.markdown("---")


        # --- SEÇÃO 2: DADOS PESSOAIS ---
        st.subheader("2. Dados Pessoais")
        col_pessoal1, col_pessoal2, col_pessoal3 = st.columns(3)
        with col_pessoal1:
            nome_candidato = st.text_input("Nome Completo*")
        with col_pessoal2:
            email_candidato = st.text_input("E-mail*")
        with col_pessoal3:
            telefone = st.text_input("Telefone de Contato")
        linkedIn_candidato = st.text_input("Perfil do LinkedIn (opcional)")

        st.markdown("---")


        # --- SEÇÃO 3: PERFIL PROFISSIONAL (MODIFICADA) ---
        st.subheader("3. Perfil Profissional")
        col1, col2 = st.columns(2)
        with col1:
            nivel_profissional = st.selectbox('Nível Profissional*', ['Júnior', 'Pleno', 'Sênior', 'Especialista', 'Desconhecido'], index=1)
            nivel_academico = st.selectbox('Nível Acadêmico*', ['Ensino Médio', 'Técnico', 'Superior Incompleto', 'Superior Completo', 'Pós-graduação', 'Mestrado', 'Doutorado', 'Desconhecido'], index=3)
        with col2:
            nivel_ingles = st.selectbox('Nível de Inglês*', ['Básico', 'Intermediário', 'Avançado', 'Fluente', 'Desconhecido'], index=1)
            nivel_espanhol = st.selectbox('Nível de Espanhol*', ['Básico', 'Intermediário', 'Avançado', 'Fluente', 'Não possuo', 'Desconhecido'], index=4)

        # --- CAMPOS DE TEXTO DETALHADOS (NOVO) ---
        conhecimentos_tecnicos = st.text_area(
            "Conhecimentos Técnicos*",
            height=200,
            placeholder="Descreva suas experiências, tecnologias que domina (Python, SQL, Power BI, etc.), projetos que participou e seus objetivos profissionais."
        )
        certificacoes = st.text_area(
            "Certificações",
            height=100,
            placeholder="Liste suas certificações relevantes para a vaga (ex: AWS Certified, Scrum Master, etc.)."
        )
        comentario = st.text_area(
            "Comentário Adicional",
            placeholder="Adicione um comentário ou nota (opcional)."
        )

        st.caption("Campos com * são obrigatórios.")
        submit_button = st.form_submit_button(label='Enviar Aplicação e Ver Compatibilidade')

    if submit_button:
        if not nome_candidato or not email_candidato or not conhecimentos_tecnicos:
            st.warning("Por favor, preencha todos os campos obrigatórios (*).")
        else:
            with st.spinner('Processando sua aplicação...'):
                # LÓGICA ATUALIZADA
                # 1. Pega a descrição completa da vaga selecionada
                descricao_vaga_completa = descricoes_vagas.get(vaga_selecionada, "")
                # 2. Combina os novos campos de texto do candidato
                texto_candidato_combinado = f"{conhecimentos_tecnicos} {certificacoes}"
                # 3. Cria o input para o modelo com a descrição completa da vaga
                texto_completo_input = f"{descricao_vaga_completa} {texto_candidato_combinado}"

                # Monta o DataFrame para o modelo
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

                # Gera o score de compatibilidade
                probabilidade = model_pipeline.predict_proba(input_df)[0][1]
                score_compatibilidade = int(probabilidade * 100)

                # Prepara os dados para salvar na base (com os novos campos)
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
                    # SALVANDO OS NOVOS CAMPOS
                    "informacoes_profissionais.conhecimentos_tecnicos": conhecimentos_tecnicos,
                    "informacoes_profissionais.certificacoes": certificacoes,
                    "comentario": comentario
                }

                # Salva os dados no arquivo CSV
                salvar_aplicacao(application_data_to_save)

                st.success(f"Obrigado, {nome_candidato}! Sua aplicação para a vaga '{vaga_selecionada}' foi recebida com sucesso.")
                st.metric(label="Seu percentual de Compatibilidade com a Vaga é:", value=f"{score_compatibilidade}%")
                st.progress(score_compatibilidade / 100.0)
                st.markdown("Boa sorte no processo! 🍀 Estamos na torcida por você.🎊")
                st.balloons()