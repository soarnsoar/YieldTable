import ROOT
import sys
from TGraphHelper import *
#sys.path.insert(0,'../python/')
#from Utils import *
#def ReadYield(inputpath,processlist):
def ReadYield(inputpath,processlist):
        ##---Read Total integrals
        myrf=ROOT.TFile.Open(inputpath)
        print inputpath
        dict_yield={}

        ##--for each process
        for process in processlist:
                histopath=process
                print histopath
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
                                        'inputfile':'../../2016/rootFile_2016__cms_scratch_jhchoi_Final2101010_0.01MEKD_REGROUP_Boosted_HMFull_V12_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root'
                                },
                                'Boost Untagged':{
                                        'cut':'__BoostedGGF_SR_UNTAGGED_M1500_C0.01',
                                        'inputfile':'../../2016/rootFile_2016__cms_scratch_jhchoi_Final2101010_0.01MEKD_REGROUP_Boosted_HMFull_V12_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root',
                                },
                                'Boost VBF':{
                                        'cut':'__BoostedVBF_SR_NoMEKDCut',
                                        'inputfile':'../../2016/rootFile_2016__cms_scratch_jhchoi_Final2101010_0.01MEKD_REGROUP_Boosted_HMFull_V12_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root',
                                },
                                'Resol GGF':{
                                        'cut':'___ResolvedGGF__SR_MEKDTAG_M400_C0.01',
                                        'inputfile':'../../2016/rootFile_2016__cms_scratch_jhchoi_Final2101010_0.01MEKD_REGROUP_Resolved_HMFull_V12_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root',
                                },
                                'Resol Untagged':{
                                        'cut':'___ResolvedGGF__SR_UNTAGGED_M400_C0.01',
                                        'inputfile':'../../2016/rootFile_2016__cms_scratch_jhchoi_Final2101010_0.01MEKD_REGROUP_Resolved_HMFull_V12_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root'
                                },
                                'Resol VBF':{
                                        'cut':'___ResolvedVBF__SR_NoMEKDCut',
                                        'inputfile':'../../2016/rootFile_2016__cms_scratch_jhchoi_Final2101010_0.01MEKD_REGROUP_Resolved_HMFull_V12_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root'
                                },
                        },
                        'inputxsec':1.,
                        'inputlumi':35.9,
                },
                '2017':{
                        'inputlist':{
                                'Boost GGF':{
                                        'cut':'__BoostedGGF_SR_MEKDTAG_M1500_C0.01',
                                        'inputfile':'../../2017/rootFile_2017__cms_scratch_jhchoi_Final2101010_0.01MEKD_REGROUP_Boosted_HMFull_V12_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root'
                                },
                                'Boost Untagged':{
                                        'cut':'__BoostedGGF_SR_UNTAGGED_M1500_C0.01',
                                        'inputfile':'../../2017/rootFile_2017__cms_scratch_jhchoi_Final2101010_0.01MEKD_REGROUP_Boosted_HMFull_V12_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root',
                                },
                                'Boost VBF':{
                                        'cut':'__BoostedVBF_SR_NoMEKDCut',
                                        'inputfile':'../../2017/rootFile_2017__cms_scratch_jhchoi_Final2101010_0.01MEKD_REGROUP_Boosted_HMFull_V12_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root',
                                },
                                'Resol GGF':{
                                        'cut':'___ResolvedGGF__SR_MEKDTAG_M400_C0.01',
                                        'inputfile':'../../2017/rootFile_2017__cms_scratch_jhchoi_Final2101010_0.01MEKD_REGROUP_Resolved_HMFull_V12_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root',
                                },
                                'Resol Untagged':{
                                        'cut':'___ResolvedGGF__SR_UNTAGGED_M400_C0.01',
                                        'inputfile':'../../2017/rootFile_2017__cms_scratch_jhchoi_Final2101010_0.01MEKD_REGROUP_Resolved_HMFull_V12_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root'
                                },
                                'Resol VBF':{
                                        'cut':'___ResolvedVBF__SR_NoMEKDCut',
                                        'inputfile':'../../2017/rootFile_2017__cms_scratch_jhchoi_Final2101010_0.01MEKD_REGROUP_Resolved_HMFull_V12_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root'
                                },
                        },

                        'inputxsec':1.,
                        'inputlumi':41.5,
                },
                '2018':{
                        'inputlist':{
                                'Boost GGF':{
                                        'cut':'__BoostedGGF_SR_MEKDTAG_M1500_C0.01',
                                        'inputfile':'../../2018/rootFile_2018__cms_scratch_jhchoi_Final2101010_0.01MEKD_REGROUP_Boosted_HMFull_V12_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root'
                                },
                                'Boost Untagged':{
                                        'cut':'__BoostedGGF_SR_UNTAGGED_M1500_C0.01',
                                        'inputfile':'../../2018/rootFile_2018__cms_scratch_jhchoi_Final2101010_0.01MEKD_REGROUP_Boosted_HMFull_V12_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root',
                                },
                                'Boost VBF':{
                                        'cut':'__BoostedVBF_SR_NoMEKDCut',
                                        'inputfile':'../../2018/rootFile_2018__cms_scratch_jhchoi_Final2101010_0.01MEKD_REGROUP_Boosted_HMFull_V12_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root',
                                },
                                'Resol GGF':{
                                        'cut':'___ResolvedGGF__SR_MEKDTAG_M400_C0.01',
                                        'inputfile':'../../2018/rootFile_2018__cms_scratch_jhchoi_Final2101010_0.01MEKD_REGROUP_Resolved_HMFull_V12_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root',
                                },
                                'Resol Untagged':{
                                        'cut':'___ResolvedGGF__SR_UNTAGGED_M400_C0.01',
                                        'inputfile':'../../2018/rootFile_2018__cms_scratch_jhchoi_Final2101010_0.01MEKD_REGROUP_Resolved_HMFull_V12_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root'
                                },
                                'Resol VBF':{
                                        'cut':'___ResolvedVBF__SR_NoMEKDCut',
                                        'inputfile':'../../2018/rootFile_2018__cms_scratch_jhchoi_Final2101010_0.01MEKD_REGROUP_Resolved_HMFull_V12_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root'
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
        #ReadYield(inputpath,processlist)
        #Year='2016'
        #proc='ggH_hww5000_c10brn00'
        prod=''
        if 'ggH' in proc:prod='ggf'
        if 'qqH' in proc:prod='vbf'
        #print Year,proc
        #print configuration[Year]['inputlist']
        my_yield=0.
        my_yield_list=[]

        total_prod=configuration[Year]['inputxsec']*configuration[Year]['inputlumi']*1000.
        for rg in configuration[Year]['inputlist']:
                inputpath=configuration[Year]['inputlist'][rg]['inputfile']
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
        #DrawMassVsEff('vbf','2016')
        for prod in prodlist:
                #continue
                for year in yearlist:
                        #DrawMassVsEff('ggf','2016')
                        DrawMassVsEff(prod,year)
