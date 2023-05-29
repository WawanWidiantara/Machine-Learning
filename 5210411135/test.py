import math

data = [84,88,65,77,71,50,91,82,74,78,80,65]
hasil = []
for i in data:
    h = ((i - 75.42)**2)
    hasil.append(h)

print((sum(hasil))/11)
print((sum(data)))

