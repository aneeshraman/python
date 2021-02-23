def denominations():
    amount = None
    try:
        amount = int(input("Enter an amount: "))
    except ValueError:
        return Exception("Wrong input")
    rupee_types = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    no_of_notes_per_type = []

    if not isinstance(amount, int) and not isinstance(amount, float):
        return Exception("Wrong input")

    no_of_notes_per_type.append(amount // rupee_types[0])
    left = amount % rupee_types[0]
    notes = amount // rupee_types[0]

    rupee_types.pop(0)

    for rupee_type in rupee_types:
        amount = left
        notes = amount // rupee_type
        no_of_notes_per_type.append(notes)
        left = amount % rupee_type

    rupee_types.insert(0, 2000)
    for i in range(len(no_of_notes_per_type)):
        if no_of_notes_per_type[i] != 0:
            print(f"Number of ₹{rupee_types[i]} notes is: {no_of_notes_per_type[i]}")


denominations()
