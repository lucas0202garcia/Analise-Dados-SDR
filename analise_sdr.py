import pandas as pd

# 1. Carregar os dados
df = pd.read_csv('leads_sdr_bruto.csv')

print("--- ANÁLISE INICIAL ---")
print(f"Total de linhas brutas: {len(df)}")
print(f"Valores nulos por coluna:\n{df.isnull().sum()}")

# 2. LIMPEZA DE DUPLICADOS
# Mostra que você se preocupa com a integridade do dado
df = df.drop_duplicates()

# 3. TRATAMENTO DE NULOS
# Leads sem origem vamos batizar de 'Desconhecido' para não perder o dado
df['origem'] = df['origem'].fillna('Desconhecido')

# 4. AJUSTE DE TIPOS
# Transformar a coluna de data em algo que o Python entenda como tempo
df['data_contato'] = pd.to_datetime(df['data_contato'])

print("\n--- APÓS LIMPEZA ---")
print(f"Total de linhas limpas: {len(df)}")
print(f"Nulos restantes: {df['origem'].isnull().sum()}")

# Salva o arquivo limpo para usarmos no Dashboard depois
df.to_csv('leads_sdr_limpo.csv', index=False)
print("\n✅ Arquivo 'leads_sdr_limpo.csv' gerado com sucesso!") 
# --- CÁLCULO DE MÉTRICAS (VISÃO ESTRATÉGICA) ---

# A. Total de Leads e Total de Vendas
total_leads = len(df)
total_vendas = len(df[df['status'] == 'Vendido'])

# B. Taxa de Conversão Geral (%)
taxa_conversao = (total_vendas / total_leads) * 100

# C. CAC (Custo de Aquisição de Cliente)
custo_total_marketing = df['custo_lead'].sum()
cac = custo_total_marketing / total_vendas if total_vendas > 0 else 0

# D. LTV Simples (Ticket Médio de Venda)
ltv = df[df['status'] == 'Vendido']['valor_venda'].mean()

# E. Taxa de No-show (%)
agendados = len(df[df['status'] == 'Agendado'])
no_shows = len(df[df['status'] == 'No-show'])
total_compromissos = agendados + no_shows
taxa_no_show = (no_shows / total_compromissos) * 100 if total_compromissos > 0 else 0

# --- MOSTRANDO OS RESULTADOS NO TERMINAL ---

print("\n" + "="*40)
print("📊 RELATÓRIO ESTRATÉGICO DE PERFORMANCE")
print("="*40)
print(f"Total de Leads Analisados: {total_leads}")
print(f"Total de Vendas Realizadas: {total_vendas}")
print(f"Taxa de Conversão Geral: {taxa_conversao:.2f}%")
print(f"CAC (Custo de Aquisição): R$ {cac:.2f}")
print(f"Ticket Médio (LTV): R$ {ltv:.2f}")
print(f"Taxa de No-show de Agendamentos: {taxa_no_show:.2f}%")
print("="*40)

# Salvando um agrupamento por origem para alimentar o Dashboard visual depois
resumo_origem = df.groupby('origem').agg({
    'status': 'count',
    'valor_venda': 'sum',
    'custo_lead': 'sum'
}).rename(columns={'status': 'qtd_leads', 'valor_venda': 'faturamento'})

resumo_origem.to_csv('resumo_performance.csv')
print("\n✅ Arquivo 'resumo_performance.csv' gerado para o Dashboard!")