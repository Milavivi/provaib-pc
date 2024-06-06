hora = int(input("Digite uma hora entre 0 e 23:"))
if 0 <= hora <= 11:
    periodo_do_dia = "manhã" 
elif 12 <= hora <= 17:
    periodo_do_dia = "tarde"
elif 18 <= hora <= 23 :
    periodo_do_dia ="noite"
print (f'é de {periodo_do_dia}')