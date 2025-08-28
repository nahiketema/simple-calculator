def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Applies the discount only if it's 20% or higher.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage (e.g., 20 for 20%).

    Returns:
        float: The final price after discount, or the original price if no discount was applied.
    """
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        print(f"A {discount_percent}% discount was applied!")
        return final_price
    else:
        print(f"No discount applied (discount was {discount_percent}%, less than 20%).")
        return price

# --- Main program to get user input and use the function ---

# Get original price from the user
try:
    original_price_input = input("Enter the original price of the item: ")
    original_price = float(original_price_input)
except ValueError:
    print("Invalid price. Please enter a number.")
    exit() # Exit if input is not a valid number

# Get discount percentage from the user
try:
    discount_percent_input = input("Enter the discount percentage (e.g., 25 for 25%): ")
    discount_percent = float(discount_percent_input)
except ValueError:
    print("Invalid discount percentage. Please enter a number.")
    exit() # Exit if input is not a valid number

# Call the function and print the result
final_price_result = calculate_discount(original_price, discount_percent)

print(f"The final price is: ${final_price_result:.2f}")
