"""
This program reads and manages the database of a company's employees through an CSV file.
The CSV file will have n rows corresponding to n employees and 6 columns representing: ID, name, date of birth(*), gender(**), address and productive points of each employee.
(*): Date of birth will be written in ISO's norm of formatting date.
(**): 1 stands for MALE and 0 stands for FEMALE.

The program's layout will be printed to console and interactive via CLI (Command-line interface).

The company's data will be stored under the format of a list of list (list[list]) to represent a table where each row stands for an employee and each column stores a data feature of that employee.

There will be 4 main features of the program, inclusively:
- Getting the number of employees.
- Querying employees by attributes.
- Adding employees.
- Removing employees.

"""

data_buffer = open(file="./employees_data.csv")
data_buffer_processed = [
    data_buffer_row.split(sep=",") for data_buffer_row in data_buffer
]
data_buffer.close()

employees = [
    [
        int(employee_id),
        name,
        int(date_of_birth),
        int(gender),
        address,
        int(productive_points),
    ]
    for employee_id, name, date_of_birth, gender, address, productive_points in data_buffer_processed
]

print(
    "Welcome to Employees Management Application.\nYour data will be read through an CSV file in a short minute.\nPlease select one of the options below that is suitable to your needs by typing to console the number standing before it."
)

while True:
    print(
        "\n(1) Getting the number of employees"
        "\n(2) Querying employees by attributes"
        "\n(3) Adding employee(s) to table"
        "\n(4) Removing employee(s) from table"
        "\n(5) Exit"
    )

    choice = int(input("Please type your choice: "))
    while choice < 1 or choice > 5:
        choice = int(
            input(
                "Number chosen doesn't appear in options\nPlease retype your choice: "
            )
        )

    if choice == 5:
        print("Exiting...")
        data_file = open("./employees_data.csv", "w")
        for employee in employees:
            for attribute in employee[:-1]:
                data_file.write(f"{attribute},")
            data_file.write(f"{employee[-1]}\n")
        break
    elif choice == 1:
        print(
            "\nYou chose `Getting the number of employees`"
            f"\nNumber of employees is: {len(employees)}"
        )
    elif choice == 2:
        print("\nYou chose `Querying employees by attributes`")

        attributes_choices_buffer = input(
            "Type your choices on a same line, seperated by `,`, each option is that option's number followed by the value you want to query for that option, seperated by a `:`"
            "\n(1) ID\n(2) Name\n(3) Date of birth\n(4) Gender\n(5) Address"
            "\nExample: `1:{value_1},2:{value_2}, ...`"
            "\nNote: Date of birth should be in ISO format, which is {Year}{Month}{Day} as a whole number, ex.: September 6th, 2004 -> 20040906"
            "\nYour input: "
        ).split(",")

        attributes_choices = []

        for atrributes_choice in attributes_choices_buffer:
            choice_id, choice_value = atrributes_choice.split(":")

            choice_id = int(choice_id) - 1

            if choice_id == 0 or choice_id == 2 or choice_id == 3 or choice_id == 5:
                choice_value = int(choice_value)

            attributes_choices.append([choice_id, choice_value])

        querried_employees = []

        for employee in employees:
            is_satisfied = True

            for attribute_id, attribute_value in attributes_choices:
                if employee[attribute_id] == attribute_value:
                    continue

                is_satisfied = False
                break

            if is_satisfied:
                querried_employees.append(employee)

        if len(querried_employees) == 0:
            print("There is no employee matching queries.")
        else:
            print("Querried result:")

        for (
            employee_id,
            name,
            date_of_birth,
            gender,
            address,
            productive_points,
        ) in querried_employees:
            print(
                f"ID: {employee_id} | Name: {name} | Date of birth: {date_of_birth} | Gender: {gender} | Address: {address} | Productive points: {productive_points}"
            )
    elif choice == 3:
        print("\nYou chose `Adding employee(s) to table`")
        employees_to_add_num = int(input("Type the number of employees to add: "))
        print(
            "Format to input an employee data:"
            "\n{ID},{Name},{Date of birth},{Gender},{Address},{Productive points}"
        )

        employees_to_add = []

        for index in range(employees_to_add_num):
            buffer = input(f"Input number {index+1}:\t").split(",")
            employee_to_add = [
                int(buffer[0]),
                buffer[1],
                int(buffer[2]),
                int(buffer[3]),
                buffer[4],
                int(buffer[5]),
            ]
            employees_to_add.append(employee_to_add)

        employees.extend(employees_to_add)

    else:
        print("\nYou chose `Remove employee(s) from table`")
        print("Type the employee(s)' ID seperated by `,`: {ID_1},{ID_2}, ...")
        ids = [int(x) for x in input("Input: ").split(",")]

        employees_to_remove = []

        for index, employee in enumerate(employees):
            for id in ids:
                if employee[0] == id:
                    employees_to_remove.append(employee)
                    break

        for employee_to_remove in employees_to_remove:
            employees.remove(employee_to_remove)
