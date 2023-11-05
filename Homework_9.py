###################################################################################################
###################################################################################################
#problem 1
#Create a Python script that reads a text file called "numbers.txt"
#containing integers and calculates their sum:
"""
file_name = "numbers.txt"
total_sum = 0
try:

    with open(file_name, "r") as file:
          for line in file:
            try:

                number = int(line)
                total_sum += number
            except ValueError:
                print(f"Skipping non-integer line: {line.strip()}")


    print("The sum of the integers in the file is:", total_sum)

except FileNotFoundError:
    print(f"The file {file_name} does not exist.")

except Exception as e:
    print(f"An error occurred: {e}")
"""

###################################################################################################
###################################################################################################
#problem 2
#Write a program that reads a text file, "words.txt," and counts the number of words in it:
"""
# Define the file name
file_name = "words.txt"

try:
       with open(file_name, "r") as file:

        file_content = file.read()


        words = file_content.split()


        word_count = len(words)


        print(f"The number of words in the file is: {word_count}")

except FileNotFoundError:
    print(f"The file {file_name} does not exist.")

except Exception as e:
    print(f"An error occurred: {e}")
"""

###################################################################################################
###################################################################################################
#problem 3
#Write a program that reads a text file, "words.txt," and counts the number of words in it:
"""
import csv

# Create or open the CSV file for writing
with open("student_scores.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(["Name", "Score"])

    # Prompt the user to enter student names and scores
    while True:
        student_name = input("Enter the student's name (or 'q' to quit): ")
        if student_name.lower() == 'q':
            break  # Exit the loop if 'q' is entered

        try:
            student_score = float(input("Enter the student's score: "))
        except ValueError:
            print("Invalid input. Please enter a numeric score.")
            continue  # Skip this iteration if the score is not numeric

        # Write the student's data to the CSV file
        writer.writerow([student_name, student_score])

print("Data has been saved to student_scores.csv.")
"""

###################################################################################################
###################################################################################################
#problem 4
#Write a program that reads a CSV file called "employee_data.csv,"
#and for each employee, calculates their total salary (considering base salary and bonuses)
#and saves it in a new CSV file called "total_salaries.csv.":
"""
import csv


# Function to calculate the total salary for an employee
def calculate_total_salary(base_salary, bonuses):
    return base_salary + bonuses


# Input and output file names
input_file = "employee_data.csv"
output_file = "total_salaries.csv"

try:
    # Open the input CSV file for reading
    with open(input_file, mode="r", newline="") as input_csvfile:
        # Create a CSV reader
        reader = csv.reader(input_csvfile)

        # Read the header row to get the field names
        header = next(reader)

        # Find the index of the "Base Salary" and "Bonuses" columns
        base_salary_index = header.index("Base Salary")
        bonuses_index = header.index("Bonuses")

        # Open the output CSV file for writing
        with open(output_file, mode="w", newline="") as output_csvfile:
            # Create a CSV writer
            writer = csv.writer(output_csvfile)

            # Write the header row for the output file
            writer.writerow(header + ["Total Salary"])

            # Process each row in the input CSV file
            for row in reader:
                base_salary = float(row[base_salary_index])
                bonuses = float(row[bonuses_index])
                total_salary = calculate_total_salary(base_salary, bonuses)

                # Write the row with the calculated total salary to the output CSV file
                writer.writerow(row + [total_salary])

    print(f"Total salaries have been calculated and saved to {output_file}.")

except FileNotFoundError:
    print(f"The file {input_file} does not exist.")

except Exception as e:
    print(f"An error occurred: {e}")
"""

###################################################################################################
###################################################################################################
#problem 5
#Design a program that reads a JSON file containing a list of products with names and prices.
#Calculate the total cost of all products and display it.:
"""
import json


products = [
    {"name": "Product A", "price": 10.99},
    {"name": "Product B", "price": 5.49},
    {"name": "Product C", "price": 7.99},
    {"name": "Product A", "price": 100.99},
    {"name": "Product B", "price": 50.49},
    {"name": "Product C", "price": 70.99},
]


with open("products.json", "w") as json_file:
    json.dump(products, json_file)


total_cost = 0
with open("products.json", "r") as json_file:
    loaded_products = json.load(json_file)
    for product in loaded_products:
        total_cost += product["price"]


print("Total cost of all products: $", total_cost)
"""

###################################################################################################
###################################################################################################
#problem 6
#Write a Python script that reads a JSON file,
#"contacts.json," containing contact information (name, email, phone).:
"""

import json

products = [
    {"name": "Angel Ivanov", "email": "angel.ivanov@example.bg", "phone": "088111111"},
    {"name": "Angel Keranov", "email": "angel.keranov@example.bg", "phone": "088111112"},
    {"name": "Angel Pavlov", "email": "angel.pavlov@example.bg", "phone": "088111113"},
    {"name": "Ivan Dimitrov", "email": "ivan.dimitrov@example.bg", "phone": "088111114"},

]

with open("contacts.json", "w") as json_file:
    json.dump(products, json_file)


json_file = "contacts.json"

try:

    with open(json_file, "r") as file:

        contacts = json.load(file)


    for contact in contacts:
        print("Name:", contact["name"])
        print("Email:", contact["email"])
        print("Phone:", contact["phone"])
        print("\n")

except FileNotFoundError:
    print(f"The file {json_file} does not exist.")

except Exception as e:
    print(f"An error occurred: {e}")
"""

###################################################################################################
###################################################################################################
#problem 7
#Create a CSV file, "student_data.csv," with student names
# and their corresponding JSON data containing exam scores.
# Write a program that reads the CSV file and calculates the average score for each student.:
"""
import json
import csv

products = [
    {"name": "Angel Ivanov", "exam1": 85, "exam2": 92, "exam3": 78},
    {"name": "Angel Keranov","exam1": 85, "exam2": 92, "exam3": 78},
    {"name": "Angel Pavlov", "exam1": 85, "exam2": 92, "exam3": 78},
    {"name": "Ivan Dimitrov","exam1": 85, "exam2": 92, "exam3": 78},

]

with open("student_data.json", "w") as json_file:
    json.dump(products, json_file)


# Read the JSON file and convert it to CSV
with open("student_data.json", "r") as json_file:
    data = json.load(json_file)

# Create a CSV file from the JSON data
with open("data.csv", "w", newline="") as csv_file:
    fieldnames = ["name", "exam1", "exam2", "exam3"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for item in data:
        writer.writerow(item)

# Calculate the total score and create a new CSV file
with open("data.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    rows = list(reader)

for row in rows:
    total_score = sum(int(row[key]) for key in row if key != "name")
    row["Total Score"] = total_score

# Create a new CSV file with calculations
with open("data_with_total.csv", "w", newline="") as new_csv_file:
    fieldnames = ["name", "exam1", "exam2", "exam3", "Total Score"]
    writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rows)

print("CSV file 'data_with_total.csv' has been created with the added 'Total Score' column.")
"""


###################################################################################################
###################################################################################################
#problem 8
#Provide an example XML file, "inventory.xml," that represents a list of products in a store.
#Write a Python program to read this XML file and print the names and prices of all products.:

import xml.etree.ElementTree as ET

# Create the root element
inventory = ET.Element("inventory")

# Create product elements
product1 = ET.Element("product")
name1 = ET.Element("name")
name1.text = "Product A"
price1 = ET.Element("price")
price1.text = "10.99"
product1.append(name1)
product1.append(price1)

product2 = ET.Element("product")
name2 = ET.Element("name")
name2.text = "Product B"
price2 = ET.Element("price")
price2.text = "5.49"
product2.append(name2)
product2.append(price2)

product3 = ET.Element("product")
name3 = ET.Element("name")
name3.text = "Product C"
price3 = ET.Element("price")
price3.text = "7.99"
product3.append(name3)
product3.append(price3)

# Append product elements to the root
inventory.append(product1)
inventory.append(product2)
inventory.append(product3)

# Create an ElementTree from the root
tree = ET.ElementTree(inventory)

# Write the ElementTree to a file
tree.write("inventory.xml")

print("XML file 'inventory.xml' has been created.")

import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse("inventory.xml")
root = tree.getroot()

# Loop through products and print names and prices
for product in root.findall("product"):
    name = product.find("name").text
    price = product.find("price").text
    print(f"Product Name: {name}")
    print(f"Product Price: {price}")
    print()
