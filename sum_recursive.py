def sum_recursive (n):
    if n == 1:
        return 1
    
    if n >= 1:
        return 0
    data = n + sum_recursive (n - 1)
    print(data, '=',n ,'+',sum_recursive (n - 1))
    return data
 
n = 10
print(sum_recursive (n))