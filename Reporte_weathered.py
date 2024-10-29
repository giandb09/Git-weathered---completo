import argparse
import requests
import json


def parse_arguments():
    parser = argparse.ArgumentParser(description="Consulta el clima de una ubicación.")
    parser.add_argument("location", type=str, help="Nombre de la ciudad y país (Ej: Asuncion,PY)")
    parser.add_argument("--format", type=str, choices=["json", "csv", "text"], default="text", help="Formato de salida")
    return parser.parse_args()

def get_weather_data(location):
    api_key = "a78a404823a0451643de78634027cc2e" 
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": api_key, "units": "metric", "lang": "es"}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def print_weather(data):
    if data:
        temp = round(data['main']['temp'], 2)
        feels_like = round(data['main']['feels_like'], 2)
        location = data['name']
        description = data['weather'][0]['description']
        
        print(f"Clima en {location}:")
        print(f"Temperatura: {temp}°C")
        print(f"Sensación térmica: {feels_like}°C")
        print(f"Condiciones: {description}")
        print(f"Humedad: {data['main']['humidity']}%")

def print_as_json(data):
    temp = round(data['main']['temp'], 2)
    feels_like = round(data['main']['feels_like'], 2)
    
    data_to_print = {
        'ubicacion': data['name'],
        'temperatura': temp,
        'sensacion_termica': feels_like,
        'descripcion': data['weather'][0]['description'],
        'humedad': data['main']['humidity']
    }
    print(json.dumps(data_to_print, indent=2, ensure_ascii=False))

def main():
    args = parse_arguments()
    
    try:
        weather_data = get_weather_data(args.location)
        
        if weather_data is None:
            raise ValueError("No se ha encontrado la ubicación o la solicitud ha tenido un problema.")
        
        if args.format == "json":
            print_as_json(weather_data)
        else:
            print_weather(weather_data)
    
    except ValueError as ve:
        print(f"Error: {ve}")
    
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")


if __name__ == "__main__":
    main()