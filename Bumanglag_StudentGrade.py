#Student Credentials
name = input("Enter your full name: ")
section = input("Enter your section: ")

#Grade Input and Input Error Handling
prelim = float(input("Enter your Preliminary Period Grade: "))
midterm = float(input("Enter your Midterm Period Grade: "))
finals = float(input("Enter your Final Period Grade: "))

if (prelim < 40 or midterm < 40 or finals < 40 or prelim > 100 or midterm > 100 or finals > 100):
    print("Error: Grade input must be only between 40 and 100")
    
else:
    final_grade = float(prelim*0.33) + (midterm*0.33) + (finals*0.33)

#Final Grade, GWA, and Description
    if final_grade >= 99 and final_grade <= 100:
        print(f"{name} | {section}")
        print(f"Final Grade: {final_grade:.0f}")
        print("GWA: 1.00 | Excellent")
        
    elif final_grade >= 96 and final_grade <= 98:
        print(f"{name} | {section}")
        print(f"Final Grade: {final_grade:.0f}")
        print("GWA: 1.25 | Outstanding")
      
    elif final_grade >= 93 and final_grade <= 95:
        print(f"{name} | {section}")
        print(f"Final Grade: {final_grade:.0f}")
        print("GWA: 1.50 | Superior")
        
    elif final_grade >= 90 and final_grade <= 92:
        print(f"{name} | {section}")
        print(f"Final Grade: {final_grade:.0f}")
        print("GWA: 1.75 | Very Good")
        
    elif final_grade >= 87 and final_grade <= 89:
        print(f"{name} | {section}")
        print(f"Final Grade: {final_grade:.0f}")
        print("GWA: 2.00 | Good")
        
    elif final_grade >= 84 and final_grade <= 86:
        print(f"{name} | {section}")
        print(f"Final Grade: {final_grade:.0f}")
        print("GWA: 2.25 | Satisfactory")
        
    elif final_grade >= 81 and final_grade <= 83:
        print(f"{name} | {section}")
        print(f"Final Grade: {final_grade:.0f}")
        print("GWA: 2.50 | Fairly Satisfactory")
        
    elif final_grade >= 78 and final_grade <= 80:
        print(f"{name} | {section}")
        print(f"Final Grade: {final_grade:.0f}")
        print("GWA: 2.75 | Fair")
        
    elif final_grade >= 75 and final_grade <= 77:
        print(f"{name} | {section}")
        print(f"Final Grade: {final_grade:.0f}")
        print("GWA: 3.00 | Passed")
        
    elif final_grade < 75:
        print(f"{name} | {section}")
        print(f"Final Grade: {final_grade:.0f}")
        print("GWA: 5.0 | Failed")