from random import randint

# This function is the heart of our code
def main():
    print cube_lln(10)
    print cube_lln(10000)
    print cube_lln(10000000)

# Simulates a cube throw
def cube():
    return randint(1, 6)

# Executing a Law of Large Numbers test
def cube_lln(throws_count):
    print "Testing {} throws:".format(throws_count)

    # Creating a storage for keeping count.
    # Every number starts from 0.
    count = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0 }

    # Do the following "throws_count" times
    for i in range(throws_count):
        # "Throw" a cube
        number = cube()
        # Keep count
        count[number] += 1

    # Return the counter
    return count


if __name__ == "__main__":
    main()