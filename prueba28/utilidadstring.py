#las constantes se ponen en mayúsculas
DIGITOS = ["0","1","2","3","4","5","6","7","8","9"]

class UtilidadString:
    @staticmethod
    def contarDigitos(lacadena:str) ->int:
        resultado = 0
        for caracter in range(0, len(lacadena)):
            if lacadena[caracter] in DIGITOS:
                resultado += 1
        return resultado


if __name__ == '__main__':
    def main():
        print(UtilidadString.contarDigitos("estoes1y esto 2"))
    main()