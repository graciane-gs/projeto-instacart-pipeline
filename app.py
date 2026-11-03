import streamlit as st
import duckdb

# Conecta ao banco DuckDB (somente leitura para maior segurança no frontend)
db_path = "data/instacart.duckdb"
conn = duckdb.connect(db_path, read_only=True)

# Configuração inicial da página
st.set_page_config(page_title="Dashboard Instacart", page_icon="🛒", layout="wide")

st.title("🛒 Dashboard Analítico - Instacart")
st.markdown("Este dashboard consome os dados diretamente da **Camada Gold (Marts)** do nosso pipeline de Engenharia de Dados.")

st.divider()

# Cria duas colunas para colocar os gráficos lado a lado
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Top Produtos mais Vendidos")
    # Traz os top 10 produtos do banco e transforma em DataFrame do Pandas (.df())
    df_top = conn.execute("SELECT product_name, total_orders FROM mart_top_products LIMIT 10").df()
    st.bar_chart(df_top, x="product_name", y="total_orders")

with col2:
    st.subheader("📅 Tendência de Pedidos por Dia da Semana")
    # Traz a tabela de dias da semana
    df_dow = conn.execute("SELECT day_of_week, total_orders FROM mart_orders_by_dow").df()
    st.line_chart(df_dow, x="day_of_week", y="total_orders")

st.divider()

st.subheader("📊 Tabela Detalhada: Produtos e Recompras")
# Traz a tabela inteira do Top Produtos para exibição tabular
df_detalhado = conn.execute("SELECT * FROM mart_top_products").df()
st.dataframe(df_detalhado, use_container_width=True)

conn.close()