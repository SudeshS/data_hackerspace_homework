#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np
import math

def histogram_times(filename):
    with open(filename, 'r') as csv_file:
        csv_data = csv.reader(csv_file)
        counter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for row in csv_data:
                time = row[1].split(':')
                try:
                    hour = int(time[0])
                    counter[hour-1] += 1
                except:
                    continue
        return counter

def weigh_pokemons(filename, weight):
    pokemon_names = []
    
    with open(filename) as json_file:
        json_data = json.load(json_file)
        for pokemon in range(len(json_data["pokemon"])):
            real_weight = float(json_data["pokemon"][pokemon]["weight"].split(" ")[0])
            if real_weight == weight:
                pokemon_names.append(json_data["pokemon"][pokemon]["name"])
    return pokemon_names

def single_type_candy_count(filename):
    with open(filename) as json_file:
        json_data = json.load(json_file)
        sum = 0
        for pokemon in range(len(json_data["pokemon"])):
            if len(json_data["pokemon"][pokemon]["type"]) == 1:
                try:
                    sum += int(json_data["pokemon"][pokemon]["candy_count"])
                except:
                    continue
    return sum

def reflections_and_projections(points):
    angle_matrix = np.matrix([[math.cos(math.pi/2), -math.sin(math.pi/2)], [math.sin(math.pi/2), math.cos(math.pi/2)]])
    
    for i in range(len(points[1])):
        distance = 1 - points[1][i] 
        points[1][i] = 1 + distance
    
    point_matrix = np.matrix(points)
    translated_matrix = angle_matrix * point_matrix
    
    projection_matrix = np.matrix([[1, 3], [3, 9]])
    projection_scalar = 1/10

    projected_matrix = projection_scalar * (projection_matrix * translated_matrix)
    return projected_matrix

def normalize(image):
    min_pixel = np.amin(image)
    max_pixel = np.amax(image)

    for (x,y) in np.ndenumerate(image): 
        image[x][y] -= min_pixel
    normalization = 255/(max_pixel - min_pixel)
    normalized_array = normalization * image
    return normalized_array

def sigmoid_normalize(image, a):
    return sigmoid_helper(image, a)

def sigmoid_helper(image, a):
    255*(1 + math.e**((-a**-1)(p-128)))**-1

print(single_type_candy_count("pokedex.json"))
print(reflections_and_projections(np.array([[1, 3, 5, 7], [2, 4, 6, 8]])))