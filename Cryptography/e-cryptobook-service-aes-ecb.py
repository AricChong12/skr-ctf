#!/usr/bin/env python3
import socket
import re

HOST = "skrctf.me"
PORT = 3017

def recv_until(s, marker=b"Choose an option:"):
    data = b""
    while marker not in data:
        chunk = s.recv(4096)
        if not chunk:
            break
        data += chunk
    return data.decode(errors="ignore")

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    
    # Banner
    print(recv_until(s))
    
    # ===== 1. Get encrypted flag =====
    s.send(b"3\n")
    resp = recv_until(s)
    print(resp)
    
    # Extract the two ciphertext blocks
    blocks = re.findall(r"[0-9a-f]{32}", resp)
    if len(blocks) < 2:
        print("[-] Failed to get flag ciphertext")
        return
    c1, c2 = blocks[0], blocks[1]
    print(f"[+] Flag CT blocks: {c1} {c2}")
    
    # ===== 2. Encrypt a known 16-byte block =====
    s.send(b"1\n")
    recv_until(s, b"Enter plaintext to encrypt:")
    s.send(b"A" * 16 + b"\n")
    resp = recv_until(s)
    print(resp)
    
    known_block = re.findall(r"[0-9a-f]{32}", resp)[0]
    print(f"[+] Known CT block: {known_block}")
    
    # ===== 3. Decrypt flag_ct || known_ct =====
    s.send(b"2\n")
    recv_until(s, b"Enter cipher text in Hex to decrypt:")
    
    payload = (c1 + c2 + known_block).encode() + b"\n"
    s.send(payload)
    
    resp = recv_until(s)
    print(resp)
    
    # Extract the flag
    m = re.search(r"SKR\{[^}]+\}", resp)
    if m:
        print("\n[+] FLAG:", m.group(0))
    else:
        print("[-] Flag not found in output")
    
    s.close()

if __name__ == "__main__":
    main()