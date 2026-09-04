from pwn import *
from string import ascii_letters, digits

r = remote('skrctf.me', 3019)
charset = '_}!?' + digits + ascii_letters[::-1]

def cycle(s):
	global r
	r.sendline(b'1')
	r.recv()
	r.sendline(s.encode())
	r.recvuntil(b'Hex:\n')
	c = r.recv(32)
	r.recv()
	r.sendline(b'2')
	r.recv()
	r.sendline(c)
	res = r.recvlineS()
	r.recv()
	return "cheat.. Hehe" in res

prefix =""
flag = "SKR{"
r.recv()
while True:
	for c in charset:
		if(cycle(flag+c)):
			flag+=c
			print(prefix[:-3]+flag)
			if(len(flag)==15):
				prefix = prefix[:-3] + flag
				flag = flag[-3:]
			break
	else:
		break
	if(flag[-1] == '}'):
		break
print(prefix[:-3] + flag)