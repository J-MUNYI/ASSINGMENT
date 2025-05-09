class Dog:
    def __init__(self, name, breed, age):
        self.name = name           
        self.breed = breed         
        self.__age = age           
    def bark(self):
        print(f"{self.name} says: Woo!")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive!")

    def info(self):
        print(f"Name: {self.name}, Breed: {self.breed}, Age: {self.__age}")


# Subclass (inheritance + polymorphism)
class GuideDog(Dog):
    def __init__(self, name, breed, age, trained):
        super().__init__(name, breed, age)
        self.trained = trained

    # Polymorphism: override the bark method
    def bark(self):
        print(f"{self.name} says: Woo! I am trained to guide my owner.")

    def guide(self):
        if self.trained:
            print(f"{self.name} is guiding their owner safely.")
        else:
            print(f"{self.name} is not trained yet.")


# Creating Dog object
dog1 = Dog("Cookie", "Mane", 3)
dog1.bark()
dog1.info()
dog1.set_age(4)
print("Updated age:", dog1.get_age())
print()

# Creating GuideDog object
guide_dog = GuideDog("Max", "Golden Retriever", 5, True)
guide_dog.bark()  
guide_dog.info()
guide_dog.guide()
