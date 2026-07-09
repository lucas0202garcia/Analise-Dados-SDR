# 📊 Análise e Tratamento de Dados - Operação de SDR

## 🎯 Objetivo do Projeto
Este projeto foi desenvolvido para resolver um problema real de operações comerciais: bases de leads descentralizadas, sujas e sem inteligência de métricas. O script atua na limpeza dos dados brutos e calcula automaticamente os principais KPIs de vendas.

## 🛠️ Tecnologias Utilizadas
* **Python** (Linguagem principal)
* **Pandas** (Limpeza, manipulação e agregação de dados)
* **Power BI** (Em desenvolvimento - para visualização do Dashboard)

## 🧹 Etapas de Tratamento de Dados (Data Cleaning)
1. Remoção de leads duplicados oriundos do CRM.
2. Tratamento de valores nulos (NaN) nas origens de tráfego.
3. Conversão e tipagem de dados temporais (DateTime).

## 🧮 Inteligência de Negócio (Métricas Calculadas)
O script gera um relatório estratégico contendo:
* **Taxa de Conversão Geral** do funil.
* **CAC (Custo de Aquisição de Cliente)** por venda.
* **LTV (Ticket Médio)** dos clientes convertidos.
* **Taxa de No-show** em agendamentos comerciais.

## 🚀 Como executar este projeto
1. Clone este repositório.
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente e instale as dependências: `pip install pandas`
4. Execute o script principal: `python analise_sdr.py`

---
*Desenvolvido focado na transição de dados e automação de processos comerciais.*