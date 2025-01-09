vacio = {}
precios = {
    "Pera": 1.60,
    "Ciruela": 1.24,
    "Manzana": 1.75
}
print(precios)

print(precios.keys())
print(precios.values())
print(precios.items())

if "Sandía" in precios:
    pSandiaaa = precios["Sandía"]
    pSandia = precios.get("Sandía")
    pMelon = precios.get("Melón", -1)


del precios["Ciruela"]
print(precios)

print('Elemento')
elemento=precios.pop('Manzana')
print(elemento)

print(precios)
print(len(precios))


precios.clear()
print(precios)