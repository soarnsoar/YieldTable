import sys
sys.path.insert(0,'python/')
from Utils import *

#def ReadYield(inputpath,processlist): return dict_yield

def ConvertToInputDict(conf):

    dict_yield=ReadYield(conf['inputpath'],conf['processlist'])
    dict_yield=CombineYield(dict_yield,conf['toCombine'])
    return dict_yield


def RunTable(Year):

    
    Year=str(Year)
    #../2016/Datacards_2016/Datacard_M2000/__BoostedGGF_SR_MEKDTAG_M1500_C0.01/Event/shapes/histos___BoostedGGF_SR_MEKDTAG_M1500_C0.01.root
    #qqH_hww000_c10brn00                         qqH_hww_SBI1000_c10brn00                     ggH_hww1000_c10brn00                         ggH_hww_SBI1000\
        #_c10brn00                     qqWWqq                                       ggWW                                         MultiV                                       tW                                    \
        #       TT                                           QCD                                          WmHWWlnuqq_M125                              Wjets                                        DY              \
        #                             ZHWWlnuqq_M125                               SingleTop                                    WpHWWlnuqq_M125                              
    conf_0_SR={
        'inputpath':'../'+Year+'/Datacards_'+Year+'/Datacard_M2000/__BoostedGGF_SR_MEKDTAG_M1500_C0.01/Event/shapes/histos___BoostedGGF_SR_MEKDTAG_M1500_C0.01.root',
        'processlist':['ggH_hww2000_c10brn00','qqH_hww2000_c10brn00','qqWWqq','ggWW','MultiV','tW','TT','QCD','WmHWWlnuqq_M125','Wjets','DY','ZHWWlnuqq_M125','SingleTop','WpHWWlnuqq_M125'],
        'toCombine':{
            'MultiBoson':{'list':['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125'],'scale':1.0},
            'Top':{'list':['TT','SingleTop','tW'],'scale':1.0},
            'Others':{'list':['DY','QCD'], 'scale':1.0},
            'ggH2000 in 1pb':{'list':['ggH_hww2000_c10brn00'],'scale':1.0},
            'qqH2000 in 1pb':{'list':['qqH_hww2000_c10brn00'],'scale':1.0},
        },
        
    }

    conf_0_SB={
        'inputpath':'../'+Year+'/Datacards_'+Year+'/Datacard_M2000/__BoostedGGF_SB_MEKDTAG_M1500_C0.01/Event/shapes/histos___BoostedGGF_SB_MEKDTAG_M1500_C0.01.root',
        'processlist':['ggH_hww2000_c10brn00','qqH_hww2000_c10brn00','qqWWqq','ggWW','MultiV','tW','TT','QCD','WmHWWlnuqq_M125','Wjets','DY','ZHWWlnuqq_M125','SingleTop','WpHWWlnuqq_M125'],
        'toCombine':{
            'MultiBoson':{'list':['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125'],'scale':1.0},
            'Top':{'list':['TT','SingleTop','tW'],'scale':1.0},
            'Others':{'list':['DY','QCD'],'scale':1.0},
            'ggH2000 in 1pb':{'list':['ggH_hww2000_c10brn00'],'scale':1.0},
            'qqH2000 in 1pb':{'list':['qqH_hww2000_c10brn00'],'scale':1.0},
        },
        
    }
    
    conf_0_TOP={
        'inputpath':'../'+Year+'/Datacards_'+Year+'/Datacard_M2000/__BoostedGGF_TOP_MEKDTAG_M1500_C0.01/Event/shapes/histos___BoostedGGF_TOP_MEKDTAG_M1500_C0.01.root',
        'processlist':['ggH_hww2000_c10brn00','qqH_hww2000_c10brn00','qqWWqq','ggWW','MultiV','tW','TT','QCD','WmHWWlnuqq_M125','Wjets','DY','ZHWWlnuqq_M125','SingleTop','WpHWWlnuqq_M125'],
        'toCombine':{
            'MultiBoson':{'list':['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125'],'scale':1.0},
            'Top':{'list':['TT','SingleTop','tW'],'scale':1.0},
            'Others':{'list':['DY','QCD'],'scale':1.0},
            'ggH2000 in 1pb':{'list':['ggH_hww2000_c10brn00'],'scale':1.0},
            'qqH2000 in 1pb':{'list':['qqH_hww2000_c10brn00'],'scale':1.0},
        },
        
    }
    
    
    conf_1_SR={
        'inputpath':'../'+Year+'/Datacards_'+Year+'/Datacard_M2000/__BoostedGGF_SR_UNTAGGED_M1500_C0.01/Event/shapes/histos___BoostedGGF_SR_UNTAGGED_M1500_C0.01.root',
        'processlist':['ggH_hww2000_c10brn00','qqH_hww2000_c10brn00','qqWWqq','ggWW','MultiV','tW','TT','QCD','WmHWWlnuqq_M125','Wjets','DY','ZHWWlnuqq_M125','SingleTop','WpHWWlnuqq_M125'],
        'toCombine':{
            'MultiBoson':{'list':['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125'],'scale':1.0},
            'Top':{'list':['TT','SingleTop','tW'],'scale':1.0},
            'Others':{'list':['DY','QCD'],'scale':1.0},
            'ggH2000 in 1pb':{'list':['ggH_hww2000_c10brn00'],'scale':1.0},
            'qqH2000 in 1pb':{'list':['qqH_hww2000_c10brn00'],'scale':1.0},
        },
        
    }
    
    conf_1_SB={
        'inputpath':'../'+Year+'/Datacards_'+Year+'/Datacard_M2000/__BoostedGGF_SB_UNTAGGED_M1500_C0.01/Event/shapes/histos___BoostedGGF_SB_UNTAGGED_M1500_C0.01.root',
        'processlist':['ggH_hww2000_c10brn00','qqH_hww2000_c10brn00','qqWWqq','ggWW','MultiV','tW','TT','QCD','WmHWWlnuqq_M125','Wjets','DY','ZHWWlnuqq_M125','SingleTop','WpHWWlnuqq_M125'],
        'toCombine':{
            'MultiBoson':{'list':['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125'],'scale':1.0},
            'Top':{'list':['TT','SingleTop','tW'],'scale':1.0},
            'Others':{'list':['DY','QCD'],'scale':1.0},
            'ggH2000 in 1pb':{'list':['ggH_hww2000_c10brn00'],'scale':1.0},
            'qqH2000 in 1pb':{'list':['qqH_hww2000_c10brn00'],'scale':1.0},
        },
        
    }
    
    conf_1_TOP={
        'inputpath':'../'+Year+'/Datacards_'+Year+'/Datacard_M2000/__BoostedGGF_TOP_UNTAGGED_M1500_C0.01/Event/shapes/histos___BoostedGGF_TOP_UNTAGGED_M1500_C0.01.root',
        'processlist':['ggH_hww2000_c10brn00','qqH_hww2000_c10brn00','qqWWqq','ggWW','MultiV','tW','TT','QCD','WmHWWlnuqq_M125','Wjets','DY','ZHWWlnuqq_M125','SingleTop','WpHWWlnuqq_M125'],
        'toCombine':{
            'MultiBoson':{'list':['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125'],'scale':1.0},
            'Top':{'list':['TT','SingleTop','tW'],'scale':1.0},
            'Others':{'list':['DY','QCD'],'scale':1.0},
            'ggH2000 in 1pb':{'list':['ggH_hww2000_c10brn00'],'scale':1.0},
            'qqH2000 in 1pb':{'list':['qqH_hww2000_c10brn00'],'scale':1.0},
        },
        
    }

    ##--VBF
    conf_2_SR={
        'inputpath':'../'+Year+'/Datacards_'+Year+'/Datacard_M2000/__BoostedVBF_SR_NoMEKDCut/Event/shapes/histos___BoostedVBF_SR_NoMEKDCut.root',
        'processlist':['ggH_hww2000_c10brn00','qqH_hww2000_c10brn00','qqWWqq','ggWW','MultiV','tW','TT','QCD','WmHWWlnuqq_M125','Wjets','DY','ZHWWlnuqq_M125','SingleTop','WpHWWlnuqq_M125'],
        'toCombine':{
            'MultiBoson':{'list':['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125'],'scale':1.0},
            'Top':{'list':['TT','SingleTop','tW'],'scale':1.0},
            'Others':{'list':['DY','QCD'],'scale':1.0},
            'ggH2000 in 1pb':{'list':['ggH_hww2000_c10brn00'],'scale':1.0},
            'qqH2000 in 1pb':{'list':['qqH_hww2000_c10brn00'],'scale':1.0},
        },
        
    }
    
    conf_2_SB={
        'inputpath':'../'+Year+'/Datacards_'+Year+'/Datacard_M2000/__BoostedVBF_SB_NoMEKDCut/Event/shapes/histos___BoostedVBF_SB_NoMEKDCut.root',
        'processlist':['ggH_hww2000_c10brn00','qqH_hww2000_c10brn00','qqWWqq','ggWW','MultiV','tW','TT','QCD','WmHWWlnuqq_M125','Wjets','DY','ZHWWlnuqq_M125','SingleTop','WpHWWlnuqq_M125'],
        'toCombine':{
            'MultiBoson':{'list':['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125'],'scale':1.0},
            'Top':{'list':['TT','SingleTop','tW'],'scale':1.0},
            'Others':{'list':['DY','QCD'],'scale':1.0},
            'ggH2000 in 1pb':{'list':['ggH_hww2000_c10brn00'],'scale':1.0},
            'qqH2000 in 1pb':{'list':['qqH_hww2000_c10brn00'],'scale':1.0},
        },
        
    }
    
    conf_2_TOP={
        'inputpath':'../'+Year+'/Datacards_'+Year+'/Datacard_M2000/__BoostedVBF_TOP_NoMEKDCut/Event/shapes/histos___BoostedVBF_TOP_NoMEKDCut.root',
        'processlist':['ggH_hww2000_c10brn00','qqH_hww2000_c10brn00','qqWWqq','ggWW','MultiV','tW','TT','QCD','WmHWWlnuqq_M125','Wjets','DY','ZHWWlnuqq_M125','SingleTop','WpHWWlnuqq_M125'],
        'toCombine':{
            'MultiBoson':{'list':['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125'],'scale':1.0},
            'Top':{'list':['TT','SingleTop','tW'],'scale':1.0},
            'Others':{'list':['DY','QCD'],'scale':1.0},
            'ggH2000 in 1pb':{'list':['ggH_hww2000_c10brn00'],'scale':1.0},
            'qqH2000 in 1pb':{'list':['qqH_hww2000_c10brn00'],'scale':1.0},
        },
        
    }



    dict_0_SR=ConvertToInputDict(conf_0_SR)
    dict_0_SB=ConvertToInputDict(conf_0_SB)
    dict_0_TOP=ConvertToInputDict(conf_0_TOP)

    dict_1_SR=ConvertToInputDict(conf_1_SR)
    dict_1_SB=ConvertToInputDict(conf_1_SB)
    dict_1_TOP=ConvertToInputDict(conf_1_TOP)

    dict_2_SR=ConvertToInputDict(conf_2_SR)
    dict_2_SB=ConvertToInputDict(conf_2_SB)
    dict_2_TOP=ConvertToInputDict(conf_2_TOP)

    
    dict_table_Boosted={
        'Boosted GGF0':{
            'SR': dict_0_SR, 
            'SB': dict_0_SB, 
            'TOP': dict_0_TOP,
        },
        'Boosted GGF1':{
            'SR': dict_1_SR, 
            'SB': dict_1_SB, 
            'TOP': dict_1_TOP,
            },

        'Boosted VBF':{
            'SR': dict_2_SR, 
            'SB': dict_2_SB, 
            'TOP': dict_2_TOP,
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

    processlist=['Wjets','Top','qqWWqq','ggWW','MultiBoson','Others','ggH2000 in 1pb','qqH2000 in 1pb']
    #mkTable(processlist,'Yield of Boosted '+prod[2]+' events of '+Year+' data','tab:bst_'+prod[1]+'_'+Year+'',dict_table_Boosted,'bst_ggf_'+Year+'.tex')
    mkTable(processlist,'Yield of Boosted events of '+Year+' data','tab:bst_'+Year+'',dict_table_Boosted,'bst_'+Year+'.tex')
    


if __name__ == '__main__':
    ###--
    import sys
    year=sys.argv[1]
    #RunTable(year,'ggf')
    #RunTable(year,'vbf')
    RunTable(year)
