def loop_array(index : int, votes : dict = {} ):
    if(index == 0):
        print("Group",votes)
        print('Enter your p:')
        p = int(input()) 
        assert n > 0, "Sorry invalid input for p" 
        suvived_group = get_index_greatest( list(votes.values()), list(votes), p )

        return suvived_group 
    else:
        print("Choose number:")
        x = int(input()) 
        assert x < 10 and  x > 0, "Sorry input should only between 10-1" 
        if x not in votes:
            votes[x] = 1
        else:
            votes[x] += 1

        suvived_group = loop_array(index - 1,votes)
        return suvived_group

def get_index_greatest(array_num : int, array_key : int, p : int = 2, index : int = 0, max_index : int = [] ):
    if(len(array_num)<=0):
        return max_index
    else:
        number = array_num[0]
        if(number > p):
            max_index.append(array_key[0])
        max_index = get_index_greatest(array_num[1:],array_key[1:], p, index+1 ,max_index)
        return max_index


print('Enter your n:')
n = int(input()) 
print('n=',n)
assert n > 0, "Sorry invalid input for n" 
votes = loop_array( n )
print("Group Survived:", votes)

