class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()


class Engine:
    def __init__(self, fuel_system):
        self.fuel_system = fuel_system

    def start(self):
        self.fuel_system.inject_fuel()
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class FuelSystem:
    def inject_fuel(self):
        print("Fuel injected")
