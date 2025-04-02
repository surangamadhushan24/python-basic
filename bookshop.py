def totalprice(price, numbers_of_books):
    return price * numbers_of_books


def discount(total):
    if total > 5000:
        discount_price = total * 0.15
    if 3000 < total < 5000:
        discount_price = total * 0.1
    else:
        discount_price = total * 0.05

    return total - discount_price


without_discount_price = totalprice(5000, 4)
final_price = discount(without_discount_price)
print(f"final price without discount {without_discount_price}")
print(f"final price with discount {final_price}")
