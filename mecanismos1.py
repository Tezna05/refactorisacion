# Funciones auxiliares para procesar diferentes tipos de datos

def process_string(data):
    print(f"Processing string: {data}")

def process_integer(data):
    print(f"Processing integer: {data}")

def process_list(data):
    print("Processing list:")
    for item in data:
        print(f" - {item}")

# Función principal para procesar el tipo de datos usando un diccionario de procesadores

def process_data(data):
    processors = {
        str: process_string,  # Si el tipo es string, usa process_string
        int: process_integer,  # Si el tipo es integer, usa process_integer
        list: process_list     # Si el tipo es list, usa process_list
    }
    
    # Obtener el procesador correspondiente o una función por defecto si el tipo no es reconocido
    processor = processors.get(type(data), lambda x: print("Unknown data type!"))
    
    # Ejecutar el procesador correspondiente
    processor(data)

# Ejemplos de uso

process_data("Hello")  # Procesando una cadena
process_data(123)      # Procesando un entero
process_data([1, 2, 3])  # Procesando una lista

# Ejemplo de un tipo de dato no soportado
process_data(3.14)  # Salida: Unknown data type!
