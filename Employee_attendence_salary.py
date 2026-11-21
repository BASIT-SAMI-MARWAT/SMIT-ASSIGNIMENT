employees = {
"Ali": 26,
"Sara": 23,
"Ahmed": 18,
"Ayesha": 30
}

full_salary = 30000

def calculate_salary(days):

   if days == 26:
      monthly_salary = full_salary
      return monthly_salary
   elif days >= 20 and days <= 25:
      percentage = full_salary * (80/100)
      monthly_salary = full_salary - percentage
      return monthly_salary
   elif days < 20:
      percentage = full_salary * (50/100)
      monthly_salary = full_salary - percentage
      return monthly_salary
   else:
      return "Invalide attendence"
   

full_salary_count = 0

for name, days in employees.items():
   salary = calculate_salary(days)
   if salary == full_salary:
      full_salary_count += 1
      
   print(f"name:{name} salary:{salary}")

print(f"amount of people who get full salary:{full_salary_count}")

# Print employee name and salary
