import os
import functions

os.system("cls")

while(True):
    print("Nomenclatura Tradicional de Oxacidos =D")
    print("Ejemplo: H1Mn1O4, ingresa la atomicidad ")
    F = str(input("Ingrese la formula : ")).upper()
    l = functions.contar_letras(F)
    if "H" in F and "O" in F and l == 3 or l == 4: 
        functions.id_valencias(F)
        break
    else:
        print("Mmm, verifica que tu compuesto sea un Oxacido o que este escrito correctamente, graciaaas.")
        break
