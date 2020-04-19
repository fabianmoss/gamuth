from theory import Tone, Interval

if __name__ == "__main__":
    s = Tone(2,3,1)
    t = Tone(-2,1,4)
    i = Interval(source=s,target=t)
    
    print(s.euler_coordinate)
    print(t.euler_coordinate)
    print(i.source.euler_coordinate)
    print(i.euclidean_distance())