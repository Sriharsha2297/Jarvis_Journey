# Advanced OOP
# n @staticmethod and @classmethod
# n @property and @setter
# n Practice: validate Robot speed > 0
# n Build BankAccount class
# n Properties with validation = axis travel limits.

from turtle import speed


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
    
    @staticmethod
    def validate_speed(speed):
        return 0 < speed <= 100          # check before creating robot

    @classmethod
    def from_string(cls, data):
        name, speed = data.split(",")
        return cls(name, int(speed))     # Robot.from_string("Fanuc,5")


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
c1.lift()           

cr = Cobot.from_string("UR10,3")
print(cr)    # Cobot(name=UR10, speed=3, payload=None


#build bank account class with properties and validation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # use _balance to indicate "private"

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative.")
        else:
            self._balance = amount

# Example usage
account = BankAccount("Alice", 1000)
print(account.owner)   # Output: Alice
print(account.balance) # Output: 1000



