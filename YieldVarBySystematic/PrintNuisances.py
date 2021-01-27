##----Print List of Nuisances in the Card
import sys
sys.path.insert(0,'../python/')
from Utils import *
from ParseDatacard import *

def Print(year=2016):
    #year=2016
    NuisanceInfo=ParseDatacard('../../'+str(year)+'/combined_card_1000.txt')
    NuisanceList=[]
    for nui in NuisanceInfo:
        print nui
        NuisanceList.append(nui)
    print NuisanceList

if __name__ == '__main__':
    Print(2018)
