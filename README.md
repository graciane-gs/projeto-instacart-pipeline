# 🛒 Pipeline de Dados Instacart (End-to-End)

Este repositório contém o projeto final prático de Engenharia de Dados, focado na construção de um pipeline *end-to-end* do zero. O objetivo é extrair dados de ficheiros CSV, processá-los utilizando a **Arquitetura Medalhão** (Raw, Refined, Marts) e disponibilizar os indicadores de negócio num **Dashboard Interativo**.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python
- **Base de Dados Analítica (OLAP):** DuckDB
- **Visualização / Frontend:** Streamlit
- **Testes Unitários:** Pytest
- **Versionamento:** Git e GitHub

## 🏗️ Arquitetura do Projeto (Medalhão)
O pipeline processa os dados em três camadas distintas para garantir a qualidade e a organização:
1. **Camada Raw (Bronze):** Ingestão dos dados brutos (CSVs) para o DuckDB sem qualquer alteração, mantendo a fidelidade da fonte original.
2. **Camada Refined (Silver):** Limpeza, padronização e cruzamento (JOINs) das tabelas de pedidos, produtos e departamentos.
3. **Camada Marts (Gold):** Tabelas agregadas com indicadores de negócio (ex: top produtos mais vendidos, tendência de pedidos por dia da semana) prontas para consumo por ferramentas de BI ou Dashboards.

## 📂 Estrutura do Repositório
- `data/`: Diretório destinado aos ficheiros CSV originais (mock data) e ao ficheiro da base de dados `instacart.duckdb`.
- `pipeline/`: Scripts de processamento de dados (`ingestao.py`, `transformacao.py`, `marts.py`).
- `tests/`: Testes unitários do projeto (`test_transformacao.py`).
- `app.py`: Aplicação web com o dashboard interativo em Streamlit.
- `popular_dados.py`: Script utilitário para popular a base de dados DuckDB com dados de teste.
- `requirements.txt`: Lista de dependências do projeto.

## 🚀 Como Executar o Projeto Localmente

**1. Instalar as dependências:**
```bash
pip install -r requirements.txt
```
**2. Executar o Pipeline de Dados (na ordem):**
```bash
python pipeline/ingestao.py       # Cria a camada Raw
python pipeline/transformacao.py  # Cria a camada Refined
python pipeline/marts.py          # Cria a camada Marts
```
**3. Iniciar o Dashboard Interativo:**
```bash
streamlit run app.py
```
O painel abrirá automaticamente no seu navegador padrão.

## 🧪 Testes Unitários
O projeto conta com testes de qualidade utilizando dados fictícios (mock data) guardados em memória, garantindo que a base de dados oficial não é afetada.
Para correr os testes, execute na raiz do projeto:
```bash
pytest
```
## 📄 Licença
Distribuído sob a licença MIT. Veja o ficheiro LICENSE para mais informações.