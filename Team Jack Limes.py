    elif player == 5:
        if getting_team_name:
            #if there was a previous round just like 
            return 'Jack Limes'
        else:
            # use history, opponent_history, score, opponent_score
            # to compute your strategy      
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            else:
                # if there was a previous round just like the last one,
                # do whatever they did in the round that followed it
                recent_round_opponent = opponent_history[-1]
                recent_round_me = history[-1]
                            
                #go through rounds before that one
                for round in range(len(history)-1):
                    prior_round_opponent = opponent_history[round]
                    prior_round_me = history[round]
                    #if one matches
                    if (prior_round_me == recent_round_me) and \
                            (prior_round_opponent == recent_round_opponent):
                        return opponent_history[round]
                # no match found
                if history[-1]=='c' and opponent_history[-1]=='b':
                    return 'b' # betray is they were severely punished last time
                else:
                    return 'c' #otherwise collude