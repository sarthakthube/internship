
def calculateElectronicsGST(a, b):
    amount = a + b
    gst = amount * 18 / 100
    return amount + gst


def calculateFashionGST(c, d):
    amount = c + d
    gst = amount * 13 / 100
    return amount + gst


def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst


def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)
    return electronics + fashion + food


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    return total - discount


a, b, c, d, e = 100, 100, 100, 100, 100

total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
payable = calculateDiscountedBill(a, b, c, d, e)

print(f"Electronics after GST = Rs. {calculateElectronicsGST(a, b):.2f}")
print(f"Fashion after GST = Rs. {calculateFashionGST(c, d):.2f}")
print(f"Food after GST = Rs. {calculateFoodGST(e):.2f}")
print(f"Total after GST = Rs. {total:.2f}")
print(f"Discount = Rs. {discount:.2f}")
print(f"Final payable amount = Rs. {payable:.2f}")
