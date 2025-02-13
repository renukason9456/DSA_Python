def myAtoi(s):
    s = s.strip()
    if not s:
        return 0
    
    sign, i = (-1, 1) if s[0] == '-' else (1, 1) if s[0] == '+' else (1, 0)
    num = 0
    
    while i < len(s) and s[i].isdigit():
        num = num * 10 + int(s[i])
        i += 1
    
    return max(-2**31, min(sign * num, 2**31 - 1))


print(myAtoi("-42"))