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

    def __str__(self):
        return f"Robot(name={self.name}, speed={self.speed})"

# Example usage
if __name__ == "__main__":  
    r1 = Robot(input('Enter robot name: '), int(input('Enter robot speed: ')))
    print(r1.name)
    print(r1)
    print(r1.speed)
    r1.move(10)

