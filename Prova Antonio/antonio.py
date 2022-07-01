while(1==1):
    nome = input("Escreva seu nome: ")
    print('Seu nome é:', nome)
    nota = int (input("Quanto você tirou na prova?"))
    print('Sua nota é:', nota)
    if  nota <= 5:
        nota = 6
    if nota > 10:
        nota = 10

    f = open('dados.txt', "a")
    f.write(f"{nome};{nota}\n")
    f.close()