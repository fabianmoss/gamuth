import numpy as np

class Tone:
    def __init__(self, octave, fifth, third):
        self.octave = octave
        self.fifth = fifth
        self.third = third

        self.euler_coordinate = np.asarray((self.octave, self.fifth, self.third))

class Interval:
    def __init__(self, source, target):
        self.source = source
        self.target = target
    
    def euclidean_distance(self):
        s = np.asarray(self.source.euler_coordinate)
        t = np.asarray(self.target.euler_coordinate)
        return np.linalg.norm(t - s)
