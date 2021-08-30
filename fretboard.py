def main():

	note_circle = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

	# # initial input
	# # set amount of guitar strings to 6 rather than use an input for convenient testing
	guitar_string_amount = 6
	guitar_string_tunes = []

	# # set tunings to E standard tuning for convenient testing
	# print('Start at the high string.')
	# for guitar_string in range(guitar_string_amount):
	# 	tune = input('What is string ' + str(guitar_string + 1) + ' tuned to?\n')
	# 	tune = tune.upper()
	# 	guitar_string_tunes.append(tune)
	guitar_string_tunes = ['E', 'A', 'D', 'G', 'B', 'E']

	# # fretboard_length set to 12 for convenient testing. A fretboard length of 12 should end with the same note as the
	# # open string. For example, an E string should cycle through the note circle and the 12th fret should be E.
	# fretboard_length = int(input('How many frets does the guitar have?\n'))
	fretboard_length = 12

	fretboard_strings = []
	for guitar_string in guitar_string_tunes:

		# figure out notes
		notes = []
		initial_position = int(note_circle.index(guitar_string))

		notes.append(note_circle[initial_position])
		current_position = initial_position + 1

		for fret in range(fretboard_length):

			notes.append(note_circle[current_position])

			if current_position == 11:
				current_position = 0
			else:
				current_position += 1

		# Append fretboard_strings list with a list containing the notes of the current string
		fretboard_strings.append(notes)

	# for guitar_string in fretboard_strings:
	# 	for note in guitar_string:
	# 		print(note)
	# 	print('\n')

	fretboard_diagram = ""
	for guitar_string in fretboard_strings:
		fretboard_diagram = fretboard_diagram + guitar_string[0]
		if guitar_string[0].endswith('#'):
			fretboard_diagram = fretboard_diagram + ' '
		else:
			fretboard_diagram = fretboard_diagram + '  '
	fretboard_diagram = fretboard_diagram + '\n'

	for i in range(len(fretboard_strings)):
		fretboard_diagram = fretboard_diagram + '-- '
	fretboard_diagram = fretboard_diagram + '\n'

	for fret in range(fretboard_length):
		for guitar_string in fretboard_strings:
			fretboard_diagram = fretboard_diagram + guitar_string[fret + 1]
			if fretboard_diagram.endswith('#'):
				fretboard_diagram = fretboard_diagram + ' '
			else:
				fretboard_diagram = fretboard_diagram + '  '
		fretboard_diagram = fretboard_diagram + '\n'
	print(fretboard_diagram)


main()