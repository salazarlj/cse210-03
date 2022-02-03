from Classes.game_seeker import Seeker_game

game1 = Seeker_game()

game1.find_a_number()
#print (game1.number_to_find)
#print (game1.number_player)

valor = game1.number
val = game1.number_player

while game1.number_player !=0:
    game1.guess_number(val, valor)
    game1.find_a_number()