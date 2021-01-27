import sys
sys.path.insert(0,'python/')
from Utils import *
from GetNuisanceList import *
from math import sqrt
#def ReadYield(inputpath,processlist): return dict_yield

#inputpath='example/histos___BoostedGGF_TOP_MEKDTAG_M1500_C0.001.root'


def GetInputPath(mass,bst,year):
    
    inputpath='../'+str(year)+'/Datacards_'+str(year)+'/Datacard_M'+str(mass)+'/__BoostedALL_SR_NoMEKDCut/Event/shapes/histos___BoostedALL_SR_NoMEKDCut.root '
    if bst=='Resolved':
        inputpath=inputpath.replace('Boosted','_Resolved')
        inputpath=inputpath.replace('SR','SR_')

    return inputpath


def GetVarOfNuisnace(proclist,nuis,mass,bst,year):

    inputpath=GetInputPath(mass,bst,year)
    var_in_ratio=ReadYieldVarProcList(inputpath,proclist,nuis)
    return var_in_ratio

def GetRMS(mylist):
    sum2=0.
    for x in mylist:
        sum2+=x**2
    return sqrt(sum2)/len(mylist)
    
    

def GetVarOfNuisnaceListShape(proclist,nuisancelist,mass,bst,year):

    inputpath=GetInputPath(mass,bst,year)
    var_in_ratio_list=[]
    for nuis in nuisancelist:
        var_in_ratio_updown=[]
        for direction in ['Up','Down']:
            var_in_ratio=ReadYieldVarProcList(inputpath,proclist,nuis+direction)
            var_in_ratio_updown.append(var_in_ratio)
        var_in_ratio=max(var_in_ratio_updown)
        var_in_ratio_list.append(var_in_ratio)

    Total_var_in_ratio=GetRMS(var_in_ratio_list)
    return Total_var_in_ratio

def PartseNuisacneValue(mystring):
    if mystring=='-':
        return '-'
    else:
        strsplit=mystring.split('/')
        varlist=[ abs(1-float(x))  for x in strsplit ]
        maxvar=max(varlist)
        return str(maxvar*100)
        
def NuisanceList2016():
    mylist=['CMS_PU_2016', 'CMS_ak4jet_jer_2016', 'CMS_ak4jet_jesAbsolute', 'CMS_ak4jet_jesAbsolute_2016', 'CMS_ak4jet_jesBBEC1', 'CMS_ak4jet_jesBBEC1_2016', 'CMS_ak4jet_jesEC2', 'CMS_ak4jet_jesEC2_2016', 'CMS_ak4jet_jesFlavorQCD', 'CMS_ak4jet_jesHF', 'CMS_ak4jet_jesHF_2016', 'CMS_ak4jet_jesRelativeBal', 'CMS_ak4jet_jesRelativeSample_2016', 'CMS_ak8jet_jer_2016', 'CMS_ak8jet_jesAbsolute', 'CMS_ak8jet_jesAbsolute_2016', 'CMS_ak8jet_jesBBEC1', 'CMS_ak8jet_jesBBEC1_2016', 'CMS_ak8jet_jesEC2', 'CMS_ak8jet_jesEC2_2016', 'CMS_ak8jet_jesFlavorQCD', 'CMS_ak8jet_jesHF', 'CMS_ak8jet_jesHF_2016', 'CMS_ak8jet_jesRelativeBal', 'CMS_ak8jet_jesRelativeSample_2016', 'CMS_ak8jet_jmr_2016', 'CMS_ak8jet_jms_2016', 'CMS_btag_cferr1', 'CMS_btag_cferr2', 'CMS_btag_hf', 'CMS_btag_hfstats1_2016', 'CMS_btag_hfstats2_2016', 'CMS_btag_lf', 'CMS_btag_lfstats1_2016', 'CMS_btag_lfstats2_2016', 'CMS_eff_Wtag_2016', 'CMS_eff_e_2016', 'CMS_eff_hww_sngele_trigger_2016', 'CMS_eff_hww_sngmu_trigger_2016', 'CMS_eff_m_2016', 'CMS_eff_prefiring_2016', 'CMS_scale_electron_2016', 'CMS_scale_met_2016', 'CMS_scale_muon_2016', 'MultiVnorm2016', 'QCDscale_Higgs_gg', 'QCDscale_Higgs_qqbar', 'QCDscale_gg_ACCEPT', 'QCDscale_qq_ACCEPT', 'QCDscale_ttbar_ACCEPT', 'UEPS_FSR', 'UEPS_ISR', 'dynorm2016', 'ggWWnorm', 'lumi_13TeV_2016', 'lumi_13TeV_BBDefl', 'lumi_13TeV_DynBeta', 'lumi_13TeV_Ghosts', 'lumi_13TeV_XYFact', 'mjjshape_2016', 'pdf_Higgs_gg', 'pdf_Higgs_qqbar', 'pdf_gg_ACCEPT', 'pdf_qq_ACCEPT', 'pdf_ttbar_ACCEPT']
    


    

def Avg(inputlist):
    return sum(inputlist)/len(inputlist)



def MakeSysTableLines(year,bst='Boosted',proclist=['Wjets','Top','Others','ggf2000','vbf2000','ggf900','vbf900','ggf400','vbf400'] ):
    '''
    'MultiBoson':{'list':['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125'],'scale':1.0},
    'Top':{'list':['TT','SingleTop','tW'],'scale':1.0},
    'Others':{'list':['DY','QCD'],'scale':1.0},
    'ggH2000 in 1pb':{'list':['ggH_hww2000_c10brn00'],'scale':1.0},
    'qqH2000 in 1pb':{'list':['qqH_hww2000_c10brn00'],'scale':1.0},
    
    '''

    #year=2016
    #NuisanceInfo=GetNuisanceList('../'+str(year)+'/combined_card_1000.txt')
    NuisanceInfo=ParseDatacard('../'+str(year)+'/combined_card_1000.txt')
    NuisanceInfo2000=ParseDatacard('../'+str(year)+'/combined_card_2000.txt')
    NuisanceInfo900=ParseDatacard('../'+str(year)+'/combined_card_900.txt')
    NuisanceInfo400=ParseDatacard('../'+str(year)+'/combined_card_400.txt')
    
    #NuisanceInfo.update(NuisanceInfo2000)
    #NuisanceInfo.update(NuisanceInfo900)
    #NuisanceInfo.update(NuisanceInfo400)

    #proclist=['']
    dict_proc={
        'ggf2000':['ggH_hww2000_c10brn00'],
        'vbf2000':['qqH_hww2000_c10brn00'],
        'ggf900':['ggH_hww900_c10brn00'],
        'vbf900':['qqH_hww900_c10brn00'],
        'ggf400':['ggH_hww400_c10brn00'],
        'vbf400':['qqH_hww400_c10brn00'],
        'Wjets':['Wjets'],
        'Top':['TT','SingleTop','tW'],
        'Others':['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125','DY','QCD']
    }

    
    #proclist=['Wjets','Top','Others','ggf2000','vbf2000','ggf900','vbf900','ggf400','vbf400']
    
    #print proclist

    TableLines=[]
    TableLines.append(['Source']+proclist)
    print sorted(NuisanceInfo)
    for nui in NuisanceInfo:

        if NuisanceInfo[nui]['type']=='lnN':
            valuelist=[]
            myNuisanceInfo=NuisanceInfo
            for proc in proclist:
                if '400' in proc: myNuisanceInfo=NuisanceInfo400
                if '900' in proc: myNuisanceInfo=NuisanceInfo900
                if '2000' in proc: myNuisanceInfo=NuisanceInfo2000
                value=PartseNuisacneValue(myNuisanceInfo[nui]['process'][dict_proc[proc][0]])
                valuelist.append(str(value))
            #print valuelist
            TableLines.append([nui.replace('_','\_')]+valuelist)
        elif NuisanceInfo[nui]['type']=='shape':
            valuelist=[]
            myNuisanceInfo=NuisanceInfo
            for proc in proclist:
                mass=1000
                #print proc
                if '400' in proc: 
                    mass=400
                    myNuisanceInfo=NuisanceInfo400
                if '900' in proc: 
                    mass=900
                    myNuisanceInfo=NuisanceInfo900
                if '2000' in proc: 
                    mass=2000
                    myNuisanceInfo=NuisanceInfo2000
                #print nui
                value=PartseNuisacneValue(myNuisanceInfo[nui]['process'][dict_proc[proc][0]])
                if value=='-':
                    valuelist.append('-')
                else:
                    up=GetVarOfNuisnace(dict_proc[proc],nui+'Up',mass,'Boosted',year)
                    down=GetVarOfNuisnace(dict_proc[proc],nui+'Down',mass,'Boosted',year)
                    valuelist.append(str(round(100*max(up,down),2)))
            #print valuelist
            TableLines.append([nui.replace('_','\_')]+valuelist)

    return TableLines
    #ggH2000=GetVarOfNuisnace(['ggH_hww2000_c10brn00'],'CMS_ak8jet_jms_2016Up',2000,'Boosted',year)
    #qqH2000=GetVarOfNuisnace(['qqH_hww2000_c10brn00'],'CMS_ak8jet_jms_2016Up',2000,'Boosted',year)
    #wjets=GetVarOfNuisnace(['Wjets'],'CMS_ak8jet_jms_2016Up',1000,'Boosted',year)
    #top=GetVarOfNuisnace(['TT','SingleTop','tW'],'CMS_ak8jet_jms_2016Up',1000,'Boosted',year)
    #others=GetVarOfNuisnace(['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125','DY','QCD'],'CMS_ak8jet_jms_2016Up',1000,'Boosted',year)

    #print 'ggH2000',ggH2000
    #print 'qqH2000',qqH2000
    #print 'wjets',wjets
    #print 'top',top
    #print 'others',others


def fuck():
    print "1"
    inputlines=MakeSysTableLines(year=2016,bst='Boosted',proclist=['Wjets','Top','Others','ggf2000','vbf2000','ggf900','vbf900','ggf400','vbf400'] )
    caption='test'
    label='tab:test'
    outputtxt='table_rawline.tex'
    #print Lines
    #mkTableUsingLine(inputlines,caption,label,outputtxt)
    mkTableUsingLine(inputlines,caption,label,outputtxt)


if __name__ == '__main__':
    #'Others':['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125','DY','QCD']
    Others=['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125','DY','QCD'] 
    lumi2016=['lumi_13TeV_2016', 'lumi_13TeV_BBDefl', 'lumi_13TeV_DynBeta', 'lumi_13TeV_Ghosts', 'lumi_13TeV_XYFact']
    ak4jes2016=['CMS_ak4jet_jesAbsolute', 'CMS_ak4jet_jesAbsolute_2016', 'CMS_ak4jet_jesBBEC1', 'CMS_ak4jet_jesBBEC1_2016', 'CMS_ak4jet_jesEC2', 'CMS_ak4jet_jesEC2_2016', 'CMS_ak4jet_jesFlavorQCD', 'CMS_ak4jet_jesHF', 'CMS_ak4jet_jesHF_2016', 'CMS_ak4jet_jesRelativeBal', 'CMS_ak4jet_jesRelativeSample_2016']

    mass=1000
    bst='Boosted'
    year=2016
    ak4jes2016_var=GetVarOfNuisnaceListShape(Others,ak4jes2016,mass,bst,year)
    print ak4jes2016_var
