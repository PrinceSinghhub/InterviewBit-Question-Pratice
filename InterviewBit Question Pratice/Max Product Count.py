"""

    Time Complexity: O(N ^ 2)
    Space Complexity: O(N ^ 2)

    Where N is the size of array.

"""


def maxProductCount(arr, n):
    # To store the product of two number as Key and value as the total number of occurrence.
    mapp = {}

    # To find all pair product and store it to dictionary with there frequencies.
    for i in range(n):
        for j in range(i + 1, n):
            a = arr[i]
            b = arr[j]
            pairproduct = a * b
            if pairproduct in mapp:
                mapp[pairproduct] += 1
            else:
                mapp[pairproduct] = 1

    # To store max product pair.
    maxProd = 0

    # To store frequency of max product.
    freq = 0

    # Traverse the Dictionary.
    for prod in mapp.keys():
        if mapp.get(prod) >= freq:
            # If frequency is same as previous max frequency then choose the one with minimum product.
            if mapp.get(prod) == freq:
                maxProd = min(maxProd, prod)
            else:
                maxProd = prod

            freq = mapp.get(prod)

    # List to store the values of max product and Quadruples.
    lst = []

    # If there is no pair having frequency count > 1.
    if (mapp.get(maxProd) == None or mapp.get(maxProd) == 1):
        # Returning the array containing max product and number of Quadruples.
        lst.append(0)
        lst.append(0)
        return lst
    else:
        # Calculating total Quadruples as all Combination a pair can have with given frequency.
        allCombinations = ((freq * (freq - 1))) // 2
        # Returning the pair of max product and number of Quadruples.
        lst.append(maxProd)
        lst.append(allCombinations)
        return lst