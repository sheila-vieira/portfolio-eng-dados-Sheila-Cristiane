# =========================================================
# Consulta de CEP via API ViaCEP
# =========================================================

# Importando bibliotecas necessárias
import requests  # Para fazer requisições HTTP à API
import pandas as pd  # Para manipulação de dados em tabelas (DataFrames)

# =========================================================
# Função para buscar informações de um CEP na API ViaCEP
# =========================================================
def get_data(cep):
    """
    Consulta o CEP na API ViaCEP e retorna os dados em formato JSON.
    
    Parâmetros:
    cep (str): CEP a ser consultado (somente números, sem traço)
    
    Retorna:
    dict: Dados do CEP se a consulta for bem-sucedida, None caso contrário.
    """
    endpoint = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        response = requests.get(endpoint, timeout=10)  # Timeout de 10 segundos

        if response.status_code == 200:  # 200 indica sucesso na requisição
            return response.json()
        else:  # Caso o status code não seja 200, retorna None e informa o erro
            print(f"Erro ao buscar CEP {cep}: {response.status_code}")
            return None

    # Tratamento de exceções de conexão e requisição
    except requests.exceptions.ConnectionError as e:
        print(f"Erro de conexão para CEP {cep}: {e}")
        return None
    except requests.exceptions.Timeout as e:
        print(f"Timeout para CEP {cep}: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição para CEP {cep}: {e}")
        return None

# =========================================================
# Leitura da lista de usuários e seus CEPs
# =========================================================
users_path = "01.bronze.raw/users.csv"  # Caminho do arquivo CSV com os usuários
users_df = pd.read_csv(users_path)  # Lê o arquivo CSV para um DataFrame

print(users_df["cep"])  # Mostra os CEPs presentes na coluna 'cep'

# Converte a coluna 'cep' para uma lista de strings
cep_lists = users_df["cep"].tolist()

# =========================================================
# Consulta de CEPs na API e armazenamento dos resultados
# =========================================================
cep_info_list = []  # Lista que irá armazenar as informações retornadas pela API

for cep in cep_lists:
    cep_clean = cep.replace("-", "")  # Remove traços do CEP, se houver
    cep_info = get_data(cep_clean)  # Chama a função para consultar o CEP
    print(cep_info)  # Exibe os dados retornados no console

    # Caso a API retorne erro, ignora o CEP
    if cep_info is None or "erro" in cep_info:
        continue

    cep_info_list.append(cep_info)  # Adiciona os dados à lista

# =========================================================
# Criação de um DataFrame com os resultados e exportação
# =========================================================
cep_info_df = pd.DataFrame(cep_info_list)  # Converte a lista de dicionários em DataFrame

# Salva os dados em um arquivo CSV
cep_info_df.to_csv("01.bronze.raw/cep_info.csv", index=False)

print("Consulta finalizada! Dados salvos em 'cep_info.csv'.")


