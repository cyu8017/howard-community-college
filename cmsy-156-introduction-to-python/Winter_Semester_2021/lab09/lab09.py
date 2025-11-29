class Car:
    def __init__(self):
        # Initialize the car attributes with default values.
        self.__year = 2000
        self.__make = "Toyota"
        self.__model = "Camry"
        self.__speed = 0

    def setYear(self, year):
        # Set the car's year of manufacture.
        self.__year = year

    def getYear(self):
        # Get the car's year of manufacture.
        return self.__year

    def setMake(self, make):
        # Set the car's make (manufacturer).
        self.__make = make

    def getMake(self):
        # Get the car's make (manufacturer).
        return self.__make

    def setModel(self, model):
        # Set the car's model.
        self.__model = model

    def getModel(self):
        # Get the car's model.
        return self.__model

    def accelerate(self):
        # Accelerate the car's speed by 5 MPH, up to a maximum of 115 MPH.
        if self.__speed <= 115:
            self.__speed += 5
        else:
            # If the speed is already at its maximum, display a warning message.
            print("Warning: you cannot go faster than 120 MPH!!")

    def brake(self):
        # Decelerate the car's speed by 5 MPH, down to a minimum of 0 MPH.
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            print("Unable to brake, the vehicle is not moving!!")

    def getSpeed(self):
        # Get the car's current speed.
        return self.__speed

    def setSpeed(self, speed):
        # Set the car's speed to a specific value.
        self.__speed = speed


def test_case(car):
    """
    This function tests the behavior of the car object when accelerating and braking.

    :param car:
        (object): An instance of the car class to be tested.

    :return:
        None: The function only prints the results.
    """

    for i in range(1, 6):
        car.accelerate()  # Call the accelerate() method to increase the car's speed.
        print("The speed of the car after acceleration number", i, "is", car.getSpeed())

    for i in range(1, 6):
        car.brake()  # Call the brake() method to decrease the car's speed.
        print("The speed of the car after brake number", i, "is", car.getSpeed())


def main():
    """
    Main function
    """

    # First Test Case:
    obj1 = Car()
    print("\nTest Case 1\n")
    test_case(obj1)

    # Second Test Case:
    obj2 = Car()
    obj2.setSpeed(100)
    print("\nTest Case 2\n")
    test_case(obj2)

    # Third Test Case:
    obj3 = Car()
    obj3.setSpeed(-5)
    print("\nTest Case 3\n")
    test_case(obj3)


if __name__ == "__main__":
    main()
