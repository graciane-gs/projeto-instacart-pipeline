import pytest
import duckdb
import pandas as pd

@pytest.fixture
def db_conn():
    """Cria uma conexão DuckDB em memória para testes isolados."""
    conn = duckdb.connect(':memory:')
    yield conn
    conn.close()

def test_refined_layer_transformation(db_conn):
    """Testa a lógica de transformação e limpeza da Camada Refined (Silver)."""
    # 1. Simula dados brutos (raw)
    db_conn.execute("CREATE TABLE raw_orders AS SELECT 1 AS order_id, 3 AS order_dow, 10 AS order_hour_of_day, 0 AS reordered")
    db_conn.execute("CREATE TABLE raw_products AS SELECT 101 AS product_id, 'Organic Milk' AS product_name, 4 AS department_id")
    
    # 2. Executa a lógica de transformação Silver
    db_conn.execute("""
        CREATE TABLE refined_orders AS 
        SELECT order_id, order_dow, order_hour_of_day, reordered 
        FROM raw_orders 
        WHERE order_id IS NOT NULL
    """)
    
    # 3. Valida se a tabela Silver foi criada corretamente
    result = db_conn.execute("SELECT COUNT(*) FROM refined_orders").fetchone()[0]
    assert result == 1, "A tabela refined_orders deveria conter 1 registo."

def test_gold_marts_aggregation(db_conn):
    """Testa a agregação de negócio da Camada Marts (Gold) para os top produtos."""
    # 1. Simula a tabela refined cruzada de pedidos e produtos
    db_conn.execute("""
        CREATE TABLE refined_orders_products AS 
        SELECT 1 AS order_id, 101 AS product_id, 'Organic Milk' AS product_name, 1 AS reordered
        UNION ALL
        SELECT 2 AS order_id, 101 AS product_id, 'Organic Milk' AS product_name, 0 AS reordered
        UNION ALL
        SELECT 3 AS order_id, 102 AS product_id, 'Banana' AS product_name, 1 AS reordered
    """)
    
    # 2. Executa a agregação de negócio (Camada Gold - mart_top_products)
    db_conn.execute("""
        CREATE TABLE mart_top_products AS 
        SELECT 
            product_id,
            product_name,
            COUNT(order_id) AS total_orders,
            SUM(reordered) AS total_reorders
        FROM refined_orders_products
        GROUP BY product_id, product_name
        ORDER BY total_orders DESC
    """)
    
    # 3. Valida se os indicadores do produto 'Organic Milk' estão corretos
    top_product = db_conn.execute("SELECT total_orders, total_reorders FROM mart_top_products WHERE product_id = 101").fetchone()
    
    assert top_product[0] == 2, "O produto Organic Milk deveria ter 2 pedidos no total."
    assert top_product[1] == 1, "O produto Organic Milk deveria ter 1 recompra."