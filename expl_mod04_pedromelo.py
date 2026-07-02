''''''''''
listas


'''''''''

frutas = ["laranja","mexirica","abacaxi","ameixa","acerola"]

#print(frutas)

print("qual fruta nova você deseja adicionar na lista ?")
nova_fruta=input()
fruta_nova=input("a fruta escolhida foi: ")

frutas.append(fruta_nova) #variavel mais atrbuto
#devo usar o ponto "frutas.append(nova_fruta)"
#para adcionar a fruta na lista

print(f'Essas são as nossas frutas: {frutas}')