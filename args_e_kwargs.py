def exibir_poema(data_extenso, *lista, **dicionario):
    texto = "\n".join(lista)  # \n é pra deixar um embaixo do outro 
                             # Tupla é passado valor separado por vírgula, dentro de ()
                             # lista = args

    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()]) # Chave e valor dentro de ([{} : {valor}])
                                                                            # kwargs = dicionario
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema("Sexta-feira, 13 de junho de 2025", 
             
            "Zen of Python", "Beautiful is better than ugly.", 
            
            autor="Tim Peters", ano="1999")