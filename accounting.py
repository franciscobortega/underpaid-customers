MELON_COST = 1.00 # global variable for cost of 1 melon

def validate_customer_payments(customer, melons, total_paid):
    """Prints our information for customers who overpaid or underpaid"""
    # determine expected amount based on melons bought and cost per melon
    total_expected = melons * MELON_COST
    # provide output for customers who paid an amount different from the expected amount
    if total_expected != total_paid:
        print(f"{customer} paid ${total_paid:.2f},",
            f"expected ${total_expected:.2f}")
        
        # ternary operator for checking if a customer overpaid or underpaid
        payment_status = "overpaid" if total_expected < total_paid else "underpaid"

        first_name = customer.split(" ")[0] # isolate first name from customer parameter

        # output statement stating whether customer overpaid or underpaid
        print(f"  !--{first_name} has {payment_status} for their melons.--!")
        
def parse_file(file):
    """Opens file and parses each line using data from each line as arguments for validate_customer_payments function"""
    # opens input file
    input_file = open(file)

    # loop through each line in the file
    for line in input_file:
        line = line.rstrip()    # remove whitespace after end of right side of line
        words = line.split("|") # list is built from each line using '|' as a delimiter

        # assign values from list to respective variable
        customer = words[1]
        melons = int(words[2])
        paid = float(words[3])

        # calls function using variables as arguments to check if customer underpaid or overpaid
        validate_customer_payments(customer, melons, paid)

    # close file once done
    input_file.close()

parse_file("customer-orders.txt")
