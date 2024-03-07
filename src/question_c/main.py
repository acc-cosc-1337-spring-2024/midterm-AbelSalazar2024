#add import
#Q3

from question_c import sum_even

while True:
    num = input("Enter number to find sum of even and q to quit: ")
    if num == "q":
        break
    ans = sum_even(int(num))
    print("Total of the sum of even is", ans)


