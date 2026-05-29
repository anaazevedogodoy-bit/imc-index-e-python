# Solicita o peso do usuário em quilogramas e converte o texto digitado para um número decimal (float)
peso = float(input("Digite o seu peso em kg (ex: 70.5): "))

# Solicita a altura do usuário em metros e também converte para um número decimal (float)
altura = float(input("Digite a sua altura em metros (ex: 1.75): "))

# Calcula o IMC dividindo o peso pela altura elevada ao quadrado
imc = peso / (altura**2)

# Exibe o valor do IMC calculado, arredondando o resultado para duas casas decimais
print(f"\nSeu IMC é: {imc:.2f}")

# Inicia a estrutura condicional para classificar o IMC do usuário
if imc < 18.5:
    # Se o IMC for menor que 18.5, executa este bloco
    print("Classificação: Abaixo do peso")

elif imc >= 18.5 and imc < 25:
    # Se a condição anterior for falsa, mas o IMC estiver entre 18.5 e 24.9, executa este bloco
    print("Classificação: Peso normal")

elif imc >= 25 and imc < 30:
    # Se as anteriores forem falsas, mas o IMC estiver entre 25 e 29.9, executa este bloco
    print("Classificação: Sobrepeso")

else:
    # Se nenhuma das condições anteriores for atendida (IMC igual ou maior que 30), executa este bloco
    print("Classificação: Obesidade")
