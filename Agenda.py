AGENDA = {}
print("\033[31mDOUGLAS MONTOVONI BATITSA\033[m")

def mostrar_contatos():
     for contato in AGENDA:
        buscar_contato(contato)

def buscar_contato(contato):
    try:
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])
        print('--------------------------------------------')
    except KeyError:
        print('\033[31m>>>> Contato inexistente <<<<\033[m')
    except Exception as error:
        print('\033[31m>>>> Um erro inesperado ocorreu <<<<\033[m')
        print(error)

def ler_detalhes_contatos():
    telefone = input('Digite o nome do telefone: ')
    email = input('Digite o nome do email: ')
    endereco = input('Digite o nome do endereco: ')
    return telefone, email, endereco

def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar()
    print('\033[31m>>>> Contato {} adicionado/editado com sucesso <<<<\033[m'.format(contato))


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print('\033[31m>>>> Contato {} excluido com sucesso <<<<\033[m'.format(contato))
    except KeyError:
        print('\033[31m>>>> Contato inexistente <<<<\033[m')
    except Exception as error:
        print('\033[31m>>>> Um erro inesperado ocorreu <<<<\033[m')
        print(error)

def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write("{},{},{},{}\n".format(contato, telefone, email, endereco))
        print('\033[31m>>>> Agenda exportada com sucesso <<<<\033[m')
    except Exception as error:
        print('\033[31m>>>> Algum erro ocorreu ao exportar contatos <<<<\033[m')
        print(error)


def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(nome, telefone, email, endereco)
    except FileNotFoundError:
        print('\033[31m>>>> Arquivo não encontrado <<<<\033[m')
    except Exception as error:
        print('\033[31m>>>> Algum erro inesperado ocorreu <<<<\033[m')
        print(error)

def salvar():
    exportar_contatos('database.csv')

def carregar():
    try:
        with open("database.csv", 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }
        print("\033[31mDATABASE CARREGANDO....... \033[m")
        print("\033[31m{} - Contatos carregados com sucesso\033[m".format(len(AGENDA)))
    except FileNotFoundError:
        print('\033[31m>>>> Arquivo não encontrado <<<<\033[m')
    except Exception as error:
        print('\033[31m>>>> Algum erro inesperado ocorreu <<<<\033[m')
        print(error)

def imprimir_menu():
    print('\033[92m=========================================')
    print("[1] - Mostrar todos os contatos da agenda")
    print("[2] - Buscar contato ")
    print("[3] - Incluir contato")
    print("[4] - Editar contato ")
    print("[5] - Excluir contato ")
    print("[6] - Exportar contatos para CSV ")
    print("[7] - Importar contatos CSV ")
    print("[0] - Fechar programa ")
    print('==================================================\033[m')

#INICIO DO PROGRAMA
carregar()
while True:

    imprimir_menu()
    escolha = input("\033[34mEcolha uma opção:\033[m")

    if escolha == '1':

        try:
            mostrar_contatos()
        except Exception as error:
            print("Erro,tente novamente")
            print(error)

    elif escolha == '2':
        contato = input("Digite o contato: ")
        buscar_contato(contato)
    elif escolha == '3':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('\033[31m>>>> Contato já existente <<<<\033[m')
        except KeyError:
            telefone, email, endereco = ler_detalhes_contatos()
            incluir_editar_contato(contato, telefone, email, endereco)

    elif escolha == '4':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('Editando contato: ', contato)
            telefone, email, endereco = ler_detalhes_contatos()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError:
            print('\033[31m>>>> Contato inexistente <<<<\033[m')

    elif escolha == '5':
        contato = input("Qual contato você deseja excluir: ")
        excluir_contato(contato)
    elif escolha == '6':
        nome_do_arquivo = input("Digite o nome do arquivo a ser Exportado: ")
        exportar_contatos(nome_do_arquivo)
    elif escolha == '7':
        nome_do_arquivo = input("Digite o nome do arquivo a ser importado: ")
        importar_contatos(nome_do_arquivo)
    elif escolha == '0':
        print("\033[31m>>>> Programa encerrado <<<<\033[m")
        break
    else:
        print("\033[31m>>>> Opção invalida <<<<\033[m")
