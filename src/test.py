from theory import Tone, Interval
import numpy as np

if __name__ == "__main__":
    s = Tone(0,-1,2) # Eb''0
    t = Tone(0,-1,0) # G0
    i = Interval(source=s,target=t)

    print(s.label)
    print(t.label)

    # print(s.accidentals)
    # print(s.step)
    
    # print(s.euler_coordinate)
    # print(t.euler_coordinate)
    # print(i.source.euler_coordinate)
    # print(i.interval)
    # print(i.euclidean_distance())