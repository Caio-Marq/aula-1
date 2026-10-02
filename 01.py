aluno = input("digite o nome do aluno: ")
ano_nascimento = int(input("digite o ano de nascimento do aluno: "))
nota1 = float(input("digite a nota do aluno: "))
nota2 = float(input("Digite a nota 2 do aluno: "))

media = (nota1 + nota2) / 2

if media >= 7:
    situacao = "aprovado"
elif media >= 5: 
    situacao = "recuperacao"
else:
    situacao = "reprovado"

ano_atual = 2026
idade = (ano_atual - ano_nascimento)

print (f"Aluno: {aluno}")
print (f"Idade: {idade}")
print (f"Media: {media}")
print (f"Situacao: {situacao}")