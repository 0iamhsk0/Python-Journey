def hashing(arr, n):
    mp = {}
    for i in range(n):
        if arr[i] in mp:
            # If element is present, increment by one
            mp[arr[i]] += 1
        else:
            # If not present, store the value as 1
            mp[arr[i]] = 1
    # Printing the values of the dictionary
    for x in mp:
        print(x, mp[x])


if __name__ == '__main__':
    arr = [10, 5, 10, 15, 10, 5]
    n = len(arr)
    hashing(arr, n)
