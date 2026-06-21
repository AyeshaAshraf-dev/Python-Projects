from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,model_name,weight,horsepower):
        self.model_name = model_name
        self._weight = weight
        self.horsepower = horsepower
        self._is_running = False
        self._current_speed = 0.0

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, new_speed):
        # This prevents the speed from ever going below 0.0
        self._current_speed = max(0.0, new_speed)

    def start(self):
        pass
    def calculating_accelration(self):
        pass
    def apply_breaking(self,brake_value):
        pass

class car(Vehicle):
    def start(self):
        self._is_running = True
        print(f"Vroom! {self.model_name} Engine Started! ")

    def calculating_accelration(self):
        accelration =  (self.horsepower/self._weight)*10
        print(f"The accelration of {self.model_name} is {accelration:.2f} m/s2")

    def apply_breaking(self,brake_value,):
        existing_speed = self.current_speed
        calculated_speed = existing_speed - brake_value
        self.current_speed = calculated_speed
        print(f"Brakes applied by {brake_value}. Current speed is now: {self.current_speed} km/h")
    


obj1 = car("Mehran E3234", 7086,433)
obj1.start()
obj1.calculating_accelration()
obj1.apply_breaking(43)