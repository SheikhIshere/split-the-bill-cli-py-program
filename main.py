"""
Project: Member Contribution Split
Description: 
This script collects contribution amounts from multiple members,
calculates total expenses, determines per-head cost, and shows
how much each member should receive or pay to balance the contributions.
"""

payment_list = []

# Get total number of members (must be integer > 2)
while True:
    mem_cnt = input("Enter total number of members: ").strip()
    if mem_cnt.isdigit():
        mem_cnt = int(mem_cnt)
        if mem_cnt > 2:
            break
        else:
            print("  Warning!!! Number of members must be greater than 2.")
    else:
        print("  Warning!!! Please enter a valid integer.")

# Collect member details
for i in range(1, mem_cnt + 1):
    print(f"\nMember {i}:")
    
    # Validate member name
    while True:
        name = input("  Enter member name: ").strip()
        if name:
            break
        else:
            print("    Warning!!! Name cannot be empty.")
    
    # Validate contribution amount
    while True:
        paid_input = input("  Enter contribution amount: ").strip()
        if paid_input.isdigit():
            paid = int(paid_input)
            break
        else:
            print("    Warning!!! Please enter a valid non-negative number.")

    # Add member to the list
    payment_list.append({'name': name, 'paid': paid})

# Calculate total and per-head contributions
total_expe = sum(p['paid'] for p in payment_list)
per_head = round(total_expe / mem_cnt)

# Compute balance for each member
for p in payment_list:
    p['balance'] = p['paid'] - per_head

# Display results
print("\n===== Contribution Summary =====\n")
for p in payment_list:
    if p['balance'] > 0:
        print(f"{p['name']:10} | Paid: {p['paid']:>10} | Per head: {per_head:>10} | Will receive: {p['balance']:>10}")
    else:
        print(f"{p['name']:10} | Paid: {p['paid']:>10} | Per head: {per_head:>10} | Will pay: {-p['balance']:>10}")
