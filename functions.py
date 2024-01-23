import data
global x

def id_valencias(F):
    if (len(F) == 6):
        hidrogeno = F[1]; oxigeno = F[5]
        hEO = data.Elementos.h * int(hidrogeno)
        oEO = data.Elementos.o * (+int(oxigeno))
        x = abs(oEO) - hEO
        nomenclatura(F,2,3,x)
    elif (len(F) == 7):
        if (F[2:4] == "SE"):
            F = F.replace("SE", "Se")
        if (F[2:4] == "CL"):
            F = F.replace("CL", "Cl")
        if (F[2:4] == "MN"):
            F = F.replace("MN", "Mn")
        hidrogeno = F[1]; oxigeno = F[6]
        hEO = data.Elementos.h * int(hidrogeno)
        oEO = data.Elementos.o * (+int(oxigeno))
        x = abs(oEO) - hEO
        nomenclatura(F,2,4,x)
    
    else:
        print("Mmm, verifica que tu compuesto sea un Oxacido o que este escrito correctamente, graciaaas.")
        

def nomenclatura(F,z,c,x):
    print("La valencia del no metal/metal es:", x)
    print("Las valencias del", data.Elementos.nombres_elementos(F[z:c]), "es",  getattr(data.Elementos, F[z:c]))
    eo = list(getattr(data.Elementos, F[z:c]))
    if(x in eo):
        if(len(eo) == 2):
            if(x == eo[0]):
                print(f"Ácido {data.Elementos.raices_elementos(F[z:c])}oso")
            elif (x == eo[1]):
                print(f"Ácido {data.Elementos.raices_elementos(F[z:c])}ico")
        elif(len(eo) == 3):
            if(x == eo[0]):
                print(f"Ácido hipo{data.Elementos.raices_elementos(F[z:c])}oso")
            elif (x == eo[1]):
                    print(f"Ácido {data.Elementos.raices_elementos(F[z:c])}oso")
            elif (x == eo[2]):
                    print(f"Ácido {data.Elementos.raices_elementos(F[z:c])}ico")
        elif (len(eo) == 4):
            if(x == eo[0]):
                print(f"Ácido hipo{data.Elementos.raices_elementos(F[z:c])}oso")
            elif (x == eo[1]):
                print(f"Ácido {data.Elementos.raices_elementos(F[z:c])}oso")
            elif (x == eo[2]):
                print(f"Ácido {data.Elementos.raices_elementos(F[z:c])}ico")
            elif (x == eo[3]):
                print(f"Ácido per{data.Elementos.raices_elementos(F[z:c])}ico")
        elif(len(eo) == 1):
            if (x == eo[0]):
                print(f"Ácido per{data.Elementos.raices_elementos(F[z:c])}ico")
    else:
        print("Al parecer hubo un error... Intenta de nuevo por favor :(")

def contar_letras(text):
    contador_letras = 0
    for caracter in text:
        if caracter.isalpha():
            contador_letras += 1
    return contador_letras
