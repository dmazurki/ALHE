# ALHE Project

Authors: Damian Mazurkiewicz and Hubert Legęć

Problem:
Placing of cameras in the room to cover all the area using as few cameras as possible.

Algorithm:
To find solution simulated annealing algorithm is used.

Modules description:
1.Metaheuristic - contains implementation of simulated annealing algorithm.
2.Temperature - contains calculations used by algorithm to determine temperature
3.Camera placing - contains representation of problem, camera with its state, quality function.
  It also has some geometrical utils to calculate camera vision area.
4.Experiments - contains some experiments, which change start parameters and present differences in results.