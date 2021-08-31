# Class module

note_circle = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']


class Guitar:

    def __init__(self, guitar_string_count, guitar_string_pitches, fretboard_length):
        self.guitar_string_count = guitar_string_count
        self.guitar_string_pitches = guitar_string_pitches
        self.fretboard_length = fretboard_length

    def set_guitar_string_count(self, count):
        self.guitar_string_count = count

    def set_guitar_string_pitches(self, pitches):
        self.guitar_string_pitches = pitches

    def set_fretboard_length(self, length):
        self.fretboard_length = length

    def get_guitar_string_count(self):
        return self.guitar_string_count

    def get_guitar_string_pitches(self):
        return self.guitar_string_pitches

    def get_fretboard_length(self):
        return self.fretboard_length


class GuitarString:

    def __init__(self, pitch, fretboard_length, notes):
        self.pitch = pitch
        self.fretboard_length = fretboard_length
        self.notes = notes

    def calculate_notes(self, pitch, fretboard_length):

        notes = []
        initial_position = int(note_circle.index(pitch))

        notes.append(note_circle[initial_position])
        current_position = initial_position + 1

        for fret in range(fretboard_length):

            notes.append(note_circle[current_position])

            if current_position == 11:
                current_position = 0
            else:
                current_position += 1

        self.notes = notes

    def set_pitch(self, pitch):
        self.pitch = pitch

    def set_fretboard_length(self, length):
        self.fretboard_length = length

    def get_pitch(self):
        return self.pitch


class Fretboard:

    def __init__(self, guitar_strings, fretboard):
        self.guitar_strings = guitar_strings
        self.fretboard = fretboard

    def build_fretboard(self, guitar_strings, fretboard):
        for guitar_string in guitar_strings:
            for note in guitar_string.notes():
                fretboard.append(note)
        self.fretboard = fretboard

    def set_guitar_strings(self, guitar_strings):
        self.guitar_strings = guitar_strings

    def get_guitar_strings(self):
        return self.guitar_strings


class Visualizer:

    def __init__(self, fretboard_notes):
        self.fretboard_notes = fretboard_notes
