    elif player == 7:
        if getting_team_name:
            return 'Team'
        else:
            if len(opponent_history)==0:
                return 'b' 
            elif history[-1]=='b' and opponent_history[-1]=='c':
                 return 'b'
            else:
                return'b'