import streamlit as st
import duckdb
import os

db_path = "data/instacart.duckdb"

# Função para garantir que o banco e todas as tabelas marts essenciais existem
def verificar_e_executar_pipeline():
    os.makedirs("data", exist_ok=True)
    precisa_executar = False
    
    if not os.path.exists(db_path):
        precisa_executar = True
    else:
        try:
            # Testa se as tabelas marts já foram criadas no banco existente
            conn_check = duckdb.connect(db_path, read_only=True)
            tables = [t[0] for t in conn_check.execute("SHOW TABLES").fetchall()]
            conn_check.close()
            
            # Se faltar alguma tabela nova, força a reexecução do pipeline
            if "mart_top_products" not in tables or "mart_orders_by_hour" not in tables or "mart_top_departments" not in tables:
                precisa_executar = True
        except Exception:
            precisa_executar = True
            
    if precisa_executar:
        st.info("🔄 Atualizando o banco de dados e executando o pipeline completo...")
        if os.path.exists("popular_dados.py"):
            os.system("python popular_dados.py")
        os.system("python pipeline/ingestao.py")
        os.system("python pipeline/transformacao.py")
        os.system("python pipeline/marts.py")
        st.success("✅ Pipeline atualizado com sucesso!")

# Executa a verificação
verificar_e_executar_pipeline()

# Conecta ao banco DuckDB
conn = duckdb.connect(db_path)

# Configuração inicial da página
st.set_page_config(page_title="Dashboard Instacart", page_icon="🛒", layout="wide")

st.title("🛒 Dashboard Analítico - Instacart")
st.markdown("Este dashboard consome os dados diretamente da **Camada Gold (Marts)** do nosso pipeline de Engenharia de Dados.")

st.divider()

# Cria duas colunas para os primeiros gráficos lado a lado
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Top Produtos mais Vendidos")
    df_top = conn.execute("SELECT product_name, total_orders FROM mart_top_products LIMIT 10").df()
    st.bar_chart(df_top, x="product_name", y="total_orders")

with col2:
    st.subheader("📅 Tendência de Pedidos por Dia da Semana")
    df_dow = conn.execute("SELECT day_of_week, total_orders FROM mart_orders_by_dow").df()
    st.line_chart(df_dow, x="day_of_week", y="total_orders")

st.divider()

# Seção de Horas de Pico
st.subheader("⏰ Horas de Pico de Pedidos (ao longo do dia)")
df_hour = conn.execute("SELECT order_hour_of_day, total_orders FROM mart_orders_by_hour ORDER BY order_hour_of_day").df()
st.area_chart(df_hour, x="order_hour_of_day", y="total_orders")

st.divider()

# Gráfico de Departamentos
st.subheader("🛒 Departamentos com Maior Volume de Vendas")
df_dept = conn.execute("SELECT department, total_orders FROM mart_top_departments ORDER BY total_orders DESC").df()
st.bar_chart(df_dept, x="department", y="total_orders")

st.divider()

st.subheader("📊 Tabela Detalhada: Produtos e Recompras")
df_detalhado = conn.execute("SELECT * FROM mart_top_products").df()
st.dataframe(df_detalhado, use_container_width=True)

conn.close()