aluno = input ("Digite o nome do aluno :")
Disciplina = input("Digite o nome a disciplina :")
N1 = float(input("Digite a primeira nota :"))
N2 = float(input("Digite a segunda nota :"))
media = (N1+N2)/2
if  media >= 6.0 :
    situação = "aprovado"
else :
    situação = "reprovado"
print (f" { aluno} está {situação} na disciplina {Disciplina}")