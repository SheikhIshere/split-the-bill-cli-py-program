"""
Documentation about this project
"""


payment_list = []

while True:
    mem_cnt = input("Enter total number of members: ").strip()
    
    # Check if it’s an integer
    if mem_cnt.isdigit():
        mem_cnt = int(mem_cnt)
        if mem_cnt > 2:
            break
        else:
            print("  Warning! Number of members must be greater than 2.")
    else:
        print("  Warning! Please enter a valid integer.")
        

for i in range(1, mem_cnt + 1):
    print(f"\nMember {i}:")
    
    # Validate name (cannot be empty)
    while True:
        name = input("  Enter member name: ").strip()
        if name:
            break
        else:
            print("    Warning! Name cannot be empty.")
    
    # Validate contribution amount (integer & non-negative)
    while True:
        paid_input = input("  Enter contribution amount: ").strip()
        if paid_input.isdigit():
            paid = int(paid_input)
            break
        else:
            print("    Warning! Please enter a valid & non-negative number.")

    # Add to payment list
    member = {'name': name, 'paid': paid}
    payment_list.append(member)


total_expe = sum(p['paid'] for p in payment_list)
per_head = round(total_expe / mem_cnt)


for p in payment_list:
    p['balance'] = p['paid'] - per_head


for p in payment_list:
    if int(p['balance']) > 0:
        print(
            f"name: {p['name']} | paid: {p['paid']} | per head: {per_head} | will receive: {p['balance']}\n"
        )
    else:
        print(
            f"name: {p['name']} | paid: {p['paid']} | per head: {per_head} | will pay: {-p['balance']}\n"
        )