ct = "SKRrRRrrRrRrRrSKrRrrRSKRRrRRRrRrrRRrrrrrrRrSKrrrrRRrRrrRrrRrrrRrRSKrrrrRSKRrRRRRrrrrrrRRRRrRSKRrRrrRrrrrrrRRSKrrRRRrRrRrrRrRRrRrrrrSKRRRrrrrrRRrRrSKRrSKRrrRRSKrrrRrRrRrrRRRrrRRRSKrRRRrRRRRSKrrrrrRrRrRRRRrrRrrrSKrrRSKrRRrrRrrrRRrrrRSKRRRRRRRRRrrrrRrSKrrRRRRRrrRRrrrrSKrrrrrrRRrRRrrrrSKrrRRRRrrrRRr"

# Split on every "SK" (the separators)
parts = ct.split("SK")[1:]          # skip the empty first element

# Length of each R/r run → letter (A=1, B=2, ...)
decoded = "".join(chr(64 + len(p)) for p in parts)

print(decoded)                      # LETTERNUMBERISCOOOOL
print(f"SKR{{{decoded}}}")          # SKR{LETTERNUMBERISCOOOOL}