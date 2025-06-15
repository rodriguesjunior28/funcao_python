salario = 2000

def salario_bonus(bonus, lista):
    global salario

    # Esse trecho aqui é pra preservar e não alterar a lista original
    # O append modifica a lista original no local, não cria uma nova lista
    lista_aux = lista.copy()
    lista_aux.append(2)

    # O extend é usado para add múltiplos elementos de um iterável
    lista1 = ["Junior", 3, "Germano", 4, "Reinaldo",]
    lista_aux.extend(lista1)
    print(f"lista aux={lista_aux}")


    salario += bonus  # Versão resumida de salario + salario = bonus
    return salario


lista = [1]
salario_com_bonus = salario_bonus(500, lista)
print(salario_com_bonus)
print(lista)