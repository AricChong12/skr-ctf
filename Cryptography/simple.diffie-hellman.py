p = 211
g = 66
a = 13
b = 37

A = pow(g, a, p)
B = pow(g, b, p)

print("Alice's Public Key:", A)
print("Bob's Public Key:", B)
print(f"SKR{{{A}_{B}}}")