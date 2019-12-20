import pickle as pkl
with open("../db/database_word.pkl", "rb") as f:
    db = pkl.load(f)
for e in db.values():
	if len(e["fonts"]) % 2 != 0 :
		print("odd situtaion")
with open("../db/database_coverage.pkl", "rb") as f:
    db2 = pkl.load(f)
print(db2)
s()

print(this_dict)
coverage['𥄎'] = [2082,2085]
coverage['𠃊'] = [8366,8367]
coverage['𣦼'] = [2513,2517]
coverage['𥄕'] = [2317,2320]
coverage['𠃉'] = [7661,7663]
coverage['𣐺'] = [4327,4328]
coverage['𦣻'] = [5663,5664]
coverage['𠘧'] = [1968,1970]
coverage['𣆪'] = [3318,3320]
coverage['𧮫'] = [1443,1444]
coverage['𦥑'] = [4497,4501]
coverage['𣎳'] = [4505,4506]
coverage['𠧪'] = [4329,4331]
coverage['𡈼'] = [5214,5217], '𠔼', '𣏟', '𩫏', '𨺅', '𥄉', '𢎘', '𠤎', '𠂹', '𠂤', '𠂢', '𥝌', '𠌶', '𡿨', '𠂇', '𢆶', '𠫓', '𠦒', '𨛜', '𠂣', '𤉡', '𠙴', '𠨍', '𠦬', '𦘒', '𦣞', '𣎵', '𠬪', '𦫳', '𠂆', '𠬜', '𠑹', '𦣹']
