def truckTour(petrolpumps):
    """
    Given a list of petrol pumps with the amount of petrol available and the distance to the next petrol pump,
    find the index of the starting petrol pump from where a truck can complete the full circle of the circular route.

    Args:
    - petrolpumps: A list of tuples representing petrol pumps, where each tuple contains two integers:
      the amount of petrol available at the petrol pump and the distance to the next petrol pump.

    Returns:
    - The index of the starting petrol pump from where a truck can complete the full circle of the circular route.
    """

    # Initialize the starting position and fuel to zero.
    position = fuel = 0

    # Loop through each petrol pump in the input list.
    for i in range(len(petrolpumps)):

        # Add the difference between the petrol available at the current petrol pump and the distance
        # to the next petrol pump to the fuel variable.
        fuel += petrolpumps[i][0] - petrolpumps[i][1]

        # If the fuel is negative, set the starting position to the next petrol pump and reset the fuel to zero.
        if fuel < 0:
            position = i + 1
            fuel = 0

    # Return the starting position from where the truck can complete the full circle.
    return position


if __name__ == '__main__':
    # Read the number of petrol pumps from the input.
    n = int(input().strip())

    # Initialize an empty list to store the petrol pumps.
    petrolpumps = []

    # Read the petrol pumps from the input and append them to the list.
    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    # Call the truckTour function to find the index of the starting petrol pump.
    result = truckTour(petrolpumps)