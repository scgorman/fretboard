### Class module

class Guitar:

    def __init__(self, guitar_string_count, guitar_string_pitches, fretboard_length):
        self.guitar_string_count = guitar_string_count
        self.guitar_string_tunings = guitar_string_pitches
        self.fretboard_length = fretboard_length

    @classmethod
    def set_guitar_string_count(cls, count):
        guitar_string_count = count

    @classmethod
    def set_guitar_string_pitches(cls, pitches):
        guitar_string_pitches = pitches

    @classmethod
    def set_fretboard_length(cls, length):
        fretboard_length = length

class Fretboard:

    def __init__(self, ):
