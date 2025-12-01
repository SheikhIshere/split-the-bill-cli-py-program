payment_list = [
    {'name': 'x', 'paid': 500000000},
    {'name': 'rahhim', 'paid': 6003000},
    {'name': 'kiddus', 'paid': 8000000},
    {'name': 'rrafiq', 'paid': 0},
    {'name': 'alex', 'paid': 750000000},
    {'name': 'y', 'paid': 500000000},
    {'name': 'kabir', 'paid': 5000000},
    {'name': 'rax', 'paid': 50000},
    {'name': 'ksi', 'paid': 300000},
    {'name': 'efs', 'paid': 655000},
    {'name': 'lina', 'paid': 12000000},
    {'name': 'omar', 'paid': 95000000},
    {'name': 'nina', 'paid': 470000000},
    {'name': 'zara', 'paid': 8800000},
    {'name': 'mike', 'paid': 250000000},
    {'name': 'sara', 'paid': 330000000},
    {'name': 'leo', 'paid': 7100000},
    {'name': 'maya', 'paid': 91000000},
    {'name': 'ryan', 'paid': 60000000},
    {'name': 'eva', 'paid': 150000000},
]


total_expe = sum(p['paid'] for p in payment_list)
per_head = round(total_expe / len(payment_list))
# per_head2 = total_expe / len(payment_list)

for p in payment_list:
    p['balance'] = p['paid'] - per_head




# print('with round', per_head)
# print('without round', per_head2)
# print('difference', per_head-per_head2)


print(payment_list)