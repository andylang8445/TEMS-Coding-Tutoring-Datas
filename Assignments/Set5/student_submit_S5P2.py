def decToBin(dec):
    if dec < 2:
        return str(dec)
    return decToBin(dec//2) + str((dec % 2))