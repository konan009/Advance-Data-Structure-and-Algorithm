
def get_index_greatest(array_num : int, num : int = 0, index : int = 0, max_index : int = 0 ):
    if(len(array_num)<=0):
        return max_index

    number = array_num[0]
    if(number > num):
        num = number
        max_index = index
        
    max_index = get_index_greatest(array_num[1:], num, index+1 ,max_index)
    return max_index

def get_highest_rating(squids_cut, votes = {}):
    if(len(squids_cut)==0):
        index = get_index_greatest(list(votes.values()))
        return  list(votes)[index]
    else:
        number = squids_cut[0]

        assert   number <= 10 , "Rating should be between 1-10" 
        assert   number >= 0 , "Rating should be between 1-10" 

        if number not in votes:
            votes[number] = 1
        else:
            votes[number] += 1

        key = get_highest_rating(squids_cut[1:], votes)
        return key
        
squids_cut  = [3, 3, 3, 3, 4, 4, 4, 2, 2, 1]
highest_rating = get_highest_rating(squids_cut)
print("Highest rating squid cut:",highest_rating)