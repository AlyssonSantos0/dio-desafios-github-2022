altura_joao = 1.30
altura_pedro = 1.50
quant_anos = 0
while altura_joao <= altura_pedro:
    altura_joao = altura_joao + 0.05
    altura_pedro = altura_pedro +0.03
    quant_anos = quant_anos + 1
print(f"Foram necessários {quant_anos}anos para João ser maior que Pedro")
print(f"Altura de João: {altura_joao}m")
print(f"altura de Pedro: {altura_pedro}m")