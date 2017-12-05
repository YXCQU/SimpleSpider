s = []

a = {
    "https": "",
    "socks": "111"
}
b = {
    "https": "122"
}

s.append(a)
s.append(b)
print(s)

print(s.remove(a))
print(s)
