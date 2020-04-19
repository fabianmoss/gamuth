"""
.. module:: musictheory
    :synopsis: a python module for music theory
 
.. moduleauthor:: Fabian C. Moss <fabianmoss@gmail.com>
"""

import numpy as np
import re

diatonic = np.array(list("FCGDAEB"))
accidentals = ["#", "b"]

class Tone:
    """ Class for tones. """
    def __init__(self, octave=None, fifth=None, third=None, name=None):
        # coordinates
        self.octave = octave
        self.fifth = fifth
        self.third = third
        self.euler_coordinate = np.asarray((self.octave, self.fifth, self.third))
        self.fifths_pos = fifth + 4 * third

        # names and labels
        self.accidentals = self.get_accs()
        self.step = self.get_step()
        self.syntonic = self.get_syntonic()
        self.label = self.get_label()

        # other representations
        self.midi_pitch = self.get_midi_pitch()
        self.frequency = self.get_frequency()
        self.pitch_class_chromatic = self.get_pitch_class_chromatic()
        self.pitch_class_circle_of_fifths = self.get_pitch_class_circle_of_fifths()

    def get_accs(self):
        '''
        Gets the accidentals of the tone (flats (`b`) or sharps (`#`))..

        Args:
            None

        Returns:
            str: The accidentals of the tone.
        '''
        accs = np.divmod(self.fifths_pos + 1, 7)[0] # shift 0 to "C"
        return np.abs(accs) * "b" if accs < 0 else np.abs(accs) * "#"

    def get_step(self):
        return diatonic[ (np.divmod(self.fifths_pos, 7)[1] + 1) % 7 ] # shift 0 to "C"

    def get_syntonic(self):
        return self.third * "\'" if self.third > 0 else np.abs(self.third) * ","

    def get_label(self):
        return self.step + self.accidentals + self.syntonic + str(self.octave)

    def get_pitch_class_circle_of_fifths(self, start=0):
        '''Get the pitch class on the tone on the circle of fifths.

        Args:
            start (int): Line-of-fifths number of the tone that gets mapped to 0 (default: C=0).

        Returns:
            int: The pitch class of the tone on the circle of fifths.
        '''
        return start + self.fifths_pos % 12

    def get_pitch_class_chromatic(self, start=0):
        '''Get the pitch class on the tone on the chromatic circle.

        Args:
            start (int): Tone that that gets mapped to 0 (default: C=0).

        Returns:
            int: The pitch class of the tone on the chromatic circle.
        '''
        return ((self.fifths_pos % 12) * 7) % 12

    def get_midi_pitch(self):
        '''Get the MIDI pitch of the tone.

        Args:
            None

        Returns:
            int: The MIDI pitch of the tone if it is in MIDI pitch range (0--128)
        '''
        m = 60 + 12 * self.octave + 7 * self.fifth + 4 * self.third

        if m in range(0,128):
            return m
        else:
            print("Outside of MIDI range.")

    def get_frequency(self, chamber_tone=440.0, precision=2):
        '''
        Get the frequency of the tone.

        Args:
            chamber_tone (float): The frequency in Hz of the chamber tone. Default: 440.0 (A)
            precision (int): Rounding precision for the frequency.

        Returns:
            float: The frequency of the tone in Hertz (Hz).
        '''
        f = 440 * 2 ** ((self.midi_pitch - 69)/12)
        return round(f, precision)

    # def get_coordinates(self):
    #     match = re.match("([A-G]#*|b*)(,*|'*)\d", self.name)
    #     self.step = match[0]
    #     self.accidentals = match[1]
    #     self.syntonic = match[2]
    #     self.octave = match[3]

    # if all(v is not None for v in [self.octave, self.fifth, self.third, self.name]):
    #     assert self.name == self.inferred_name

class Interval:
    """ Class for an interval between two tones `s` (source) and `t` (target). """
    def __init__(self, source, target):
        self.source = source
        self.target = target

        self.interval = target.euler_coordinate - source.euler_coordinate
    
    def euclidean_distance(self):
        '''
        Calculates the Euclidean distance between two tones
        with coordinates in Euler space.

        Args:
            None
            
        Returns:
            float: The Euclidean distance between two tones `s` (source) and `t` (target).        
        '''
        s = np.asarray(self.source.euler_coordinate)
        t = np.asarray(self.target.euler_coordinate)
        return np.linalg.norm(t - s)

    # def get_interval_name(self):
