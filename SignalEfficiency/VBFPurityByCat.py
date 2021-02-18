import ROOT
import glob
import sys
from TGraphHelper import *
from LatinoAnalysis.Tools.commonTools import *
#this_xsec=HiggsXS.GetHiggsProdXS('YR4','13TeV','ggH',int(MX),'bsm')*HiggsXS.GetHiggsBR('YR4','H_WW',int(MX),'bsm')
#this_xsec=HiggsXS.GetHiggsProdXS('YR4','13TeV','vbfH',int(MX),'bsm')*HiggsXS.GetHiggsBR('YR4','H_WW',int(MX),'bsm')
PrintPath=False

HiggsXS = HiggsXSection()


#sys.path.insert(0,'../python/')
#from Utils import *
#def ReadYield(inputpath,processlist):
def ReadYield(inputpath,processlist):
        ##---Read Total integrals
        myrf=ROOT.TFile.Open(inputpath)
        if PrintPath: print inputpath
        dict_yield={}

        ##--for each process
        for process in processlist:
                histopath=process
                if PrintPath:print histopath
                myhisto=myrf.Get(histopath)
                dict_yield[process]=myhisto.Integral()

        myrf.Close()
        return dict_yield


def GetMassPoints(Year):
        ggf='../../'+Year+'/MassPoints/List_MX.py'
        vbf='../../'+Year+'/MassPoints/List_MX_VBF.py'

        exec(open(ggf,'r'))
        exec(open(vbf,'r'))
        
        List_MX_common=list(set(List_MX).intersection(List_MX_VBF))
        #List_MX+List_MX_VBF

        return sorted(List_MX_common)


def GetConf():

	##../../2016/rootFile_2016_cms_scratch_jhchoi_Statonly_noTreeBase_NoMEKD_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root
        #rootFile_2016__cms_scratch_jhchoi_Final2101010_0.01MEKD_REGROUP_Boosted_HMFull_V12_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR
        #rootFile_2016__cms_scratch_jhchoi_Final2101010_0.01MEKD_REGROUP_Resolved_HMFull_V12_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR

	configuration={
                '2016':{
                        'inputlist':{
                                'Boost GGF':{
                                        'cut':'__BoostedGGF_SR_MEKDTAG_M1500_C0.01',
                                        'inputfile':'../../2016/rootFile*Boosted*SR*/hadd.root'
                                },
                                'Boost Untagged':{
                                        'cut':'__BoostedGGF_SR_UNTAGGED_M1500_C0.01',
                                        'inputfile':'../../2016/rootFile*Boosted*SR*/hadd.root',
                                },
                                'Boost VBF':{
                                        'cut':'__BoostedVBF_SR_NoMEKDCut',
                                        'inputfile':'../../2016/rootFile*Boosted*SR*/hadd.root',
                                },
                                'Resol GGF':{
                                        'cut':'___ResolvedGGF__SR_MEKDTAG_M400_C0.01',
                                        'inputfile':'../../2016/rootFile*Resolved*SR*/hadd.root',
                                },
                                'Resol Untagged':{
                                        'cut':'___ResolvedGGF__SR_UNTAGGED_M400_C0.01',
                                        'inputfile':'../../2016/rootFile*Resolved*SR*/hadd.root'
                                },
                                'Resol VBF':{
                                        'cut':'___ResolvedVBF__SR_NoMEKDCut',
                                        'inputfile':'../../2016/rootFile*Resolved*SR*/hadd.root'
                                },
                                ##--DNN
                                'Boost GGFDNN':{
                                        'cut':'__BoostedGGFDNN_SR_MEKDTAG_M1500_C0.01',
                                        'inputfile':'../../2016/rootFile*Boosted*SR*/hadd.root'
                                },
                                'Boost UntaggedDNN':{
                                        'cut':'__BoostedGGFDNN_SR_UNTAGGED_M1500_C0.01',
                                        'inputfile':'../../2016/rootFile*Boosted*SR*/hadd.root',
                                },
                                'Boost VBFDNN':{
                                        'cut':'__BoostedVBFDNN_SR_NoMEKDCut',
                                        'inputfile':'../../2016/rootFile*Boosted*SR*/hadd.root',
                                },
                                'Resol GGFDNN':{
                                        'cut':'___ResolvedGGFDNN__SR_MEKDTAG_M400_C0.01',
                                        'inputfile':'../../2016/rootFile*Resolved*SR*/hadd.root',
                                },
                                'Resol UntaggedDNN':{
                                        'cut':'___ResolvedGGFDNN__SR_UNTAGGED_M400_C0.01',
                                        'inputfile':'../../2016/rootFile*Resolved*SR*/hadd.root'
                                },
                                'Resol VBFDNN':{
                                        'cut':'___ResolvedVBFDNN__SR_NoMEKDCut',
                                        'inputfile':'../../2016/rootFile*Resolved*SR*/hadd.root'
                                },

                        },
                        'inputxsec':1.,
                        'inputlumi':35.9,
                },
                '2017':{
                        'inputlist':{
                                'Boost GGF':{
                                        'cut':'__BoostedGGF_SR_MEKDTAG_M1500_C0.01',
                                        'inputfile':'../../2017/rootFile*Boosted*SR*/hadd.root'
                                },
                                'Boost Untagged':{
                                        'cut':'__BoostedGGF_SR_UNTAGGED_M1500_C0.01',
                                        'inputfile':'../../2017/rootFile*Boosted*SR*/hadd.root',
                                },
                                'Boost VBF':{
                                        'cut':'__BoostedVBF_SR_NoMEKDCut',
                                        'inputfile':'../../2017/rootFile*Boosted*SR*/hadd.root',
                                },
                                'Resol GGF':{
                                        'cut':'___ResolvedGGF__SR_MEKDTAG_M400_C0.01',
                                        'inputfile':'../../2017/rootFile*Resolved*SR*/hadd.root',
                                },
                                'Resol Untagged':{
                                        'cut':'___ResolvedGGF__SR_UNTAGGED_M400_C0.01',
                                        'inputfile':'../../2017/rootFile*Resolved*SR*/hadd.root'
                                },
                                'Resol VBF':{
                                        'cut':'___ResolvedVBF__SR_NoMEKDCut',
                                        'inputfile':'../../2017/rootFile*Resolved*SR*/hadd.root'
                                },

                                ##--DNN
                                'Boost GGFDNN':{
                                        'cut':'__BoostedGGFDNN_SR_MEKDTAG_M1500_C0.01',
                                        'inputfile':'../../2017/rootFile*Boosted*SR*/hadd.root'
                                },
                                'Boost UntaggedDNN':{
                                        'cut':'__BoostedGGFDNN_SR_UNTAGGED_M1500_C0.01',
                                        'inputfile':'../../2017/rootFile*Boosted*SR*/hadd.root',
                                },
                                'Boost VBFDNN':{
                                        'cut':'__BoostedVBFDNN_SR_NoMEKDCut',
                                        'inputfile':'../../2017/rootFile*Boosted*SR*/hadd.root',
                                },
                                'Resol GGFDNN':{
                                        'cut':'___ResolvedGGFDNN__SR_MEKDTAG_M400_C0.01',
                                        'inputfile':'../../2017/rootFile*Resolved*SR*/hadd.root',
                                },
                                'Resol UntaggedDNN':{
                                        'cut':'___ResolvedGGFDNN__SR_UNTAGGED_M400_C0.01',
                                        'inputfile':'../../2017/rootFile*Resolved*SR*/hadd.root'
                                },
                                'Resol VBFDNN':{
                                        'cut':'___ResolvedVBFDNN__SR_NoMEKDCut',
                                        'inputfile':'../../2017/rootFile*Resolved*SR*/hadd.root'
                                },
                        },

                        'inputxsec':1.,
                        'inputlumi':41.5,
                },
                '2018':{
                        'inputlist':{
                                'Boost GGF':{
                                        'cut':'__BoostedGGF_SR_MEKDTAG_M1500_C0.01',
                                        'inputfile':'../../2018/rootFile*Boosted*SR*/hadd.root'
                                },
                                'Boost Untagged':{
                                        'cut':'__BoostedGGF_SR_UNTAGGED_M1500_C0.01',
                                        'inputfile':'../../2018/rootFile*Boosted*SR*/hadd.root',
                                },
                                'Boost VBF':{
                                        'cut':'__BoostedVBF_SR_NoMEKDCut',
                                        'inputfile':'../../2018/rootFile*Boosted*SR*/hadd.root',
                                },
                                'Resol GGF':{
                                        'cut':'___ResolvedGGF__SR_MEKDTAG_M400_C0.01',
                                        'inputfile':'../../2018/rootFile*Resolved*SR*/hadd.root',
                                },
                                'Resol Untagged':{
                                        'cut':'___ResolvedGGF__SR_UNTAGGED_M400_C0.01',
                                        'inputfile':'../../2018/rootFile*Resolved*SR*/hadd.root'
                                },
                                'Resol VBF':{
                                        'cut':'___ResolvedVBF__SR_NoMEKDCut',
                                        'inputfile':'../../2018/rootFile*Resolved*SR*/hadd.root'
                                },
                                ##--DNN
                                'Boost GGFDNN':{
                                        'cut':'__BoostedGGFDNN_SR_MEKDTAG_M1500_C0.01',
                                        'inputfile':'../../2018/rootFile*Boosted*SR*/hadd.root'
                                },
                                'Boost UntaggedDNN':{
                                        'cut':'__BoostedGGFDNN_SR_UNTAGGED_M1500_C0.01',
                                        'inputfile':'../../2018/rootFile*Boosted*SR*/hadd.root',
                                },
                                'Boost VBFDNN':{
                                        'cut':'__BoostedVBFDNN_SR_NoMEKDCut',
                                        'inputfile':'../../2018/rootFile*Boosted*SR*/hadd.root',
                                },
                                'Resol GGFDNN':{
                                        'cut':'___ResolvedGGFDNN__SR_MEKDTAG_M400_C0.01',
                                        'inputfile':'../../2018/rootFile*Resolved*SR*/hadd.root',
                                },
                                'Resol UntaggedDNN':{
                                        'cut':'___ResolvedGGFDNN__SR_UNTAGGED_M400_C0.01',
                                        'inputfile':'../../2018/rootFile*Resolved*SR*/hadd.root'
                                },
                                'Resol VBFDNN':{
                                        'cut':'___ResolvedVBFDNN__SR_NoMEKDCut',
                                        'inputfile':'../../2018/rootFile*Resolved*SR*/hadd.root'
                                },
                        },

                        'inputxsec':1.,
                        'inputlumi':59.7,
                }
        }

        return configuration
def GetEff(proc,Year):
        #/cms_scratch/jhchoi/Final2101010_0.01MEKD_REGROUP/YieldTable/SignalEfficiency
        ###---
        configuration=GetConf()
        MX=int(GetMassInProc(proc))
        #ReadYield(inputpath,processlist)
        #Year='2016'
        #proc='ggH_hww5000_c10brn00'
        prod=''
        if 'ggH' in proc:
                prod='ggf'
                this_xsec=HiggsXS.GetHiggsProdXS('YR4','13TeV','ggH',int(MX),'bsm')*HiggsXS.GetHiggsBR('YR4','H_WW',int(MX),'bsm')
        if 'qqH' in proc:
                prod='vbf'
                this_xsec=HiggsXS.GetHiggsProdXS('YR4','13TeV','vbfH',int(MX),'bsm')*HiggsXS.GetHiggsBR('YR4','H_WW',int(MX),'bsm')
        #print Year,proc
        #print configuration[Year]['inputlist']
        my_yield=0.
        my_yield_list=[]
        #this_xsec=HiggsXS.GetHiggsProdXS('YR4','13TeV','ggH',int(MX),'bsm')*HiggsXS.GetHiggsBR('YR4','H_WW',int(MX),'bsm')
        #this_xsec=HiggsXS.GetHiggsProdXS('YR4','13TeV','vbfH',int(MX),'bsm')*HiggsXS.GetHiggsBR('YR4','H_WW',int(MX),'bsm')


        #total_prod=configuration[Year]['inputxsec']*configuration[Year]['inputlumi']*1000.
        total_prod=this_xsec*configuration[Year]['inputlumi']*1000.
        for rg in configuration[Year]['inputlist']:
                #if prod=='ggf' and 'VBF' in rg: continue
                #if prod=='vbf' and 'GGF' in rg: continue
                inputpath=glob.glob(configuration[Year]['inputlist'][rg]['inputfile'])[0]
                #__BoostedALL_SR_NoMEKDCut
                #___ResolvedALL__SR_NoMEKDCut
                cut=configuration[Year]['inputlist'][rg]['cut']
                histopath=cut+'/Event/histo_'+proc
                #print cutname
                #print histopath
                this_yield=ReadYield(inputpath,[histopath])
                #print 'type(this_yield)',type(this_yield)
                #print 'type(total_prod)',type(total_prod)
                if not prod in configuration[Year]['inputlist'][rg]:configuration[Year]['inputlist'][rg][prod]={}
                configuration[Year]['inputlist'][rg][prod]['eff']=this_yield[histopath]/total_prod
                configuration[Year]['inputlist'][rg][prod]['yield']=this_yield[histopath]
                my_yield+=this_yield[histopath]



        
        eff=my_yield/total_prod
        #print 'eff=',eff
        return eff,configuration


def GetProcName(prod,mass):
        proc=None
        if prod=='ggf':proc='ggH_hww'+str(mass)+'_c10brn00'
        if prod=='vbf':proc='qqH_hww'+str(mass)+'_c10brn00'
        return proc
def GetMassInProc(proc):
        return proc.split('hww')[1].split('_')[0]
def DrawMassVsTotalEff(prod,Year,min_mass=200):
        #ggH_hww5000_c10brn00
        proc='ggH_hww5000_c10brn00'
        
                
        masslist=GetMassPoints(Year)
        xlist=[]
        ylist=[]

        for mass in masslist:
                if mass<min_mass:continue
                proc=GetProcName(prod,mass)
                eff,configuration=GetEff(proc,Year)
                ylist.append(eff)
                xlist.append(mass)
        mygr=TGraph_Maker(xlist,ylist)
        c=ROOT.TCanvas()
        mygr.Draw()
        c.SaveAs(prod+'.pdf')


def GetTotalEff(prod,Year,min_mass=200):
        #ggH_hww5000_c10brn00
        proc='ggH_hww5000_c10brn00'
        
                
        masslist=GetMassPoints(Year)
        xlist=[]
        ylist=[]

        for mass in masslist:
                if mass<min_mass:continue
                proc=GetProcName(prod,mass)
                eff,configuration=GetEff(proc,Year)
                ylist.append(eff)
                xlist.append(mass)
        return xlist,ylist
def GetEffOfCat(prod,cat,Year,min_mass=200):
        #ggH_hww5000_c10brn00
        proc='ggH_hww5000_c10brn00'
        
                
        masslist=GetMassPoints(Year)
        xlist=[]
        ylist=[]

        for mass in masslist:
                if mass<min_mass:continue
                proc=GetProcName(prod,mass)
                total_eff,configuration=GetEff(proc,Year)
                #configuration[Year]['inputlist'][rg][prod]['eff']
                eff=configuration[Year]['inputlist'][cat][prod]['eff']
                ylist.append(eff)
                xlist.append(mass)
        return xlist,ylist

def GetVBFEffOfCat(prod,cat,Year,min_mass=200):
        #ggH_hww5000_c10brn00
        proc='ggH_hww5000_c10brn00'
        isBoost=False
        if 'Boost' in cat:
                isBoost=True
        if 'Resol' in cat:
                isBoost=False
        masslist=GetMassPoints(Year)
        xlist=[]
        ylist=[]
        print '--',prod,cat,'--'
        for mass in masslist:
                #print mass
                if mass<min_mass:continue
                proc=GetProcName(prod,mass)
                total_eff,configuration=GetEff(proc,Year)
                #configuration[Year]['inputlist'][rg][prod]['eff']
                #configuration[Year]['inputlist'][rg][prod]['yield']
                deno=0.
                for rg in configuration[Year]['inputlist']:
                        if isBoost:
                                if 'Boost' in rg and not 'DNN' in rg :deno+=configuration[Year]['inputlist'][rg][prod]['yield']
                        else :
                                if 'Resol' in rg and not 'DNN' in rg :deno+=configuration[Year]['inputlist'][rg][prod]['yield']
                        
                eff=configuration[Year]['inputlist'][cat][prod]['yield']/deno
                ylist.append(eff)
                xlist.append(mass)
        return xlist,ylist

def GetVBFPurityOfCat(prod,isDNN,cat,Year,min_mass=200):
        #ggH_hww5000_c10brn00
        proc='ggH_hww5000_c10brn00'
        isBoost=False
        if 'Boost' in cat:
                isBoost=True
        if 'Resol' in cat:
                isBoost=False
        masslist=GetMassPoints(Year)
        xlist=[]
        ylist=[]
        
        print '--',prod,'--'
        for mass in masslist:
                #print mass
                if mass<min_mass:continue
                proc_ggf=GetProcName('ggf',mass)
                proc_vbf=GetProcName('vbf',mass)
                total_eff_ggf,configuration_ggf=GetEff(proc_ggf,Year) ##--ggf sig yield
                total_eff_vbf,configuration_vbf=GetEff(proc_vbf,Year) ##--vbf sig yield
                #configuration[Year]['inputlist'][rg][prod]['eff']
                #configuration[Year]['inputlist'][rg][prod]['yield']
                ggf_yield=0.
                vbf_yield=0.
                for rg in configuration_ggf[Year]['inputlist']:

                        if isBoost:
                                if 'Resol' in rg : continue
                        else:
                                if 'Boost' in rg: continue
                        if isDNN:
                                if not 'DNN' in rg: continue
                        else:
                                if 'DNN' in rg : continue
                        if prod=='ggf':
                                if 'VBF' in rg: continue
                        if prod=='vbf':
                                if not 'VBF' in rg: continue
                                
                        ggf_yield+=configuration_ggf[Year]['inputlist'][rg]['ggf']['yield']
                        vbf_yield+=configuration_vbf[Year]['inputlist'][rg]['vbf']['yield']
                        
                #purity=configuration[Year]['inputlist'][cat][prod]['yield']/deno
                if prod=='ggf': 
                        purity=ggf_yield/(ggf_yield+vbf_yield)
                if prod=='vbf': 
                        purity=vbf_yield/(ggf_yield+vbf_yield)
                ylist.append(purity)
                xlist.append(mass)
        return xlist,ylist

def GetMassVsEffTGr(bst,Year,min_mass=200):
        #prod
        prodlist=['ggf','vbf']

        grlist={}

        for prod in prodlist:
                grlist[prod]={}#GetVBFEffOfCat
                #gr_total={'title':'Total '+prod+' sig'}
                #gr_total['xlist'], gr_total['ylist']=GetTotalEff(prod,Year)
                #gr_total['gr']=TGraph_Maker(gr_total['xlist'], gr_total['ylist'])
                

                ##---
                if 'Boost' in bst:
                        gr_Boost_GGF={'title':prod+' sig in Boost GGF Cat.'}
                        gr_Boost_GGF['xlist'], gr_Boost_GGF['ylist']=GetVBFEffOfCat(prod,'Boost GGF',Year)
                        gr_Boost_GGF['gr']=TGraph_Maker(gr_Boost_GGF['xlist'], gr_Boost_GGF['ylist'])
                        
                        gr_Boost_Untagged={'title':prod+' sig in Boost Untagged Cat.'}
                        gr_Boost_Untagged['xlist'], gr_Boost_Untagged['ylist']=GetVBFEffOfCat(prod,'Boost Untagged',Year)
                        gr_Boost_Untagged['gr']=TGraph_Maker(gr_Boost_Untagged['xlist'], gr_Boost_Untagged['ylist'])
                        
                        gr_Boost_VBF={'title':prod+' sig in Boost VBF Cat.'}
                        gr_Boost_VBF['xlist'], gr_Boost_VBF['ylist']=GetVBFEffOfCat(prod,'Boost VBF',Year)
                        gr_Boost_VBF['gr']=TGraph_Maker(gr_Boost_VBF['xlist'], gr_Boost_VBF['ylist'])
                if 'Resol' in bst:
                        gr_Resol_GGF={'title':prod+' sig in Resol GGF Cat.'}
                        gr_Resol_GGF['xlist'], gr_Resol_GGF['ylist']=GetVBFEffOfCat(prod,'Resol GGF',Year)
                        gr_Resol_GGF['gr']=TGraph_Maker(gr_Resol_GGF['xlist'], gr_Resol_GGF['ylist'])
                        
                        gr_Resol_Untagged={'title':prod+' sig in Resol Untagged Cat.'}
                        gr_Resol_Untagged['xlist'], gr_Resol_Untagged['ylist']=GetVBFEffOfCat(prod,'Resol Untagged',Year)
                        gr_Resol_Untagged['gr']=TGraph_Maker(gr_Resol_Untagged['xlist'], gr_Resol_Untagged['ylist'])
                        
                        gr_Resol_VBF={'title':prod+' sig in Resol VBF Cat.'}
                        gr_Resol_VBF['xlist'], gr_Resol_VBF['ylist']=GetVBFEffOfCat(prod,'Resol VBF',Year)
                        gr_Resol_VBF['gr']=TGraph_Maker(gr_Resol_VBF['xlist'], gr_Resol_VBF['ylist'])

                ##--
                if 'Boost' in bst:

                        gr_Boost_NONVBF={'title':prod+' sig in Boosted NonVBF Cat.'}
                        gr_Boost_NONVBF['xlist']=gr_Boost_GGF['xlist']
                        gr_Boost_NONVBF['ylist']=[]
                        for idx in range(len(gr_Boost_NONVBF['xlist'])):
                                eff_com=gr_Boost_GGF['ylist'][idx]+gr_Boost_Untagged['ylist'][idx]
                                #+gr_Boost_VBF['ylist'][idx]
                                gr_Boost_NONVBF['ylist'].append(eff_com)
                        gr_Boost_NONVBF['gr']=TGraph_Maker(gr_Boost_NONVBF['xlist'], gr_Boost_NONVBF['ylist'])
                        #gr_Boost_NONVBF['gr'].SetLineColor(2)
                if 'Resol' in bst:

                        gr_Resol_NONVBF={'title':prod+' sig in Resolved NonVBF Cat.'}
                        gr_Resol_NONVBF['xlist']=gr_Resol_GGF['xlist']
                        gr_Resol_NONVBF['ylist']=[]
                        for idx in range(len(gr_Resol_NONVBF['xlist'])):
                                eff_com=gr_Resol_GGF['ylist'][idx]+gr_Resol_Untagged['ylist'][idx]
                                #+gr_Resol_VBF['ylist'][idx]
                                gr_Resol_NONVBF['ylist'].append(eff_com)
                        gr_Resol_NONVBF['gr']=TGraph_Maker(gr_Resol_NONVBF['xlist'], gr_Resol_NONVBF['ylist'])
                        #gr_Resol_NONVBF['gr'].SetLineColor(4)

                ##--DNN
                if 'Boost' in bst:

                        gr_Boost_GGFDNN={'title':prod+' sig in Boost GGFDNN Cat.'}
                        gr_Boost_GGFDNN['xlist'], gr_Boost_GGFDNN['ylist']=GetVBFEffOfCat(prod,'Boost GGFDNN',Year)
                        gr_Boost_GGFDNN['gr']=TGraph_Maker(gr_Boost_GGFDNN['xlist'], gr_Boost_GGFDNN['ylist'])
                        
                        gr_Boost_UntaggedDNN={'title':prod+' sig in Boost UntaggedDNN Cat.'}
                        gr_Boost_UntaggedDNN['xlist'], gr_Boost_UntaggedDNN['ylist']=GetVBFEffOfCat(prod,'Boost Untagged',Year)
                        gr_Boost_UntaggedDNN['gr']=TGraph_Maker(gr_Boost_UntaggedDNN['xlist'], gr_Boost_UntaggedDNN['ylist'])
                        
                        gr_Boost_VBFDNN={'title':prod+' sig in Boost VBFDNN Cat.'}
                        gr_Boost_VBFDNN['xlist'], gr_Boost_VBFDNN['ylist']=GetVBFEffOfCat(prod,'Boost VBFDNN',Year)
                        gr_Boost_VBFDNN['gr']=TGraph_Maker(gr_Boost_VBFDNN['xlist'], gr_Boost_VBFDNN['ylist'])
                if 'Resol' in bst:

                        gr_Resol_GGFDNN={'title':prod+' sig in Resol GGFDNN Cat.'}
                        gr_Resol_GGFDNN['xlist'], gr_Resol_GGFDNN['ylist']=GetVBFEffOfCat(prod,'Resol GGFDNN',Year)
                        gr_Resol_GGFDNN['gr']=TGraph_Maker(gr_Resol_GGFDNN['xlist'], gr_Resol_GGFDNN['ylist'])
                        
                        gr_Resol_UntaggedDNN={'title':prod+' sig in Resol UntaggedDNN Cat.'}
                        gr_Resol_UntaggedDNN['xlist'], gr_Resol_UntaggedDNN['ylist']=GetVBFEffOfCat(prod,'Resol UntaggedDNN',Year)
                        gr_Resol_UntaggedDNN['gr']=TGraph_Maker(gr_Resol_UntaggedDNN['xlist'], gr_Resol_UntaggedDNN['ylist'])
                        
                        gr_Resol_VBFDNN={'title':prod+' sig in Resol VBFDNN Cat.'}
                        gr_Resol_VBFDNN['xlist'], gr_Resol_VBFDNN['ylist']=GetVBFEffOfCat(prod,'Resol VBFDNN',Year)
                        gr_Resol_VBFDNN['gr']=TGraph_Maker(gr_Resol_VBFDNN['xlist'], gr_Resol_VBFDNN['ylist'])

                ##--
                if 'Boost' in bst:

                        gr_Boost_NONVBFDNN={'title':prod+' sig in Boosted NonVBFDNN Cat.'}
                        gr_Boost_NONVBFDNN['xlist']=gr_Boost_GGF['xlist']
                        gr_Boost_NONVBFDNN['ylist']=[]
                        for idx in range(len(gr_Boost_NONVBFDNN['xlist'])):
                                eff_com=gr_Boost_GGFDNN['ylist'][idx]+gr_Boost_UntaggedDNN['ylist'][idx]
                                #+gr_Boost_VBF['ylist'][idx]
                                gr_Boost_NONVBFDNN['ylist'].append(eff_com)
                        gr_Boost_NONVBFDNN['gr']=TGraph_Maker(gr_Boost_NONVBFDNN['xlist'], gr_Boost_NONVBFDNN['ylist'])
                        #gr_Boost_NONVBF['gr'].SetLineColor(2)
                
                if 'Resol' in bst:

                        gr_Resol_NONVBFDNN={'title':prod+' sig in Resolved NonVBFDNN Cat.'}
                        gr_Resol_NONVBFDNN['xlist']=gr_Resol_GGF['xlist']
                        gr_Resol_NONVBFDNN['ylist']=[]
                        for idx in range(len(gr_Resol_NONVBFDNN['xlist'])):
                                eff_com=gr_Resol_GGFDNN['ylist'][idx]+gr_Resol_UntaggedDNN['ylist'][idx]
                                #+gr_Resol_VBFDNN['ylist'][idx]
                                gr_Resol_NONVBFDNN['ylist'].append(eff_com)
                        gr_Resol_NONVBFDNN['gr']=TGraph_Maker(gr_Resol_NONVBFDNN['xlist'], gr_Resol_NONVBFDNN['ylist'])
                        #gr_Resol_NONVBF['gr'].SetLineColor(4)


                ##--
                if 'Boost' in bst:

                        gr_Boost={'title':prod+' sig in Boosted Cat.'}
                        gr_Boost['xlist']=gr_Boost_GGF['xlist']
                        gr_Boost['ylist']=[]
                        for idx in range(len(gr_Boost['xlist'])):
                                eff_com=gr_Boost_GGF['ylist'][idx]+gr_Boost_Untagged['ylist'][idx]+gr_Boost_VBF['ylist'][idx]
                                gr_Boost['ylist'].append(eff_com)
                        gr_Boost['gr']=TGraph_Maker(gr_Boost['xlist'], gr_Boost['ylist'])
                        gr_Boost['gr'].SetLineColor(2)
                if 'Resol' in bst:
        
                        gr_Resol={'title':prod+' sig in Resolved Cat.'}
                        gr_Resol['xlist']=gr_Resol_GGF['xlist']
                        gr_Resol['ylist']=[]
                        for idx in range(len(gr_Resol['xlist'])):
                                eff_com=gr_Resol_GGF['ylist'][idx]+gr_Resol_Untagged['ylist'][idx]+gr_Resol_VBF['ylist'][idx]
                                gr_Resol['ylist'].append(eff_com)
                        gr_Resol['gr']=TGraph_Maker(gr_Resol['xlist'], gr_Resol['ylist'])
                        #gr_Resol['gr'].SetLineColor(4)
                        
                        #grlist[prod]['total']=gr_total


                if 'Boost' in bst:

                        grlist[prod]['Boost_GGF_CAT']=gr_Boost_GGF
                        grlist[prod]['Boost_Untagged_CAT']=gr_Boost_Untagged
                        grlist[prod]['Boost_VBF_CAT']=gr_Boost_VBF
                        grlist[prod]['Boost_NONVBF_CAT']=gr_Boost_NONVBF
                if 'Resol' in bst:


                        grlist[prod]['Resol_GGF_CAT']=gr_Resol_GGF
                        grlist[prod]['Resol_Untagged_CAT']=gr_Resol_Untagged
                        grlist[prod]['Resol_VBF_CAT']=gr_Resol_VBF
                        grlist[prod]['Resol_NONVBF_CAT']=gr_Resol_NONVBF
                ##--DNN
                if 'Boost' in bst:

                        grlist[prod]['Boost_GGFDNN_CAT']=gr_Boost_GGFDNN
                        grlist[prod]['Boost_UntaggedDNN_CAT']=gr_Boost_UntaggedDNN
                        grlist[prod]['Boost_VBFDNN_CAT']=gr_Boost_VBFDNN
                        grlist[prod]['Boost_NONVBFDNN_CAT']=gr_Boost_NONVBFDNN
                if 'Resol' in bst:

                        grlist[prod]['Resol_GGFDNN_CAT']=gr_Resol_GGFDNN
                        grlist[prod]['Resol_UntaggedDNN_CAT']=gr_Resol_UntaggedDNN
                        grlist[prod]['Resol_VBFDNN_CAT']=gr_Resol_VBFDNN
                        grlist[prod]['Resol_NONVBFDNN_CAT']=gr_Resol_NONVBFDNN

                for gr in grlist[prod]:
                        if prod=='ggf':
                                grlist[prod][gr]['gr'].SetLineColor(4)
                        if prod=='vbf':
                                grlist[prod][gr]['gr'].SetLineColor(2)
        return grlist

def GetMassVsPurityTGr(bst,Year,min_mass=200):
        #prod
        prodlist=['ggf','vbf']

        grlist={}

        for prod in prodlist:
                grlist[prod]={}#GetVBFEffOfCat
                #gr_total={'title':'Total '+prod+' sig'}
                #gr_total['xlist'], gr_total['ylist']=GetTotalEff(prod,Year)
                #gr_total['gr']=TGraph_Maker(gr_total['xlist'], gr_total['ylist'])
                

                ##---
                if 'Boost' in bst:
                        gr_Boost_GGF={'title':prod+' purity in Boost GGF Cat.'}
                        gr_Boost_GGF['xlist'], gr_Boost_GGF['ylist']=GetVBFPurityOfCat(prod,False,bst,Year)
                        gr_Boost_GGF['gr']=TGraph_Maker(gr_Boost_GGF['xlist'], gr_Boost_GGF['ylist'])
                        
                        gr_Boost_VBF={'title':prod+' purity in Boost VBF Cat.'}
                        gr_Boost_VBF['xlist'], gr_Boost_VBF['ylist']=GetVBFPurityOfCat(prod,False,bst,Year)
                        gr_Boost_VBF['gr']=TGraph_Maker(gr_Boost_VBF['xlist'], gr_Boost_VBF['ylist'])

                        gr_Boost_GGFDNN={'title':prod+' purity in Boost GGFDNN Cat.'}
                        gr_Boost_GGFDNN['xlist'], gr_Boost_GGFDNN['ylist']=GetVBFPurityOfCat(prod,True,bst,Year)
                        gr_Boost_GGFDNN['gr']=TGraph_Maker(gr_Boost_GGFDNN['xlist'], gr_Boost_GGFDNN['ylist'])
                        
                        gr_Boost_VBFDNN={'title':prod+' purity in Boost VBFDNN Cat.'}
                        gr_Boost_VBFDNN['xlist'], gr_Boost_VBFDNN['ylist']=GetVBFPurityOfCat(prod,True,bst,Year)
                        gr_Boost_VBFDNN['gr']=TGraph_Maker(gr_Boost_VBFDNN['xlist'], gr_Boost_VBFDNN['ylist'])


                if 'Resol' in bst:
                        gr_Resol_GGF={'title':prod+' purity in Resol GGF Cat.'}
                        gr_Resol_GGF['xlist'], gr_Resol_GGF['ylist']=GetVBFPurityOfCat(prod,False,bst,Year)
                        gr_Resol_GGF['gr']=TGraph_Maker(gr_Resol_GGF['xlist'], gr_Resol_GGF['ylist'])
                        
                        gr_Resol_VBF={'title':prod+' purity in Resol VBF Cat.'}
                        gr_Resol_VBF['xlist'], gr_Resol_VBF['ylist']=GetVBFPurityOfCat(prod,False,bst,Year)
                        gr_Resol_VBF['gr']=TGraph_Maker(gr_Resol_VBF['xlist'], gr_Resol_VBF['ylist'])

                        gr_Resol_GGFDNN={'title':prod+' purity in Resol GGFDNN Cat.'}
                        gr_Resol_GGFDNN['xlist'], gr_Resol_GGFDNN['ylist']=GetVBFPurityOfCat(prod,True,bst,Year)
                        gr_Resol_GGFDNN['gr']=TGraph_Maker(gr_Resol_GGFDNN['xlist'], gr_Resol_GGFDNN['ylist'])
                        
                        gr_Resol_VBFDNN={'title':prod+' purity in Resol VBFDNN Cat.'}
                        gr_Resol_VBFDNN['xlist'], gr_Resol_VBFDNN['ylist']=GetVBFPurityOfCat(prod,True,bst,Year)
                        gr_Resol_VBFDNN['gr']=TGraph_Maker(gr_Resol_VBFDNN['xlist'], gr_Resol_VBFDNN['ylist'])

                if 'Boost' in bst:

                        grlist[prod]['Boost_GGF_CAT']=gr_Boost_GGF
                        grlist[prod]['Boost_VBF_CAT']=gr_Boost_VBF

                        grlist[prod]['Boost_GGFDNN_CAT']=gr_Boost_GGFDNN
                        grlist[prod]['Boost_VBFDNN_CAT']=gr_Boost_VBFDNN
                if 'Resol' in bst:
                        grlist[prod]['Resol_GGF_CAT']=gr_Resol_GGF
                        grlist[prod]['Resol_VBF_CAT']=gr_Resol_VBF
                        grlist[prod]['Resol_GGFDNN_CAT']=gr_Resol_GGFDNN
                        grlist[prod]['Resol_VBFDNN_CAT']=gr_Resol_VBFDNN

                for gr in grlist[prod]:
                        if prod=='ggf':
                                grlist[prod][gr]['gr'].SetLineColor(4)
                        if prod=='vbf':
                                grlist[prod][gr]['gr'].SetLineColor(2)
        return grlist


def DrawMassVsVBFPurity(bst,Year,min_mass=200):
        grdict=GetMassVsPurityTGr(bst,Year)
        gr_list=[grdict['vbf'][bst+'_VBF_CAT'],
                 grdict['ggf'][bst+'_VBF_CAT'],
                 grdict['vbf'][bst+'_VBFDNN_CAT'],
                 grdict['ggf'][bst+'_VBFDNN_CAT'],

        ]
        xmin=5000.
        xmax=-1
        ymin=5000.
        ymax=-1
        for gr in gr_list:
                title=gr['title']
                xlist=gr['xlist']
                ylist=gr['ylist']
                if min(xlist)<xmin : xmin=min(xlist)
                if max(xlist)>xmax : xmax=max(xlist)
                if min(ylist)<ymin : ymin=min(ylist)
                if max(ylist)>ymax : ymax=max(ylist)
                
                #if 'total' in title:
                #        gr['gr'].SetLineColor(1)
                #        gr['gr'].SetLineWidth(3)
                #if 'Boost' in title:
                #        gr['gr'].SetLineStyle(1)
                #if 'Resol' in title:
                #        gr['gr'].SetLineStyle(2)
                #if 'GGF' in title:
                #        gr['gr'].SetLineColor(2)
                #if 'Untagged' in title:
                #        gr['gr'].SetLineColor(4)
                #if 'VBF' in title:
                #        gr['gr'].SetLineColor(3)
                if 'ggf sig' in title:
                        gr['gr'].SetLineColor(4)
                if 'vbf sig' in title:
                        gr['gr'].SetLineColor(2)
                if 'DNN' in title:
                        gr['gr'].SetLineStyle(2)
        ##--Draw
        c=ROOT.TCanvas()
        xlabel='M(X) [GeV]'
        ylabel='Purity'
        firstgr=gr_list[0]['gr']
        #print 'ymin',ymin
        #print 'ymax',ymax
        frametitle=' Purity'
        frame = ROOT.TH2F("frame",frametitle,firstgr.GetN(),xmin,xmax,100,ymin*0.9,ymax*1.4)
        frame.SetStats(0)
        frame.SetYTitle(ylabel)
        frame.GetYaxis().SetTitleSize(0.05)
        frame.GetYaxis().SetLabelSize(0.03)
        frame.SetXTitle(xlabel)
        frame.GetXaxis().SetTitleSize(0.035)
        frame.GetXaxis().SetLabelSize(0.03)
        frame.GetXaxis().SetTitleOffset(1.5)
        frame.Draw()

        for gr in gr_list:
                #mygr.Draw()
                gr['gr'].Draw('l same')

        ##--legend
        leg= ROOT.TLegend(0.5,0.75,0.95,0.94)
        leg.SetFillColor(0)
        leg.SetBorderSize(1)
        leg.SetTextFont(8)
        leg.SetTextSize(20)
        #for idx in range(0,Ngr):
        for gr in gr_list:
                #graph_list[idx].Draw("l same")
                leg.AddEntry(gr['gr'], gr['title'],"l")
        leg.Draw('sames')
        c.SaveAs(bst+'_purity_'+Year+'.pdf')



def DrawMassVsVBFEff(bst,Year,min_mass=200):
        grdict=GetMassVsEffTGr(bst,Year)
        gr_list=[grdict['vbf'][bst+'_VBF_CAT'],
                 grdict['ggf'][bst+'_VBF_CAT'],
                 grdict['vbf'][bst+'_VBFDNN_CAT'],
                 grdict['ggf'][bst+'_VBFDNN_CAT'],

        ]
        xmin=5000.
        xmax=-1
        ymin=5000.
        ymax=-1
        for gr in gr_list:
                title=gr['title']
                xlist=gr['xlist']
                ylist=gr['ylist']
                if min(xlist)<xmin : xmin=min(xlist)
                if max(xlist)>xmax : xmax=max(xlist)
                if min(ylist)<ymin : ymin=min(ylist)
                if max(ylist)>ymax : ymax=max(ylist)
                
                #if 'total' in title:
                #        gr['gr'].SetLineColor(1)
                #        gr['gr'].SetLineWidth(3)
                #if 'Boost' in title:
                #        gr['gr'].SetLineStyle(1)
                #if 'Resol' in title:
                #        gr['gr'].SetLineStyle(2)
                #if 'GGF' in title:
                #        gr['gr'].SetLineColor(2)
                #if 'Untagged' in title:
                #        gr['gr'].SetLineColor(4)
                #if 'VBF' in title:
                #        gr['gr'].SetLineColor(3)
                if 'ggf sig' in title:
                        gr['gr'].SetLineColor(4)
                if 'vbf sig' in title:
                        gr['gr'].SetLineColor(2)
                if 'DNN' in title:
                        gr['gr'].SetLineStyle(2)
        ##--Draw
        c=ROOT.TCanvas()
        xlabel='M(X) [GeV]'
        ylabel='Eff.'
        firstgr=gr_list[0]['gr']
        #print 'ymin',ymin
        #print 'ymax',ymax
        frametitle=' Eff.'
        frame = ROOT.TH2F("frame",frametitle,firstgr.GetN(),xmin,xmax,100,ymin*0.9,ymax*1.4)
        frame.SetStats(0)
        frame.SetYTitle(ylabel)
        frame.GetYaxis().SetTitleSize(0.05)
        frame.GetYaxis().SetLabelSize(0.03)
        frame.SetXTitle(xlabel)
        frame.GetXaxis().SetTitleSize(0.035)
        frame.GetXaxis().SetLabelSize(0.03)
        frame.GetXaxis().SetTitleOffset(1.5)
        frame.Draw()

        for gr in gr_list:
                #mygr.Draw()
                gr['gr'].Draw('l same')

        ##--legend
        leg= ROOT.TLegend(0.5,0.75,0.95,0.94)
        leg.SetFillColor(0)
        leg.SetBorderSize(1)
        leg.SetTextFont(8)
        leg.SetTextSize(20)
        #for idx in range(0,Ngr):
        for gr in gr_list:
                #graph_list[idx].Draw("l same")
                leg.AddEntry(gr['gr'], gr['title'],"l")
        leg.Draw('sames')
        c.SaveAs(bst+'_'+Year+'.pdf')

def DrawMassVsEff(prod,Year,min_mass=200):
        #ggH_hww5000_c10brn00



        #masslist=GetMassPoints(Year)
        #xlist=[]
        #ylist=[]

        gr_total={'title':'Total'}
        gr_total['xlist'], gr_total['ylist']=GetTotalEff(prod,Year)
        gr_total['gr']=TGraph_Maker(gr_total['xlist'], gr_total['ylist'])


        ##---
        gr_Boost_GGF={'title':'Boost GGF'}
        gr_Boost_GGF['xlist'], gr_Boost_GGF['ylist']=GetEffOfCat(prod,'Boost GGF',Year)
        gr_Boost_GGF['gr']=TGraph_Maker(gr_Boost_GGF['xlist'], gr_Boost_GGF['ylist'])

        gr_Boost_Untagged={'title':'Boost Untagged'}
        gr_Boost_Untagged['xlist'], gr_Boost_Untagged['ylist']=GetEffOfCat(prod,'Boost Untagged',Year)
        gr_Boost_Untagged['gr']=TGraph_Maker(gr_Boost_Untagged['xlist'], gr_Boost_Untagged['ylist'])

        gr_Boost_VBF={'title':'Boost VBF'}
        gr_Boost_VBF['xlist'], gr_Boost_VBF['ylist']=GetEffOfCat(prod,'Boost VBF',Year)
        gr_Boost_VBF['gr']=TGraph_Maker(gr_Boost_VBF['xlist'], gr_Boost_VBF['ylist'])

        gr_Resol_GGF={'title':'Resol GGF'}
        gr_Resol_GGF['xlist'], gr_Resol_GGF['ylist']=GetEffOfCat(prod,'Resol GGF',Year)
        gr_Resol_GGF['gr']=TGraph_Maker(gr_Resol_GGF['xlist'], gr_Resol_GGF['ylist'])

        gr_Resol_Untagged={'title':'Resol Untagged'}
        gr_Resol_Untagged['xlist'], gr_Resol_Untagged['ylist']=GetEffOfCat(prod,'Resol Untagged',Year)
        gr_Resol_Untagged['gr']=TGraph_Maker(gr_Resol_Untagged['xlist'], gr_Resol_Untagged['ylist'])

        gr_Resol_VBF={'title':'Resol VBF'}
        gr_Resol_VBF['xlist'], gr_Resol_VBF['ylist']=GetEffOfCat(prod,'Resol VBF',Year)
        gr_Resol_VBF['gr']=TGraph_Maker(gr_Resol_VBF['xlist'], gr_Resol_VBF['ylist'])
        

        #---
        gr_Boost={'title':'Boosted Cat.'}
        gr_Boost['xlist']=gr_Boost_GGF['xlist'] 
        gr_Boost['ylist']=[]
        for idx in range(len(gr_Boost['xlist'])):
                eff_com=gr_Boost_GGF['ylist'][idx]+gr_Boost_Untagged['ylist'][idx]+gr_Boost_VBF['ylist'][idx]
                gr_Boost['ylist'].append(eff_com)
        gr_Boost['gr']=TGraph_Maker(gr_Boost['xlist'], gr_Boost['ylist'])
        gr_Boost['gr'].SetLineColor(2)

        gr_Resol={'title':'Resolved Cat.'}
        gr_Resol['xlist']=gr_Resol_GGF['xlist'] 
        gr_Resol['ylist']=[]
        for idx in range(len(gr_Resol['xlist'])):
                eff_com=gr_Resol_GGF['ylist'][idx]+gr_Resol_Untagged['ylist'][idx]+gr_Resol_VBF['ylist'][idx]
                gr_Resol['ylist'].append(eff_com)
        gr_Resol['gr']=TGraph_Maker(gr_Resol['xlist'], gr_Resol['ylist'])
        gr_Resol['gr'].SetLineColor(4)
        #gr_list=[gr_total,gr_Boost_GGF,gr_Boost_Untagged,gr_Boost_VBF,gr_Resol_GGF,gr_Resol_Untagged,gr_Resol_VBF]
        #gr_list=[gr_total,gr_Boost_GGF,gr_Boost_Untagged,gr_Boost_VBF,gr_Resol_GGF,gr_Resol_Untagged,gr_Resol_VBF]
        gr_list=[gr_total,gr_Boost,gr_Resol]
        ##---SetStyle

        xmin=5000.
        xmax=-1
        ymin=5000.
        ymax=-1
        for gr in gr_list:
                title=gr['title']
                xlist=gr['xlist']
                ylist=gr['ylist']
                if min(xlist)<xmin : xmin=min(xlist)
                if max(xlist)>xmax : xmax=max(xlist)
                if min(ylist)<ymin : ymin=min(ylist)
                if max(ylist)>ymax : ymax=max(ylist)
                if 'total' in title:
                        gr['gr'].SetLineColor(1)
                        gr['gr'].SetLineWidth(3)
                if 'Boost' in title:
                        gr['gr'].SetLineStyle(1)
                if 'Resol' in title:
                        gr['gr'].SetLineStyle(2)
                if 'GGF' in title:
                        gr['gr'].SetLineColor(2)
                if 'Untagged' in title:
                        gr['gr'].SetLineColor(4)
                if 'VBF' in title:
                        gr['gr'].SetLineColor(3)


        
        #mygr=TGraph_Maker(xlist,ylist)
        ##--Draw
        c=ROOT.TCanvas()
        xlabel='M(X) [GeV]'
        ylabel='Eff.*Acc.'
        firstgr=gr_list[0]['gr']
        #print 'ymin',ymin
        #print 'ymax',ymax
        frametitle='['+prod+'] Eff. X Acc.'
        frame = ROOT.TH2F("frame",frametitle,firstgr.GetN(),xmin,xmax,100,ymin*0.9,ymax*1.4)
        frame.SetStats(0)
        frame.SetYTitle(ylabel)
        frame.GetYaxis().SetTitleSize(0.05)
        frame.GetYaxis().SetLabelSize(0.03)
        frame.SetXTitle(xlabel)
        frame.GetXaxis().SetTitleSize(0.035)
        frame.GetXaxis().SetLabelSize(0.03)
        frame.GetXaxis().SetTitleOffset(1.5)
        frame.Draw()

        for gr in gr_list:
                #mygr.Draw()
                gr['gr'].Draw('l same')

        ##--legend
        leg= ROOT.TLegend(0.5,0.75,0.95,0.94)
        leg.SetFillColor(0)
        leg.SetBorderSize(1)
        leg.SetTextFont(8)
        leg.SetTextSize(20)
        #for idx in range(0,Ngr):
        for gr in gr_list:
                #graph_list[idx].Draw("l same")
                leg.AddEntry(gr['gr'], gr['title'],"l")
        leg.Draw('sames')



        c.SaveAs(prod+'_'+Year+'.pdf')


if __name__ == '__main__':

        ##--
        ##GetMassPoints(Year)
        
        #TGraph_Maker(xlist,ylist)
        #ggH_hww5000_c10brn00
        prodlist=['ggf','vbf']
        yearlist=['2016','2017','2018']
        #yearlist=['2016']
        #DrawMassVsEff('vbf','2016')
        #def DrawMassVsVBFEff(bst,Year,min_mass=200):

        for prod in prodlist:
                #continue
                for year in yearlist:
                        #DrawMassVsEff('ggf','2016')
                        #DrawMassVsEff(prod,year)
                        DrawMassVsVBFPurity('Boost',year)
                        DrawMassVsVBFPurity('Resol',year)
