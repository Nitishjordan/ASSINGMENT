import sys
user1 = input("USER 1 NAME:")
user2 = input("USER 2 NAME:")	
ans='y'
def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("%s WINS"%user1)
        else:
            return("%s WINS"%user2)
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("%s WINS "%user1)
        else:
            return("%s WINS"%user2)
    elif u1 == 'paper':
        if u2 == 'rock':
            return("%s WINS"%user1)
        else:
            return("%s WINS" %user2)
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()




while ans=='y':
	
	user1_answer = input("%s,  choose rock, paper or scissors?" % user1)
	user2_answer = input("%s,  rock, paper or scissors?" % user2)
	print(compare(user1_answer, user2_answer))
	print("Do you want to play more (Y/N)" )
	ans=input()