datos = list()
operadores = list()


def Presionar(text):

    global datos

    if datos.len() == 0:

        text += "√"
        operadores.append("√")

    return text
