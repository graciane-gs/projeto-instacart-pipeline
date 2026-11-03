import duckdb

def test_transformacao_camada_refined():
    # 1. Cria uma base de dados temporária em memória (não afeta o projeto real)
    conn = duckdb.connect(':memory:')
    
    # 2. Cria dados inventados (Mock Data) para as tabelas raw
    conn.execute("""
        CREATE TABLE raw_orders AS 
        SELECT 1 AS order_id, 100 AS user_id, 1 AS order_number, 2 AS order_dow, 8 AS order_hour_of_day;
        
        CREATE TABLE raw_order_products AS 
        SELECT 1 AS order_id, 10 AS product_id, 1 AS add_to_cart_order, 0 AS reordered;
        
        CREATE TABLE raw_products AS 
        SELECT 10 AS product_id, 'Biscoito de Chocolate' AS product_name, 1 AS department_id;
        
        CREATE TABLE raw_departments AS 
        SELECT 1 AS department_id, 'Doces' AS department;
    """)
    
    # 3. Executa a mesma lógica de transformação que temos no pipeline
    query = """
    CREATE TABLE refined_order_details AS 
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
    
    # 4. Vai buscar o resultado para verificarmos se a lógica funcionou
    resultado = conn.execute("SELECT * FROM refined_order_details").df()
    
    # 5. Validação (Asserts) - Testa se os dados cruzaram corretamente
    assert len(resultado) == 1, "A tabela final deveria ter exatamente 1 linha"
    assert resultado['product_name'][0] == 'Biscoito de Chocolate', "O nome do produto não cruzou corretamente"
    assert resultado['department'][0] == 'Doces', "O departamento não cruzou corretamente"
    
    conn.close()