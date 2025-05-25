import os
import time
from supabase import create_client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

COINS = ["XRP","ADA","QNT","LINK","FLR","XLM","ALGO","IOTA","XDC","BTC"]

def fetch_signals():
for coin in COINS:
record = {"coin": coin, "rsi_1m": 50, "updated_at": "now()"}
supabase.table("signal_matrix").insert(record).execute()

if name == "main":
while True:
fetch_signals()
time.sleep(10)
