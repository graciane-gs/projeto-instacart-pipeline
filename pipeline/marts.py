import duckdb

def criar_marts():
    db_path = "data/instacart.duckdb"
    conn = duckdb.connect(db_path)
    
    print("Iniciando a criação da Camada Marts (Gold)...")
    
    # Mart 1: Top Produtos (Total de pedidos e recompras por produto)
    query_top_products = """
    CREATE OR REPLACE TABLE mart_top_products AS 
    SELECT 
        product_name,
        department,
        COUNT(order_id) AS total_orders,
        SUM(CAST(reordered AS INT)) AS total_reorders
    FROM refined_order_details
    GROUP BY product_name, department
    ORDER BY total_orders DESC
    """
    conn.execute(query_top_products)
    
    # Mart 2: Pedidos por Dia da Semana
    query_dow = """
    CREATE OR REPLACE TABLE mart_orders_by_dow AS 
    SELECT 
        day_of_week,
        COUNT(DISTINCT order_id) AS total_orders
    FROM refined_order_details
    GROUP BY day_of_week
    ORDER BY day_of_week
    """
    conn.execute(query_dow)
    
    print("Marts criadas com sucesso: 'mart_top_products' e 'mart_orders_by_dow'!")
    
    # Lista todas as tabelas para visualizarmos a evolução do banco
    tabelas = conn.execute("SHOW TABLES").fetchall()
    print(f"Tabelas finais no banco: {tabelas}")
    
    conn.close()

if __name__ == "__main__":
    criar_marts()