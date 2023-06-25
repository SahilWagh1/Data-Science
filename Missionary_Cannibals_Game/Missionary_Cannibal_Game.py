from IPython.display import clear_output
boat_side ='Right'
missionaries_on_right = 3
cannibals_on_right =3
missionaries_on_left = 0
cannibals_on_left =0
while True:
    missionaries = int(input("Enter the number of missionaries on the boat:"))
    cannibals = int(input("Enter the number of cannibals on the boat:"))

    if missionaries+cannibals > 2 or missionaries+cannibals < 1:
        print("Invalid move 1")
        continue
    if boat_side == 'Right':
        if missionaries > missionaries_on_right or cannibals > cannibals_on_right:
            print("Invalid move 2")
            continue
    else:
        if missionaries > missionaries_on_left or cannibals > cannibals_on_left:
            print("Invalid move 2")
            continue
    if boat_side == 'Right':
        missionaries_on_right -=missionaries
        cannibals_on_right -= cannibals
        missionaries_on_left += missionaries
        cannibals_on_left +=cannibals
        boat_side = 'Left'
        print('\U0001f482'*missionaries_on_left,'\U0001f479'*cannibals_on_left,'|\U0001f6A2','\U0001f30a'*5,'|','\U0001f482'*missionaries_on_right,'\U0001f479'*cannibals_on_right)
    else:
        missionaries_on_left -= missionaries
        cannibals_on_left -= cannibals
        missionaries_on_right += missionaries
        cannibals_on_right += cannibals
        boat_side = 'Right'
        print('\U0001f482'*missionaries_on_left,'\U0001f479'*cannibals_on_left,'|','\U0001f30a'*5,'\U0001f6A2|','\U0001f482'*missionaries_on_right,'\U0001f479'*cannibals_on_right)
    if missionaries_on_right < cannibals_on_right and missionaries_on_right > 0:
        print("YOU LOSE")
        break
    elif missionaries_on_left <cannibals_on_left and missionaries_on_left >0:
        print("YOU LOSE")
        break
    if missionaries_on_left == 3 and cannibals_on_left ==3:
        print("YOU WIN")
        break
print("Game Over")
