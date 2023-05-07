import csv

filename = "df5ed275-f840-4ecb-965b-4b4863107632.csv"

fields = []
rows = []

Dict = {}


names = set()
typ = set()
rcm = set()
cob = set()


with open(filename, 'r') as file:

    csvread = csv.reader(file)

    fields = next(csvread)

    for row in csvread:
        rows.append(row)

    print("rows", csvread.line_num)


print("Field names are:" + ','.join(field for field in fields))

for row in rows:
    name = ""
    for i, col in enumerate(row):
        if i < 4:
            name += " " + col
        if i == 0:
            names.add(col)
        if i == 1:
            typ.add(col)
        if i == 2:
            rcm.add(col)
        if i == 3:
            cob.add(col)
    Dict[name] = {"num" : 0, "yes" : 0, "cost" : 0}


def calc(a, b):
    ret = 0
    for row in rows:
        yes = 0
        am = 0
        for col in row:
            if col == a or col == b:
                am += 1
            if col == "Yes":
                yes = 1
        if am == 2 and yes == 1:
            ret += 1
    return ret

    
opt = []

for n in names:
    for t in typ:
        for r in rcm:
            for c in cob:
                name = n + " " + t + " " + r + " " + c
                score = 0

                score += calc(n, t)
                score += calc(n, r)
                score += calc(n, c)
                score += calc(t, r)
                score += calc(t, c)
                score += calc(r, c)

                opt.append((score, name))


opt.sort()

for (s, n) in opt:
    print(s, n)


options = [

    "Apprenticed under M. Escher Uncategorizable Thing Wood and Dreams Obsessively Detailed",
    "Self-Taught Uncategorizable Thing Wood and Wood Hastily Sketched",
    "Apprenticed under P. Stamatin, "
]

for op in options:
    for (s, n) in opt:
        if n == op:
            print(n, s)


