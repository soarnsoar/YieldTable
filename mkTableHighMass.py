import sys
import copy
sys.path.insert(0,'python/')
from Utils import *

#def ReadYield(inputpath,processlist): return dict_yield

def ConvertToInputDict(conf):
    inputpath=conf['inputpath']
    print inputpath
    #MASS=inputpath.split('Datacards_M')[1].split('/')[0]
    #ggH_hww400_c10brn00,qqH_hww400_c10brn00
    #dict_yield=ReadYield(conf['inputpath'],conf['processlist'])
    dict_yield=ReadYield(inputpath,conf['processlist'])
    dict_yield=CombineYield(dict_yield,conf['toCombine'])
    return dict_yield


def ConverToResolved(conf):
    newconf=copy.deepcopy(conf)
    inputpath=conf['inputpath']
    newconf['inputpath']=inputpath.replace("Boosted","_Resolved")
    newconf['inputpath']=newconf['inputpath'].replace("GGF","GGF_")
    newconf['inputpath']=newconf['inputpath'].replace("VBF","VBF_")
    newconf['inputpath']=newconf['inputpath'].replace("MEKDTAG_M1500","MEKDTAG_M400")
    newconf['inputpath']=newconf['inputpath'].replace("UNTAGGED_M1500","UNTAGGED_M400")
    newconf['inputpath']=newconf['inputpath'].replace("Datacard_M2000","Datacard_M400")
    #print newconf['inputpath']
    #___ResolvedGGF__TOP_MEKDTAG_M400_C0.01
    #__BoostedGGF_SR_MEKDTAG_M1500_C0.01

    ##--M400 instead of M2000
    newconf['processlist']=['ggH_hww400_c10brn00','qqH_hww400_c10brn00']+conf['processlist']
    newconf['processlist'].remove('ggH_hww2000_c10brn00')
    newconf['processlist'].remove('qqH_hww2000_c10brn00')
    ##--add 1pb norm signal for M400
    newconf['toCombine']['ggH400 in 10pb']={'list':['ggH_hww400_c10brn00'],'scale':10.0}
    newconf['toCombine']['qqH400 in 10pb']={'list':['qqH_hww400_c10brn00'],'scale':10.0}
    del newconf['toCombine']['ggH2000 in 1pb']
    del newconf['toCombine']['qqH2000 in 1pb']
    #print "newconf['inputpath']=",newconf['inputpath']
    return newconf
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
            #'ggH400 in 1pb':{'list':['ggH_hww400_c10brn00'],'scale':1.0},
            #'qqH400 in 1pb':{'list':['qqH_hww400_c10brn00'],'scale':1.0},
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
            #'ggH400 in 1pb':{'list':['ggH_hww400_c10brn00'],'scale':1.0},
            #'qqH400 in 1pb':{'list':['qqH_hww400_c10brn00'],'scale':1.0},
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
            #'ggH400 in 1pb':{'list':['ggH_hww400_c10brn00'],'scale':1.0},
            #'qqH400 in 1pb':{'list':['qqH_hww400_c10brn00'],'scale':1.0},
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
            #'ggH400 in 1pb':{'list':['ggH_hww400_c10brn00'],'scale':1.0},
            #'qqH400 in 1pb':{'list':['qqH_hww400_c10brn00'],'scale':1.0},
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
            #'ggH400 in 1pb':{'list':['ggH_hww400_c10brn00'],'scale':1.0},
            #'qqH400 in 1pb':{'list':['qqH_hww400_c10brn00'],'scale':1.0},
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
            #'ggH400 in 1pb':{'list':['ggH_hww400_c10brn00'],'scale':1.0},
            #'qqH400 in 1pb':{'list':['qqH_hww400_c10brn00'],'scale':1.0},
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
            #'ggH400 in 1pb':{'list':['ggH_hww400_c10brn00'],'scale':1.0},
            #'qqH400 in 1pb':{'list':['qqH_hww400_c10brn00'],'scale':1.0},
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
            #'ggH400 in 1pb':{'list':['ggH_hww400_c10brn00'],'scale':1.0},
            #'qqH400 in 1pb':{'list':['qqH_hww400_c10brn00'],'scale':1.0},
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
            #'ggH400 in 1pb':{'list':['ggH_hww400_c10brn00'],'scale':1.0},
            #'qqH400 in 1pb':{'list':['qqH_hww400_c10brn00'],'scale':1.0},
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
        'Boosted GGF':{
            'SR': dict_0_SR, 
            'SB': dict_0_SB, 
            'TOP': dict_0_TOP,
        },
        'Boosted untagged':{
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
    
    ##
    conf_0_SR_res=ConverToResolved(conf_0_SR)
    conf_0_SB_res=ConverToResolved(conf_0_SB)
    conf_0_TOP_res=ConverToResolved(conf_0_TOP)

    conf_1_SR_res=ConverToResolved(conf_1_SR)
    conf_1_SB_res=ConverToResolved(conf_1_SB)
    conf_1_TOP_res=ConverToResolved(conf_1_TOP)

    conf_2_SR_res=ConverToResolved(conf_2_SR)
    conf_2_SB_res=ConverToResolved(conf_2_SB)
    conf_2_TOP_res=ConverToResolved(conf_2_TOP)
    ##
    dict_0_SR_res=ConvertToInputDict(conf_0_SR_res)
    dict_0_SB_res=ConvertToInputDict(conf_0_SB_res)
    dict_0_TOP_res=ConvertToInputDict(conf_0_TOP_res)

    dict_1_SR_res=ConvertToInputDict(conf_1_SR_res)
    dict_1_SB_res=ConvertToInputDict(conf_1_SB_res)
    dict_1_TOP_res=ConvertToInputDict(conf_1_TOP_res)

    dict_2_SR_res=ConvertToInputDict(conf_2_SR_res)
    dict_2_SB_res=ConvertToInputDict(conf_2_SB_res)
    dict_2_TOP_res=ConvertToInputDict(conf_2_TOP_res)


    dict_table_Resolved={
        'Resolved GGF':{
            'SR': dict_0_SR_res, 
            'SB': dict_0_SB_res, 
            'TOP': dict_0_TOP_res,
        },
        'Resolved Untagged':{
            'SR': dict_1_SR_res, 
            'SB': dict_1_SB_res, 
            'TOP': dict_1_TOP_res,
            },

        'Resolved VBF':{
            'SR': dict_2_SR_res, 
            'SB': dict_2_SB_res, 
            'TOP': dict_2_TOP_res,
            }
    }
    ##    if bst=='Resolved':
    #    inputpath=inputpath.replace("__Boosted","_Resolved")
    #    inputpath=inputpath.replace("GGF","GGF_")
    #    inputpath=inputpath.replace("VBF","VBF_")
    #    inputpath=inputpath.replace("M1500","M400")



    #dict_comb= {
        
    #    'testcut':dict_yield,
    #    'testcut2':dict_yield,
        
    #}
    
    #def mkTable(cutlist,proclist,tablecation,tablealias,input_dict,outputtxt):
    #cutlist=['testcut','testcut2']
    #mkTable(cutlist,['smWW'],'caption','alias',dict_comb,'test.tex')
    #mkTable(cutlist,processlist,'caption','alias',dict_comb,'test.tex')

    processlist_Boosted=['Wjets','Top','qqWWqq','ggWW','MultiBoson','Others','ggH2000 in 1pb','qqH2000 in 1pb']
    #mkTable(processlist,'Yield of Boosted '+prod[2]+' events of '+Year+' data','tab:bst_'+prod[1]+'_'+Year+'',dict_table_Boosted,'bst_ggf_'+Year+'.tex')
    mkTable(processlist_Boosted,'Yield of Boosted events of '+Year+' data','tab:bst_'+Year+'',dict_table_Boosted,'bst_'+Year+'.tex')

    processlist_Resolved=['Wjets','Top','qqWWqq','ggWW','MultiBoson','Others','ggH400 in 10pb','qqH400 in 10pb']
    #mkTable(processlist,'Yield of Resolved '+prod[2]+' events of '+Year+' data','tab:res_'+prod[1]+'_'+Year+'',dict_table_Resolved,'res_ggf_'+Year+'.tex')
    mkTable(processlist_Resolved,'Yield of Resolved events of '+Year+' data','tab:res_'+Year+'',dict_table_Resolved,'res_'+Year+'.tex')
    


if __name__ == '__main__':
    ###--
    import sys
    year=sys.argv[1]
    #RunTable(year,'ggf')
    #RunTable(year,'vbf')
    RunTable(year)

