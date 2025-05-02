palavra = 'yurizin'
sugestao = 'i'


nova = ''

for i in range(len(palavra)):
    if sugestao == palavra[i]:
        nova += sugestao + " "
        contIndice = i
    else:
        nova += "_ "

print(nova)




