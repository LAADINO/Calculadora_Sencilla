texto = ""
operadores = ("÷", "X", "-", "+")


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
        elif texto[-1] not in ("%", "^"):
            texto += simbolo

    elif simbolo == "%":
        if any(op in texto for op in operadores):
            if texto[-1] in operadores or texto[-1].isdigit():
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

        if len(texto) == 0:
            texto = "0^"
        elif texto[-1] not in ("%", "√"):
            texto += simbolo

    elif simbolo == "=":

        n1 = ""
        n2 = ""

        if "√√" in texto:

            print(f"hay un √√ en la ecuacion {texto}")
        else:
            if texto.endswith(operadores):
                texto = texto[:-1]

            for i, c in enumerate(texto):
                if c == "√":

                    n1 = ""

                    if texto[i - 1] in operadores:
                        op = texto[i - 1]
                        j = i - 2
                    else:
                        op = ""
                        j = i - 1

                    while j >= 0 and (texto[j].isdigit() or texto[j] == "."):
                        n1 = texto[j] + n1
                        texto = texto[:j] + texto[i + 1 :]
                        j -= 1

                    n1 = float(n1)
                    n1_aux = str(int(n1))
                    n1 = str(round((n1 ** (1 / 2)), 4))
                    if op.endswith(operadores):
                        texto = texto[:i] + n1_aux + op + n1 + texto[i + 1 :]
                    else:
                        texto = (
                            texto[:i] + str(round((n1 ** (1 / 2)), 4)) + texto[i + 1 :]
                        )

                elif c == "^":
                    print("Entro a ^")

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
            elif texto.endswith(("√", "%", "^")):
                for c in reversed(texto):
                    if c.endswith(("√", "%", "^")):
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
            if texto.endswith(("√", "%", "^")):
                for c in reversed(texto):
                    if c.endswith(("√", "%", "^")):
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
