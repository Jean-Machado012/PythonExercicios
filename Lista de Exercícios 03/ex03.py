a = 80000
txA = 0.03
paisA = (a * txA)
b = 200000
txB = 0.015
paisB = (b * txB)
ano = 0
while a < b:
    a = a (paisA * txA)
    b = b + (paisB * txB)
    ano += 1
print(f'Foi necessário {ano} anos para que o País A superasse a população do País B')