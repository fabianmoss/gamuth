from main import Tone, Interval
import numpy as np

if __name__ == "__main__":
    s = Tone(0,-1,-1) # Db,0
    t = Tone(0,1,1) # B'0
    i = Interval(source=s,target=t)

    print(s.label)
    print(t.label)
    print(i.interval)

    print(t.pitch_class_chromatic)
    print(s.pitch_class_circle_of_fifths)
    print(s.midi_pitch, t.midi_pitch)
    print(s.frequency,t.frequency)

    # print(s.accidentals)
    # print(s.step)
    
    # print(s.euler_coordinate)
    # print(t.euler_coordinate)
    # print(i.source.euler_coordinate)
    # print(i.interval)
    # print(i.euclidean_distance())