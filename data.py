class Elementos:
    @staticmethod
    def nombres_elementos(simbolo):
        elementos = {
            "N": "Nitrogeno",
            "C": "Carbono",
            "S": "Azufre",
            "P": "Fosforo",
            "Se": "Selenio",
            "Cl": "Cloro",
            "Br": "Bromo",
            "I": "Yodo",
            "AT": "Astato",
            "CR": "Cromo",
            "Mn": "Manganeso",
            "W": "Wolframio",
            "V": "Vanadio"
        }
        try:
            if simbolo in elementos:
                return elementos[simbolo]
        except:
            print("Elemento desconocido: {simbolo}")
         
    def raices_elementos(simb2):
        elementos = {
            "N": "nitr",
            "C": "carbon",
            "S": "sulfur",
            "P": "fosfor",
            "Se": "selen",
            "Cl": "clor",
            "Br": "brom",
            "I": "iod",
            "AT": "astat",
            "CR": "cromo",
            "Mn": "mangan",
            "W": "wolfram",
            "V": "vanadio"
        }
        try:
            if simb2 in elementos:
                return elementos[simb2]
        except:
            print("Elemento desconocido: {simb2}")
        
    h = +1; o = -2
    C = [2, 4]
    N = [3, 5]
    P = [1, 3, 5]
    S = [2, 4, 6]
    Se = [2,4,6]
    Cl = [1,3,5,7]
    Br = [1,3,5,7]
    I = [1,3,5,7]
    At = [1,3,5,7]
    Mn = [7]
    Cr = [6]
    W = [6]
    V = [5]