import socket, base64

def get_ct(msg: bytes) -> bytes:
    s = socket.create_connection(("skrctf.me", 3013))
    s.recv(4096)                       # banner
    s.send(b"1\n")
    s.recv(4096)                       # "Enter message..."
    s.send(msg + b"\n")
    data = s.recv(4096).decode()
    s.close()
    # extract the Base64 part
    b64 = data.split("Base64: ")[1].split("\n")[0].strip()
    return base64.b64decode(b64)

# long enough to cover the whole key + a bit
pt = b"A" * 64
ct = get_ct(pt)
key = bytes(a ^ b for a, b in zip(pt, ct))
print(key.decode())   # SKR{XOR_1s_n0t_@_5eCur3_3nCrypt10n}SKR{XOR_1s_n0t_...