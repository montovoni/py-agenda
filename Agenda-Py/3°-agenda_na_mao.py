agenda = {
    "Douglas": {
        "Telefone": 32423423,
        "E-mail": "douglas@gmail.com",
        "Endereco": "Av 2"
    },
    "Nivaldo": {
        "Telefone": 7686788658,
        "E-mail": "nivaldo@gmail.com",
        "Endereco": "Av 3"
    },
    "Geslaine": {
        "Telefone": 4357383568,
        "E-mail": "geslaine@gmail.com",
        "Endereco": "Av 4"
    },
    "Lucas":{
        "Telefone": 3264363456,
        "E-mail": "lucas@gmail.com",
        "Endereco": "Av 4353"
    }
}

agenda["Silva"] = {
        "Telefone": 4543534543,
        "E-mail": "silva@gmail.com",
        "Endereco": "Av 55"
}

agenda.pop("Douglas") #remove o DOuglas

for contanto in agenda:
    print(contanto)
