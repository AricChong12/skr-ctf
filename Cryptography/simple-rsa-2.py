p = 11
q = 17
n = p * q
e = 3
c = 103

phi = (p - 1) * (q - 1)

# Find d
d = pow(e, -1, phi)

# Decrypt
m = pow(c, d, n)

print("n =", n)
print("phi =", phi)
print("d =", d)
print("m =", m)