l = []
prev = ""
tot = 0
count = 0

with open("Intervals_122014.csv", "r") as f:
    f.readline()
    for line in f:
        temp = line.split(',')
        if prev != temp[0]:
            if count != 0 and tot != 0:
                print("{},{},{}".format(prev, tot, tot/count))
            prev = temp[0]
            count = 0
            tot = 0
        try:
            tot += float(temp[4])
            count += 1
        except ValueError:
            pass
