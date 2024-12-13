from random import randit

spisok1 = []
for i in range(10):
    spisok1.append(randit(1, 100))

print(*spisok1)

spisok1.sort()
print(*spisok1)
print(len(set(spisok1)))
