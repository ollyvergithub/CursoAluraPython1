print("********************************")
print('Bem vindo ao jogo de adivinhação')
print("********************************")

numero_secreto = 42

chute = input("Digite o seu número: ")

print("Você digitou ", chute)

if (numero_secreto == chute):
    print("Você acertou")
else:
    print("Você errou")

numero = int(chute)

if (numero_secreto == numero):
    print("Você acertou")
else:
    print("Você errou")

print("Fim do Jogo!")

numero1 = 10
numero2 = 10
if(numero1 == numero2):
    print("São números iguais")

idade1 = 10
idade2 = "20"
print(idade1 + idade2)