arquivo = open("emails.txt")

conteudos =arquivo.readlines()

for linhas in conteudos:
    print(linhas,linhas.strip())
