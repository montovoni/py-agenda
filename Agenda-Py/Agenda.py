AGENDA = {}
print("BY DOUGLAS MONTOVONI BATITSA")
print('==================================================')

def mostrar_contatos():
     for contato in AGENDA:
        buscar_contato(contato)

def buscar_contato(contato):
    try:
        print('--------------------------------------------')
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])
        print('--------------------------------------------')
    except KeyError:
        print('>>>> Contato inexistente <<<<  ')
    except Exception as error:
        print('>>>> Um erro inesperado ocorreu <<<<  ')
        print(error)

def ler_detalhes_contatos():
    telefone = input('Digite o telefone: ')
    email    = input('Digite o email: ')
    endereco = input('Digite o endereco: ')
    print('--------------------------------------------')
    return telefone, email, endereco

def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar()
    print('>>>> Contato {} adicionado/editado com sucesso <<<<  '.format(contato))


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print('>>>> Contato {} excluido com sucesso <<<<'.format(contato))
    except KeyError:
        print('>>>> Contato inexistente <<<<')
    except Exception as error:
        print('>>>> Um erro inesperado ocorreu <<<<')
        print(error)

def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write("{},{},{},{}\n".format(contato, telefone, email, endereco))
        print('>>>> Agenda exportada com sucesso <<<<')
    except Exception as error:
        print('>>>> Algum erro ocorreu ao exportar contatos <<<<')
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
        print('>>> Arquivo não encontrado <<<<')
    except Exception as error:
        print('>>>> Algum erro inesperado ocorreu <<<<')
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
        print("DATABASE CARREGANDO.......   ")
        print("{} - Contatos carregados com sucesso  ".format(len(AGENDA)))
    except FileNotFoundError:
        print('>>>> Arquivo não encontrado <<<<')
    except Exception as error:
        print('>>>> Algum erro inesperado ocorreu <<<<')
        print(error)

def imprimir_menu():
    print('==================================================')
    print("[1] - Mostrar todos os contatos da agenda")
    print("[2] - Buscar contato ")
    print("[3] - Incluir contato")
    print("[4] - Editar contato ")
    print("[5] - Excluir contato ")
    print("[6] - Exportar contatos para CSV ")
    print("[7] - Importar contatos CSV ")
    print("[0] - Fechar programa ")
    print('==================================================')

#INICIO DO PROGRAMA
carregar()
while True:

    imprimir_menu()
    escolha = input("Ecolha uma opção:  ")

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
        print('--------------------------------------------')
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('--------------------------------------------')
            print('>>>> Contato já existente <<<<')
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
            print('>>>> Contato inexistente <<<<  ')

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
        print(">>> Programa encerrado <<<< ")
        break
    else:
        print(">>>> Opção invalida <<<< ")