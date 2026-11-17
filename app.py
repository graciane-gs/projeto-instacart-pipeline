import streamlit as st
import duckdb
import os

db_path = "data/instacart.duckdb"

# Função para garantir que o banco e as tabelas Gold existam
def garantir_banco_criado():
    os.makedirs("data", exist_ok=True)
    
    # Conecta ao DuckDB (cria o arquivo se não existir)
    conn = duckdb.connect(db_path)
    
    # Verifica se as tabelas marts já existem
    tables = [t[0] for t in conn.execute("SHOW TABLES").fetchall()]
    
    if "mart_top_products" not in tables:
        st.info("🔄 Gerando dados e executando o pipeline pela primeira vez...")
        
        # Se você tiver os scripts de população e pipeline, executa-os de forma segura:
        try:
            import popular_dados
            # Se popular_dados tiver uma função principal, chame-a aqui, senão o os.system funciona:
        except Exception:
            pass
            
        # Execução robusta via subprocess/os para garantir criação correta
        os.system("python popular_dados.py")
        os.system("python pipeline/ingestao.py")
        os.system("python pipeline/transformacao.py")
        os.system("python pipeline/marts.py")
        
        st.success("✅ Pipeline executado com sucesso!")
    
    conn.close()

# Garante que o banco está pronto antes de conectar para o dashboard
garantir_banco_criado()

# Conexão principal para o dashboard
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