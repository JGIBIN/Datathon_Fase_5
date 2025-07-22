# Decision AI Recruiter

Este é um projeto de um assistente de recrutamento que utiliza Inteligência Artificial para otimizar o processo de seleção. A aplicação foi desenvolvida com Streamlit e permite a análise de compatibilidade de candidatos a vagas em tempo real.

## 🎯 O Desafio

O objetivo deste projeto é resolver um desafio de negócio, demonstrando como a IA pode ser aplicada para melhorar a eficiência do recrutamento.

## 🚀 Instalação e Execução

Para executar este projeto em sua máquina local, siga os passos abaixo.

### Pré-requisitos

- Python 3.7 ou superior
- `pip` (gerenciador de pacotes do Python)

### Passos

1.  **Clone o repositório (ou faça o download dos arquivos):**

    Se o projeto estiver em um repositório git, use o comando:
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DO_DIRETORIO>
    ```
    Caso contrário, apenas certifique-se de que todos os arquivos (`app.py`, `requirements.txt`, `config.py`, `utils.py` e a pasta `assets`) estejam no mesmo diretório.

2.  **Crie e ative um ambiente virtual (Recomendado):**

    É uma boa prática usar um ambiente virtual para isolar as dependências do projeto.
    ```bash
    # Criar ambiente virtual
    python -m venv venv

    # Ativar no Windows
    .\venv\Scripts\activate

    # Ativar no macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**

    Todas as bibliotecas necessárias estão listadas no arquivo `requirements.txt`. Para instalá-las, execute o seguinte comando no seu terminal:
    ```bash
    pip install -r requirements.txt
    ```
    Isso instalará as seguintes bibliotecas:
    - pandas
    - numpy
    - scikit-learn
    - xgboost
    - joblib
    - unidecode
    - nltk
    - streamlit

4.  **Execute a aplicação:**

    Com as dependências instaladas, inicie o servidor do Streamlit com o comando:
    ```bash
    streamlit run app.py
    ```
    A aplicação será aberta automaticamente no seu navegador padrão.

## 🏛️ Estrutura do Projeto

-   `app.py`: Ponto de entrada da aplicação Streamlit, a página inicial.
-   `requirements.txt`: Lista de todas as dependências do Python para o projeto.
-   `config.py`: Arquivo de configuração para as páginas e caminhos de assets.
-   `utils.py`: Funções utilitárias, como a configuração da página.
-   `pages/`: Diretório contendo as outras páginas da aplicação (`1_🎯_O_Desafio.py`, `2_✏️_Cadastro_na_Vaga.py`).
-   `assets/`: Diretório para armazenar arquivos estáticos, como o logo da empresa.
-   `models/`: Contém os modelos e dados necessários para a predição (`decision_model.pkl`, `descricoes_vagas.json`, `vagas_disponiveis.json`).
-   `dados/`: Armazena os dados utilizados (`df_final.parquet`).