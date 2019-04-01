def print_ladder(height):
    for x in range(height):
        for y in range(x):
            print("🔳", end="")
        print("")
