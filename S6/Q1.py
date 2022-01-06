import numpy as np
import random

# NOTE: I wasn't able to solve the intersection between 3d line segments to 3d mesh object
# My code ended up 3d Travelling salesman problem 

def generate_population(number_of_population, path_no, path):
    population = []
    number_to_n = np.arange(start=0, stop=path_no, step=1)

    for i in range(0, number_of_population):
        shuffled_number = np.random.permutation(number_to_n)
        array = []
        for j in range(0, len(shuffled_number)):
            array.append( path[shuffled_number[j]] ) 
        population.append(array)

    return np.array(population)

def fitness_function(population):
    distance = 0 

    for i in range(0, len(population[0])):
        if(i+1 < len(population[0])):
            distance += ( population[:,i] - population[:,i+1] )**2

    distance = np.sqrt(np.sum(distance,axis=1))

    return distance

def selection(ranking, population,top_number):
    global highest_recorded_number
    def get_ranking(population):
        temp = population.argsort()
        ranks = np.empty_like(temp)
        ranks[temp] = np.arange(len(population))
        ranking = {}
        
        for i in range(0, len(population)):
            ranking[ranks[i]] = population[i]

        return ranking 

    ranking = get_ranking(ranking)

    if( highest_recorded_number > ranking[0]):
        highest_recorded_number = ranking[0]
        print("Highest Score:",highest_recorded_number)

    selectionResults = []
    ranking_len = len(ranking)

    for i in range( 0, top_number ):
        index = int( list(ranking).index(i) )
        selectionResults.append(population[index])

    for i in range(0, ranking_len - top_number):
        rand_number = random.randint(0, ranking_len - 1 )
        selectionResults.append(population[rand_number])

    return selectionResults
    
def crossover(selected_population,top_number):
    children = []

    def cross_breed(parent1,parent2):
        ranking_len = len(parent1)
        rand_number1 = random.randint(0, ranking_len - 1 ) 
        rand_number2 = random.randint(0, ranking_len - 1 ) 

        startGene = min(rand_number1, rand_number2)
        endGene = max(rand_number1, rand_number2)

        child = []
        for i in range(startGene, endGene):
            child.append(parent1[i])


        if( len(child) == 0):
            child = parent2
        else:
            for item in parent2:
                if not (item == child).all(1).any():
                    child.append( item )

            child = np.array( child )

        return child

    for i in range(0,top_number):
        children.append(selected_population[i])

    pool = random.sample(selected_population, len(selected_population))
    length = len(selected_population) - top_number

    for i in range(0, length):
        child = cross_breed(pool[i], pool[len(selected_population)-i-1])
        children.append(child)
        
    return np.array( children ) 


def mutate_population(population, mutation_rate):
    
    def mutate(individual, mutation_rate):
        mutated_individual = individual.tolist()
        for swapped in range( len(mutated_individual) ):
            if(random.random() < mutation_rate):
                swapWith = random.randint(0, len(individual) - 1 )
                mutated_individual[swapped], mutated_individual[swapWith] = mutated_individual[swapWith], mutated_individual[swapped]

        return np.array( mutated_individual )

    for ind in range(0, len(population) ):
        mutatedInd = mutate(population[ind], mutation_rate)
        population[ind] = mutatedInd

        
    return population

top_number = 100
mutation_rate=0.01
highest_score = 0

highest_recorded_number = 1000

NUMBER_OF_POPULATION = 200
number_of_generation  = 100

PATH_NO = 10

np.random.seed(0)
paths = np.random.randint(low=0, high=100, size=(PATH_NO,3))
population = generate_population(NUMBER_OF_POPULATION,PATH_NO,paths)



for gen in range(number_of_generation):
    distance = fitness_function(population)
    selected_population = selection(distance, population, top_number)
    bred_population = crossover(selected_population,top_number)
    mutated_population = mutate_population(bred_population, mutation_rate)
    population = mutated_population


