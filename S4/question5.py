
def traverse_heaven(point : int, path : int = [], total_sum : int = 0):
        index_i, index_j = point
        if(index_i < len(environment) - 1 ):
                path.append(environment[index_i][index_j])
                total_sum += environment[index_i][index_j]
                point,path,total_sum =  traverse_heaven( (index_i+1, index_j), path, total_sum )
                return point,path,total_sum
        elif(index_j < len(environment[0])  ):
                path.append(environment[index_i][index_j])
                total_sum += environment[index_i][index_j]
                point,path,total_sum =   traverse_heaven( (index_i, index_j+1), path, total_sum )
                return point, path,total_sum

        return point,path,total_sum

environment = [ [1 ,4 ,7 ,11,15],
                [2 ,5 ,8 ,12,19],
                [3 ,6 ,9 ,16,22],
                [10,13,14,17,24],
                [18,21,23,26,30]]

initial_point = (0,0)
last_point, path, total_sum = traverse_heaven( initial_point )
print("Hardest path to heaven:", path)
print("Sum:", total_sum)