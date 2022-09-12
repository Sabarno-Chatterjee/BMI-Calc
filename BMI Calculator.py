# 🚨 Don't change the code below 👇
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
h= float(height)
w= float(weight)
bmi= w / (h * h)
new= int(bmi)
print(f"Your Body Mass Index is {new}")
