import numpy as np,operator
import random

def fitness_function(image_population,ideal_score,block_dimension):
    img_scores = []
    for img in range(0, len(image_population) ):
        img_score = get_image_score(image_population[img],block_dimension)
        score = mean_squared_error(img_score,ideal_score)
        img_scores.append(score)
    return img_scores
    
def get_image_score(image,block_dimension):
    row, column = image.shape
    row_sqr,col_sqr = block_dimension

    img_scores = []
    for i in range(0, int(row/row_sqr) ):
        index_i = i*row_sqr
        score = []
        for j in range(0, int(column/col_sqr) ):
            index_j = j*col_sqr
            average = image[index_i:index_i+row_sqr,index_j:index_j+col_sqr].sum()/(row_sqr*col_sqr) 
            score.append(average)

        img_scores.append(score)
    
    return img_scores

def mean_squared_error(score,ideal_score):
    mse = (np.array(score) - np.array(ideal_score))**2
    return mse

def get_ranking(population):
    temp = population.argsort()
    ranks = np.empty_like(temp)
    ranks[temp] = np.arange(len(population))
    ranking = {}
    
    for i in range(0, len(population)):
        ranking[ranks[i]] = population[i]

    return ranking 

def selection(score, population, top_number):
    global highest_score
    total_sum_score = []
    for i in range(0, len(score) ):
        total_sum_score.append(np.sum(score[i]))

    scores = np.array(total_sum_score)
    ranking = get_ranking(scores)

    selectionResults = []
    ranking_len = len(ranking)
    if(highest_score>ranking[0] or highest_score == 0):
        highest_score = ranking[0]
        print("Highest Score:",ranking[0])

    for i in range( 0, top_number ):
        index = int( list(ranking).index( i) )
        selectionResults.append(population[index])

    for i in range(0, ranking_len - top_number):
        rand_number = random.randint(0, ranking_len - 1 )
        selectionResults.append(population[rand_number])

    return selectionResults

# Cross over happens by dividing image into 4 division
def crossover_function(population,top_selection,probability_crossover=0.5):
    crossover_result = []
    population_len = len(population)

    for i in range( 0, top_selection ):
        crossover_result.append(population[i])

    for i in range(top_selection, population_len , 2):
        parent1, parent2 = population[i], population[i+1]

        if( random.random() < probability_crossover ):
            row_pt = random.randint(0, len(parent1) -1) + 1
            col_pt = random.randint(0, len(parent1[0]) -1) + 1

            child1 = np.full_like(parent1,0)
            child2 = np.full_like(parent1,0)

            child1[:row_pt,:col_pt]  = parent1[:row_pt,:col_pt] # UPPER LEFT
            child1[row_pt:,:col_pt]  = parent2[row_pt:,:col_pt] # LOWER LEFT
            child1[:row_pt,col_pt:]  = parent1[:row_pt,col_pt:] # UPPER RIGHT
            child1[row_pt:,col_pt:]  = parent2[row_pt:,col_pt:] # LOWER RIGHT

            child2[:row_pt,:col_pt]  = parent2[:row_pt,:col_pt] # UPPER LEFT
            child2[row_pt:,:col_pt]  = parent1[row_pt:,:col_pt] # LOWER LEFT
            child2[:row_pt,col_pt:]  = parent2[:row_pt,col_pt:] # UPPER RIGHT
            child2[row_pt:,col_pt:]  = parent1[row_pt:,col_pt:] # LOWER RIGHT
        
            crossover_result.append(child1)
            crossover_result.append(child2)
        else:
            crossover_result.append(parent1)
            crossover_result.append(parent2)

    return crossover_result

# Mutation happen in block square with random
def mutation(population, top_selection,block_dimension, probability_mutation=0.001):
    population_len = len(population)
    mutated_population = list(population)

    for img_index in range( population_len - top_selection, population_len ):
        row, column = mutated_population[img_index].shape
        row_sqr,col_sqr = block_dimension

        for i in range(0, int(row/row_sqr) ):
            index_i = i*row_sqr
            for j in range(0, int(column/col_sqr) ):
                index_j = j*col_sqr
                if( random.random() < probability_mutation ):
                    random_number = random.random()
                    mutated_block = np.full_like(mutated_population[img_index][index_i:index_i+row_sqr,index_j:index_j+col_sqr], random_number)
                    mutated_population[img_index][index_i:index_i+row_sqr,index_j:index_j+col_sqr] =  mutated_block

    return mutated_population

POPULATION_NUMBER = 100
np.random.seed(0)

block_dimension = (4,4) # 4 x 4
image_dimension = (256,256)

img_row,img_col = image_dimension
highest_score = 0

mona_lisa_image = np.random.rand(img_row,img_col)
population = np.random.rand(POPULATION_NUMBER,img_row,img_col)
top_selection = 40

ideal_score = get_image_score(mona_lisa_image,block_dimension)

# This might take a while
number_of_generation = 200

for gen in range(number_of_generation):
    population_score = fitness_function( population, ideal_score, block_dimension )
    selected_population = selection( population_score, population, top_selection)
    crossover_population = crossover_function( selected_population, top_selection )
    mutated_population = mutation( crossover_population, top_selection, block_dimension )
    population = mutated_population