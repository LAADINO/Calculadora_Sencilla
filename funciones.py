texto = ""
numeros = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
operadores = ("√", "%", "÷", "X", "-", "+", "^", ".")


def validacion_operador(simbolo):

    global texto

    if len(texto) == 0:

        texto = "0"
        texto += simbolo

    elif texto[-1] in operadores:
        texto = texto[:-1] + simbolo

    else:
        texto += simbolo


def logica_precionar(simbolo):

    global texto

    if simbolo == "√":

        if len(texto) == 0:
            texto += simbolo
        elif texto[-1] != ".":
            texto += simbolo

    elif simbolo == "%":

        validacion_operador(simbolo)

    elif simbolo == "⌫":

        if len(texto) > 0:

            texto = texto[:-1]

            if len(texto) == 1 and texto[0] == "0":

                texto = texto[:-1]

    elif simbolo == "÷":

        validacion_operador(simbolo)

    elif simbolo == "X":

        validacion_operador(simbolo)

    elif simbolo == "-":

        validacion_operador(simbolo)

    elif simbolo == "+":

        validacion_operador(simbolo)

    elif simbolo == "^":

        validacion_operador(simbolo)

    elif simbolo == "=":

        datos = list()
        operadores = list()

        for i in range(len(texto)):

            if texto[i] in operadores:
                print("Hola")

    elif simbolo == ".":

        if len(texto) == 0:

            texto = "0."

        if texto[-1] in numeros:

            texto += "."
    elif simbolo == "0":

        if len(texto) != 1:

            texto += "0"

    else:

        texto += simbolo

        if len(texto) == 2 and texto[0] == "0":
            texto = texto[1:]

    return texto
