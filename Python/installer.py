import os
import time

os.system('pip install asyncio')

loading_animation = ["|", "/", "-", "\\"]
for _ in range(20):
    for symbol in loading_animation:
        print(f"Installing... {symbol}", end="\r")
        time.sleep(0.1)
