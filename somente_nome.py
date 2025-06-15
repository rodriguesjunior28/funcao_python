# Aqui somente por nome e coloca o * Keyword (palavra-chave)

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro(modelo="Palio", ano=1998, placa="CON-6172", marca="Fiat", motor="1.5", combustivel="Gasolina")