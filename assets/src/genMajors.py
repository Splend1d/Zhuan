import pandas as pd
import pickle as pkl

df = pd.read_csv('../db/database.txt')
zhuan_no = df['小篆編號']
df2 = pd.read_csv('../db/database_meaning.txt',sep='\t')
majors_all = df2[df2.columns[2]]
majors = {}
for m,z in zip(majors_all,zhuan_no):
	try:
		thism = m.split('‧')[1][0]
	except:
		continue
	try:
		majors[thism].append(int(z))
	except:
		majors[thism] = [int(z)]
#print(majors)
covered = []
for m in majors:
	check_passed = []
	for w in majors[m]:
		if w +1 in majors[m] or w -1 in majors[m]:
			check_passed.append(w)
	majors[m] = list(set(check_passed))
	covered += majors[m]
print(majors.keys())
#print(sorted(covered))
for x in range(1,9832):
	if covered.count(x) == 0:
		print(x,"not covered")
	elif covered.count(x) > 1:
		print(x,"dupped")


#---- patch not covered
majors['上'].append(6)
majors['上'].append(9)
majors['三'].append(77)


with open("../db/dbmajors.pkl","wb") as f:
	pkl.dump(majors,f)