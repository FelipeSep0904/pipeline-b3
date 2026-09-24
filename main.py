import yfinance as yf
import supabase as sp
import os 

# conectar ao Supabase
from dotenv import load_dotenv
from supabase import create_client
load_dotenv()
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
banco_dados = create_client(supabase_url, supabase_key)


# extrair e limpar os dados
acao_petr = yf.Ticker("PETR4.SA")
historico = acao_petr.history(period="1y")
dados_limpos = historico[["Open", "Close", "High", "Low"]]
dados_limpos.index = dados_limpos.index.date