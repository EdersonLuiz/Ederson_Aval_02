atendimento = ["paciente1", "paciente2", "paciente3", "paciente4", "paciente5"]
valor = 0
print ("Aperte 0 parar adicionar paciente e 1 para remover!")

valor = int (input("Valor: "))

if valor == 0:
    paciente = str(input("Nome do paciente: "))
    atendimento.append(paciente)
else:
    print (atendimento)
    numero = int (input("Qual paciente quer remover?"))
    atendimento.pop(numero)
