




m1 = float(input("Enter marks1: "))
m2 = float(input("Enter marks2: "))
m3 = float(input("Enter marks3: "))

# Check if any marks are greater than 100 (invalid input)
if m1 > 100 or m2 > 100 or m3 > 100:
    print("Invalid input. Marks should be between 0 and 100.")
else:
    # Calculate the total percentage
    total_percentage = (m1 + m2 + m3) / 300 * 100

    # Check if the student has passed
    if total_percentage >= 40 and m1 >= 33 and m2 >= 33 and m3 >= 33:
        print("Pass with total percentage:", total_percentage)
    else:
        print("Fail with total percentage:", total_percentage)
