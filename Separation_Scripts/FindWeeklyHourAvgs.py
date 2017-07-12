import sys
from datetime import datetime as dt

class User:
    def __init__(self, ID = ""):
        self.totals = [0.0] * 7 * 24
        self.counts = [0] * 7 * 24
        self.avgs = [""] * 7 * 24
        self.ID = ID
        self.count = 0
    def nextLine(self, entry):
        arr = entry.split(',')

        if self.ID != arr[0]:
            if self.count > 0:
                print(str(self))
            self.__init__(arr[0])

        self.count += 1

        try:
            reading = float(arr[4])
            dayIndex = dt.strptime(arr[3].split(' ')[0],'%d-%b-%Y').weekday()
            hourIndex = int(arr[3].split(" ")[1].split(":")[0])

            self.totals[dayIndex * 24 + hourIndex] += reading
            self.counts[dayIndex * 24 + hourIndex] += 1
        except Exception as e:
            #print(e)
            pass

    def calcAvgs(self):
        for i in range(len(self.avgs)):
            self.avgs[i] = str(0 if self.counts[i] == 0 else self.totals[i] / self.counts[i])
    def __str__(self):
       self.calcAvgs()
       return self.ID + "," + ",".join(self.avgs)


prevID = ""
user = User("")

print('"Id","{}"'.format('","'.join([str(i) for i in range(len(user.avgs))])))

with open(sys.argv[1], "r") as f:
    f.readline()
    for line in f:
        user.nextLine(line)
