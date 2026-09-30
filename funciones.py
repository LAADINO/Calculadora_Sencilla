texto = ""
operadores = ("√", "%", "÷", "X", "-", "+", "^")


def resolver(cadena):

    print("hola")


def validacion_operador(simbolo):

    global texto

    if len(texto) == 0:

        texto = "0"
        texto += simbolo

    elif texto[-1] in operadores or texto[-1] == ".":
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

        print("Hola")

    elif simbolo == ".":
        if "." in texto and texto[-1] not in operadores:
            for i, c in reversed(list(enumerate(texto))):
                if c in operadores:
                    numero = texto[-i:]
                    if "." not in numero:
                        texto += "."

        elif len(texto) == 0:
            texto += "0."
        elif texto[-1] in operadores:
            texto += "0."
        elif texto[-1].isdigit():
            texto += "."
    elif simbolo == "0":

        if len(texto) != 1:

            texto += "0"

    else:

        texto += simbolo

        if len(texto) == 2 and texto[0] == "0":
            texto = texto[1:]

    print(texto)

    return texto
