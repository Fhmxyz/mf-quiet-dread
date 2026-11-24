import os

LINE = "LGTM — the tests pass, the types check, and I stopped understanding this file three refactors ago, so it belongs to all of us now."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
