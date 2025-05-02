palavra = 'yuri'
sugestao = 'i'

cont = 0
for i in range(len(palavra)):
    cont +=1
cont = '_ ' * cont
print(cont)

for i in range(len(palavra)):
    if sugestao == palavra[i]:
        print(i)
        print(palavra[i])
