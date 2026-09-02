c = 4821735227044737729172894050832578813733965898452420107360773622174975905446542522417312328623823461

def integer_cube_root(n):
    lo = 0
    hi = 1

    while hi ** 3 <= n:
        hi *= 2

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if mid ** 3 <= n:
            lo = mid
        else:
            hi = mid

    return lo

m = integer_cube_root(c)

# Convert integer m to bytes without Crypto
flag = m.to_bytes((m.bit_length() + 7) // 8, 'big')

print(flag)