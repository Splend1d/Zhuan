import os
import json
imgsown = set(os.listdir('../db/img'))
print(imgsown)

with open('../db/database_word.json','r') as f:
	db = json.load(f)

imgsneed = []
for v in db.values():
	imgsneed += v['fonts'][0] 
	imgsneed += v['fonts'][1]
imgsnotown = []
for img in imgsneed:
	if img + '.png' not in imgsown:
		imgsnotown.append(img)
print(len(imgsown))
print(len(imgsnotown))
 