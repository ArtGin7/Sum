def count_sum(data):
    sum_bread = 0
    sum_banana = 0

    for date, product, quantity in data:
        if product == 'Bread':
            if date in ['07.05.2022', '08.05.2022']:
                sum_bread += quantity
        elif product == 'Banana':
            if date in ['07.05.2022', '08.05.2022']:
                sum_banana += quantity

    return sum_bread, sum_banana

if __name__ == "__main__":
    data = []

    for _ in range(2):  # Для каждой даты
        date = input("Enter the date (DD.MM.YYYY): ")
        bread_quantity = int(input("Enter the quantity of Bread: "))
        banana_quantity = int(input("Enter the quantity of Banana: "))
        
        data.append((date, 'Bread', bread_quantity))
        data.append((date, 'Banana', banana_quantity))

    sum_bread, sum_banana = count_sum(data)

    print(f"Sum of Bread = {sum_bread}")
    print(f"Sum of Banana = {sum_banana}")