import time

unsorted = []; sorted = []; isEven = True
decisionMade = False; correctInput = False
correctPath = False


##### Odd functions #####

def ascendingOdd(indexFirst, indexLast):

    small = min(unsorted)
    big = max(unsorted)

    for i in range(iterations):

        sorted.insert(indexFirst, small)
        sorted.insert(indexLast, big)
        unsorted.remove(small)
        unsorted.remove(big)

        small = min(unsorted)
        big = max(unsorted)

        indexFirst += 1
        indexLast += 1
    sorted.insert(indexFirst, unsorted[0])
    return(sorted, iterations)


def descendingOdd(indexFirst, indexLast):

    small = min(unsorted)
    big = max(unsorted)

    for i in range(iterations):

        sorted.insert(indexFirst, big)
        sorted.insert(indexLast, small)
        unsorted.remove(big)
        unsorted.remove(small)

        small = min(unsorted)
        big = max(unsorted)

        indexFirst += 1
        indexLast += 1
    sorted.insert(indexFirst, unsorted[0])
    return(sorted, iterations)


##### Even functions #####

def ascendingEven(indexFirst, indexLast):

    small = min(unsorted)
    big = max(unsorted)

    for i in range(1, iterations):

        sorted.insert(indexFirst, small)
        sorted.insert(indexLast, big)
        unsorted.remove(small)
        unsorted.remove(big)

        small = min(unsorted)
        big = max(unsorted)

        indexFirst += 1
        indexLast += 1
    sorted.insert(indexFirst, small)
    sorted.insert(indexLast, big)
    return(sorted, iterations)


def descendingEven(indexFirst, indexLast):

    small = min(unsorted)
    big = max(unsorted)

    for i in range(1, iterations):

        sorted.insert(indexFirst, big)
        sorted.insert(indexLast, small)
        unsorted.remove(big)
        unsorted.remove(small)

        small = min(unsorted)
        big = max(unsorted)

        indexFirst += 1
        indexLast += 1
    sorted.insert(indexFirst, big)
    sorted.insert(indexLast, small)
    return(sorted, iterations)


def prompt():
    while (decisionMade is False):
        print("\nMethods:-")
        print("1. Manual entry of integers\n2. Supply a number list file")
        decision = input("\nSelect method number: ")
        if (decision == "1"):
            while (correctInput is False):
                try:
                    unsorted = list(map(int, input("\nInput integers to sort (separated by spaces): ").split()))
                    break
                except ValueError:
                    print("\nInvalid character(s) entered. Input only integers. Try again.\n")
                    continue
            break

        elif (decision == "2"):
            unsorted = []
            while (correctPath is False):
                try:
                    filePath = input("\nEnter the file path here: ")
                    with open(filePath) as file:
                        for num in file:
                            integerize = int(num)
                            unsorted.append(integerize)
                        file.close()
                    break

                except FileNotFoundError:
                    print("\nEither file does not exist or invalid path entered. Try again.\n")
                    continue
            break

        else:
            print("\nInvalid entry. Choose either option 1 or 2. Try again.\n")
            continue
    return (unsorted)


##### Main #####

unsorted = prompt()

iterations = (len(unsorted) // 2)
indexFirst = 0
indexLast = indexFirst + 1

if ((len(unsorted)) % 2 == 0):
    isEven = True
else:
    isEven = False

print("\nOrder:-")
print("1. Ascending\n2. Descending")
ascdesc = input("\nSelect order number (Default = Ascending): ") or "1"
ascdesc = ascdesc.lower()

print("\nWorking...", end='')

start = time.time()

if (ascdesc == "1"):
    small = min(unsorted)
    big = max(unsorted)
    if isEven is True:
        ascendingEven(indexFirst, indexLast)
    elif isEven is False:
        ascendingOdd(indexFirst, indexLast)

elif (ascdesc == "2"):
    small = max(unsorted)
    big = min(unsorted)
    if isEven is True:
        descendingEven(indexFirst, indexLast)
    elif isEven is False:
        descendingOdd(indexFirst, indexLast)

completionTime = time.time() - start

print("\n\nSorted list: ", sorted)
try:
    print("\n\nThe task completed successfully in %f seconds. (at ~%d accesses/sec)" % (completionTime, iterations // completionTime))
    print("Press any key to exit.")
    input()
except ZeroDivisionError:
    print("\n\nThe task completed successfully in zero seconds.")
    print("Press any key to exit.")
    input()
