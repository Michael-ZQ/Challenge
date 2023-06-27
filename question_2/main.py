# Write a query to print the id, first_name and last_name. To filter the
# names, concatenate the first and last names to create a combined
# name. Return the names of customers whose combined names are less
# than 12 letters long. Sort the results by their combined name lengths,
# then alphabe tically, case insensitive, by combined name, then by id. All
# sorts are ascending.


def filter_names(customers):
    filter_customers = []

    for customer in customers:
        full_name = get_full_name(customer)
        if len(full_name) < 12:
            filter_customers.append(customer)

    # The reverse=False parameter is used to ensure ascending order.
    filter_customers.sort(key=lambda x: (len(get_full_name(x)), get_full_name(x), x["id"]), reverse=False)

    for customer in filter_customers:
        print(f"ID: {customer['id']}, Full Name: {customer['first_name']} {customer['last_name']}")

    return filter_customers


def get_full_name(customer):
    return customer["first_name"] + customer["last_name"]


if __name__ == "__main__":
    # Example usage
    customers_data = [
        {"id": 1, "first_name": "Alex", "last_name": "White"},
        {"id": 2, "first_name": "Tyler", "last_name": "Hanson"},
        {"id": 3, "first_name": "Jordan", "last_name": "Fernandez"},
        {"id": 4, "first_name": "Drew", "last_name": "Bradley"},
        {"id": 5, "first_name": "Blake", "last_name": "Fuller"},
        {"id": 6, "first_name": "Spencer", "last_name": "Johnston"},
        {"id": 7, "first_name": "Ellis", "last_name": "Gutierrez"},
        {"id": 8, "first_name": "Morgan", "last_name": "Thomas"},
        {"id": 9, "first_name": "Riley", "last_name": "Garza"},
    ]

    filter_names(customers_data)
