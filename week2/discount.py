def discount():
    items = int(input("Enter the number of items you want to buy: "))
    if items > 3:
        print("Discount applied!")
    else:
        print("No discount!")



def main():
    discount()

if __name__ == "__main__":
    main()
