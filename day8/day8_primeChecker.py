# Write your code below this line ๐
def prime_checker(number):
    for i in range(2, number):
        if number % i == 0:
            print("Not prime")
            return
    print("Prime")
    return

# Write your code above this line ๐
# Do NOT change any of the code below๐


n = int(input("Check this number: "))
prime_checker(number=n)



