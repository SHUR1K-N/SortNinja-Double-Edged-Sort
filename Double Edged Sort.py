import time

unsorted = []; sorted = []
decisionMade = False; correctInput = False
correctPath = False


def ascending(indexFirst, indexLast):

    small = min(unsorted); big = max(unsorted)

    for i in range(iterations):

        sorted.insert(indexFirst, small), sorted.insert(indexLast, big)
        unsorted.remove(small), unsorted.remove(big)

        if (len(unsorted) >= 1):
            small = min(unsorted); big = max(unsorted)
            indexFirst += 1; indexLast += 1

    if (len(unsorted) >= 1):
        sorted.insert(indexFirst, unsorted[0])


def descending(indexFirst, indexLast):

    small = min(unsorted); big = max(unsorted)

    for i in range(iterations):

        sorted.insert(indexFirst, big), sorted.insert(indexLast, small)
        unsorted.remove(big), unsorted.remove(small)

        if (len(unsorted) >= 1):
            small = min(unsorted); big = max(unsorted)
            indexFirst += 1; indexLast += 1

    if (len(unsorted) >= 1):
        sorted.insert(indexFirst, unsorted[0])


##### Main #####

if __name__ == "__main__":

    while (decisionMade is False):
        print("\nMethods:-")
        print("1. Manual entry of integers\n2. Supply a number list file")
        try:
            decision = int(input("\nSelect method number: "))
            if (decision == 1):
                while (correctInput is False):
                    try:
                        unsorted = list(map(int, input("\nInput integers to sort (separated by spaces): ").split()))
                    except ValueError:
                        print("\nInvalid character(s) entered. Input only integers. Try again.\n")
                        continue
                    correctInput = True

            elif (decision == 2):
                unsorted = []
                while (correctPath is False):
                    try:
                        filePath = input("\nEnter file path here: ")
                        with open(filePath, "r") as file:
                            for number in file:
                                unsorted.append(int(number))

                    except FileNotFoundError:
                        print("\nEither file does not exist or invalid path entered. Try again.\n")
                        continue
                    correctPath = True

        except:
            print("\nInvalid entry. Choose either option 1 or 2. Try again.\n")
            continue
        decisionMade = True

    iterations = (len(unsorted) // 2)
    indexFirst = 0
    indexLast = indexFirst + 1
    decisionMade = False

    print("\nOrder:-")
    print("1. Ascending\n2. Descending")
    while (decisionMade is False):
        try:
            ascdesc = int(input("\nSelect order number (Default = Ascending): ") or 1)
        except:
            print("\nInvalid entry. Choose either option 1 or 2. Try again.\n")
            continue
        decisionMade = True

    print("\nWorking...", end='')

    start = time.time()

    if (ascdesc == 1):
        ascending(indexFirst, indexLast)

    elif (ascdesc == 2):
        descending(indexFirst, indexLast)

    completionTime = time.time() - start

    print("\n\nSorted list: ", sorted)
    try:
        rate = iterations // completionTime
        print(f"\n\nThe task completed successfully in {completionTime} seconds. (at ~{rate} accesses/sec)")
        print("Press any key to exit.")
        input()
    except ZeroDivisionError:
        print("\n\nThe task completed successfully in zero seconds.")
        print("Press any key to exit.")
        input()
