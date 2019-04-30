import numpy
import sys

def calculate_distance(atom1, atom2):
    bond_length = numpy.sqrt((atom1[0]-atom2[0])**2+(atom1[1]-atom2[1])**2+(atom1[2]-atom2[2])**2)

    return bond_length

def bond_check(atom_distance, minimum_length=0, maximum_length=1.5):
    if atom_distance > minimum_length and atom_distance <= maximum_length:
        return True
    else:
        return False

def open_xyz(filename):
    xyz_file = numpy.genfromtxt(fname=filename, skip_header=2, dtype='unicode')
    symbols = xyz_file[:,0]
    coord = (xyz_file[:,1:])
    coord = coord.astype(numpy.float)
    return symbols, coord

if __name__ == "__main__":

	if len(sys.argv) != 2:
		print('Incorrect input! Please try again.')
		exit()

	xyzfilename = sys.argv[1]
	symbols, coord = open_xyz(xyzfilename)
	for numA, atomA in enumerate(coord):
		for numB, atomB in enumerate(coord):
			if numB > numA:
				bond_length_AB = calculate_distance(atomA, atomB)
				if bond_check(bond_length_AB):
					print(F'{symbols[numA]} to {symbols[numB]} : {bond_length_AB:.3f}')
