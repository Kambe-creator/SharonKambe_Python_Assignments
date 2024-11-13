def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or higher.
    
    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage to be applied.
    
    Returns:
    - float: The final price after applying the discount, or the original price if no discount is applied.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Function to validate if a string can be converted to float
def is_valid_float(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

# Prompt the user for input
price_input = input("Enter the original price of the item: ")
discount_input = input("Enter the discount percentage: ")

# Validate inputs
if not is_valid_float(price_input) or not is_valid_float(discount_input):
    print("\nInvalid input. Please enter numerical values for price and discount percentage.")
else:
    # Convert inputs to float
    price = float(price_input)
    discount_percent = float(discount_input)
    
    # Calculate the final price
    final_price = calculate_discount(price, discount_percent)
    
    # Output the result
    if final_price != price:
        print(f"\nThe final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"\nNo discount applied. The price remains: ${price:.2f}")



