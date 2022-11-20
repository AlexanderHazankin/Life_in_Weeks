from time import sleep

print("Hi, lets check how much left till you will become 90 years old")
sleep(1)
age = int(input("What is your current age? "))
sleep(1)

months = (90 - age) * 12
weeks = (90 - age) * 52
days = (90 - age) * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
