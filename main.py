import os
# One-liner entry (102 chars): the line below is the whole submission.
# Writes to /output/entry.txt.
LINE = "I am resigning because the office plant has a better career path than I do, and frankly, it earned it."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
