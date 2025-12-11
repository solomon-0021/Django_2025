def calculate_sales_total(file_name):
    with open(file_name, 'r') as file:
        sales = []
        for line in file:
            try:
                amount = float(line.strip())
                sales.append(amount)
            except ValueError:
                continue
    return sum(sales)


def main():
    file_name = 'sales.txt'
    total_sales = calculate_sales_total(file_name)
    print(f'Total Sales: ${total_sales:.2f}')

if __name__ == '__main__':
    main()