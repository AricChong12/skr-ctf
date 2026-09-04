from pwn import remote

HOST, PORT = "skrctf.me", 3018
BLOCK = 16

io = remote(HOST, PORT)

def menu():
    io.recvuntil(b"Choose an option: ")

def get_flag_blocks():
    menu()
    io.sendline(b"3")
    io.recvuntil(b"Encrypted flag:\n")
    blocks = []
    while True:
        line = io.recvline().strip()
        if line == b"" or b"1. Encrypt" in line:
            break
        blocks.append(line.decode())
    return blocks

def encrypt(plaintext: bytes):
    menu()
    io.sendline(b"1")
    io.recvuntil(b"Enter plaintext to encrypt: ")
    io.sendline(plaintext)
    io.recvuntil(b"Ciphertext in Hex:\n")
    blocks = []
    while True:
        line = io.recvline().strip()
        if line == b"" or b"1. Encrypt" in line:
            break
        blocks.append(line.decode())
    return blocks

def decrypt(hexdata: str):
    menu()
    io.sendline(b"2")
    io.recvuntil(b"Enter cipher text in Hex to decrypt: ")
    io.sendline(hexdata.encode())
    line = io.recvline().strip().decode()
    return line

# 1) Leak flag ciphertext blocks
flag_blocks = get_flag_blocks()
print("[*] Flag ciphertext blocks:", flag_blocks)

# 2) Get ciphertext of a known block
known_plain = b"A" * BLOCK
known_cipher = encrypt(known_plain)[0]
print("[*] Known cipher block:", known_cipher)

# 3) Decrypt each flag block using the ECB block-independence trick
recovered = ""
for i, blk in enumerate(flag_blocks):
    combo = known_cipher + blk
    resp = decrypt(combo)
    print(f"[*] Block {i} raw response: {resp}")
    if "Decrypted plaintext: " in resp:
        text = resp.split("Decrypted plaintext: ", 1)[1]
        piece = text[len(known_plain):]  # strip the known "AAAA..." prefix
        recovered += piece
    else:
        print(f"[!] Block {i} was blocked or errored: {resp}")

print("[+] Recovered flag:", recovered.rstrip("\x00"))
io.close()