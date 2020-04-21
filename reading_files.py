employee_file = open('employees.txt', 'r+')
employee_file2 = open('employees2.txt', 'w')

employee_file2.write('Darmaji - Farmer')

print(employee_file.read())

employee_file.close()
employee_file2.close()
