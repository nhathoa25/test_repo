with open('Road Accident Data.csv', 'r') as file:
    row_count = sum(1 for row in file)
print("Số dòng:", row_count)
