import heuristics
import os

from convert_string import parse_cube, parse_algorithm, print_fun
from astar import Astar

os.system("color")
solved = []

with open("cubos_ejemplo.txt", "r") as file:
	for line in file:
		astar = Astar(line.strip(), heuristics.example_heuristic)
		solved.append(parse_cube(line.strip()))
		sol, exp, tim = astar.search()
		print_fun(f'''
		Solution:	    {sol}
		Expanded nodes: {exp}
		Time:		    {tim}
		-----------------------------------------------------
		'''
		)
		solved.append(parse_algorithm(sol))

# Con esto obtienen un archivo de texto en el formato necesario para el visualizador 3D
with open("parsed.txt", "w") as file:
	file.writelines(solved)
