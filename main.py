import yfinance as yf
import supabase as sp
import os 
import pandas as pd
import numpy as np

# conectar ao Supabase
from dotenv import load_dotenv
from supabase import create_client
load_dotenv(override=True)
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
banco_dados = create_client(supabase_url, supabase_key)


# extrair, limpar e enviar os dados
acao_petr = yf.Ticker("PETR4.SA")
historico = acao_petr.history(period="1y")
dados_limpos = historico[["Open", "Close", "High", "Low"]].copy()
dados_limpos.index = dados_limpos.index.date
dados_limpos = dados_limpos.reset_index()
dados_limpos.columns = ["Data", "Open", "Close", "High", "Low"]
dados_limpos["Data"] = dados_limpos["Data"].astype(str)
dados_enviar = dados_limpos.to_dict(orient="records")
resposta = banco_dados.table("historico_petr4").upsert(dados_enviar).execute()