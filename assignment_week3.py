small = 3.5
medium = 4.5
large = 5.5

print("=== Coffee Shop Order System ===")
print("Enter drink sizes: small, medium, or large")
print("Type 'done' when finished ordering\n")

total = 0

while True:
    order = input("Enter drink size: ")
    if order == 'small':
        price = small
    elif order == 'medium':
        price = medium
    elif order == 'large':
        price = large
    elif order == 'done':
        break
    total += price
    print(f"Price: ${price:.2f}")
    print(f"Current total: ${total:.2f}\n")
    
print("\n=== Order Summary ===")
print(f"Subtotal: ${total:.2f}")

if total >= 20:
    loyalty_discount = 3
else:
    loyalty_discount = 0

print(f"Loyalty Discount: -${loyalty_discount:.2f}")
print(f"Final Total: ${total-loyalty_discount:.2f}")
print("Thank you for your order!\n\n")


