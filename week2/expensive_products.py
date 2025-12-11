def get_expensive_products(products, threshold):
    """Return a product that has price greater than the threshold."""
    # use list comprehension to filter products
    return [product for product in products if product > threshold]


def main():
    products = [299, 29, 59, 300, 250, 499, 199]
    threshold = 100
    expensive_products = get_expensive_products(products=products, threshold=threshold)
    print("Expensive products:", expensive_products)


if __name__ == "__main__":
    main()
