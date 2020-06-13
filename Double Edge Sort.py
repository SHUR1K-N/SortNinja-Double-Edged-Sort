array = []; sorted = []; isEven = True


##### Odd functions #####

def ascendingOdd():
    if isEven is False:

        iterations = (len(array) // 2)
        indexfirst = 0
        indexlast = indexfirst + 1

        small = min(array)
        big = max(array)

        for i in range(iterations):

            sorted.insert(indexfirst, small)
            sorted.insert(indexlast, big)
            array.remove(small)
            array.remove(big)

            small = min(array)
            big = max(array)

            indexfirst += 1
            indexlast += 1
        sorted.insert(indexfirst, array[0])
    return(sorted)


def descendingOdd():
    if isEven is False:

        iterations = (len(array) // 2)
        indexfirst = 0
        indexlast = indexfirst + 1

        small = min(array)
        big = max(array)

        for i in range(iterations):

            sorted.insert(indexfirst, big)
            sorted.insert(indexlast, small)
            array.remove(big)
            array.remove(small)

            small = min(array)
            big = max(array)

            indexfirst += 1
            indexlast += 1
        sorted.insert(indexfirst, array[0])
    return(sorted)


##### Even functions #####

def ascendingEven():
    if isEven is True:

        iterations = (len(array) // 2)
        indexfirst = 0
        indexlast = indexfirst + 1

        small = min(array)
        big = max(array)

        for i in range(1, iterations):

            sorted.insert(indexfirst, small)
            sorted.insert(indexlast, big)
            array.remove(small)
            array.remove(big)

            small = min(array)
            big = max(array)

            indexfirst += 1
            indexlast += 1
        sorted.insert(indexfirst, small)
        sorted.insert(indexlast, big)
    return(sorted)


def descendingEven():
    if isEven is True:

        iterations = (len(array) // 2)
        indexfirst = 0
        indexlast = indexfirst + 1

        small = min(array)
        big = max(array)

        for i in range(1, iterations):

            sorted.insert(indexfirst, big)
            sorted.insert(indexlast, small)
            array.remove(big)
            array.remove(small)

            small = min(array)
            big = max(array)

            indexfirst += 1
            indexlast += 1
        sorted.insert(indexfirst, big)
        sorted.insert(indexlast, small)
    return(sorted)


##### Main #####

array = list(map(int, input("Input integers to sort (separated by spaces): ").split()))

if ((len(array)) % 2 == 0):
    isEven = True
else:
    isEven = False

ascdesc = input("\nAscending or Descending? ")
ascdesc = ascdesc.lower()

if (ascdesc == "ascending"):
    small = min(array)
    big = max(array)
    if isEven is True:
        ascendingEven()
    elif isEven is False:
        ascendingOdd()

elif (ascdesc == "descending"):
    small = max(array)
    big = min(array)
    if isEven is True:
        descendingEven()
    elif isEven is False:
        descendingOdd()

print("\nSorted array: ", sorted)
print("\n\nPress any key to exit.")
input()
