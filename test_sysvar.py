import sys
sys.path.insert(0,'python/')
from Utils import *

#def ReadYield(inputpath,processlist): return dict_yield

#inputpath='example/histos___BoostedGGF_TOP_MEKDTAG_M1500_C0.001.root'
M=1000


inputpath='../2016/Datacards_2016/Datacard_M'+str(M)+'/__BoostedALL_SR_NoMEKDCut/Event/shapes/histos___BoostedALL_SR_NoMEKDCut.root '

#def ReadYieldVar(inputpath,process,nuisance):
a=ReadYieldVar(inputpath,'ggH_hww'+str(M)+'_c10brn00','CMS_ak8jet_jms_2016Up')
print a*100,'(%)'
