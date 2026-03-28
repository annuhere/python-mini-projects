def get_input():
    cat = input("Enter category (Food, Transport, Entertainment, etc.): ").title()
    amt = float(input("Enter expense amount: "))
    return cat, amt

def add_expenses(exp, cat, amt):
    if cat not in exp:
        exp[cat] = []
    exp[cat].append(amt)

def show_all(exp):
    print("\n--- All Expenses by Category ---")
    for cat in exp:
        print(f"{cat}: {exp[cat]}")

def show_totals(exp):
    print("\n--- Total Expenses by Category ---")
    total = 0
    for cat in exp:
        cat_total = sum(exp[cat])
        print(f"{cat}: {cat_total}")
        total += cat_total
    print(f"\nTotal: {total}")

def main():
    exp = {}
    while True:
        cat, amt = get_input()
        add_expenses(exp, cat, amt)
        more = input("Add another expense? (yes/no): ").lower()
        if more != "yes":
            break
    show_all(exp)
    show_totals(exp)

main()
