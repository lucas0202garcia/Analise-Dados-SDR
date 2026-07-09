import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configurações para que o seu resultado seja igual ao meu
np.random.seed(42) 
n_leads = 1000

# Gerando datas dos últimos 90 dias
data_inicial = datetime.now() - timedelta(days=90)
datas = [data_inicial + timedelta(days=np.random.randint(0, 90)) for _ in range(n_leads)]

# Origens de tráfego e Status que você conhece da sua rotina
origens = ['Meta Ads', 'Google Ads', 'Outbound', 'Indicação', 'LinkedIn']
status_lista = ['Lead', 'SQL', 'Agendado', 'Vendido', 'No-show']
probabilidades = [0.4, 0.2, 0.2, 0.1, 0.1] 

data = {
    'data_contato': datas,
    'origem': np.random.choice(origens, n_leads),
    'status': np.random.choice(status_lista, n_leads, p=probabilidades),
    'custo_lead': np.random.uniform(10, 80, n_leads), 
    'valor_venda': np.random.choice([0, 1500, 3000, 5000], n_leads, p=[0.9, 0.05, 0.03, 0.02])
}

df = pd.DataFrame(data)

# --- SIMULANDO DADOS SUJOS (Para mostrar serviço pro recrutador) ---
# 1. Deixando 50 leads sem origem (nulos)
df.loc[df.sample(n=50).index, 'origem'] = np.nan

# 2. Criando 20 leads duplicados
duplicados = df.sample(n=20)
df = pd.concat([df, duplicados], ignore_index=True)

# Salva o arquivo na sua pasta
df.to_csv('leads_sdr_bruto.csv', index=False)
print("✅ SUCESSO: O arquivo 'leads_sdr_bruto.csv' foi criado!")