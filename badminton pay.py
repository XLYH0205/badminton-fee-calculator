class Player:
    players = []
    cost_shuttlecocks = 0

    def __init__(self, name, shuttlecock_amount, shuttlecock_price) -> None:
        self.name = name
        self.shuttlecock_amount = shuttlecock_amount
        self.shuttlecock_price = shuttlecock_price
        self.shuttlecock_price = shuttlecock_price

        self.total = 0

        Player.cost_shuttlecocks += (self.shuttlecock_amount * self.shuttlecock_price)
        Player.players.append(self)

    def __str__(self):
        return f"{self.name}({self.shuttlecock_amount}, {self.shuttlecock_price})"
    
    def __repr__(self) -> str:
        return f"{self.name}"
    
    def total_fees(self):
        self.total +=  (Player.cost_shuttlecocks / len(Player.players)) - (self.shuttlecock_amount * self.shuttlecock_price)
        return self.total


with open('input.txt', 'r') as file:
    content = file.read()

names = [name[2:].strip() for name in content.strip().split('\n')[1:]]
print('---------------------Players registration---------------------')
for name in names:
    print(name)
    shuttlecock_amount = int(input('Enter shuttlecock amount: '))
    if shuttlecock_amount:
        shuttlecock_price = float(input('Enter shuttlecock price per dozen: ')) / 12.
    else:
        shuttlecock_price = 0
    Player(name, shuttlecock_amount, shuttlecock_price)

print('\n')
total_hour = int(input('Enter total play hour: '))
court_price = float(input('Enter court price per hour: '))

for hour in range(total_hour):
    players = Player.players
    player_numbers = len(players)
    court_amount = int(input(f'Enter court amount at Hour{hour+1}: '))

    absentH = input(f'Anyone absent at Hour{hour+1}? (yes / no): ')
    absentees = []
    if absentH == 'yes':
        for player in players:
            absent = input(f'Is {player} absent at Hour {hour+1}? (yes / no): ')
            if absent == 'yes':
                absentees.append(player)
                player_numbers -= 1
    
    for player in players:
        if player in absentees:
            continue
        player.total += ((court_amount*court_price)/player_numbers)
    
total_fees = Player.cost_shuttlecocks
for player in Player.players:
    player_total = player.total_fees()
    total_fees += player_total
    print(player, player_total)
print(f'Total fees: {total_fees}')

exitInp = input(f'Press enter to exit: ')
