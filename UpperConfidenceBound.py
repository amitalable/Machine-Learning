import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import math

class UpperConfidenceBound:
  def __init__(self,path,  N, d):
    self.__dataset = pd.read_csv(path)
    self.__N = N
    self.__d = d
    self.__movie_selected = []
    self.__number_of_selection = [0] * self.__d 
    self.__total_rank = 0
    self.__sum_of_movie_rank = [0]*self.__d  

  def implement_ucb(self):
    for user in range(1, self.__N + 1):
      movie = -1
      max_upper_bound = 0 
      for movie_index in range(0, self.__d):
        if self.__number_of_selection[movie_index] > 0:
          avg_rank = self.__sum_of_movie_rank[movie_index] / self.__number_of_selection[movie_index]
          delta_i = math.sqrt(1.5 * (math.log(user) / self.__number_of_selection[movie_index]))
          upper_bound = avg_rank + delta_i
        else:
          upper_bound = 1e500
        if upper_bound > max_upper_bound:
          max_upper_bound = upper_bound
          movie = movie_index
      self.__movie_selected.append(movie)
      self.__number_of_selection[movie] += 1
      ranks = self.__dataset.values[user-1, movie]
      self.__sum_of_movie_rank[movie] += ranks
      self.__total_rank += ranks
  
  def visualization(self):
    plt.hist(self.__movie_selected)
    plt.title('Histogram of Movies Ranks')
    plt.xlabel('Movies')
    plt.ylabel('Number of times each Movie was liked')
    plt.show()



path = "Book1.csv"
N = 100
d = 5
ucb = UpperConfidenceBound(path,N,d)
ucb.implement_ucb()
ucb.visualization()
