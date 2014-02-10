
def save_transaction(price, credit_card, description):
    with open("transactions.txt", "a") as f:
        f.write('%16s%07d%16s\n' % (credit_card, price*100, description))



    