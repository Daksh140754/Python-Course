def cube(number):
    return number*number*number
def div_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False
print(div_three(9))
print(div_three(5))