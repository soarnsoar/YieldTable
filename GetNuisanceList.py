f=open('../2016/combined_card_1000.txt','r')

lines=f.readlines()



doread=False

nuisance_info={}

for line in lines:
        if '-------------' in line:continue
	splitline=line.split()
	if 'rate'==splitline[0]:
                #print line
                doread=True
                continue
        if len(splitline)>1:
                if 'rateParam'==splitline[1]:
                        continue
                
        if doread:
                #print line
                nuis=splitline[0]
                constraint=splitline[1]
                nuisance_info[nuis]={'type':constraint}
f.close()

print sorted(nuisance_info)
