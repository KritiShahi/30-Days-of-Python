"""The user should be given three prompts where they'll be asked to provide different information about an employee.
One prompt should ask for the employee's name, another should ask for their hourly wage,
and the final one should ask how many hours the employee worked this week.
All employee names should be stripped of any excess white space, and should be in title case.
Calculate the employee's total earnings for the week. It's also worth keeping in mind that the employee's wage,
or the numbers of hours they worked, might not be a whole number.
For example, output like this would be appropriate: Regina George earned $800 this week."""
employee_name = input("Enter the employee name ").strip().title()
hourly_wage = input("Enter the hourly wage")
hours_worked = input("Enter the hours worked in a week")
print(f"{employee_name} earned ${float(hourly_wage) * float(hours_worked) :.2f} this week")
