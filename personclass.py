class Person:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def introduce(self):
    print(f"Hello! My name is {self.name}. I am {self.age} years old and I identify as {self.gender}.")

# Create an instance of Person
person1 = Person("Alice", 30, "female")

# Call the introduce method
person1.introduce()
