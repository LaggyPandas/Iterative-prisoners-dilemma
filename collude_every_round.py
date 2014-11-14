    elif player == 4:
        if getting_team_name:
            return 'collude every round'
        else:     
            if len(opponent_history)==0:
                return 'c'
            else:
                returner = opponent_history[-1]
                return returner