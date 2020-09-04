#Authour Matt Amponsah mma6356@psu.edu
gp1 = input("Enter your course 1 letter grade: ")

credit1 = float(input("Enter your course 1 credit: "))

if gp1 == 'A': gp1 = float(4.0)
elif gp1 == 'A-': gp1 = float(3.67)
elif gp1 == 'B+': gp1 = float(3.33)
elif gp1 == 'B': gp1 = float(3.0)
elif gp1 == 'B-': gp1 = float(2.67)
elif gp1 == 'C+': gp1 = float(2.33)
elif gp1 == 'C': gp1 = float(2.0)
elif gp1 == 'D': gp1 = float(1.0)
elif gp1 == 'F': gp1 = float(0.0)
else: print(f"Grade point for course 1 is: {0.0}")

fgp1 = ((gp1 * credit1) / credit1)

print(f"Grade point for course 1 is: {fgp1}")

gp2 = input("Enter your course 2 letter grade: ")

credit2 = float(input("Enter your course 2 credit: "))

if gp2 == 'A': gp2 = float(4.0)
elif gp2 == 'A-': gp2 = float(3.67)
elif gp2 == 'B+': gp2 = float(3.33)
elif gp2 == 'B': gp2 = float(3.0)
elif gp2 == 'B-': gp2 = float(2.67)
elif gp2 == 'C+': gp2 = float(2.33)
elif gp2 == 'C': gp2 = float(2.0)
elif gp2 == 'D': gp2 = float(1.0)
elif gp2 == 'F': gp2 = float(0.0)
else: print(f"Grade point for course 2 is: {0.0}")

fgp2 = (gp2 * credit2) / credit2

print(f"Grade point for course 2 is: {fgp2}")

gp3 = input("Enter your course 3 letter grade: ")

credit3 = float(input("Enter your course 3 credit: "))

if gp3 == 'A': gp3 = float(4.0)
elif gp3 == 'A-': gp3 = float(3.67)
elif gp3 == 'B+': gp3 = float(3.33)
elif gp3 == 'B': gp3 = float(3.0)
elif gp3 == 'B-': gp3 = float(2.67)
elif gp3 == 'C+': gp3 = float(2.33)
elif gp3 == 'C': gp3 = float(2.0)
elif gp3 == 'D': gp3 = float(1.0)
elif gp3 == 'F': gp3 = float(0.0)
else: print(f"Grade point for course 3 is: {0.0}")

fgp3 = (gp3 * credit3) / credit3

print(f"Grade point for course 3 is: {fgp3}")

GPA = (gp1 * credit1 + gp2 * credit2 + gp3 * credit3) / (
    credit1 + credit2 + credit3)

print(f"Your GPA is: {GPA}")
