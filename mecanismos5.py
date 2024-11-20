# Clase base
class Vehicle:
    def calculate_travel_time(self, distance):
        raise NotImplementedError("Subclasses must implement this method")

# Clases derivadas
class Car(Vehicle):
    def calculate_travel_time(self, distance):
        speed = 60  # km/h
        time = distance / speed
        return f"Travel time by car: {time:.2f} hours"

class Bicycle(Vehicle):
    def calculate_travel_time(self, distance):
        speed = 15  # km/h
        time = distance / speed
        return f"Travel time by bicycle: {time:.2f} hours"

class Bus(Vehicle):
    def calculate_travel_time(self, distance):
        speed = 40  # km/h
        time = distance / speed
        return f"Travel time by bus: {time:.2f} hours"

# Lista de vehículos
vehicles = [
    Car(),
    Bicycle(),
    Bus()
]

# Procesar los tiempos de viaje usando polimorfismo
distance = 100  # Cambia la distancia según sea necesario
for vehicle in vehicles:
    print(vehicle.calculate_travel_time(distance))

