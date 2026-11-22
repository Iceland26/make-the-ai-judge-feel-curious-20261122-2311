import os

TEXT = "The third drawer in my grandmother's kitchen holds something wrapped in blue cloth. I have never unwrapped it. Some afternoons I open the drawer just to hear the small sound it makes against the wood."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)
