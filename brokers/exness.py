import requests
from config import EXNESS_API_KEY

BASE_URL = "https://api.exness.com/"

def connect():
    print("[Exness] Connected (stub)")
    # Implement actual API auth here

def place_order(signal):
    print(f"[Exness] Placing order: {signal}")
    # Implement order logic
