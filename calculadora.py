continuar_usando = "SIM"

while continuar_usando == "SIM":

  print("SELECIONE A OPERAÇÃO DESEJADA")
  print("+ para Adição")
  print("- para Subtração")
  print("* para Multiplicação")
  print("/ para Divisão")

  operacao = input("\nQual operação você deseja realizar? ")

  if operacao == "+":
    a1 = float(input("\nDigite o primeiro valor: "))
    a2 = float(input("Digite o segundo valor: "))
    adicao = a1 + a2
    print("\nResultado da adição: ",adicao,"\n")
    print("*"*33,"\n")
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")

  if operacao == "-":
    b1 = float(input("\nDigite o primeiro valor: "))
    b2 = float(input("Digite o segundo valor: "))
    subtracao = b1 - b2
    print("\nResultado da subtração: ",subtracao,"\n")
    print("*"*33,"\n")
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")

  if operacao == "*":
    c1 = float(input("\nDigite o primeiro valor: "))
    c2 = float(input("Digite o segundo valor: "))
    multiplicacao = c1 * c2
    print("\nResultado da multiplicação: ",multiplicacao,"\n")
    print("*"*33,"\n")
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")

  if operacao == "/":
    d1 = float(input("\nDigite o primeiro valor: "))
    d2 = float(input("Digite o segundo valor: "))
    while d2 == 0:                 
      print("O segundo valor não pode ser zero!")
      d2 = float(input("\nDigite o segundo valor (diferente de zero): "))
    divisao = d1 / d2
    print("\nResultado da divisão: ",divisao,"\n")
    print("*"*33,"\n")
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")