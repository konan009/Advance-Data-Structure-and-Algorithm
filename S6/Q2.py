import numpy as np,operator
import random


BODY_FAT = 0
BREED = 1
WEIGHT = 2
WON_AWARD = 3
IS_VACCINATED = 4
AGE = 5
INTELLIGENCE = 6

DOG1 = 0
DOG2 = 1

breed = [ 'Pug', 'Corgi', 'German Shepard' , 'Golden Retriever' , 'Poodle']

def individual_dog():
    body_fat = random.random()
    dog_breed = random.choice(breed)
    weight = random.randint(1, 100 ) 
    has_won_award = random.randint(0, 1)
    is_vaccinated = random.randint(0, 1)
    age = random.randint(1, 5)
    intelligence = random.random()

    return [body_fat, dog_breed, weight, has_won_award, is_vaccinated, age, intelligence]

def fitness_function(population):
    score_array = []
    
    for i in range( len(population) ):
        score = 0

        if( population[i][DOG1][BREED] == population[i][DOG2][BREED]):
            score += 1
        
        for dog_i in range( len(population[i]) ):
            weight = int( population[i][dog_i][WEIGHT] )
            body_fat = float( population[i][dog_i][BODY_FAT] )
            age = int( population[i][dog_i][AGE] )
            has_won_award = int( population[i][dog_i][WON_AWARD] )

            weight_category = None
            if( weight < 40 ):
                weight_category = 'Poor'
                score -= 1
            elif( weight >= 40 and  weight <= 80):
                weight_category = 'Good'
            else:
                weight_category = 'Average'
    
            if( body_fat >= 0 and  body_fat <= 0.25):
                body_fat_category = 'Excellent'
            elif( body_fat >= 25 and  body_fat <= 75):
                body_fat_category = 'Average'
            elif( body_fat >= 75):
                body_fat_category = 'Poor'

            if( age == 3 ):
                score += 1
            elif( age > 3 and has_won_award == 1):
                score -= 1
            elif( age > 3 and has_won_award is not 1):
                score -= 2

            if(has_won_award and weight_category == 'Good' ):
                score += 1

        score_array.append(score)

    return np.array( score_array )


def selection(score_array, population,top_number):
    global highest_score
    def get_ranking(population):
        temp = population.argsort()
        ranks = np.empty_like(temp)
        ranks[temp] = np.arange(len(population))
        ranking = {}
        
        for i in range(0, len(population)):
            ranking[ranks[i]] = population[i]

        return ranking 

    ranking = get_ranking(score_array)

    selectionResults = []
    ranking_len = len(ranking)
    if(ranking[0]>highest_score):
        highest_score = ranking[0]
        print("Highest Score:",highest_score)

    for i in range( 0, top_number ):
        index = int( list(ranking).index( ranking_len - 1 - i) )
        selectionResults.append(population[index])

    for i in range(0, ranking_len - top_number):
        rand_number = random.randint(0, ranking_len - 1 )
        selectionResults.append(population[rand_number])

    return selectionResults


def crossover(selected_population,top_number):
    children = []

    def cross_breed( pair1 , pair2 ):
        ranking_len = len(pair1[0])
        rand_number1 = random.randint(0, ranking_len - 1 ) 
        rand_number2 = random.randint(0, ranking_len - 1 ) 

        startGene = min(rand_number1, rand_number2)
        endGene = max(rand_number1, rand_number2)

        chromosome11 = pair1[DOG1][startGene:endGene]
        chromosome12 = pair1[DOG2][startGene:endGene]

        chromosome21 = pair2[DOG1][startGene:endGene]
        chromosome22 = pair2[DOG2][startGene:endGene]
        
        pair1[DOG1][startGene:endGene], pair1[DOG2][startGene:endGene] = chromosome22, chromosome21
        pair2[DOG1][startGene:endGene], pair2[DOG2][startGene:endGene] = chromosome12, chromosome11

        return pair1, pair2

    for i in range(0,top_number):
        children.append(selected_population[i])

    pool = random.sample(selected_population, len(selected_population))
    length = len(selected_population) - top_number

    for i in range(0, length):
        pair1, pair2 = cross_breed(pool[i], pool[len(selected_population)-i-1])
        pool[i],pool[len(selected_population)-i-1] = pair1, pair2

    for i in range(top_number, len(selected_population) ):
        children.append(pool[i])
        
    return children


def mutate_population(population, mutation_rate, top_selected):
    mutated_population = population.copy()
    for pair in range(top_selected, len(mutated_population)-1):
        for dog in range(0, 2):
            if(random.random() < mutation_rate):
                mutated_population[pair][dog][BODY_FAT] = random.random()
                
            if(random.random() < mutation_rate):
                mutated_population[pair][dog][BREED] = random.choice(breed)

            if(random.random() < mutation_rate):
                mutated_population[pair][dog][WEIGHT] = random.randint(1, 100 ) 
                
            if(random.random() < mutation_rate):
                mutated_population[pair][dog][WON_AWARD] = random.randint(0, 1)

            if(random.random() < mutation_rate):
                mutated_population[pair][dog][AGE] = random.randint(1, 5)
            
            if(random.random() < mutation_rate):
                mutated_population[pair][dog][INTELLIGENCE] = random.random()

            if(random.random() < mutation_rate):
                mutated_population[pair][dog][IS_VACCINATED] = random.randint(0, 1)

    return mutated_population

POPULATION_NUMBER = 1000
number_of_generation = 500

mutation_rate = 0.01
top_number = 400
highest_score = 0

population = []

for i in range(POPULATION_NUMBER):
    dog1 = individual_dog()
    dog2 = individual_dog()
    population.append([dog1,dog2])

mutation_rate = 0.1

for gen in range(number_of_generation):
    score_array = fitness_function(population)
    selected_population = selection(score_array,population,top_number)
    crossover_population = crossover(selected_population,top_number)
    mutated_population = mutate_population(crossover_population, mutation_rate, top_number)
    population = mutated_population

