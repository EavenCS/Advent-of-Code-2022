X = [l.strip() for l in open('Day1.in')]

A = []
for elf in ('\n'.join(X)).split('\n\n'):
    q = 0
    for x in elf.split('\n'):
        q += int(x)
    A.append(q)
A = sorted(Q)
print(Q[-1])

