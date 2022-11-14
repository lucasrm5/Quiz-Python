print("Bem vindo ao nosso quiz")
answer_user = input("Vamos começar? (S/N)")
print(answer_user)

if answer_user != "S":
    quit()

score = 0

print("Começando...")
print("1 - Quais o menor e o maior país do mundo? \n (A) Vaticano e Rússia \n (B) Nauru e China \n (C) Mônaco e Canadá \n (D) Malta e EUA \n (E) San Marino e Índia \n")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Correto!")
    score = score + 1 # TODA RESPOSTA CORRETA SERÁ INCREMENTADO 1 PONTO
else:
    print("Incorreto!")

print()
print("2 - Qual o nome do presidente do Brasil que ficou conhecido como Jango? \n (A) Jânio Quadros \n (B) Jacinto Anjos \n (C) Getúlio Vargas \n (D) João Figueiredo \n (E) João Goulart \n")
answer_2 = input("Resposta: ")

if answer_2 == "E":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print()
print("3 - Qual o livro mais vendido no mundo a seguir à Bíblia? \n (A) O Senhor dos Anéis \n (B) Dom Quixote \n (C) O Pequeno Príncipe \n (D) Ela, a Feiticeira \n (E) Um Conto de Duas Cidades \n ")
answer_3 = input("Resposta: ")

if answer_3 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print()
print("4 - Quantas casas decimais tem o número pi? \n (A) Duas \n (B) Centenas \n (C) Infinitas \n (D) Vinte \n (E) Milhares \n")
answer_4 = input("Resposta: ")

if answer_4 == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print()
print("5 - Atualmente, quantos elementos químicos a tabela periódica possui? \n (A) 113 \n (B) 109 \n (C) 108 \n (D) 118 \n (E) 92 \n")
answer_5 = input("Resposta: ")

if answer_5 == "D":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print()
print("6 - Quais os países que têm a maior e a menor expectativa de vida do mundo? \n (A) Japão e Serra Leoa \n (B) Austrália e Afeganistão \n (C) Itália e Chade \n (D) Brasil e Congo \n (E) EUA e Angola \n")
answer_6 = input("Resposta: ")

if answer_6 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print()
print("7 - Quanto tempo a luz do Sol demora para chegar à Terra? \n (A) 12 minutos \n (B) 1 dia \n (C) 12 horas \n (D) 8 minutos \n (E) 12 segundos \n")
answer_7 = input("Resposta: ")

if answer_7 == "D":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print()
print("8 - Em que período da pré-história o fogo foi descoberto? \n (A) Neolítico \n (B) Paleolítico \n (C) Idade dos Metais \n (D) Período da Pedra Polida \n (E) Idade Média \n")
answer_8 = input("Resposta: ")

if answer_8 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print()
print("9 - Em qual local da Ásia o português é língua oficial? \n (A) Índia \n (B) Filipinas \n (C) Moçambique \n (D) Macau \n (E) Portugal \n")
answer_9 = input("Resposta: ")

if answer_9 == "D":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")


print()
print("10 - Qual destes países é transcontinental? \n (A) Rússia \n (B) Filipinas \n (C) Marrocos \n (D) Groenlândia \n (E) Tanzânia \n")
answer_10 = input("Resposta: ")

if answer_10 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print(f"Nosso quiz acabou ... Sua pontuação final foi: {score} / 10")