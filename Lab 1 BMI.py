"""
Calculate User's BMI and provide interpretation.
Prompt for weight in pounds, feet and inches, output interpretation (weight under normal over obese)
Then, calculate BMI by dividing weight in pounds (lb) by height in inches (in) squared and multiplying by a conversion factor of 703.

IF INPUT IS STRING, TELL THEM TO DO IT AGAIN

weight 150
feeet 5
in 8
BMI 22.807
Normal

W 200
F5
I8
BMI 30
Obese

>>> "123".isalnum()
True
>>> "123a".isalnum()
True
>>> "123abc".isalnum()
True
>>> "123abc".isalpha()
False
>>> "123abc".isdigit()
False
>>> "123".isdigit()
True
>>> "123".isalpha()
False

or type(weight)==str
	
"""
while(1):
	print("Hello! Please enter information to determine your BMI.")
	while (1):
		weight = input("Enter your weight as a number of pounds: ")
		while (weight.isdigit()==False):
			weight=input("Enter your weight as a number of pounds with no letters: ")
		weight=float(weight)
		if weight>1400:
			print("Have you broken the all-time record for heaviest adult human? The heaviest person documented in human history was an American man by the name of Jon Brower Minnoch (September 29, 1941 – September 10, 1983) who weighed 1400 pounds. Please enter a lower weight in pounds.")
		elif weight<4.7:
			print("Have you broken the all-time record for lightest adult human? The lightest adult human documented in human history was Lucia Zarate, who was afflicted with Majewski osteodysplastic primordial dwarfism type II and weighed 4.7 pounds at the age of 17. Please enter a higher weight in pounds.")
		else:
			break
	
	while (1):
		height = input("Enter your height in feet, please round down to the nearest foot: ")
		while (height.isdigit()==False):
			height=input("Enter your height as a number of feet with no letters: ")
		height=float(height)
		if height>8:
			print("Have you broken the all-time record for tallest adult human? The tallest person documented in human history was an American man by the name of Robert Wadlow (1941 – 1983) who was 8 feet and 11 inches tall. Please enter a lower height in feet.")
		elif height<1:
			print("Have you broken the all-time record for shortest adult human? The shortest adult human documented in human history was Chandra Bahadur Dangi who was 1 foot and 9.51 inches tall. Please enter a higher height in feet: ")
		else:
			break
	
	while (1):
		inches = input("Enter the remainder of your height in inches: ")
		while (inches.isdigit()==False):
			inches=input("Enter the remainder of your height as a number of inches with no letters: ")
		inches=float(inches)
		if (inches>11 or inches<0):
			print("Please enter a valid number for the remainder of your height in inches.")
		else:
			break
	
	height=(height*12 + inches)**2
	#print("Height inches squared: ", height)
	BMI=(weight/height)*703
	print("Resulting BMI is: ", BMI)
	if BMI<18.5:
		print("You are underweight.")
	if BMI>=18.5 and BMI<25:
		print("You are a healthy weight.")
	if BMI>=25 and BMI<30:
		print("You are overweight.") 
	if BMI>=30 and BMI<35:
		print("You are Class 1 obese.")
	if BMI>=35 and BMI<40:
		print("You are Class 2 obese.")
	if BMI>=40:
		print("You are Class 3 obese.")
	print("\n")
