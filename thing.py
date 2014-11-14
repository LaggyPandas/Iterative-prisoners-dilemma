elif player == 2:
        if getting_team_name:
            return 'flaming corndogs'
        else:
            if len(opponent_history)==0:
                return 'C'
            elif history[-1]=='C' and opponent_history[-1]=='b':
                return 'B'
            else:
                if random.random()<0.15:
                    return 'B'
                else:
                    return 'C'