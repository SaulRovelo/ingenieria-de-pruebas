def calificacion(puntaje):
    # Verificar tipo
    if not isinstance(puntaje, (int, float)):
        raise TypeError(f"El puntaje debe ser numérico (int o float), se recibió {type(puntaje).__name__}")

    # Verificar rango
    if 0 <= puntaje <= 10:
        if 9 <= puntaje <= 10:
            return "A"
        elif 7.5 <= puntaje < 9:
            return "B"
        elif 6 <= puntaje < 7.5:
            return "S"
        else:
            return "NA"
    else:
        # Lanzar excepción si el valor está fuera del rango
        raise ValueError(f"El puntaje debe estar entre 0 y 10, se recibió {puntaje}")
