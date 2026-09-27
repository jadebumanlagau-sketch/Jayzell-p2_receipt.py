def average(g1, g2, g3):
    return (g1 + g2 + g3) / 3

def result(avg):
  if avg >= 90:
    return "Excellent"
  elif avg >= 80:
    return "Very Good"
  elif avg >= 75:
    return "Passed"
  else:
    return "Failed"
    
students = int(input("How many students? "))

while students < 3:
  print("Please enter at least 3 students.")
  students = int(input("How many students? "))
  
for i in range(students):
  name = input("Name: ")
  grade1 = float(input("Grade: "))
  grade2 = float(input("Grade: "))
  grade3 = float(input("Grade: "))

  avg = average(grade1, grade2, grade3)
  status = result(avg)
  
  print("average:", round(avg, 2))
  print("status:", status)
  print()
