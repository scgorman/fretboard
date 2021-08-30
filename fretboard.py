noteCircle = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

tune = ''
fretboardLength = int

# initial input
tune = input('What is the string tuned to?\n')
tune = tune.upper()

fretboardLength = int(input('How many frets does the guitar have?\n'))

# figure out notes
notes = []
initialPosition = int(noteCircle.index(tune))

notes.append(noteCircle[initialPosition])
currentPosition = initialPosition + 1

for fret in range(fretboardLength):
	#	++fret
	notes.append(noteCircle[currentPosition])
	if currentPosition == 11:
		currentPosition = 0
	else:
		currentPosition += 1
	print(notes)