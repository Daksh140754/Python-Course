import math
trig_val = int(input("Enter your angle in degrees: "))
rad = math.radians(trig_val)
choice = math.sin(rad)
choice2 = math.cos(rad)
choice3 = math.tan(rad)

print(f"The Sine of {trig_val} is: {choice}")
print(f"The Cosine of {trig_val} is: {choice2}")
print(f"The Tangent of {trig_val} is: {choice3}")