import os
import pandas as pd


class NormalizeData:
    """
    Classe responsável por normalizar arquivos da camada Bronze
    e salvá-los na camada Silver em formato Parquet.
    """

    def __init__(self, input_path, output_path):
        """
        Inicializa os caminhos de entrada e saída do pipeline.

        Parâmetros:
        input_path (str): Diretório onde estão os arquivos brutos (Bronze)
        output_path (str): Diretório onde os arquivos tratados serão salvos (Silver)
        """
        self.input_path = input_path
        self.output_path = output_path

        # Cria o diretório de saída caso ainda não exista
        os.makedirs(self.output_path, exist_ok=True)

    def convert_to_string(self, df):
        """
        Converte colunas do tipo list para string.

        Essa conversão é necessária porque o método drop_duplicates
        não funciona corretamente com colunas que possuem listas.
        """
        for col in df.columns:
            # Verifica se a coluna possui ao menos um valor do tipo list
            if df[col].apply(lambda x: isinstance(x, list)).any():
                # Converte listas para string, mantendo os demais valores
                df[col] = df[col].apply(
                    lambda x: str(x) if isinstance(x, list) else x
                )
        return df

    def load_df_from_file(self, file, ext):
        """
        Carrega um DataFrame a partir de um arquivo CSV ou JSON.

        Parâmetros:
        file (str): Nome do arquivo
        ext (str): Extensão do arquivo

        Retorna:
        pd.DataFrame ou None: DataFrame carregado ou None se o formato não for suportado
        """
        input_file = os.path.join(self.input_path, file)

        # Leitura de arquivos CSV
        if ext.lower() == ".csv":
            return pd.read_csv(input_file)

        # Leitura de arquivos JSON
        elif ext.lower() == ".json":
            try:
                # Tenta ler JSON no formato padrão
                return pd.read_json(input_file)
            except ValueError:
                # Caso seja JSON line-delimited (uma linha por registro)
                return pd.read_json(input_file, lines=True)

        # Caso o formato não seja suportado, retorna None
        else:
            return None

    def normalize_data(self):
        """
        Executa o processo completo de normalização dos dados:
        - percorre os arquivos do diretório Bronze
        - carrega os dados
        - trata colunas com listas
        - remove registros duplicados
        - salva os dados tratados em Parquet na camada Silver
        """
        for file in os.listdir(self.input_path):
            # Separa o nome do arquivo da extensão
            name, ext = os.path.splitext(file)

            # Carrega o DataFrame conforme o tipo do arquivo
            df = self.load_df_from_file(file, ext)

            # Ignora arquivos com formatos não suportados
            if df is None:
                print(f"Arquivo {file} ignorado (formato não suportado)")
                continue

            # Normaliza colunas que possuem listas
            df = self.convert_to_string(df)

            # Remove registros duplicados e reorganiza o índice
            df = df.drop_duplicates().reset_index(drop=True)

            # Define o caminho do arquivo de saída em formato Parquet
            output_file = os.path.join(self.output_path, f"{name}.parquet")

            # Salva o DataFrame tratado na camada Silver
            df.to_parquet(output_file, index=False)

            print(f"Processed and saved: {output_file}")


# =========================================================
# Execução do script
# =========================================================
if __name__ == "__main__":
    # Define os diretórios de entrada e saída
    input_path = "01.bronze.raw"
    output_path = "02.silver.validated"

    # Cria a instância da classe e executa a normalização
    normalizer = NormalizeData(input_path, output_path)
    normalizer.normalize_data()
