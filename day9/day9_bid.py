bids = {}

end_of_bids = False

while not end_of_bids:
    price = int(input('Price of the bid\n'))
    name = input('Name of the bidder\n')
    bids.update({name: price})
    next_bid = input('Is there anyone else? y/n\n')
    if next_bid == 'n':
        end_of_bids = True

higher = 0
winner = None

for key in bids:
    if bids[key] > higher:
        higher = bids[key]
        winner = key

print(f"{winner}: {higher}")
