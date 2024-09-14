from preloaded import Like, Dislike, Nothing

def like_or_dislike(lst):
    cur_state = None
    
    for state in lst:
        if cur_state is not None and cur_state == state:
            cur_state = None
        else:
            cur_state = state
    
    return cur_state if cur_state != None else "Nothing"