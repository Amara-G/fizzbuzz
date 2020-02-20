file = open("Trails.csv")
def task_1(file):
	l = []
	m = []
	n = []
	o = []
	for i in file:
		l = i.split(",")
		#print(l)
		for each in l:
			if 'GOOD' == l(9):
				g.append(l)
				print(g)
			elif 'MARGINAL' == l(9)
				m.append(l)
				print(m)
			else ' ' == l(9):
				e.append(l)
				print(e)
task_1(file)
file = open("Trails.csv")
def task1_a(file):
        k = []
        for i in file:
                k = i.split(",")
                for each in k:
                        if k[10]v>= '2000':
                                t.append(k)
				print(k)
file = open("Trails.csv")
def task1_b(file):
        count_Active = []
        count_lighting = []
        count_bc = []
        for i in file:
                l = i.split(",")
                for each in l:
                        if l[15] == 'ACTIVE':
                                count_Active += 1
                        if l[12] == 'YES':
                                count_lighting += 1
                        if l[23] == 'YES' and l[25] == 'YES'
                                count_bc += 1
                print("ACTIVE=", count_Active)
                print("lighting=", count_lighting)
                print("hiking and walking = ", count_bc)
