lista_alunos = []
for r in range(1):
    print(" "*100)
    print("-"*100)
    Aluno = {"Matricula": int( input("Matrícula: ")), "Nome": input("Nome Completo: "),
            "Data_nasc": input("Data de Nascimento: "), "Serie": input("Série: "),
             "Turma": input("Turma: "), "Turno": input("Turno: "), "Colegio": input("Colégio: ")}
    lista_alunos.append(Aluno)
    print(Aluno.get("Matricula"))