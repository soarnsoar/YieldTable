import sys
sys.path.insert(0,'python/')
from Utils import *

#def ReadYield(inputpath,processlist): return dict_yield

inputpath='example/histos___BoostedGGF_TOP_MEKDTAG_M1500_C0.001.root'

#def ReadYieldVar(inputpath,process,nuisance):
a=ReadYieldVar(inputpath,'ggH_hww1500_c10brn00','CMS_ak8jet_jms_2016Up')
print a*100,'(%)'
