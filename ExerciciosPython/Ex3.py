print("Bem-vindo ao sistema de cadastramento de notas colaborador!")
nota1 = float(input("Insira a nota do primeiro bimestre: "))
nota2 = float(input("Insira a nota do segundo bimestre: "))
nota3 = float(input("Insira a nota do terceiro bimestre: "))
nota4 = float(input("Insira a nota do quarto bimestre: "))
media = (nota1+nota2+nota3+nota4)/4

if(media>=7):
    print("Aluno aprovado com média: ",media)
else:
    print("Aluno retido com média: ",media)

