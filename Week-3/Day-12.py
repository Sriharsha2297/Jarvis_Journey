# Inheritance & Special Methods
# n class Cobot(Robot): inherits from Robot
# n __str__: controls print(robot)
# n super().__init__() — call parent constructor
# n Practice: Vehicle, Car, Truck inheritance
# n Inheritance = base PLC template with variants.

class Robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self, distance):
        time = distance / self.speed
        print(f"{self.name} will take {time:.2f} hours to move {distance} units.")

    def __str__(self):
        return f"Robot(name={self.name}, speed={self.speed})"

class Cobot(Robot):
    def __init__(self, name, speed, payload):
        super().__init__(name, speed)   # call parent __init__
        self.payload = payload          # new attribute

    def lift(self):
        print(f"{self.name} is lifting {self.payload}kg safely.")

    def __str__(self):                  # override __str__
        return f"Cobot(name={self.name}, speed={self.speed}, payload={self.payload})"


# --- Using imported Robot ---
r1 = Robot(input('Enter robot name: '), int(input('Enter robot speed: ')))
print(r1.name)
print(r1)
print(r1.speed)
r1.move(10)

print("---")

# --- Using Cobot subclass ---
c1 = Cobot(input('Enter cobot name: '), int(input('Enter cobot speed: ')), int(input('Enter cobot payload: ')))
print(c1)           # Cobot(name=UR10, speed=3, payload=10)
c1.move(10)         # inherited from Robot ✅
c1.lift()           # Cobot-specific method ✅

