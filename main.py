from logic import calcular_arbitraje, calcular_apuesta_ideal

# Datos de prueba (Basados en tu Ejemplo 1 de la imagen: Nadal)
c1 = 2.22  # Casa 1 paga 2.22 si gana
c2 = 1.95  # Casa 2 paga 1.95 si pierde (o gana el rival)
inversion = 100

es_segura, valor = calcular_arbitraje(c1, c2)

if es_segura:
    a1, a2 = calcular_apuesta_ideal(inversion, c1, c2)
    print(f"✅ ¡Apuesta Segura Detectada! (Factor: {valor:.2f})")
    print(f"💰 Invierte ${a1} en Casa 1 y ${a2} en Casa 2")
    print(f"📈 Ganancia garantizada: ${round((a1 * c1) - inversion, 2)}")
else:
    print(f"❌ No hay arbitraje. Factor: {valor:.2f} (Debe ser > 1)")
