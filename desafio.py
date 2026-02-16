bonus_ano = 1000.00

# 1) Solicite ao usuário que digite seu nome:
nome = input("Digite seu nome: ")

# 2) Solicite ao usuário que digite o valor do seu salário:
salario = float(input("Digite o valor do seu salário: "))

# 3) Informe o valor do bonus.
bonus_usuario = float(input("Digite o valor do bônus: "))

# 4) Calculo o valor do bonus final.
valor_bonus = bonus_ano + salario * bonus_usuario

# 5) Imprima uma mensagem personalizada para o usuário, informando o valor do bônus final.
print(f"{nome}, o valor do seu bônus final é: R${valor_bonus:.2f}")
