# Mini Project — Robot Fleet Manager
# n Robot class: name, model, speed, status
# n Fleet class: manages list of Robots
# n Methods: add_robot, get_active, get_fastest
# n Save fleet to JSON
# n CLI menu
# n This should feel like managing your shop floor.

class Robot:
    def __init__(self, name, model, speed, status):
        self.name = name
        self.model = model
        self.speed = speed
        self.status = status

    def __str__(self):
        return f"Robot(name={self.name}, model={self.model}, speed={self.speed}, status={self.status})"
    
class Fleet:
    def __init__(self):
        self.robots = []

    def add_robot(self, robot):
        self.robots.append(robot)

    def get_active(self):
        return [r for r in self.robots if r.status == 'active']

    def get_fastest(self):
        return max(self.robots, key=lambda r: r.speed)

# Save fleet to JSON
    def save_to_json(self, filename):
        import json
        with open(filename, 'w') as f:
            json.dump([r.__dict__ for r in self.robots], f, indent=4)  

# Example usage
fleet = Fleet() 
fleet.add_robot(Robot("R1", "ModelA", 5, "active"))
fleet.add_robot(Robot("R2", "ModelB", 3, "inactive"))  

# CLI menu
def menu():
    print("1. Add Robot")
    print("2. Show Active Robots")
    print("3. Show Fastest Robot")
    print("4. Save Fleet to JSON")
    print("5. Exit")

    choice = input("Enter your choice: ")
    return choice



if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == '1':
            name = input("Enter robot name: ")
            model = input("Enter robot model: ")
            speed = int(input("Enter robot speed: "))
            status = input("Enter robot status (active/inactive): ")
            fleet.add_robot(Robot(name, model, speed, status))
        elif choice == '2':
            print("Active Robots:")
            for r in fleet.get_active():
                print(r)
        elif choice == '3':
            print("\nFastest Robot:")
            print(fleet.get_fastest())
        elif choice == '4':
            fleet.save_to_json("fleet_data.json")
        elif choice == '5':
            break
