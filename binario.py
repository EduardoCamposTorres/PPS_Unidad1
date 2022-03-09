
def esBinario(strbinario):
    for digito in strbinario:
        if digito != "0" and digito != "1":
            return False
    return True

strbinario = str(input("Introduce un numero binario:"))

if esBinario(strbinario):
    print("El numero en decimal es:", int(strbinario, 2))
else:
    print("El numero introducido no es un numero binario.")