# Decision AI Recruiter

Este é um projeto de um assistente de recrutamento que utiliza Inteligência Artificial para otimizar o processo de seleção da empresa Decision. A aplicação foi desenvolvida com Streamlit e permite a análise de compatibilidade de candidatos a vagas em tempo real.

## 🎯 O Desafio

O objetivo deste projeto é resolver um desafio de negócio, demonstrando como a IA pode ser aplicada para melhorar a eficiência do recrutamento, atacando dores como a falta de padronização, dificuldade em medir engajamento e o conflito entre agilidade e qualidade na seleção.

## 🚀 Instalação e Execução

Para executar este projeto em sua máquina local, siga os passos abaixo.

### Pré-requisitos

- Python 3.7 ou superior
- `pip` (gerenciador de pacotes do Python)

### Passos

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd <NOME_DO_DIRETORIO>
    ```

2.  **Crie e ative um ambiente virtual (Recomendado):**
    ```bash
    # Criar ambiente virtual
    python -m venv venv

    # Ativar no Windows
    .\venv\Scripts\activate

    # Ativar no macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    Todas as bibliotecas necessárias estão listadas no arquivo `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    Com as dependências instaladas, inicie o servidor do Streamlit:
    ```bash
    streamlit run app.py
    ```
    A aplicação será aberta automaticamente no seu navegador.

## 🏛️ Estrutura do Projeto

-   `app.py`: Ponto de entrada da aplicação, a página inicial.
-   `requirements.txt`: Lista de todas as dependências do Python.
-   `config.py`: Arquivo de configuração para as páginas e assets.
-   `utils.py`: Funções utilitárias compartilhadas.
-   `pages/`: Diretório contendo as outras páginas da aplicação.
-   `assets/`: Diretório para armazenar arquivos estáticos (logo).
-   `models/`: Contém o modelo treinado e os dados das vagas.
-   `prospects_database.csv`: Arquivo onde os dados das aplicações são salvos.

## 👥 Membros do Grupo

-   **Isaura Lima de Oliveira** - RM358471
-   **Jorge Diego Guarda Gibin** - RM359181
-   **Thiago de Mendonça Modesto** - RM358841