# Base class
class Vehicle:
    def move(self):
        pass

# Subclass 1
class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road!")

# Subclass 2
class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky!")

# Subclass 3
class Boat(Vehicle):
  def move(self):
    print("Row your boat in the dam!")
