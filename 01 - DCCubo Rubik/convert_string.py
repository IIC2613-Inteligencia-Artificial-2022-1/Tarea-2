color = True

COLORS = {
'O':(255, 165, 0),
'W': (255, 255, 255),
'Y': (255, 255, 0),
'G': (0, 255, 0),
'B': (0, 0 , 255),
'R': (255, 0 , 0)
}             


def parse_cube(cube):
	cube = cube.replace("O", "U").replace("Y", "L").replace("W", "F").replace("W", "F").replace("R", "D").replace("G", "R")
	parsed_cube = []

	parsed_cube.append(cube[0:9])

	for e in range(3, 7):
		for i in range(3 * e, 3 * e + 12 * 3, 12):
			parsed_cube.append(cube[i:i + 3])

	parsed_cube.append(cube[45:54])

	return ''.join(parsed_cube) +'\n'

def parse_algorithm(algorithm):
	algorithm = algorithm.replace('->', ' ').replace('i', '\'')

	return algorithm[1:] +'\n'

def print_fun(string):
	new_str = ''
	if not color:
		print(string)
	else:
		for i in range(len(string)):
			col = COLORS.get(string[i])
			if col and not (string[i+1] == 'i' or string[i+1] == '-'):
				new_str += colored(*col,string[i])
			else:
				new_str += string[i]
		print(new_str)

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
