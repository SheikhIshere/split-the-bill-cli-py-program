"""
unoptimized error pron version
"""
payment_list = []
mem_cnt = int(input('How many you are in total: '))

for _ in range(mem_cnt):
    name = input('please enter member name: ')
    paid = int(input('please enter the member contribution amount: '))
    member = {
        'name': name,
        'paid': paid
    }
    payment_list.append(member)




# _payment_list = demo = [
#     {
#         'name': 'kuddus',
#         'paid': 50,    
#     },
#     {
#         'name': 'kuddus',
#         'paid': 50,    
#     },
#     {
#         'name': 'kuddus',
#         'paid': 50,    
#     },
#     {
#         'name': 'kuddus',
#         'paid': 50,    
#     },
    
# ]


# # for _ in _payment_list:
# #     total_expe = sum(p['paid'])

total_expe = sum(p['paid'] for p in payment_list)
# per_head = round(total_expe / mem_cnt) # for debug due to check differences 
per_head = round(total_expe / mem_cnt)

for p in payment_list:
    p['balance'] = p['paid'] - per_head

for p in payment_list:
    # printing the final out put
    if int(p['balance']) > 0:
        print(
            f'name: {p['name']} paid: {p['paid']} per head cost: {per_head} will get: {p['balance']} \n'
        )
    else:
        print(
            f'name: {p['name']} paid: {p['paid']} per head cost: {per_head} will pay: {p['balance'] * -1} \n'
        )