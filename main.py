
while True:
    palavra = 'yurizin'
    sugestao = input("Digite sua sugestão: ")

    nova = ''

    for i in range(len(palavra)):
        if sugestao == palavra[i]:
            nova += sugestao + " "
            contIndice = i
        else:
            nova += "_ "
    print(nova)
    if sugestao == palavra:
        print("Palavra correta!")
        break




