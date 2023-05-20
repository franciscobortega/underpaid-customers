MELON_COST = 1.00

customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00

def validate_customer_payments(customer, melons, total_paid):
    """Prints our information for customers who overpaid or underpaid"""
    total_expected = melons * MELON_COST
    if total_expected != total_paid:
        print(f"{customer} paid ${total_paid:.2f},",
            f"expected ${total_expected:.2f}"
            )
    

validate_customer_payments(customer1_name, customer1_melons, customer1_paid)
validate_customer_payments(customer2_name, customer2_melons, customer2_paid)
validate_customer_payments(customer3_name, customer3_melons, customer3_paid)
validate_customer_payments(customer4_name, customer4_melons, customer4_paid)
validate_customer_payments(customer5_name, customer5_melons, customer5_paid)
validate_customer_payments(customer6_name, customer6_melons, customer6_paid)
