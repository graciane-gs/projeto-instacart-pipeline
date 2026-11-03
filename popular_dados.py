import duckdb

# Conecta ao DuckDB na pasta data
conn = duckdb.connect("data/instacart.duckdb")

# 1. Top Produtos
conn.execute("""
    CREATE OR REPLACE TABLE mart_top_products AS 
    SELECT * FROM (VALUES 
        ('Banana', 'Produce', 15420, 12000),
        ('Organic Strawberries', 'Produce', 9820, 7500),
        ('Organic Baby Spinach', 'Produce', 8430, 6100),
        ('Milk', 'Dairy Eggs', 6120, 5000),
        ('Bag of Organic Bananas', 'Produce', 5310, 4100)
    ) AS t(product_name, department, total_orders, total_reorders)
""")

# 2. Pedidos por Dia da Semana
conn.execute("""
    CREATE OR REPLACE TABLE mart_orders_by_dow AS 
    SELECT * FROM (VALUES 
        ('Segunda-feira', 12400),
        ('Terça-feira', 14200),
        ('Quarta-feira', 13800),
        ('Quinta-feira', 12900),
        ('Sexta-feira', 15600),
        ('Sábado', 18900),
        ('Domingo', 17200)
    ) AS t(day_of_week, total_orders)
""")

# 3. NOVO: Pedidos por Hora do Dia (Horas de Pico)
conn.execute("""
    CREATE OR REPLACE TABLE mart_orders_by_hour AS 
    SELECT * FROM (VALUES 
        (8, 2100),
        (9, 4500),
        (10, 6800),
        (11, 8200),
        (12, 9500),
        (13, 8900),
        (14, 7600),
        (15, 7100),
        (16, 7800),
        (17, 9200),
        (18, 11200),
        (19, 9800),
        (20, 6400)
    ) AS t(order_hour_of_day, total_orders)
""")

conn.close()
print("Dados populados com sucesso, incluindo horas de pico!")