def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")



salvar_carro("Fiat", "Palio", 1998, "CON-6172") # Nesse caso se o usuário inverter a ordem simplesmente o python vai deixar

salvar_carro(marca="Fiat", modelo="Palio", ano=1998, placa="CON-6172") # Nesse caso ela não dará erro pq ele já passa nomeado ou seja
                                                                       # Falando a ordem de cada argumento

salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1998, "placa": "CON-6172"}) # Nessa caso ele tá passadno um dicionário representado (**)
                                                                                       # Por debaixo dos panos ele fica igual ao de cima