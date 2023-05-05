# pylint: disable=missing-docstring
def truck_tour(petrol_pumps):
    """
    Given a list of petrol pumps with the amount of petrol available and the
    distance to the next petrol pump, find the index of the starting petrol
    pump from where a truck can complete the full circle of the circular route.

    Args:
    - petrolpumps: A list of tuples representing petrol pumps, where each
    tuple contains two integers: the amount of petrol available at the petrol
    pump and the distance to the next petrol pump.

    Returns:
    - The index of the starting petrol pump from where a truck can complete
    the full circle of the circular route.
    """

    # Initialize the starting position and fuel to zero.
    position = fuel = 0

    # Loop through each petrol pump in the input list.
    for i, petrol_pump in enumerate(petrol_pumps):
        # Add the difference between the petrol available at
        # the current petrol pump and the distance
        # to the next petrol pump to the fuel variable.
        fuel += petrol_pump[0] - petrol_pump[1]

        # If the fuel is negative, set the starting position to the next petrol
        # pump and reset the fuel to zero.
        if fuel < 0:
            position = i + 1
            fuel = 0

    # Return the starting position from where the truck can complete the full circle.
    return position

