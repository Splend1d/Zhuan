import pickle as pkl
import json

with open("../db/majors_coverage.pkl", "rb") as f:
    dbcoverage = pkl.load(f)
#print(dbcoverage)
#print(freq2000)
all_ = set()

print("-before patch-")
print("duplicates:",)
for k,v in dbcoverage.items():
	

	for i in range(int(v[0]),int(v[1])+1):
		if i not in all_:
			all_.add(i)
		else:
			print(k,i)

print("can't find major part : ")
for i in range(1,9832):
	if i not in all_:
		print(i)

#125 major parts have over 10 entries, choose them as database


#fix mismatched terms
dbcoverage['犛'] = [774,776]
# fix can't crawl terms
dbcoverage['𥄎'] = [2082,2085]
dbcoverage['𠃊'] = [8366,8367]
dbcoverage['𣦼'] = [2513,2517]
dbcoverage['𥄕'] = [2317,2320]
dbcoverage['𠃉'] = [7661,7663]
dbcoverage['𣐺'] = [4327,4328]
dbcoverage['𦣻'] = [5663,5664]
dbcoverage['𠘧'] = [1968,1970]
dbcoverage['𣆪'] = [3318,3320]
dbcoverage['𧮫'] = [1443,1444]
dbcoverage['𦥑'] = [1774,1775]
dbcoverage['𣎳'] = [4505,4506]
dbcoverage['𠧪'] = [4329,4331]
dbcoverage['𡈼'] = [5214,5217]
dbcoverage['𠔼'] = [4777,4780]
dbcoverage['𣏟'] = [4507,4509]
dbcoverage['𩫏'] = [3310,3311] 
dbcoverage['𨺅'] = [9662,9665]
dbcoverage['𥄉'] = [5674,5675] 
dbcoverage['𢎘'] = [4322,4326] 
dbcoverage['𠤎'] = [5187,5190] 
dbcoverage['𠂹'] = [3863,3863]
dbcoverage['𠂤'] = [9565,9567]
dbcoverage['𠂢'] = [7457,7459]
dbcoverage['𥝌'] = [3868,3870]
dbcoverage['𠌶'] = [3864,3865] 
dbcoverage['𡿨'] = [7438,7438]
dbcoverage['𠂇'] = [1921,1922]
dbcoverage['𢆶'] = [2489,2491]
dbcoverage['𠫓'] = [9736,9738]
dbcoverage['𠦒'] = [2479,2482] 
dbcoverage['𨛜'] = [4165,4167] 
dbcoverage['𠂣'] = [5226,5227] 
dbcoverage['𤉡'] = [6100,6100] 
dbcoverage['𠙴'] = [3146,3146]
dbcoverage['𠨍'] = [5764,5765] 
dbcoverage['𠦬'] = [8065,8066] 
dbcoverage['𦘒'] = [1927,1929]
dbcoverage['𦣞'] = [7785,7786]
dbcoverage['𣎵'] = [3850,3855]
dbcoverage['𠬪'] = [2504,2512] 
dbcoverage['𦫳'] = [2314,2316] 
dbcoverage['𠂆'] = [8320,8323]
dbcoverage['𠬜'] = [1763,1765]
dbcoverage['𠑹'] = [5440,5441]
dbcoverage['𦣹'] = [2215,2221]
# fix 小學堂 bug
dbcoverage['鹿'] = [6228,6253]
print("-after patch-")
print("duplicates:",)
all_.clear()
for k,v in dbcoverage.items():
	

	for i in range(int(v[0]),int(v[1])+1):
		if i not in all_:
			all_.add(i)
		else:
			print(k,i)

print("can't find major part : ")
for i in range(1,9832):
	if i not in all_:
		print(i)


with open("../db/majors_coverage.json", "w") as f:
    json.dump(dbcoverage, f)

