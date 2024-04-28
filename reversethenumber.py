def print_numbers(order, print_style, start, end, update):
    if order == "f":
        numbers = range(start, end + update, update)
    else:
        numbers = range(end, start - update, -update)

    if print_style == "r":
        for number in numbers:
            print(number, end=" ")
    else:
        for number in numbers:
            print(number, end=" ")


order = input("Enter the order (f(forward) or r(reverse)): ")
printstyl = input("Enter the print style (r(row) or c(colon)): ")
st = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
update = int(input("Enter the update value: "))


print_numbers(order, printstyl, st, end, update)
