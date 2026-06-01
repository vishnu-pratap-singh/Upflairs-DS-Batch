print("hello")

def calculate_bill(price,quantity,discount):
    total_bill=price*quantity
    discount_applied=(total_bill*discount)/100
    bill_payable=total_bill-discount_applied
    print(f'final payable amount {bill_payable}')

calculate_bill(500,3,10)

# final payable amount 1350.0