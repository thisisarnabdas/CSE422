import random

def calculate_fitness(chromosome, num_courses, num_timeslots):
    overlap_penalty = 0
    consistency_penalty = 0
    course_count = [0] * num_courses
    for timeslot in range(num_timeslots):
        segment = chromosome[timeslot * num_courses:(timeslot + 1) * num_courses]
        scheduled_courses = sum(segment)
        if scheduled_courses > 1:
            overlap_penalty += (scheduled_courses - 1)
        for course_index in range(num_courses):
            if segment[course_index] == 1:
                course_count[course_index] += 1
    for count in course_count:
        if count != 1:
            consistency_penalty += abs(count - 1)
    return -(overlap_penalty + consistency_penalty)


def select_parents(population):
    return random.sample(population, 2)

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2

def mutate(chromosome):
    mutation_index = random.randint(0, len(chromosome) - 1)
    chromosome[mutation_index] = 1 - chromosome[mutation_index]
    return chromosome

def initialize_population(population_size, num_courses, num_timeslots):
    population = []
    for individual in range(population_size):
        chromosome = [random.randint(0, 1) for i in range(num_courses * num_timeslots)]
        # print(chromosome)
        population.append(chromosome)
    return population

def genetic_algorithm(num_courses, num_timeslots, population_size, max_iterations):
    population = initialize_population(population_size, num_courses, num_timeslots)
    best_fitness = float('-inf')
    best_chromosome = None
    for generation in range(max_iterations):
        new_population = []
        for pair in range(population_size // 2):
            parent1, parent2 = select_parents(population)
            offspring1, offspring2 = crossover(parent1, parent2)
            offspring1 = mutate(offspring1)
            offspring2 = mutate(offspring2)
            new_population.extend([offspring1, offspring2])
        population = new_population
        for chromosome in population:
            fitness = calculate_fitness(chromosome, num_courses, num_timeslots)
            if fitness > best_fitness:
                best_fitness = fitness
                best_chromosome = chromosome
    return best_chromosome, best_fitness


population_size = 100
max_iterations = 1000
input_line = input()
num_courses, num_timeslots = map(int, input_line.split())
courses = [input() for i in range(num_courses)]
best_chromosome, best_fitness = genetic_algorithm(num_courses, num_timeslots, population_size, max_iterations)
print(''.join(map(str, best_chromosome)))
print(best_fitness)

population = initialize_population(population_size, num_courses, num_timeslots)
parent1, parent2 = select_parents(population)
def two_point_crossover(parent1, parent2):
    length = len(parent1)
    point1 = random.randint(1, length - 2)
    point2 = random.randint(point1 + 1, length - 1)
    offspring1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    offspring2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
    return offspring1, offspring2

offspring1, offspring2 = two_point_crossover(parent1, parent2)
print(f"Parent 1: {parent1}")
print(f"Parent 2: {parent2}")
print(f"Offspring 1: {offspring1}")
print(f"Offspring 2: {offspring2}")

