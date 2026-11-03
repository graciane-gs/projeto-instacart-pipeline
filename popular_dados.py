import duckdb

# Conecta ao DuckDB na pasta data
conn = duckdb.connect("data/instacart.duckdb")

# Insere dados de teste na tabela de top produtos
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

# Insere dados de teste na tabela de dias da semana
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

conn.close()
print("Dados populados com sucesso!")