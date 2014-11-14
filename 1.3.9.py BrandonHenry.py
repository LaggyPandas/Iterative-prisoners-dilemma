 elif player == 6:
        if getting_team_name:
            return 'fire penguin disco pandas'
        else:
            size = len(history)
            if(size%3==0):
                return 'c'
            else:
                return 'b'