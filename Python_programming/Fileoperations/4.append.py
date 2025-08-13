file_name = "F:/students.txt"

with open(file_name, 'a') as f1:

    while True:
        data = input("Enter Product details or type EXIT:")

        if data.lower() == 'exit':
            break

        if not data:
            break

        f1.write(data)

        f1.write('\n')
print("Data has been appended succesfully")

