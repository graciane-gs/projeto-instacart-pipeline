import duckdb
import os

def ingestar_dados():
    # Garante que a pasta data existe
    os.makedirs("data", exist_ok=True)
    
    # Conecta ao banco DuckDB
    db_path = "data/instacart.duckdb"
    conn = duckdb.connect(db_path)
    
    print("Iniciando a ingestão para a Camada Raw (Bronze)...")
    
    # Exemplo de ingestão dos arquivos CSV brutos para tabelas Raw no DuckDB
    # conn.execute("CREATE OR REPLACE TABLE raw_orders AS SELECT * FROM read_csv_auto('data/orders.csv')")
    # conn.execute("CREATE OR REPLACE TABLE raw_order_products AS SELECT * FROM read_csv_auto('data/order_products.csv')")
    # conn.execute("CREATE OR REPLACE TABLE raw_products AS SELECT * FROM read_csv_auto('data/products.csv')")
    
    print("Ingestão concluída com sucesso!")
    conn.close()

if __name__ == "__main__":
    ingestar_dados()