#  Projeto ETL – Pipeline de Dados (Bronze → Silver → PostgreSQL)

Este projeto implementa um **pipeline ETL completo**, desde a ingestão de dados brutos até a persistência em banco de dados PostgreSQL, seguindo boas práticas de organização em camadas (**Bronze / Silver**) e preparação para análise exploratória.

O objetivo é demonstrar habilidades em **engenharia de dados**, **tratamento de dados estruturados e semi-estruturados**, **persistência em banco relacional** e **análise exploratória com Python**.

---

##  Arquitetura do Projeto

Projeto_ETL/
├── 01.bronze.raw/
│   ├── users.csv
│   └── cryptocurrencies.json
│
├── 02.silver.validated/
│
├── normalize_data.py
├── load_to_db.py
├── db.py
│
├── docker-compose.yml
├── Data_View_ETL.ipynb
└── README.md


##  Fluxo do Pipeline ETL

### 1️ Camada Bronze – Dados Brutos
- Dados armazenados sem tratamento
- Formatos suportados:
  - CSV
  - JSON (padrão e line-delimited)
- Nenhuma modificação estrutural é feita nesta camada

---

### 2️ Camada Silver – Dados Tratados
O script `normalize_data.py` executa as seguintes etapas:

- Leitura dos arquivos da camada Bronze
- Conversão de colunas do tipo `list` para `string`
- Remoção de registros duplicados
- Padronização do formato de saída
- Persistência dos dados em **Parquet**

Essa etapa garante dados **consistentes, deduplicados e prontos para consumo analítico**.

---

### 3️ Persistência em Banco de Dados (PostgreSQL)
Os arquivos Parquet da camada Silver são carregados no PostgreSQL utilizando:

- Docker + docker-compose
- Classe `Database` para:
  - Criar tabelas dinamicamente a partir dos DataFrames
  - Inserir dados no banco
  - Executar consultas SQL

Cada arquivo Parquet gera automaticamente uma tabela no banco.

---

##  Banco de Dados (Docker)

O PostgreSQL é executado via Docker com a seguinte configuração:

- **Usuário:** postgres  
- **Senha:** postgres  
- **Banco:** postgres  
- **Porta:** 5432  

O volume é persistente, garantindo que os dados não sejam perdidos ao reiniciar o container.

Para subir o banco de dados:

```bash
docker-compose up -d

Análise Exploratória de Dados

O notebook Data_View_ETL.ipynb realiza:

Visualização inicial dos dados de usuários

Estatísticas descritivas

Cálculo de idade a partir da data de nascimento

Distribuição de idades e gênero

Análise de criptomoedas por market cap

Gráficos simples para validação dos dados

Essa etapa valida a qualidade dos dados após o ETL e demonstra preparo para análises posteriores.

Tecnologias Utilizadas

Python

Pandas

PostgreSQL

Docker / Docker Compose

Parquet

Matplotlib

Jupyter Notebook

Como Executar o Projeto

1️ Subir o banco de dados:

docker-compose up -d


2️ Executar o pipeline de normalização:

python normalize_data.py


3️ Carregar os dados no PostgreSQL:

python load_to_db.py


4️ Abrir o notebook para análise exploratória:

jupyter notebook Data_View_ETL.ipynb

Objetivo do Projeto

Este projeto foi desenvolvido com foco em portfólio, demonstrando:

Organização de dados em camadas (Lakehouse)

Tratamento de dados semi-estruturados

Criação de pipelines ETL reutilizáveis

Persistência em banco relacional

Validação e análise exploratória dos dados
