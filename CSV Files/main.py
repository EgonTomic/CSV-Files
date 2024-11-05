with open("data.csv", "r") as data_file:
    for row in data_file:

        row_data = row.split(",")

        name = row_data[0]
        age = row_data[1]
        gender = row_data[2]

        print(f"{name} is {age} years old nad gender {gender}")