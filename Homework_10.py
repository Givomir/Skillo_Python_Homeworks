###################################################################################################
###################################################################################################
#problem 0
#Create a program that checks if a given word or phrase is a palindrome
#(reads the same forwards and backward):
"""
def is_palindrome(word):
    # Convert the word to lowercase and remove non-alphanumeric characters
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    # Compare the cleaned word with its reverse
    return cleaned_word == cleaned_word[::-1]
# Get input from the user
user_input = input("Enter a word or phrase: ")
# Check if the input is a palindrome
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
"""


###################################################################################################
###################################################################################################
#problem 1
#Write a function that checks if a given number is prime or not:
"""
def is_prime(number):
    # Check if the number is less than 2 (not prime)
    if number < 2:
        return False
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # Number is divisible, not prime
    return True  # No factors found, prime

# Test cases
test_number1 = 5
test_number2 = 12

print(f"{test_number1} is prime: {is_prime(test_number1)}")
print(f"{test_number2} is prime: {is_prime(test_number2)}")
"""


###################################################################################################
###################################################################################################
#problem 2
#Write a program to reverse a given string without using string slicing.:
"""
def reverse_string(input_string):
    reversed_string = ""
    # Iterate through the characters in reverse order
    for char in input_string[::-1]:
        reversed_string += char
    return reversed_string

# Test the function
original_string = "Hello, Python!"
reversed_result = reverse_string(original_string)

print(f"Original String: {original_string}")
print(f"Reversed String: {reversed_result}")
"""


###################################################################################################
###################################################################################################
#problem 3
#Create a program that checks if two given strings are anagrams of each other.:
"""
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)

# Test cases
test_str1 = "Listen"
test_str2 = "Silent"

result = are_anagrams(test_str1, test_str2)

if result:
    print(f"{test_str1} and {test_str2} are anagrams.")
else:
    print(f"{test_str1} and {test_str2} are not anagrams.")
"""

###################################################################################################
###################################################################################################
#problem 4
#Write a program that counts the number of words in a given string.:

"""
def count_words(input_string):
    # Split the string into words using whitespace as the delimiter
    words = input_string.split()
    # Count the number of words
    return len(words)

# Test the function
input_string = "This is a sample sentence for testing."
word_count = count_words(input_string)

print(f"The number of words in the string is: {word_count}")
"""


###################################################################################################
###################################################################################################
#problem 5
#Create a program that reads a CSV file, "sales.csv",
#containing sales data, and a JSON file, "products.json," with product information.
#Calculate the total revenue for each product and save it in a new CSV file called "product_revenue.csv.":
"""
import csv
import json
products = [

        {"product_id": 1, "name": "Product A", "price": 10},
        {"product_id": 2, "name": "Product B", "price": 15},
]

with open("products.json", "w") as json_file:
    json.dump(products, json_file)

def calculate_product_revenue(sales_file, products_file, output_file):
    # Read product information from the JSON file
    with open(products_file, 'r') as json_file:
        products_data = json.load(json_file)

    # Initialize a dictionary to store product revenue
    product_revenue = {}

    # Ensure 'products_data' is a list of dictionaries with 'product_id' key
    if isinstance(products_data, list) and all(
            isinstance(product, dict) and 'product_id' in product for product in products_data):
        product_revenue = {str(product['product_id']): 0.0 for product in products_data}

        # Read sales data from the CSV file and calculate total revenue for each product
        with open(sales_file, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                product_id = row['product_id']
                quantity_sold = float(row['quantity_sold'])

                # Check if the product_id exists in 'product_revenue'
                if product_id in product_revenue:
                    product_price = float(products_data[int(product_id)]['price'])
                    total_revenue = quantity_sold * product_price
                    product_revenue[product_id] += total_revenue

        # Write the results to a new CSV file
        with open(output_file, 'w', newline='') as output_csv:
            fieldnames = ['product_id', 'product_name', 'total_revenue']
            csv_writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
            csv_writer.writeheader()

            for product_id, total_revenue in product_revenue.items():
                product_name = products_data[int(product_id)]['name']
                csv_writer.writerow(
                    {'product_id': product_id, 'product_name': product_name, 'total_revenue': total_revenue})

        print("Product revenue calculation completed. Results saved in 'product_revenue.csv'.")
    else:
        print("Invalid 'products.json' file structure. Please check the format.")


# Test the function
calculate_product_revenue('sales.csv', 'products.json', 'product_revenue.csv')
"""

###################################################################################################
###################################################################################################
#problem 6
#Develop a Python script that reads a JSON file called "inventory.json"
#with information about products and their quantities.
#Create a new CSV file, "low_stock.csv," containing the names of products with a quantity less than 10.":
"""
import json
import csv

inventory = [

        {"name": "Product A", "quantity": 5},
        {"name": "Product B", "quantity": 3},
        {"name": "Product C", "quantity": 2},
        {"name": "Product D", "quantity": 2},
        {"name": "Product E", "quantity": 1},
        {"name": "Product F", "quantity": 8},
        {"name": "Product G", "quantity": 25},
        {"name": "Product H", "quantity": 35},
]

with open("inventory.json", "w") as json_file:
    json.dump(inventory, json_file)


def identify_low_stock_products(json_file, csv_file):
    # Read product information from the JSON file
    with open(json_file, 'r') as json_file:
        inventory_data = json.load(json_file)

    # Identify products with a quantity less than 10
    low_stock_products = [product['name'] for product in inventory_data if product['quantity'] < 10]

    # Write the results to a new CSV file
    with open(csv_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Product Name'])  # Write header

        # Write names of low stock products
        csv_writer.writerows(map(lambda x: [x], low_stock_products))

    print(f"Low stock products saved in '{csv_file}'.")

# Test the function
identify_low_stock_products('inventory.json', 'low_stock.csv')
"""


###################################################################################################
###################################################################################################
#problem 7
#Write a program that is given a number and an array and checks
#if there is a pair of numbers in the array that has a sum equal to the given number. ( two-sum problem )":

def has_pair_with_sum(arr, target_sum):
    seen_numbers = set()

    for num in arr:
        complement = target_sum - num

        if complement in seen_numbers:
            return True  # Pair found
        else:
            seen_numbers.add(num)

    return False  # No pair found

# Example usage
numbers_array = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11]
target_number = 0

if has_pair_with_sum(numbers_array, target_number):
    print(f"There is a pair with sum {target_number}.")
else:
    print(f"No pair found with sum {target_number}.")
