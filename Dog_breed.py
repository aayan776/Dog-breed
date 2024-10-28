class Dog:
    def __init__(self, breed, size, age):
        self.breed = breed
        self.size = size
        self.age = age
dog_breed = input("Enter the breed of your dog: ")
dog_size = input("Enter length of dog: ")
dog_age = input("How old is dog: ")
dog = Dog(dog_breed, dog_size, dog_age)
print(f"I have a {dog.breed}. They are {dog.age} years old. They are {dog.size} feet long.")