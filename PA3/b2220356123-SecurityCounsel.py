
import sys
# -*- coding:utf-8 -*-

# OUTPUT IS WRITTEN.
def write_output(output):
    with open("agents_aid_outputs", "w") as file:
        file.writelines(output)

# THE INPUT FILE IS SEPARATED LINE BY LINE AND CREATED A DICTIONARY.
def process_create_line(line):
    if line.startswith("create"):
        data = line.strip().split(',')
        name = data[0].strip()
        accuracy = float(data[1].strip())
        counsel = int(data[2].strip())
        incidence = data[3].strip()
        rate = str(data[3]).split("/")
        name = name[7:]

        if counsel == 1:
            counsel = "Bomber"
        else:
            counsel = "Not Bomber"

        dict_main = {
            "Interrogee Name": name,
            "Core Accuracy": accuracy,
            "Counsel": counsel,
            "Local Bomber Incidence": incidence,
            "Counsel Risk": "No Risk"
        }
        return dict_main
    else:
        return None

# INPUT FILE IS READ.
def reading_input(file_two):
    with open(file_two, 'r') as file:
        splitting_lines = file.readlines()
    return splitting_lines

# SYSTEM SUGGESTS RELEASING OR ARRESTING THE PERSON UP TO RISK RATE.
def recommend(dict_list, user_name):
    for person in dict_list:
        if person["Interrogee Name"] == user_name:

            if "Counsel Risk" not in person:
                numerator = int(person["Local Bomber Incidence"].split("/")[0])
                accuracy = person["Core Accuracy"]
                counsel = person["Counsel"]
                counsel_risk = calculate_risk(numerator, accuracy, counsel)
                person["Counsel Risk"] = counsel_risk

            if person["Counsel Risk"] == "No Risk":
                return f"System suggests to release {user_name}.\n"

            if person["Counsel Risk"] != "No Risk":
                counsel_risk = "{:.2f}%".format(person["Counsel Risk"] * 100)
                return f"Interrogee {user_name} has a counsel risk of {counsel_risk}.\n"

    return f"Recommendation for {user_name} cannot be calculated due to absence.\n"

# PERSON IS REMOVED.
def remove_person(dict_list, user_name):
    for person in dict_list:
        if person["Interrogee Name"] == user_name:
            dict_list.remove(person)
            return f"Interrogee {user_name} is removed.\n"
    return f"{user_name} isn't found in the list.\n"

# THE TABLE IS WRITTEN IN SEQUENCE.
def print_table(dict_main):
    table_header = "Interrogee  Core(%)     Counsel      Local Bomber    Counsel\n" + \
                   "Name        Accuracy                 Incidence       Risk\n" + \
                   "-------------------------------------------------------------\n"
    output = [table_header]

    for person in dict_main:
        if person['Counsel Risk'] == "No Risk":
            counsel_risk = "No Risk"
        else:
            risk = calculate_risk(person['Core Accuracy'], person['Counsel'])
            counsel_risk = "{:.2f}%".format(risk * 100)

        person_data = "{:<12} {:<10.2f} {:<12} {:<15} {:<10}\n".format(
            person['Interrogee Name'],
            person['Core Accuracy'] * 100,
            person['Counsel'],
            person['Local Bomber Incidence'],
            counsel_risk
        )
        output.append(person_data)

    output.append("-------------------------------------------------------------\n")

    return ''.join(output)


# THE RISK OF BEING BOMBER OPTION IS CALCULATED.
def calculate_risk(numerator, accuracy, counsel):
    number_one = numerator * accuracy
    number_two = ( 100000 - numerator ) - ( 100000 - numerator ) * accuracy
    number_three = numerator - numerator * accuracy
    number_four = accuracy * (100000 - numerator)

    if counsel == "Not Bomber":
        counsel_risk = number_three / ( number_three + number_four )
    else:
        counsel_risk = number_two / ( number_two + number_one )

    return counsel_risk


def main(file_two):
    dict_list = []
    lines = reading_input(file_two)
    output = []

    for line in lines:
        if line.startswith("create"):
            result = process_create_line(line)
            if result is not None:
                dict_list.append(result)
                output.append(f"Interrogee {result['Interrogee Name']} is recorded.\n")
        elif line.startswith("remove"):
            user_to_remove = line.strip().split()[1]
            output.append(remove_person(dict_list, user_to_remove))
        elif line.startswith("list"):
            output.append(print_table(dict_list))
        elif line.startswith("recommend"):
            user_to_recommend = line.strip().split()[1]
            output.append(recommend(dict_list, user_to_recommend))
        elif line.startswith("risk"):
            data = line.strip().split(',')
            if len(data) == 6:
                user_name, numerator, accuracy, counsel = data[1:]
                numerator = int(numerator.strip())
                accuracy = float(accuracy.strip())
                counsel = counsel.strip()
                risk = calculate_risk(numerator, accuracy, counsel)
                for person in dict_list:
                    if person["Interrogee Name"] == user_name:
                        person["Counsel Risk"] = risk
                        output.append(f"Risk calculated for {user_name}.\n")
                        break

    write_output(output)


if __name__ == '__main__':
    if not len(sys.argv) == 2:
        print("Try correctly please.")
        sys.exit(1)
    file_two = sys.argv[1]
    main(file_two)
