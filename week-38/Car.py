'''
Create a Python class Car that represents a car. 
The car should be initialized with its make, model, and year of manufacture. 
The class should have the following methods:

get_details(): 
    This method should return a string representing 
    the details of the car in the format “make model (year)”.
set_details(new_make, new_model, new_year): 
    This method should set new details for the car.
age(): 
    This method should calculate and return the 
    age of the car based on the current year. 
    Assume the current year is 2023.
    To test your implementation, 
    create a Car object with make “Toyota”, model “Corolla”, and year 2015. 
    Update the details to make “Honda”, model “Civic”, and year 2018, 
    and then calculate and print the age of the car.
'''

from datetime import date

class Car:
    this_year = date.today().year
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        
    def get_details(self):
        return f'{self.make} {self.model} ({self.year})'
    
    def set_details(self, new_make, new_model, new_year):
        self.make = new_make
        self.model = new_model
        self.year = new_year
        
    def age(self):
        return self.this_year - self.year
        
def test():
    myCar = Car("Toyota", "Corolla", 2015)
    print(myCar.get_details())
    
    myCar.set_details("Honda", "Civic", 2018)
    
    print(myCar.get_details())
    print(myCar.age(), "years")
    
if __name__ == "__main__":
    test()
    

    
