def algoritmoFichero(linea):

    datos = []
    elemento = ""

    for i in range(len(linea)):
        if(linea[i] != " "):
            elemento += str(linea[i])
        else:
            datos.append(int(elemento))
            elemento = ""

    datos.append(int(elemento))

    return datos