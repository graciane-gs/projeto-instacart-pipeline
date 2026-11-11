# 🛒 Pipeline de Dados Instacart (End-to-End)

<div align="justify">
Este repositório contém o projeto final prático de Engenharia de Dados, focado na construção de um pipeline <em>end-to-end</em> do zero. O objetivo é extrair dados de arquivos CSV, processá-los utilizando a <strong>Arquitetura Medalhão</strong> (Raw, Refined, Marts) e disponibilizar os indicadores de negócio em um <strong>Dashboard Interativo</strong>.
</div>

🚀 **Dashboard Interativo em Produção:** [Acessar Instacart Pipeline](https://instacart-pipeline.streamlit.app/)

## 🛠️ Tecnologias Utilizadas

**Linguagem:** Python
**Banco de Dados Analítico (OLAP):** DuckDB
**Visualização / Frontend:** Streamlit
**Testes Unitários:** Pytest
**Versionamento:** Git e GitHub

## 🏗️ Arquitetura do Projeto (Medalhão)

<div align="justify">
O pipeline processa os dados em três camadas distintas para garantir a qualidade e a organização:
</div>

**Camada Raw (Bronze):** Ingestão dos dados brutos (CSVs) para o DuckDB sem qualquer alteração, mantendo a fidelidade da fonte original.
**Camada Refined (Silver):** Limpeza, padronização e cruzamento (JOINs) das tabelas de pedidos, produtos e departamentos.
**Camada Marts (Gold):** Tabelas agregadas com indicadores de negócio (ex: top produtos mais vendidos, tendência de pedidos por dia da semana) prontas para consumo por ferramentas de BI ou Dashboards.

## 📂 Estrutura do Repositório

`data/`: Diretório destinado aos arquivos CSV originais (mock data) e ao arquivo do banco de dados `instacart.duckdb`.
`pipeline/`: Scripts de processamento de dados (`ingestao.py`, `transformacao.py`, `marts.py`).
`tests/`: Testes unitários do projeto (`test_transformacao.py`).
`app.py`: Aplicação web com o dashboard interativo em Streamlit.
`popular_dados.py`: Script utilitário para popular o banco de dados DuckDB com dados de teste.
`requirements.txt`: Lista de dependências do projeto.

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

O dashboard abrirá automaticamente no seu navegador padrão.

## 🎯 Perguntas de Negócio Respondidas pelo App

<div align="justify">
Este dashboard foi desenhado para responder rapidamente a questões logísticas e comerciais essenciais:
</div>

**Quais são os produtos favoritos dos clientes?** (Identificação dos itens com maior volume de pedidos e recompras).

**Em quais dias da semana o e-commerce tem pico de vendas?** (Análise de comportamento temporal para dimensionamento de estoque e servidores).

**Quais são os horários de maior fluxo de pedidos ao longo do dia?** (Identificação de janelas críticas de pico operacional).

## 🔍 Granularidade dos Dados (Grãos)

<div align="justify">
A modelagem nas camadas do pipeline seguiu rigorosamente a definição do grão analítico para evitar duplicações e garantir performance no DuckDB:
</div>

**`mart_top_products` (Camada Gold):** O grão é de 1 linha por Produto (`product_id` / `product_name`), agregando o total de pedidos e recompras daquele item.

**`mart_orders_by_dow` (Camada Gold):** O grão é de 1 linha por Dia da Semana, consolidando o volume global de pedidos para cada dia.

**`mart_orders_by_hour` (Camada Gold):** O grão é de 1 linha por Hora do Dia (0 a 23h), mapeando a distribuição horária da demanda.


## 🧪 Testes Unitários

<div align="justify">
O projeto conta com testes de qualidade utilizando dados fictícios (mock data) armazenados em memória, garantindo que o banco de dados oficial não seja afetado.
</div>

Para executar os testes, rode na raiz do projeto:

```bash
pytest
```

## 📄 Licença

Distribuído sob a licença MIT. Veja o arquivo LICENSE para mais informações.

## 🤖 Onde a IA errou

<div align="justify">
Durante o desenvolvimento deste projeto, a Inteligência Artificial (Gemini) foi utilizada como suporte (pair programming), mas exigiu senso crítico e correções manuais ao longo do processo. Alguns exemplos incluem:
</div>

**Formatação e Markdown:** A IA inseriu tags HTML (`
<div align="justify">`) de forma muito abrangente no `README.md`, o que acabou quebrando a renderização visual das listas e dos blocos de código no GitHub. Foi necessário corrigir manualmente a posição das tags.

**Cache do Git vs .gitignore:** Embora a IA tenha sugerido criar o `.gitignore` para a pasta `.devcontainer` e para arquivos `.duckdb`, ela não alertou inicialmente que o arquivo `instacart.duckdb` já havia sido rastreado pelo Git. Isso exigiu uma intervenção posterior com `git rm --cached` para limpar o histórico do repositório remoto.

**Tamanho de Fontes:** Ao criar a seção de Autora, a IA sugeriu o uso de caracteres (`##` e `---`) que transformaram os links em títulos gigantes, exigindo revisão da sintaxe Markdown para voltar ao padrão normal.


## 👩🏽‍💻 Autora

**Graciane Santana**  
*Desafio Engenheiro de Dados Júnior*

🔗 **GitHub:** [@graciane-gs](https://github.com/graciane-gs)  
💼 **LinkedIn:** [Conecte-se comigo](https://www.linkedin.com/in/graciane-santana) 