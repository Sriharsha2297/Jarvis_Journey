# Classes & Objects
# n class Robot: def __init__(self, name, speed):
# n self refers to the specific instance
# n r1 = Robot('Fanuc', 5)
# n r1.name | r1.speed
# n Add methods: def move(self, distance):


class Robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self, distance):
        time = distance / self.speed
        print(f"{self.name} will take {time:.2f} hours to move {distance} units.")

# Create an instance of Robot
r1 = Robot(input('Enter robot name: '), int(input('Enter robot speed: ')))
# Access attributes
print(r1.name)  # Output: Fanuc
print(r1.speed)  # Output: 5
# Call the move method
r1.move(10)  # Output: Fanuc will take 2.00 hours to move 10 units.

