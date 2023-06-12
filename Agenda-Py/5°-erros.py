# Erros em tempo de compilação
# Erros em tempo de execução
# Erros de lógica


try:
    n1 = float(input("Número 1:")) #ValuerError
    n2 = float(input("Número 2:")) #ValuerError

    print(n1/n2) #ZeroDivisionError
except ValueError as error:
    print("Inválido, digite apenas números")
except ZeroDivisionError as error:
    print("Não pode ser feita divisão por 0")
except Exception as error:
    print("Algum erro ocorreu")
    print(error)
finally:
    print("Fim do programa")