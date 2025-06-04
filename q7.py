class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """

    def __init__(self, make, model, year):
        # Initialize the car's make, model, and year attributes
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        # Print the car details in "Year Make Model" format
        print(f"{self.year} {self.make} {self.model}")


# Create an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Call the describe_car method to display the car details
my_car.describe_car()  # Output: 2020 Toyota Corolla
