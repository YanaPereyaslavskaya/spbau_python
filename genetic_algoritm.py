import random
import numpy as np
from scipy.stats import kstest

# размер популяции
population_size = 100

# число поколений
n_generations = 50

# вероятность кроссинговера
pc = 0.7

# вероятность мутации
pm = 0.1


# задаём функцию, для которой будем подбирать параметры
def test_func(x):
    return np.sin(x)


# функция для генерации случайных особей
def random_individual(bounds):
    return np.array([random.uniform(bounds[i][0], bounds[i][1]) for i in range(len(bounds))])


# функция оценки приспособленности особи
def fitness(individual):
    data = test_func(individual)
    d, p_value = kstest(data, 'norm')
    return 1 - d


# функция для селекции особей
def selection(population):
    fitness_vals = [fitness(individual) for individual in population]
    return [population[i] for i in np.argsort(fitness_vals)[-int(population_size * 0.2):]]


# функция для кроссинговера особей
def crossover(parent1, parent2):
    if random.random() < pc:
        if len(parent1) > 1:
            crossover_point = random.randint(1, len(parent1) - 1)
        else:
            crossover_point = 0
        child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
        child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
        return child1, child2
    else:
        return parent1, parent2


# функция для мутации особи
def mutation(individual):
    if random.random() < pm:
        mutation_point = random.randint(0, len(individual) - 1)
        individual[mutation_point] = random.uniform(-5, 5)
    return individual


# задаём границы значений для каждой случайной величины
bounds = [(-5, 5)]

# генерируем начальную популяцию
population = [random_individual(bounds) for _ in range(population_size)]

# запускаем алгоритм
for i in range(n_generations):
    # селекция
    selected = selection(population)

    # кроссинговер
    offspring = []
    while len(offspring) < population_size:
        parent1 = random.choice(selected)
        parent2 = random.choice(selected)
        child1, child2 = crossover(parent1, parent2)
        offspring.append(mutation(child1))
        offspring.append(mutation(child2))

    # заменяем текущую популяцию потомками
    population = offspring

    # дополняем текущую популяцию случайно сгенерированными особями
    population += [random_individual(bounds) for _ in range(population_size - len(population))]

    # выводим информацию о текущем лучшем решении
    best = max(population, key=fitness)
    print("Generation {}, Best Fitness: {:.4f}, Parameters: {}".format(i + 1, fitness(best), best))
