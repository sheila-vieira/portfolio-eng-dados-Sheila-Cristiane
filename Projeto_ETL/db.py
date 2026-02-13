import psycopg2


class Database:
    """
    Classe responsável por gerenciar a conexão com o banco de dados PostgreSQL
    e executar operações básicas como criação de tabelas, inserção e consultas.
    """

    def __init__(self, db_name, user, password, host='localhost', port=5432):
        """
        Inicializa a conexão com o banco de dados.

        Parâmetros:
        db_name (str): Nome do banco de dados
        user (str): Usuário do banco
        password (str): Senha do banco
        host (str): Endereço do servidor (default: localhost)
        port (int): Porta de conexão (default: 5432)
        """
        self.connection = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )

        # Cria um cursor para execução de comandos SQL
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, df):
        """
        Cria uma tabela no banco de dados com base nas colunas de um DataFrame.
        Todas as colunas são criadas como tipo TEXT.

        Parâmetros:
        table_name (str): Nome da tabela a ser criada
        df (DataFrame): DataFrame que define a estrutura da tabela
        """
        cursor = self.connection.cursor()

        # Monta a definição das colunas no formato SQL
        columns = ", ".join([f"{col} TEXT" for col in df.columns])

        # Cria a tabela caso ela ainda não exista
        cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        )

        self.connection.commit()
        cursor.close()

    def insert_data(self, table_name, df):
        """
        Insere os dados de um DataFrame em uma tabela do banco.

        Parâmetros:
        table_name (str): Nome da tabela
        df (DataFrame): DataFrame com os dados a serem inseridos
        """
        cursor = self.connection.cursor()

        # Itera linha a linha do DataFrame
        for _, row in df.iterrows():
            # Cria placeholders (%s) de acordo com o número de colunas
            placeholders = ", ".join(["%s"] * len(row))

            # Executa o comando de inserção
            cursor.execute(
                f"INSERT INTO {table_name} VALUES ({placeholders})",
                tuple(row)
            )

        self.connection.commit()
        cursor.close()

    def execute_query(self, query):
        """
        Executa uma query SQL genérica e retorna os resultados.

        Parâmetros:
        query (str): Query SQL a ser executada

        Retorna:
        list: Resultado da consulta
        """
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def select_all_data_from_table(self, table_name, limit=10):
        """
        Retorna registros de uma tabela com limite de linhas.

        Parâmetros:
        table_name (str): Nome da tabela
        limit (int): Quantidade máxima de registros (default: 10)

        Retorna:
        list: Registros retornados da tabela
        """
        cursor = self.connection.cursor()
        cursor.execute(
            f"SELECT * FROM {table_name} LIMIT {limit}"
        )
        results = cursor.fetchall()
        cursor.close()
        return results

    def close(self):
        """
        Fecha o cursor e a conexão com o banco de dados.
        Deve ser chamado ao final do uso da classe.
        """
        self.cursor.close()
        self.connection.close()
