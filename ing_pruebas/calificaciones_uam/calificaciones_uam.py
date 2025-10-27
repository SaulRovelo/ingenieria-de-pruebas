def calificacion(puntaje):
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