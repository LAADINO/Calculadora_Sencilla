datos = list()
operadores = list()
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

        validacion_operador(simbolo)

    elif simbolo == "%":

        validacion_operador(simbolo)

    elif simbolo == "⌫":

        if len(texto) > 0:

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

        print("Condiciones de ")

    elif simbolo == ".":

        if len(texto) == 0:

            texto = "0."

        if texto[-1] in numeros:

            texto += "."

    else:

        texto += simbolo

    return texto
