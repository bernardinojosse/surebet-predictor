def calcular_arbitraje(cuota_casa1, cuota_casa2):
    """
    Verifica la condición: (B - 1) * (A - 1) > 1
    donde B y A son las cuotas de cada casa.
    """
    condicion = (cuota_casa1 - 1) * (cuota_casa2 - 1)
    es_segura = condicion > 1
    return es_segura, condicion

def calcular_apuesta_ideal(total_a_invertir, cuota_casa1, cuota_casa2):
    """
    Calcula cuánto dinero poner en cada casa para 
    maximizar ganancias según la imagen.
    """
    # Proporción basada en el inverso de las cuotas
    inv_c1 = 1 / cuota_casa1
    inv_c2 = 1 / cuota_casa2
    prob_total = inv_c1 + inv_c2
    
    apuesta_c1 = (inv_c1 / prob_total) * total_a_invertir
    apuesta_c2 = (inv_c2 / prob_total) * total_a_invertir
    
    return round(apuesta_c1, 2), round(apuesta_c2, 2)
