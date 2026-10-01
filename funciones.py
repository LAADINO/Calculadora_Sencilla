texto = ""
operadores = ("÷", "X", "-", "+", "^")
op_basicos = (
    "÷",
    "X",
    "-",
    "+",
)


def resolver():

    print("HOLA")


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

        if len(texto) == 0:
            texto = "0√"
        else:
            texto += simbolo

    elif simbolo == "%":
        if any(op in texto for op in op_basicos):
            if texto[-1] in op_basicos or texto[-1].isdigit():
                texto += simbolo

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

        if "√√" in texto:

            print(f"hay un √√ en la ecuacion {texto}")
        else:
            print("no tiene √√")

    elif simbolo == ".":
        if simbolo in texto and texto[-1] not in operadores:
            for i, c in reversed(list(enumerate(texto))):
                if c in operadores:
                    numero = texto[i + 1 :]
                    if simbolo not in numero:
                        texto += simbolo
        elif len(texto) == 0:
            texto += "0."
        elif texto[-1] in operadores:
            texto += "0."
        elif texto[-1].isdigit():
            texto += simbolo

    elif simbolo == "0":

        if len(texto) != 0:

            if texto[-1] in operadores:
                texto += simbolo
            elif texto[-1].isdigit() and texto[-1] != simbolo:
                texto += simbolo
            elif texto.endswith(("√", "%")):
                for c in reversed(texto):
                    if c.endswith(("√", "%")):
                        texto = texto[:-1]
                    else:
                        break
                texto += simbolo
            elif len(texto) != 1:
                if texto[-1].isdigit() and texto[-1] != simbolo:
                    texto += simbolo
        else:
            if len(texto) != 1:
                if texto[-1].isdigit():
                    texto += simbolo

    else:

        if len(texto) != 0:
            if texto.endswith(("√", "%")):
                for c in reversed(texto):
                    if c.endswith(("√", "%")):
                        texto = texto[:-1]
                    else:
                        break
                texto += simbolo

            else:
                texto += simbolo

                if len(texto) == 2 and texto[0] == "0":
                    texto = texto[1:]
        else:

            print(len(texto))
            texto += simbolo

            if len(texto) == 2 and texto[0] == "0":
                texto = texto[1:]

    print(texto)

    return texto
