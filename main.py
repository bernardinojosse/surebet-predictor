import os
import requests
from logic import calcular_arbitraje, calcular_apuesta_ideal

# Configuración mediante Variables de Entorno (Secrets)
API_KEY = os.getenv('ODDS_API_KEY')
DEPORTE = 'upcoming'  # Analiza todos los deportes próximos
REGIONES = 'us,eu'    # Incluye casas de apuestas de América y Europa
INVERSION_TEST = 1000 # Capital de ejemplo

def buscar_surebets():
    if not API_KEY:
        print("❌ ERROR: No se detectó la ODDS_API_KEY en los Secrets de GitHub.")
        return

    # URL de la API para obtener momios (Odds)
    url = f'https://api.the-odds-api.com/v4/sports/{DEPORTE}/odds/'
    params = {
        'apiKey': API_KEY,
        'regions': REGIONES,
        'markets': 'h2h',
        'oddsFormat': 'decimal'
    }

    try:
        print(f"📡 Conectando con The Odds API...")
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            print(f"❌ Error en la API: {response.status_code}")
            return

        eventos = response.json()
        print(f"🔍 Analizando {len(eventos)} eventos deportivos en busca de arbitraje...\n")

        for evento in eventos:
            home = evento['home_team']
            away = evento['away_team']
            
            mejor_c_home = 0
            mejor_c_away = 0
            casa_h, casa_a = "", ""

            # Buscamos la mejor cuota para cada lado entre todas las casas
            for bookie in evento.get('bookmakers', []):
                for market in bookie.get('markets', []):
                    if market['key'] == 'h2h':
                        for outcome in market['outcomes']:
                            if outcome['name'] == home and outcome['price'] > mejor_c_home:
                                mejor_c_home = outcome['price']
                                casa_h = bookie['title']
                            elif outcome['name'] == away and outcome['price'] > mejor_c_away:
                                mejor_c_away = outcome['price']
                                casa_a = bookie['title']

            # Validamos con la lógica matemática
            es_segura, factor = calcular_arbitraje(mejor_c_home, mejor_c_away)

            if es_segura:
                apuesta_h, apuesta_a = calcular_apuesta_ideal(INVERSION_TEST, mejor_c_home, mejor_c_away)
                ganancia = round((apuesta_h * mejor_c_home) - INVERSION_TEST, 2)
                
                print(f"✅ ¡SUREBET ENCONTRADA! ({home} vs {away})")
                print(f"👉 Apostar ${apuesta_h} en {casa_h} ({mejor_c_home})")
                print(f"👉 Apostar ${apuesta_a} en {casa_a} ({mejor_c_away})")
                print(f"📈 Ganancia asegurada: ${ganancia} (Factor: {round(factor, 4)})\n")

    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    buscar_surebets()
