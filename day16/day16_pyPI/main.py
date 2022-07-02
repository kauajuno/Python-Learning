from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon', ['Bulbasaur', 'Ivysaur', 'Venusaur',  'Charmander', 'Charmeleon', 'Charizard',
                             'Squirtle', 'Wartortle', 'Blastoise'])
table.add_column('Pokedex Number', list(range(1, 10)))
table.add_column('Type', ['Grass' for i in range(3)] + ['Fire' for j in range(3)] + ['Water' for k in range(3)])
table.align = 'l'


print(table)
