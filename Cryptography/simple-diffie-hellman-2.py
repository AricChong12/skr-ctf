p = 211
g = 66
a = 13
b = 37

# Public keys
A = pow(g, a, p)
B = pow(g, b, p)

# Shared secret
s_alice = pow(B, a, p)
s_bob = pow(A, b, p)

print("Alice Public Key:", A)
print("Bob Public Key:", B)
print("Shared Secret (Alice):", s_alice)
print("Shared Secret (Bob):", s_bob)

print(f"SKR{{{s_alice}}}")