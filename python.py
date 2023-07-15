# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# we are using zero-indexing for the series

def fib(n):
    new_list = list([0, 1])

    for i in range(2, n+1):
        # print(i, new_list[i-2], new_list[i-1])
        new_list.append(new_list[i-2] + new_list[i-1])
    return(new_list[n]) 

print(fib(8))