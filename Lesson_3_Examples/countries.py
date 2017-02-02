# Given the variable countries defined as:

# #             Name    Capital  Populations (millions)
# countries = [['China','Beijing',1350],
#              ['India','Delhi',1210],
#              ['Romania','Bucharest',21],
#              ['United States','Washington',307]]
#
# print "Capital of India is", countries[1][1]
#
# # Write code to print out the capital of India
# # by accessing the list

# Given the variable countries defined as:


#             Name      Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

population_of_romania = countries[2][2]
print population_of_romania
population_of_china = countries[0][2]
print population_of_china
multiple_romania_population = float(population_of_china)/float(population_of_romania)
print "Romania's population is the population", multiple_romania_population

## What multiple of Romania's population is the population
# of China? Calculate this by accessing the list and
# dividing the population of China (1350)
# by the population of Romania (21).
# Please print your result.
