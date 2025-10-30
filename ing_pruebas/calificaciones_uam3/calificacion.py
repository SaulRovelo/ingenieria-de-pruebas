def calificacion_uam(puntaje):

    #Excepcion de tipo valor
    if not (0 <= puntaje <= 10):
        raise ValueError(f"El puntaje debe estar entre 0 y 10, se recibió: {puntaje}")
    
    #excepcion de tipo tipo
    if not isinstance(puntaje, (int, float)):
        raise TypeError(f"El puntaje debe ser un número, se recibió: {type(puntaje).__name__}")

    if 9 <= puntaje <= 10:
        return "A"
    elif 7.5 <= puntaje < 9:
        return "B"
    elif 6 <= puntaje < 7.5:
        return "S"
    elif 0 <= puntaje < 6:
        return "NA"
    else:
        return f"Puntaje inválido: {puntaje}"

