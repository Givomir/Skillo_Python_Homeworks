###################################################################################################
###################################################################################################
#problem 0
#Fix the mistakes in the following snippet:


items = {"Coffee": 2.2, "Tea": 1.5, "Chocolate": 2.5}
income = 0

for item in items.keys():
    qty = int(input(f"How many {item}s have you sold? "))
    income = income + qty * items[item]
print("Problem 0 answer")
print(f"\nThe income today was £{income:0.2f}")


###################################################################################################
###################################################################################################
#problem 1
#Rewrite the following function so it is exception safe:

def get_integer_input():
    while True:
        try:
            num = int(input("Enter an integer: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
print("Problem 1 answer")
number = get_integer_input()
print("You entered:", number)


###################################################################################################
###################################################################################################
#problem 2
#Research and understand how does selections sort work:

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:  # Fix: Compare arr[j] with arr[min_index]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
