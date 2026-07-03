def get_items():
    items = {}
    item_name=''
    while item_name != 'done':
        item_name = input("Enter item name: ")
        if item_name == 'done':
            break
        item_price = int(input("Enter item price: "))
        items[item_name] = item_price
    return items

def print_items(items):
    print('Items:')
    total=0
    for k, v in items.items():
        print(f'{k} {v}')
        total += v
    print(f'Total: {total}')