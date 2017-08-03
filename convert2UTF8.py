# coding=utf-8
import sys
import os
import chardet
from tqdm import tqdm 
import colorama

## useage: this.py dir_you_want_to_walk

if __name__ == '__main__':
	targets = []
	for root, dirs, files in tqdm(os.walk(sys.argv[1])):
		for name in files:

			if name[-4:] != '.cpp' and name[-2:] != '.h' : continue
			targets.append(os.path.join(root,name))
	pt = tqdm(targets, desc='Converting to UTF8')

	for t in pt:
		f = open(t, 'rb')
		content = f.read()
		detected_code = chardet.detect(content)
		f.close()
		tqdm.write(str(detected_code['confidence']) + '\t' + str(detected_code['encoding']) + "\t"  + t)
		if(detected_code['encoding']=="UTF-8-SIG" or detected_code['encoding']=="None"):continue
		if(detected_code['confidence']>0.8):
			utf8content = content.decode(detected_code['encoding'], 'ignore')
			f = open(t, 'w', encoding='utf-8-sig',newline='')
			f.write(utf8content)
			f.close()