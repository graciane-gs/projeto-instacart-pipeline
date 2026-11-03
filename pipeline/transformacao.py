import duckdb

def refinar_dados():
    db_path = "data/instacart.duckdb"
    conn = duckdb.connect(db_path)
    
    print("Iniciando a transformação para a Camada Refined (Silver)...")
    
    # Cria a tabela refinada unindo pedidos, itens, produtos e departamentos
    query = """
    CREATE OR REPLACE TABLE refined_order_details AS 
    SELECT 
        o.order_id,
        o.user_id,
        o.order_number,
        o.order_dow AS day_of_week,
        o.order_hour_of_day,
        op.add_to_cart_order,
        op.reordered,
        p.product_name,
        d.department
    FROM raw_orders o
    JOIN raw_order_products op ON o.order_id = op.order_id
    JOIN raw_products p ON op.product_id = p.product_id
    JOIN raw_departments d ON p.department_id = d.department_id
    """
    conn.execute(query)
    
    print("Transformação concluída! Tabela 'refined_order_details' criada.")
    conn.close()

if __name__ == "__main__":
    refinar_dados()