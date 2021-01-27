import sys
sys.path.insert(0,'python/')
from Utils import *

#def ReadYield(inputpath,processlist): return dict_yield

def ConvertToInputDict(conf):

    dict_yield=ReadYield(conf['inputpath'],conf['processlist'])
    dict_yield=CombineYield(dict_yield,conf['toCombine'])
    return dict_yield


def RunTable():
    #../2016/Datacards_2016/Datacard_M2000/__BoostedGGF_SR_MEKDTAG_M1500_C0.001/Event/shapes/histos___BoostedGGF_SR_MEKDTAG_M1500_C0.001.root
    #qqH_hww1000_c10brn00                         qqH_hww_SBI1000_c10brn00                     ggH_hww1000_c10brn00                         ggH_hww_SBI1000\
        #_c10brn00                     qqWWqq                                       ggWW                                         MultiV                                       tW                                    \
        #       TT                                           QCD                                          WmHWWlnuqq_M125                              Wjets                                        DY              \
        #                             ZHWWlnuqq_M125                               SingleTop                                    WpHWWlnuqq_M125                              
    conf_2016_GGF0_SR={
        'inputpath':'../2016/Datacards_2016/Datacard_M2000/__BoostedGGF_SR_MEKDTAG_M1500_C0.01/Event/shapes/histos___BoostedGGF_SR_MEKDTAG_M1500_C0.01.root',
        'processlist':['ggH_hww2000_c10brn00','qqH_hww2000_c10brn00','qqWWqq','ggWW','MultiV','tW','TT','QCD','WmHWWlnuqq_M125','Wjets','DY','ZHWWlnuqq_M125','SingleTop','WpHWWlnuqq_M125'],
        'toCombine':{
            'MultiBoson':['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125'],
            'Top':['TT','SingleTop','tW'],
            'Others':['DY','QCD'],
        },
        
    }

    conf_2016_GGF0_SB={
        'inputpath':'../2016/Datacards_2016/Datacard_M2000/__BoostedGGF_SB_MEKDTAG_M1500_C0.01/Event/shapes/histos___BoostedGGF_SB_MEKDTAG_M1500_C0.01.root',
        'processlist':['ggH_hww2000_c10brn00','qqH_hww2000_c10brn00','qqWWqq','ggWW','MultiV','tW','TT','QCD','WmHWWlnuqq_M125','Wjets','DY','ZHWWlnuqq_M125','SingleTop','WpHWWlnuqq_M125'],
        'toCombine':{
            'MultiBoson':['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125'],
            'Top':['TT','SingleTop','tW'],
            'Others':['DY','QCD'],
        },
        
    }

    conf_2016_GGF0_TOP={
        'inputpath':'../2016/Datacards_2016/Datacard_M2000/__BoostedGGF_TOP_MEKDTAG_M1500_C0.01/Event/shapes/histos___BoostedGGF_TOP_MEKDTAG_M1500_C0.01.root',
        'processlist':['ggH_hww2000_c10brn00','qqH_hww2000_c10brn00','qqWWqq','ggWW','MultiV','tW','TT','QCD','WmHWWlnuqq_M125','Wjets','DY','ZHWWlnuqq_M125','SingleTop','WpHWWlnuqq_M125'],
        'toCombine':{
            'MultiBoson':['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125'],
            'Top':['TT','SingleTop','tW'],
            'Others':['DY','QCD'],
        },
        
    }


    conf_2016_GGF1_SR={
        'inputpath':'../2016/Datacards_2016/Datacard_M2000/__BoostedGGF_SR_UNTAGGED_M1500_C0.01/Event/shapes/histos___BoostedGGF_SR_UNTAGGED_M1500_C0.01.root',
        'processlist':['ggH_hww2000_c10brn00','qqH_hww2000_c10brn00','qqWWqq','ggWW','MultiV','tW','TT','QCD','WmHWWlnuqq_M125','Wjets','DY','ZHWWlnuqq_M125','SingleTop','WpHWWlnuqq_M125'],
        'toCombine':{
            'MultiBoson':['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125'],
            'Top':['TT','SingleTop','tW'],
            'Others':['DY','QCD'],
        },
        
    }

    conf_2016_GGF1_SB={
        'inputpath':'../2016/Datacards_2016/Datacard_M2000/__BoostedGGF_SB_UNTAGGED_M1500_C0.01/Event/shapes/histos___BoostedGGF_SB_UNTAGGED_M1500_C0.01.root',
        'processlist':['ggH_hww2000_c10brn00','qqH_hww2000_c10brn00','qqWWqq','ggWW','MultiV','tW','TT','QCD','WmHWWlnuqq_M125','Wjets','DY','ZHWWlnuqq_M125','SingleTop','WpHWWlnuqq_M125'],
        'toCombine':{
            'MultiBoson':['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125'],
            'Top':['TT','SingleTop','tW'],
            'Others':['DY','QCD'],
        },
        
    }

    conf_2016_GGF1_TOP={
        'inputpath':'../2016/Datacards_2016/Datacard_M2000/__BoostedGGF_TOP_UNTAGGED_M1500_C0.01/Event/shapes/histos___BoostedGGF_TOP_UNTAGGED_M1500_C0.01.root',
        'processlist':['ggH_hww2000_c10brn00','qqH_hww2000_c10brn00','qqWWqq','ggWW','MultiV','tW','TT','QCD','WmHWWlnuqq_M125','Wjets','DY','ZHWWlnuqq_M125','SingleTop','WpHWWlnuqq_M125'],
        'toCombine':{
            'MultiBoson':['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125'],
            'Top':['TT','SingleTop','tW'],
            'Others':['DY','QCD'],
        },
        
    }



    dict_2016_GGF0_SR=ConvertToInputDict(conf_2016_GGF0_SR)
    dict_2016_GGF0_SB=ConvertToInputDict(conf_2016_GGF0_SB)
    dict_2016_GGF0_TOP=ConvertToInputDict(conf_2016_GGF0_TOP)

    dict_2016_GGF1_SR=ConvertToInputDict(conf_2016_GGF1_SR)
    dict_2016_GGF1_SB=ConvertToInputDict(conf_2016_GGF1_SB)
    dict_2016_GGF1_TOP=ConvertToInputDict(conf_2016_GGF1_TOP)

    
    dict_table_Boosted={
        'Boosted GGF0':{
            'SR': dict_2016_GGF0_SR, 
            'SB': dict_2016_GGF0_SB, 
            'TOP': dict_2016_GGF0_TOP,
        },
        'Boosted GGF1':{
            'SR': dict_2016_GGF0_SR, 
            'SB': dict_2016_GGF0_SB, 
            'TOP': dict_2016_GGF0_TOP,
            }
    }

    #dict_comb= {
        
    #    'testcut':dict_yield,
    #    'testcut2':dict_yield,
        
    #}
    
    #def mkTable(cutlist,proclist,tablecation,tablealias,input_dict,outputtxt):
    #cutlist=['testcut','testcut2']
    #mkTable(cutlist,['smWW'],'caption','alias',dict_comb,'test.tex')
    #mkTable(cutlist,processlist,'caption','alias',dict_comb,'test.tex')

    processlist=['Wjets','Top','qqWWqq','ggWW','MultiBoson','Others']
    mkTable(processlist,'Yield of Boosted gluon-gluon fusion events of 2016 data','tab:bst_ggf_2016',dict_table_Boosted,'bst_ggf_2016.tex')
    


if __name__ == '__main__':
    ###--
    RunTable()
