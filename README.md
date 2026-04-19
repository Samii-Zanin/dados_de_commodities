# Pipeline ETL de Cotações de Commodities

## 📌 Visão Geral

Este projeto implementa um **pipeline ETL (Extract, Transform, Load)** desenvolvido em Python para coletar, tratar e armazenar automaticamente cotações de commodities agrícolas disponíveis publicamente na web.

A aplicação foi criada para resolver uma necessidade real de dados atualizados em um projeto acadêmico, onde o consumo via API seria a solução ideal, porém as APIs disponíveis eram pagas. Como alternativa, foi desenvolvido um processo automatizado de **web scraping**, permitindo a ingestão periódica de dados de forma estruturada e confiável.

O sistema executa as seguintes etapas:

- Extração automática de dados de um site público
- Tratamento e padronização das informações coletadas
- Armazenamento dos dados em um banco relacional
- Execução automatizada em horários definidos

Este projeto demonstra, na prática, conceitos fundamentais de **Engenharia de Dados**, incluindo automação, pipelines de dados, integração com banco de dados e organização modular de código.

---

## 🏗️ Arquitetura do Pipeline

O pipeline segue a arquitetura clássica de Engenharia de Dados:

**Extract → Transform → Load**

### Extract (Extração)

Responsável por coletar os dados diretamente da fonte web utilizando Selenium.

Principais responsabilidades:

- Acessar página com conteúdo dinâmico
- Localizar elementos da tabela de commodities
- Extrair dados brutos
- Garantir sincronização com carregamento da página

Tecnologias utilizadas:

- Selenium
- WebDriver
- WebDriverWait

---

### Transform (Transformação)

Responsável por limpar, padronizar e estruturar os dados extraídos.

Principais transformações realizadas:

- Conversão de valores monetários (ex: R$ 1.357,77 → 1357.77)
- Extração de produto, estado (UF) e praça
- Conversão de variação percentual
- Padronização de datas
- Estruturação em formato tabular
- Normalização de dados

Tecnologias utilizadas:

- Pandas
- Regex (expressões regulares)
- Manipulação de strings

---

### Load (Carga)

Responsável por persistir os dados tratados em um banco de dados relacional.

Principais responsabilidades:

- Conexão segura com banco de dados
- Inserção de dados em tabela
- Suporte a diferentes estratégias de inserção
- Encerramento seguro da conexão

Tecnologias utilizadas:

- SQLAlchemy
- MySQL

---

## ⏱️ Automação da Execução

O pipeline possui uma rotina de execução automatizada que funciona como uma **DAG simplificada**, responsável por executar o processo ETL em horários definidos.

Características:

- Execução contínua
- Verificação de horário em tempo real
- Execução automática do pipeline
- Evita múltiplas execuções simultâneas

Essa abordagem simula o comportamento de ferramentas de orquestração utilizadas em ambientes produtivos, como:

- Apache Airflow
- Cron Jobs
- Orquestradores de workflows

---

## 🧩 Estrutura do Projeto

```
project/
│
├── config/
│   └── connection.py
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── etl.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## 🧠 Tecnologias Utilizadas

- Python
- Selenium
- Pandas
- SQLAlchemy
- MySQL
- Regex
- Dotenv

---

## 🔐 Variáveis de Ambiente

O projeto utiliza um arquivo `.env` para configuração segura do banco de dados.

Exemplo:

```
DB_USER=usuario
DB_PASSWORD=senha
DB_HOST=localhost
DB_PORT=3306
DB_NAME=nome_do_banco
DB_TABLE=nome_da_tabela
```

---

## ▶️ Como Executar o Projeto

### 1) Clonar o repositório

```
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2) Acessar o diretório

```
cd seu-repositorio
```

### 3) Criar ambiente virtual

```
python -m venv venv
```

### 4) Ativar ambiente virtual

Windows:

```
venv\Scripts\activate
```

Linux / Mac:

```
source venv/bin/activate
```

### 5) Instalar dependências

```
pip install -r requirements.txt
```

### 6) Configurar variáveis de ambiente

Criar arquivo `.env` na raiz do projeto.

---

### 7) Executar o pipeline

```
python src/etl.py
```

---

## 📊 Fluxo do Pipeline

1) Sistema inicia execução
2) Verifica horário programado
3) Coleta dados do site
4) Trata e padroniza dados
5) Insere dados no banco
6) Aguarda próxima execução

---

## 🎯 Objetivos do Projeto

Este projeto foi desenvolvido com os seguintes objetivos:

- Aplicar conceitos reais de Engenharia de Dados
- Automatizar ingestão de dados
- Estruturar pipeline ETL
- Trabalhar com dados públicos
- Demonstrar integração entre sistemas
- Desenvolver solução sob restrições técnicas e de custo

---

## 🚀 Possíveis Evoluções do Projeto

Melhorias técnicas que podem ser implementadas:

- Logging estruturado
- Tratamento robusto de exceções
- Controle de integridade de dados
- Criação de chave primária
- Containerização com Docker
- Orquestração com Airflow
- Monitoramento do pipeline
- Armazenamento incremental
- Testes automatizados
- Validação de qualidade de dados

---

## 👨‍💻 Autor

Projeto desenvolvido como aplicação prática de conceitos de **Engenharia de Dados**, com foco em automação, organização de pipelines e integração de dados.

