def calcular_arbitraje(cuota_a, cuota_b):
    """
    Verifica la condición matemática: (a - 1) * (b - 1) > 1
    """
    if cuota_a <= 1 or cuota_b <= 1:
        return False, 0
    
    factor = (cuota_a - 1) * (cuota_b - 1)
    es_segura = factor > 1
    return es_segura, factor

def calcular_apuesta_ideal(total_inversion, cuota_a, cuota_b):
    """
    Calcula la distribución de capital para asegurar el mismo retorno.
    """
    inv_a = 1 / cuota_a
    inv_b = 1 / cuota_b
    prob_total = inv_a + inv_b
    
    apuesta_a = (inv_a / prob_total) * total_inversion
    apuesta_b = (inv_b / prob_total) * total_inversion
    
    return round(apuesta_a, 2), round(apuesta_b, 2)
