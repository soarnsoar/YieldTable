import sys
sys.path.insert(0,'python/')
from Utils import *

#def ReadYield(inputpath,processlist): return dict_yield

inputpath='example/histos___BoostedGGF_TOP_MEKDTAG_M1500_C0.001.root'
processlist=['qqWWqq','ggWW']


dict_yield=ReadYield(inputpath,processlist)

#def CombineYield(dict_yield,dict_combine):
dict_combine={
    'smWW':['qqWWqq','ggWW']
}
#dict_yield=CombineYield(dict_yield,dict_combine)


print dict_yield


dict_comb= {

'testcut':dict_yield,
'testcut2':dict_yield,

}

#def mkTable(cutlist,proclist,tablecation,tablealias,input_dict,outputtxt):
cutlist=['testcut','testcut2']
#mkTable(cutlist,['smWW'],'caption','alias',dict_comb,'test.tex')
mkTable(cutlist,processlist,'caption','alias',dict_comb,'test.tex')
