import numpy as np
import re

diatonic = np.array(list("FCGDAEB"))
accidentals = ["#", "b"]

class Tone:
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

    def get_accs(self):
        accs = np.divmod(self.fifths_pos + 1, 7)[0] # shift 0 to "C"
        return np.abs(accs) * "b" if accs < 0 else np.abs(accs) * "#"

    def get_step(self):
        return diatonic[ (np.divmod(self.fifths_pos, 7)[1] + 1) % 7 ] # shift 0 to "C"

    def get_syntonic(self):
        return self.third * "\'" if self.third > 0 else np.abs(self.third) * ","

    def get_label(self):
        return self.step + self.accidentals + self.syntonic + str(self.octave)

    # def get_coordinates(self):
    #     match = re.match("([A-G]#*|b*)(,*|'*)\d", self.name)
    #     self.step = match[0]
    #     self.accidentals = match[1]
    #     self.syntonic = match[2]
    #     self.octave = match[3]

    # if all(v is not None for v in [self.octave, self.fifth, self.third, self.name]):
    #     assert self.name == self.inferred_name

class Interval:
    def __init__(self, source, target):
        self.source = source
        self.target = target

        self.interval = target.euler_coordinate - source.euler_coordinate
    
    def euclidean_distance(self):
        s = np.asarray(self.source.euler_coordinate)
        t = np.asarray(self.target.euler_coordinate)
        return np.linalg.norm(t - s)

    # def get_interval_name(self):
