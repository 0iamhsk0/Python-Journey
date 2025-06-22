def prefixsum(arr):
    n = len(arr)
    prefix_arr = [0] * n
    
    prefix_arr[0] = arr[0]

    for i in range(1, n):
        prefix_arr[i] = prefix_arr[i-1] + arr[i]
    
    return prefix_arr





if __name__ == '__main__':
    x = [1,2,3,4,5]
    totalsum = prefixsum(x)
    for i in totalsum:
        print(i, end = " ")

