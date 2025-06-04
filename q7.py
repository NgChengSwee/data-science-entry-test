class Car:
    """
    A class representing a car.

    Attributes:
    - make (str): The brand of the car.
    - model (str): The specific model of the car.
    - year (int): The manufacturing year of the car.

    Methods:
    - describe_car(): Prints car details in "Year Make Model" format.
    """

    def __init__(self, make, model, year):
        # Initialize the car's make, model, and year attributes
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        # Print the car details in "Year Make Model" format
        print(f"{self.year} {self.make} {self.model}")

# Create an instance of class Car
my_car = Car("Toyota", "Corolla", 2020)

# Call the method describe_car to display the car details
my_car.describe_car()  # Expected output: 2020 Toyota Corolla
