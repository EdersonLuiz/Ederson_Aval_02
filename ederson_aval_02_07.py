mês = input ("Insira o mês de seu nascimento: ")
dia =  int (input("Insira o dia de seu nascimento: "))

primavera = ["setembro", "outubro", "novembro"]
verao = ["dezembro", "janeiro", "fevereiro"]
outono = ["março", "abril", "maio"]
inverno = ["junho", "julho", "agosto"]

if mês == "setembro" or "outubro" or "novembro":
    print ("Primavera!")
elif mês == "dezembro" or "janeiro" or "fevereiro":
    print ("Verão!")
elif mês == "março" or "abril" or "maio":
    print ("Outono!")
else:
    print ("Inverno!")
if dia > 31:
    print ("Dia inválido!")