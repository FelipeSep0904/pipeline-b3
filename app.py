import streamlit as st 
import plotly.express as px
import pandas as pd
import os

# conectar ao Supabase
from dotenv import load_dotenv
from supabase import create_client
load_dotenv(override=True)
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
banco_dados = create_client(supabase_url, supabase_key)

# puxar tabela 
resposta = banco_dados.table("historico_petr4").select("*").execute()
df = pd.DataFrame(resposta.data)
df = df.round({"Close": 2})

# configurar streamlit e plotly
st.title ("Histórico de Preços da PETR4")
ultimo_preço = df["Close"].iloc[-1]
ultimo_preço_formatado = f"R$ {ultimo_preço:.2f}"
maior_preço = df ["Close"].max()
menor_preço = df ["Close"].min()
col1, col2, col3 = st.columns(3)
variação = df["Close"].iloc[-1] - df["Close"].iloc[-2]
col1.metric(label="Último Preço", value=ultimo_preço_formatado, delta=f"{variação:.2f}", border = True)
col2.metric(label="Maior Preço", value=f"R$ {maior_preço:.2f}", border = True)
col3.metric(label="Menor Preço", value=f"R$ {menor_preço:.2f}", border = True)
figura = px.line(df, x="Data", y="Close")
st.plotly_chart(figura)

