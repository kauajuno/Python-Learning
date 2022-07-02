# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
store = 0
cont = 0
for height in student_heights:
    store += height
    cont += 1

store /= cont
print(round(store))





