def relationship_status(from_member, to_member, social_graph):
    first_case = to_member in social_graph[from_member]["following"]
    second_case = from_member in social_graph [to_member]["following"]
    if first_case and second_case:
        return("friends")
    elif first_case:
        return("follower")
    elif second_case:
        return("followed by")
    else:
        return("no relationship")
    
def tic_tac_toe(board):
    y = 0
    sizing = len(board)

    for n in range(0, sizing):
        if board[n].count(board[n][0]) == sizing:
            if board[n][0] != "":
                return(board[n][0])
            else:
                return "NO WINNER"

    for n in range(0, sizing):
        for x in range(0, sizing):
            if board[x][n] == board[x - 1][n]:
                y += 1
            else:
                y = 0
            if y == sizing:
                if board[x][n] != "":
                    return(board[x][n])
                else:
                    return "NO WINNER"
                
    for n in range(0, sizing):
        if board[n][n] == board[n - 1][n - 1]:
            y += 1
        else:
            y = 0
        if y == sizing:
            if board[n][n] != "":
                return(board[n][n])
            else:
                return "NO WINNER"
            
    if y != sizing:
        y = 0
    
    for n in range(1, sizing):
        if board[sizing - n][n - 1] == board[sizing - n - 1][n]:
            y += 1
        else:
            y = 0
        if y == (sizing - 1):
            if board[sizing - n - 1][n] != "":
                return(board[sizing - n - 1][n])
            else:
                return "NO WINNER"
            
    if y != sizing:
        return "NO WINNER"
            
def eta(first_stop, second_stop, route_map):
    time_elapsed = 0
    stop = first_stop

    while stop != second_stop:
        for legs in route_map:
            if legs[0] == stop:
                time_elapsed += route_map[legs]['travel_time_mins']
                stop = legs[1]
                break

    return time_elapsed