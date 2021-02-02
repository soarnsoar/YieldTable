import ROOT
import sys
#sys.path.insert(0,'../python/')
#from Utils import *
#def ReadYield(inputpath,processlist):
def ReadYield(inputpath,processlist):
        ##---Read Total integrals
        myrf=ROOT.TFile.Open(inputpath)

        dict_yield={}

        ##--for each process
        for process in processlist:
                histopath=process
                #print histopath
                myhisto=myrf.Get(histopath)
                dict_yield[process]=myhisto.Integral()

        myrf.Close()
        return dict_yield


def GetConf():

	##../../2016/rootFile_2016_cms_scratch_jhchoi_Statonly_noTreeBase_NoMEKD_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root
        #rootFile_2016__cms_scratch_jhchoi_WW_mass_finebinning_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR
        #rootFile_2016__cms_scratch_jhchoi_WW_mass_finebinning_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR

	configuration={
                '2016':{
                        'inputlist':{
                                '__BoostedGGF_SR_NoMEKDCut':'../../2016/rootFile_2016__cms_scratch_jhchoi_WW_mass_finebinning_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root',
                                '__BoostedVBF_SR_NoMEKDCut':'../../2016/rootFile_2016__cms_scratch_jhchoi_WW_mass_finebinning_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root',
                                '___ResolvedGGF__SR_NoMEKDCut':'../../2016/rootFile_2016__cms_scratch_jhchoi_WW_mass_finebinning_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root',
                                '___ResolvedVBF__SR_NoMEKDCut':'../../2016/rootFile_2016__cms_scratch_jhchoi_WW_mass_finebinning_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root'
                        },
                        'inputxsec':1.,
                        'inputlumi':35.9,
                },
                '2017':{
                        'inputlist':{
                                '__BoostedGGF_SR_NoMEKDCut':'../../2017/rootFile_2017__cms_scratch_jhchoi_WW_mass_finebinning_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root',
                                '__BoostedVBF_SR_NoMEKDCut':'../../2017/rootFile_2017__cms_scratch_jhchoi_WW_mass_finebinning_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root',
                                '___ResolvedGGF__SR_NoMEKDCut':'../../2017/rootFile_2017__cms_scratch_jhchoi_WW_mass_finebinning_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root',
                                '___ResolvedVBF__SR_NoMEKDCut':'../../2017/rootFile_2017__cms_scratch_jhchoi_WW_mass_finebinning_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root'
                        },
                        'inputxsec':1.,
                        'inputlumi':41.5,
                },
                '2018':{
                        'inputlist':{
                                '__BoostedGGF_SR_NoMEKDCut':'../../2018/rootFile_2018__cms_scratch_jhchoi_WW_mass_finebinning_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root',
                                '__BoostedGGF_SR_NoMEKDCut':'../../2018/rootFile_2018__cms_scratch_jhchoi_WW_mass_finebinning_Boosted_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root',
                                '___ResolvedVBF__SR_NoMEKDCut':'../../2018/rootFile_2018__cms_scratch_jhchoi_WW_mass_finebinning_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root',
                                '___ResolvedVBF__SR_NoMEKDCut':'../../2018/rootFile_2018__cms_scratch_jhchoi_WW_mass_finebinning_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_SR/hadd.root'
                        },
                        'inputxsec':1.,
                        'inputlumi':59.7,
                }
        }

        return configuration
if __name__ == '__main__':
        ###---
        configuration=GetConf()
        #ReadYield(inputpath,processlist)
        Year='2016'
        proc='ggH_hww1000_c10brn00'

        print Year,proc
        #print configuration[Year]['inputlist']
        my_yield=0.
        for cutname in configuration[Year]['inputlist']:
                inputpath=configuration[Year]['inputlist'][cutname]
                #__BoostedALL_SR_NoMEKDCut
                #___ResolvedALL__SR_NoMEKDCut
                histopath=cutname+'/Event/histo_'+proc
                #print cutname
                #print histopath
                this_yield=ReadYield(inputpath,[histopath])
                my_yield+=this_yield[histopath]


        total_prod=configuration[Year]['inputxsec']*configuration[Year]['inputlumi']*1000.
        
        eff=my_yield/total_prod
        print 'eff=',eff
        

