import sys

def sofp_marker(s):
	v = []
	for i, c in enumerate(s):
		if c not in v:
			v.append(c)
		else:
			ind = v.index(c)
			v = v[ind+1:]
			v.append(c)
		
		if len(v) == 14:
			return i+1
	raise Exception("No 14 unique characters found")

if __name__ == '__main__':
	input = open(sys.argv[1] if len(sys.argv) > 1 else 'input.in').read()
	print("Part 2: ", sofp_marker(input))
