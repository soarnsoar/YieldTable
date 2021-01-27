def Vaidation(nuilist,nuidict):
    listfromdict=[]
    for group in nuidict:
        listfromdict+=nuidict[group]['list']
    
    print 'len(listfromdict)=',len(listfromdict)
    print 'len(nuilist)=',len(nuilist)
    for nui in nuilist:
        if not nui in listfromdict:
            print '!!Missing->',nui
    for nui in listfromdict:
        if not nui in nuilist:
            print '!!Wrong->',nui
        
        
    if len(set(listfromdict))!=len(listfromdict):
           print "Double Counting!@!!"


list2018=['CMS_btag_lfstats2_2018', 'CMS_ak8jet_jesBBEC1', 'CMS_ak8jet_jesAbsolute', 'mjjshape_2018', 'CMS_ak4jet_jesRelativeBal', 'CMS_ak4jet_jesEC2_2018', 'lumi_13TeV_LSCale', 'CMS_ak8jet_jesEC2_2018', 'pdf_gg_ACCEPT', 'CMS_btag_hfstats2_2018', 'CMS_HEM1516_2018', 'CMS_ak4jet_jesAbsolute_2018', 'CMS_ak4jet_jer_2018', 'CMS_ak4jet_jesFlavorQCD', 'UEPS_FSR', 'QCDscale_Higgs_gg', 'CMS_ak8jet_jesEC2', 'pdf_Higgs_gg', 'CMS_ak4jet_jesRelativeSample_2018', 'CMS_ak4jet_jesHF', 'CMS_ak8jet_jesHF', 'QCDscale_Higgs_qqbar', 'lumi_13TeV_XYFact', 'CMS_eff_e_2018', 'lumi_13TeV_CurrCalib', 'CMS_eff_hww_sngele_trigger_2018', 'UEPS_ISR', 'CMS_ak8jet_jesFlavorQCD', 'CMS_ak8jet_jesHF_2018', 'CMS_ak8jet_jesAbsolute_2018', 'CMS_ak4jet_jesAbsolute', 'CMS_btag_hfstats1_2018', 'CMS_ak8jet_jesRelativeBal', 'CMS_eff_m_2018', 'QCDscale_qq_ACCEPT', 'CMS_PU_2018', 'CMS_eff_Wtag_2018', 'pdf_qq_ACCEPT', 'CMS_btag_lf', 'lumi_13TeV_2018', 'pdf_Higgs_qqbar', 'CMS_ak4jet_jesEC2', 'MultiVnorm2018', 'CMS_ak4jet_jesHF_2018', 'pdf_ttbar_ACCEPT', 'dynorm2018', 'CMS_btag_lfstats1_2018', 'CMS_ak4jet_jesBBEC1', 'CMS_ak8jet_jer_2018', 'CMS_ak4jet_jesBBEC1_2018', 'QCDscale_ttbar_ACCEPT', 'ggWWnorm', 'CMS_scale_met_2018', 'CMS_btag_cferr1', 'CMS_btag_cferr2', 'CMS_scale_muon_2018', 'CMS_ak8jet_jesBBEC1_2018', 'CMS_btag_hf', 'CMS_ak8jet_jms_2018', 'CMS_eff_hww_sngmu_trigger_2018', 'QCDscale_gg_ACCEPT', 'CMS_ak8jet_jesRelativeSample_2018', 'CMS_ak8jet_jmr_2018', 'CMS_scale_electron_2018']


print len(list2018)

NuisanceCategory2018={
    'lumionisty':{
        'alias':'Luminosity', 
        'type':'norm',
        'list':['lumi_13TeV_LSCale', 'lumi_13TeV_XYFact', 'lumi_13TeV_CurrCalib', 'lumi_13TeV_2018']
    },
    'ak4jet_jes_jer':{
        'alias':'AK4Jet JES/JER', 
        'list':['CMS_ak4jet_jesEC2_2018', 'CMS_ak4jet_jesRelativeBal', 'CMS_ak4jet_jer_2018', 'CMS_ak4jet_jesAbsolute_2018', 'CMS_ak4jet_jesFlavorQCD', 'CMS_ak4jet_jesHF', 'CMS_ak4jet_jesRelativeSample_2018', 'CMS_ak4jet_jesAbsolute', 'CMS_ak4jet_jesHF_2018', 'CMS_ak4jet_jesEC2', 'CMS_ak4jet_jesBBEC1_2018', 'CMS_ak4jet_jesBBEC1']
    },
    'ak8jet_jes_jer':{
        'alias':'AK8Jet JES/JER', 
        'list':['CMS_ak8jet_jesBBEC1', 'CMS_ak8jet_jesHF_2018', 'CMS_ak8jet_jesAbsolute', 'CMS_ak8jet_jesEC2_2018', 'CMS_ak8jet_jesEC2', 'CMS_ak8jet_jesHF', 'CMS_ak8jet_jesFlavorQCD', 'CMS_ak8jet_jesAbsolute_2018', 'CMS_ak8jet_jesRelativeBal', 'CMS_ak8jet_jer_2018', 'CMS_ak8jet_jesRelativeSample_2018', 'CMS_ak8jet_jesBBEC1_2018']

    },
    'wtag_jms_jmr':{
        'alias':'WtagAK8Jet JMSJMR',
        'list':['CMS_ak8jet_jms_2018', 'CMS_ak8jet_jmr_2018']
    },
    'Wtag_eff':{
        'alias':'WtagAK8Jet Eff.',
        'list':['CMS_eff_Wtag_2018']
    },
    'mjjshape':{
        'alias':'AK4Jet MjjShape',
        'list':['mjjshape_2018'],
        },
    'btag':{
        'alias':'B-tagging',
        'list':['CMS_btag_lf', 'CMS_btag_hfstats2_2018', 'CMS_btag_lfstats2_2018', 'CMS_btag_hfstats1_2018', 'CMS_btag_lfstats1_2018', 'CMS_btag_cferr1', 'CMS_btag_cferr2', 'CMS_btag_hf']
    },
    'MET':{
        'alias':'Missing Energy',
        'list':['CMS_scale_met_2018']
    },
    'pdf_accept':{
        'alias':'PDF Acceptance',
        'list':['pdf_gg_ACCEPT', 'pdf_qq_ACCEPT', 'pdf_ttbar_ACCEPT']
    },
    'qcdscale_accept':{
        'alias':'QCD scale Acceptance',
        'list':['QCDscale_qq_ACCEPT', 'QCDscale_ttbar_ACCEPT', 'QCDscale_gg_ACCEPT'],
        },
    'xsec_pdf':{
        'alias':'PDF Signal Norm.',
        'type':'norm',
        'list':['pdf_Higgs_qqbar', 'pdf_Higgs_gg']
    },
    'xsec_qcdscale':{
        'alias':'QCD scale Norm.',
        'type':'norm',
        'list':['QCDscale_Higgs_gg', 'QCDscale_Higgs_qqbar'],
    },
    'PS':{
        'alias':'Parton Shower Model',
        'list':['UEPS_FSR', 'UEPS_ISR']
    },
    'bkgnorm':{
        'alias':'Background Norm.',
        'type':'norm',
        'list':['ggWWnorm', 'MultiVnorm2018', 'dynorm2018'],
    },
    'ElectronTrigger':{
        'alias':'ElectronTrigger Effieicny',
        'list':['CMS_eff_hww_sngele_trigger_2018'],
    },
    'MuonTrigger':{
        'alias':'MuonTrigger Effieicny',
        'list':['CMS_eff_hww_sngmu_trigger_2018']
    },
    'ElectronID':{
        'alias':'Electron Identification',
        'list':['CMS_eff_e_2018'],
        },
    'MuonID':{
        'alias':'Muon Identification',
        'list':['CMS_eff_m_2018'],
    },
    'ElectronEnergyScale':{
        'alias':'Electron Energy Scale',
        'list':['CMS_scale_electron_2018']
    },
    'MuonEnergyScale':{
        'alias':'Muon Momentum Scale',
        'list':['CMS_scale_muon_2018']
    },
    'pu':{
        'alias':'PileUp',
        'list':['CMS_PU_2018']
    },
    'HEM1516':{
        'alias':'HEM15/16',
        'list':['CMS_HEM1516_2018']
    }
}

Vaidation(list2018,NuisanceCategory2018)
#print [NuisanceCategory2018[nui]['alias'] for nui in NuisanceCategory2018]
print [nui for nui in NuisanceCategory2018]
