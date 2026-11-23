
num = int(input("Enter a sweet number: "))
is_negative = num < 0
num = abs(num)
reversed_num = 0
while num > 0:
    digit = num % 10                      
    reversed_num = (reversed_num * 10) + digit  
    num = num // 10                       
if is_negative:
    reversed_num = -reversed_num
print("Your Sweet Reversed Number :", reversed_num)
