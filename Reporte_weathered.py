import argparse  # permite manejar argumentos desde la terminal.
import requests  # se usa para hacer solicitudes HTTP (en este caso, para obtener datos del clima).
import json      # nos ayuda a manejar datos en formato JSON, convirtiéndolos a strings o dicts.

# Función para analizar los argumentos de línea de comandos.
def parse_arguments():
    parser = argparse.ArgumentParser(description="Consulta el clima de una ubicación.") # objeto ArgumentParser - describe el propósito del programa.
   
    # Añadimos un argumento posicional "location" que es obligatorio.
    parser.add_argument("location", type=str, help="Nombre de la ciudad y país (Ej: Asuncion,PY)") #indica la ciudad y país (ej: Asuncion,PY).
    
    # Añadimos un argumento opcional "--format" que permite elegir el formato de salida.
    parser.add_argument("--format", type=str, choices=["json", "csv", "text"], default="text", help="Formato de salida")
    
    # Retornamos los argumentos parseados como un objeto con las opciones especificadas.
    return parser.parse_args()

def get_weather_data(location):
    # Pedimos al usuario que ingrese la clave de API.
    # a78a404823a0451643de78634027cc2
    api_key = input("Por favor, ingrese su clave de API de OpenWeatherMap: ")
    
    # URL base de la API de OpenWeatherMap.
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Definimos los parámetros de la solicitud que se enviará a la API.
    params = {
        "q": location,          
        "appid": api_key,       
        "units": "metric",      
        "lang": "es"            
    }
    
    # Realizamos una solicitud GET a la API con los parámetros.
    response = requests.get(base_url, params=params)
    
    # Verificamos si la solicitud fue exitosa.
    if response.status_code == 200:
        return response.json()  # Si fue exitosa, devolvemos los datos JSON.
    else:
        return None             # Si hubo un error, devolvemos None.

def print_weather(data): # imprimir los datos del clima
    # Verificamos que los datos existan.
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

def print_as_json(data): # imprimir datos del clima.
    temp = round(data['main']['temp'], 2)
    feels_like = round(data['main']['feels_like'], 2)
    
    # Creamos un diccionario con la información del clima.
    data_to_print = {
        'ubicacion': data['name'],
        'temperatura': temp,
        'sensacion_termica': feels_like,
        'descripcion': data['weather'][0]['description'],
        'humedad': data['main']['humidity']
    }
    
    # Convertimos el diccionario a un string JSON y lo imprimimos con una indentación de 2.
    print(json.dumps(data_to_print, indent=2, ensure_ascii=False))

# Función principal que ejecuta el flujo del programa.
def main():
    # Analizamos los argumentos ingresados desde la línea de comandos.
    args = parse_arguments()
    
    try:
        # Obtenemos los datos del clima de la ubicación proporcionada.
        weather_data = get_weather_data(args.location)
        
        # Verificamos si los datos son None, en cuyo caso lanzamos un error.
        if weather_data is None:
            raise ValueError("No se ha encontrado la ubicación o la solicitud ha tenido un problema.")
        
        # Dependiendo del formato seleccionado, imprimimos los datos en JSON o texto.
        if args.format == "json":
            print_as_json(weather_data)
        else:
            print_weather(weather_data)
    
    # Capturamos errores específicos y mostramos un mensaje claro.
    except ValueError as ve:
        print(f"Error: {ve}")
    
    # Capturamos cualquier otro error inesperado y mostramos un mensaje genérico.
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

# Punto de entrada del programa. Ejecuta la función principal si el archivo se ejecuta directamente.
if __name__ == "__main__":
    main()
