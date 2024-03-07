#write functions here, don't add input('') statements here!
#Q3

def sum_even(num):
    sum = 0
    for i in range(0, num+1):
        if i % 2 == 0:
            sum = sum + i
    return sum