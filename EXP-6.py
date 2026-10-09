def vacuum_cleaner():
    room = {'A': 'Dirty', 'B': 'Dirty'}
    pos = 'A'
    while 'Dirty' in room.values():
        print("Vacuum at", pos)
        if room[pos] == 'Dirty':
            print("Cleaning", pos)
            room[pos] = 'Clean'
        if pos == 'A':
            pos = 'B'
        else:
            pos = 'A'
    print("All rooms are clean!")
vacuum_cleaner()