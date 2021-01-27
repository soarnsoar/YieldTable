

def GetNuisanceList(cardpath):
        #f=open('../2016/combined_card_1000.txt','r')
        f=open(cardpath,'r')
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
                        values=[x  for x in splitline[2:] if x!='-']
                        value=0
                        for x in values:
                               this_valuelist=[ abs(float(y)-1) for y in x.split('/') ]
                               this_value=max(this_valuelist)
                               if this_value>value:value=this_value
                        #valuemax=max( [ max[float(y) for y in x.split('/') for x in splitline[2:] if x!='-']])
                        nuisance_info[nuis]={'type':constraint,'value':value+1}
        f.close()

        #print sorted(nuisance_info)
        return nuisance_info

def ParseDatacard(cardpath):
        f=open(cardpath,'r')
        lines=f.readlines()
                
        doread=False
        
        nuisance_info={}
        processcount=0
        processlist=[]
        for line in lines:
                if '-------------' in line:continue
                splitline=line.split()

                if 'process'==splitline[0]:
                        processcount+=1
                        if processcount==1:
                                processlist=splitline[1:]
                        #print line
                        #doread=True
                        continue
                if len(splitline)>1:
                        if 'rateParam'==splitline[1] or 'autoMC' in line:
                                continue
                if 'rate' == splitline[0]:
                        doread=True
                        continue
                if doread:
                        #print line
                        nuis=splitline[0]
                        constraint=splitline[1]
                        #values=[x  for x in splitline[2:] if x!='-']
                        #value=0
                        #for x in values:
                        #       this_valuelist=[ abs(float(y)-1) for y in x.split('/') ]
                        #       this_value=max(this_valuelist)
                        #       if this_value>value:value=this_value
                        #valuemax=max( [ max[float(y) for y in x.split('/') for x in splitline[2:] if x!='-']])
                        #nuisance_info[nuis]={'type':constraint,'value':value+1}
                        values=splitline[2:]
                        #print nuis
                        #print processlist
                        #print values
                        #print len(processlist)
                        #print len(values)
                        nuisance_info[nuis]={'type':constraint,'process':{}}
                        for i_proc in range(len(processlist)):
                                nuisance_info[nuis]['process'][processlist[i_proc]]=values[i_proc]
        f.close()

        #print sorted(nuisance_info)
        return nuisance_info


if __name__ == '__main__':
        #a=GetNuisanceList('../2016/combined_card_1000.txt')
        #print sorted(a)
        #print a['QCDscale_Higgs_gg']['value']
        nuisanceinfo=ParseDatacard('../2016/combined_card_1000.txt') 
        print nuisanceinfo['lumi_13TeV_DynBeta']['process']['Wjets']
