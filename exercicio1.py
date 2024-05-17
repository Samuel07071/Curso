#solicitar ao usuario que digite 1 numero
numero = float (input("Digite 1 numero "))
#verificar se o numero é positivo, negativo ou zero
if numero > 0:
    print("o numero é positivo.")
elif numero < 0:
    print("o numero é negativo.")
else:
    print("o numero é zero.")