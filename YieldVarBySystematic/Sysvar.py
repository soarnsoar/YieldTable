import sys
sys.path.insert(0,'../python/')
from Utils import *
from ParseDatacard import ParseDatacard
from math import sqrt
import copy
#def ReadYield(inputpath,processlist): return dict_yield

#inputpath='example/histos___BoostedGGF_TOP_MEKDTAG_M1500_C0.001.root'
SamplesToShow={
    'ggf2000':['ggH_hww2000_c10brn00'],
    'vbf2000':['qqH_hww2000_c10brn00'],
    'ggf900':['ggH_hww900_c10brn00'],
    'vbf900':['qqH_hww900_c10brn00'],
    'ggf400':['ggH_hww400_c10brn00'],
    'vbf400':['qqH_hww400_c10brn00'],
    'Wjets':['Wjets'],
    'Top':['TT','SingleTop','tW'],
    'Others':['MultiV','WmHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125','DY','QCD','ggWW','qqWWqq']
}

def GetInputPath(mass,bst,year):
    
    inputpath='../../'+str(year)+'/Datacards_'+str(year)+'/Datacard_M'+str(mass)+'/__BoostedALL_SR_NoMEKDCut/Event/shapes/histos___BoostedALL_SR_NoMEKDCut.root '
    if bst=='Resolved':
        inputpath=inputpath.replace('Boosted','_Resolved')
        inputpath=inputpath.replace('SR','_SR')

    return inputpath


def GetVarOfNuisnace(proclist,nuis,mass,bst,year):

    inputpath=GetInputPath(mass,bst,year)
    var_in_ratio=ReadYieldVarProcList(inputpath,proclist,nuis)
    return var_in_ratio

def GetRMS(mylist):
    sum2=0.
    for x in mylist:
        sum2+=x**2
    if len(mylist)==0:return 0
    return sqrt(sum2)/len(mylist)
    
    

def GetVarOfNuisnaceListShape(proclist,nuisancelist,mass,bst,year):

    inputpath=GetInputPath(mass,bst,year)
    var_in_ratio_list=[]
    for nuis in nuisancelist:

        ##--within updown
        var_in_ratio_updown=[]
        for direction in ['Up','Down']:
            var_in_ratio=ReadYieldVarProcList(inputpath,proclist,nuis+direction)
            var_in_ratio_updown.append(var_in_ratio)
        var_in_ratio=max(var_in_ratio_updown)
        ##--took larger one of up/down
        var_in_ratio_list.append(var_in_ratio)
        
    Total_var_in_ratio=GetRMS(var_in_ratio_list)
    return Total_var_in_ratio

def GetVarOfNuisnaceListlnN(proclist,nuisancelist,mass,bst,year):
    ##--ParseDatacard
    #    NuisanceInfo=ParseDatacard('../'+str(year)+'/combined_card_1000.txt')
    NuisanceInfo=ParseDatacard('../../'+str(year)+'/combined_card_'+str(mass)+'.txt')
    #nuisance_info[nuis]={'type':constraint,'process':{}}
    
    #NuisanceInfo[]
    #value=nuisanceinfo['lumi_13TeV_DynBeta']['process']['Wjets']
    TotalVarList=[]
    for nui in nuisancelist:
        nuivarlist=[]
        for proc in proclist:
            thisvar=NuisanceInfo[nui]['process'][proc]
            if thisvar=='-':
                continue
            if '/' in thisvar:
                templist1=thisvar.split('/')
                templist2=[]
                for x in templist1:
                    templist2.append(float(x))
                thisvar=max(templist2)
            nuivarlist.append(float(thisvar)-1)
        if len(nuivarlist)==0:
            #print nui,'->len(nuivarlist)==0'
            continue
        TotalVarList.append(max(nuivarlist))
    return GetRMS(TotalVarList)

def PartseNuisacneValue(mystring):
    if mystring=='-':
        return '-'
    else:
        strsplit=mystring.split('/')
        varlist=[ abs(1-float(x))  for x in strsplit ]
        maxvar=max(varlist)
        return str(maxvar*100)

def Avg(inputlist):
    return sum(inputlist)/len(inputlist)
def ConvertToPercent(x):
    return round(float(x),4)*100


def TestNuisanceDict2016(Sample,bst='Boosted'):
    print "===2016===="
    print bst
    print "----",Sample,"----"
    exec(open('Nuisance2016.py','r'))
    #NuisanceCategory2016[NuisanceGroup]['list']
    #GetVarOfNuisnaceListShape(listsample,nuisancelist,massofpath,bst,year)

    OrderRaw=['xsec_qcdscale', 'ak4jet_jes_jer', 'xsec_pdf', 'ElectronTrigger', 'ak8jet_jes_jer', 'ElectronEnergyScale', 'PS', 'pu', 'MuonTrigger', 'MuonID', 'pdf_accept', 'ElectronID', 'Wtag_eff', 'qcdscale_accept', 'lumionisty', 'wtag_jms_jmr', 'btag', 'MuonEnergyScale', 'MET', 'mjjshape', 'Prefireing', 'bkgnorm']
    Order=['lumionisty','ak4jet_jes_jer','ak8jet_jes_jer','wtag_jms_jmr','btag','Wtag_eff','Prefireing','MET','ElectronTrigger','MuonTrigger','ElectronID','MuonID','ElectronEnergyScale','MuonEnergyScale','mjjshape','pu','xsec_qcdscale','xsec_pdf','qcdscale_accept','pdf_accept','bkgnorm','PS']
    print len(OrderRaw)
    print len(Order)
    mass=1000
    for NuiGroup in Order:
        print NuisanceCategory2016[NuiGroup]['alias']
    varlist=[]
    for NuiGroup in Order:
        
        
        NuiList=NuisanceCategory2016[NuiGroup]['list']
        #SampleList=SamplesToShow['Wjets']
        if '400' in Sample : mass=400
        if '900' in Sample : mass=900
        if '2000' in Sample : mass=2000
        SampleList=SamplesToShow[Sample]
        if not 'type' in NuisanceCategory2016[NuiGroup]:
            thisvar=GetVarOfNuisnaceListShape(SampleList,NuiList,mass,bst,2016)
        elif NuisanceCategory2016[NuiGroup]['type']=='norm':
            thisvar=GetVarOfNuisnaceListlnN(SampleList,NuiList,mass,bst,2016)
        else:
            thisvar=GetVarOfNuisnaceListShape(SampleList,NuiList,mass,bst,2016)
        thisvar_100=ConvertToPercent(thisvar)
        #print NuisanceCategory2016[NuiGroup]['alias'],thisvar_100
        print '&'+str(thisvar_100)
        #print thisvar
        #varlist.append(str(thisvar_100))
        #return str(thisvar_100)
    return varlist
def TestNuisanceDict2017(Sample,bst='Boosted'):
    print "===2017===="
    print bst
    print "----",Sample,"----"
    exec(open('Nuisance2017.py','r'))
    #NuisanceCategory2017[NuisanceGroup]['list']
    #GetVarOfNuisnaceListShape(listsample,nuisancelist,massofpath,bst,year)

    OrderRaw=['QCD scale Norm.', 'AK4Jet JES/JER', 'PDF Signal Norm.', 'ElectronTrigger Effieicny', 'AK8Jet JES/JER', 'Electron Energy Scale', 'Parton Shower Model', 'PileUp', 'MuonTrigger Effieicny', 'Muon Identification', 'PDF Acceptance', 'Electron Identification', 'WtagAK8Jet Eff.', 'QCD scale Acceptance', 'Luminosity', 'WtagAK8Jet JMSJMR', 'B-tagging', 'Muon Momentum Scale', 'Missing Energy', 'AK4Jet MjjShape', 'Prefiring', 'Background Norm.']
    Order=['lumionisty','ak4jet_jes_jer','ak8jet_jes_jer','wtag_jms_jmr','btag','Wtag_eff','Prefireing','MET','ElectronTrigger','MuonTrigger','ElectronID','MuonID','ElectronEnergyScale','MuonEnergyScale','mjjshape','pu','xsec_qcdscale','xsec_pdf','qcdscale_accept','pdf_accept','bkgnorm','PS']
    print len(OrderRaw)
    print len(Order)
    mass=1000
    for NuiGroup in Order:
        print NuisanceCategory2017[NuiGroup]['alias']
    for NuiGroup in Order:

        
        NuiList=NuisanceCategory2017[NuiGroup]['list']
        #SampleList=SamplesToShow['Wjets']
        if '400' in Sample : mass=400
        if '900' in Sample : mass=900
        if '2000' in Sample : mass=2000
        SampleList=SamplesToShow[Sample]
        if not 'type' in NuisanceCategory2017[NuiGroup]:
            thisvar=GetVarOfNuisnaceListShape(SampleList,NuiList,mass,bst,2017)
        elif NuisanceCategory2017[NuiGroup]['type']=='norm':
            thisvar=GetVarOfNuisnaceListlnN(SampleList,NuiList,mass,bst,2017)
        else:

            thisvar=GetVarOfNuisnaceListShape(SampleList,NuiList,mass,bst,2017)
        thisvar_100=ConvertToPercent(thisvar)
        #print NuisanceCategory2017[NuiGroup]['alias'],thisvar_100
        print '&'+str(thisvar_100)
        #print thisvar


def TestNuisanceDict2018(Sample,bst='Boosted'):
    print "===2018===="
    print bst
    print "----",Sample,"----"
    exec(open('Nuisance2018.py','r'))
    #NuisanceCategory2018[NuisanceGroup]['list']
    #GetVarOfNuisnaceListShape(listsample,nuisancelist,massofpath,bst,year)

    OrderRaw=['xsec_qcdscale', 'ak4jet_jes_jer', 'xsec_pdf', 'ElectronTrigger', 'ak8jet_jes_jer', 'ElectronEnergyScale', 'PS', 'pu', 'MuonTrigger', 'MuonID', 'pdf_accept', 'ElectronID', 'qcdscale_accept', 'Wtag_eff', 'HEM1516', 'lumionisty', 'wtag_jms_jmr', 'btag', 'MuonEnergyScale', 'MET', 'mjjshape', 'bkgnorm']


    Order=['lumionisty','ak4jet_jes_jer','ak8jet_jes_jer','wtag_jms_jmr','btag','Wtag_eff','HEM1516','MET','ElectronTrigger','MuonTrigger','ElectronID','MuonID','ElectronEnergyScale','MuonEnergyScale','mjjshape','pu','xsec_qcdscale','xsec_pdf','qcdscale_accept','pdf_accept','bkgnorm','PS']
    print len(OrderRaw)
    print len(Order)
    mass=1000
    for NuiGroup in Order:
        print NuisanceCategory2018[NuiGroup]['alias']
    for NuiGroup in Order:

        
        NuiList=NuisanceCategory2018[NuiGroup]['list']
        #SampleList=SamplesToShow['Wjets']
        if '400' in Sample : mass=400
        if '900' in Sample : mass=900
        if '2000' in Sample : mass=2000
        SampleList=SamplesToShow[Sample]
        if not 'type' in NuisanceCategory2018[NuiGroup]:
            thisvar=GetVarOfNuisnaceListShape(SampleList,NuiList,mass,bst,2018)
        elif NuisanceCategory2018[NuiGroup]['type']=='norm':
            thisvar=GetVarOfNuisnaceListlnN(SampleList,NuiList,mass,bst,2018)
        else:

            thisvar=GetVarOfNuisnaceListShape(SampleList,NuiList,mass,bst,2018)
        thisvar_100=ConvertToPercent(thisvar)
        #print NuisanceCategory2018[NuiGroup]['alias'],thisvar_100
        print '&'+str(thisvar_100)
        #print thisvar


if __name__ == '__main__':
    ##--
    slist=['Wjets','Top','Others','ggf2000','vbf2000','ggf900','vbf900','ggf400','vbf400']
    slist=['Wjets','Top','Others','ggf2000','vbf2000','ggf400','vbf400']
    varlist={}
    for S in slist:
        #TestNuisanceDict('Wjets')
        #TestNuisanceDict('Top')
        #TestNuisanceDict('Others)
        #varlist[S]=copy.deepcopy(TestNuisanceDict2016(S))
        #varlist.append(var)
        #TestNuisanceDict2016(S)
        #TestNuisanceDict2017(S)
        #TestNuisanceDict2018(S)

        TestNuisanceDict2018(S,'Resolved')
        #TestNuisanceDict2017(S)
        #TestNuisanceDict2018(S)
    #print '&'.join(varlist)
