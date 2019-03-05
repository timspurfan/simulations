'''
QUESTION:
Standard deck of cards: 26 red, 26 black
Draw one at a time, stop whenever.
If card is red, gain a dollar.  If black, lose a dollar.

How much should you be willing to pay to play the game?
'''

'''
SOLUTION:
Let (b,r) represent the amount of black and red cards remaining in the deck, resepectively.
Let f(b,r) = expected value of that position.

At that point then, you've made (26-r)-(26-b)=b-r

Will continue if (1/2*f(b-1,r)+1/2*f(b,1-r)) >= b-r
'''

#
# LET'S COMPARE TOP DOWN VS BOTTOM UP TIME
#


#itinitialize 27x27 list


ev_list = [[0 for i in range(27)] for i in range(27)]

#f(0,r) = 0
#f(b,0) = b


for i in range(27):
    ev_list[0][i] = 0
    ev_list[i][0] = i

for i in range(1, 27):
    for j in range(1, 27):
        stop_playing = i-j
        keep_playing = (i/(i+j))*(ev_list[i-1][j]) + (j/(i+j))*(ev_list[i][j-1])
        ev_list[i][j] = max(stop_playing, keep_playing)

print(ev_list[26][26])