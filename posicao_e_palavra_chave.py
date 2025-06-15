# Quando quiser por posição coloca / 
# Quando quiser nomeado coloca *
# Marca dica opcional como exemplo que podemos colocar das duas formas

def criar_carro(modelo, ano, placa, /, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1998, "CON-6172", marca="Fiat", motor="1.5", combustivel="Gasolina")