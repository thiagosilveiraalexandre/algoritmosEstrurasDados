vet = [3,8,10,15,19,25,28,33,35,40,42,46,47,53,56,61,65,71,74,79]

def Buscasequencial(vet,a):
    for i in range(len(vet)):
        if vet[i] == a:
            print("Achou " + str(vet[i]))
            break
        else:
            i +=1


a = int(input("Digite seu Número: "))


Buscasequencial(vet,a)