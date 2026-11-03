import duckdb
import os

def ingestar_dados():
    os.makedirs("data", exist_ok=True)
    
    db_path = "data/instacart.duckdb"
    conn = duckdb.connect(db_path)
    
    print("Iniciando a ingestão para a Camada Raw (Bronze)...")
    
    # Agora sim, lendo os CSVs e criando as tabelas!
    conn.execute("CREATE OR REPLACE TABLE raw_departments AS SELECT * FROM read_csv_auto('data/departments.csv')")
    conn.execute("CREATE OR REPLACE TABLE raw_products AS SELECT * FROM read_csv_auto('data/products.csv')")
    conn.execute("CREATE OR REPLACE TABLE raw_orders AS SELECT * FROM read_csv_auto('data/orders.csv')")
    conn.execute("CREATE OR REPLACE TABLE raw_order_products AS SELECT * FROM read_csv_auto('data/order_products.csv')")
    
    print("Ingestão concluída com sucesso! Tabelas Raw criadas.")
    
    tabelas = conn.execute("SHOW TABLES").fetchall()
    print(f"Tabelas no banco: {tabelas}")
    
    conn.close()

if __name__ == "__main__":
    ingestar_dados()