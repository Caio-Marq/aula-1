# crie um algoritmo que leia 3 valores (lados de um triângulo)
# determine se formam um triângulo, e se formar verifique
# se é um equilátero, isósceles ou escaleno. 

lado1 = float(input("me dê o valor do primeiro lado"))
lado2 = float(input("me dê o valor do segundo lado"))
lado3 = float(input("me dê o valor do terceiro lado"))

triangulo = lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1

eq = (lado1 == lado2 == lado3)
iso = (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3)

if triangulo:
   "é um triangulo"
else:
     "não é um triangulo"

if eq:
    Resultado = "é um equilatero"

elif iso:
   Resultado = "é um isoseles"

else:
    "É um escaleno"

print (f"triangulo: {triangulo}")
print (f"Resultado: {Resultado}")