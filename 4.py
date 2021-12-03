data = [2, 2, 2, 7, 23, 1, 44, 44, 3, 3, 2, 10, 7, 4, 11]
unique_data = []
[unique_data.append(num) for num in data if num not in unique_data]
print(unique_data)
