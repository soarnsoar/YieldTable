def Vaidation(nuilist,nuidict):
    listfromdict=[]
    for group in nuidict:
        listfromdict+=nuidict[group]['list']
    
    print 'len(listfromdict)=',len(listfromdict)
    print 'len(nuilist)=',len(nuilist)
    for nui in nuilist:
        if not nui in listfromdict:
            print '!!Missing->',nui

        
        
    if len(set(listfromdict))!=len(listfromdict):
           print "Double Counting!@!!"


list2016=['CMS_ak4jet_jesEC2_2016', 'QCDscale_qq_ACCEPT', 'CMS_ak8jet_jesBBEC1', 'CMS_ak8jet_jesHF_2016', 'CMS_ak8jet_jesAbsolute', 'CMS_ak4jet_jesRelativeBal', 'QCDscale_ttbar_ACCEPT', 'pdf_gg_ACCEPT', 'CMS_ak4jet_jer_2016', 'ggWWnorm', 'CMS_ak4jet_jesAbsolute_2016', 'lumi_13TeV_Ghosts', 'CMS_btag_lf', 'mjjshape_2016', 'CMS_btag_hfstats2_2016', 'CMS_ak8jet_jesFlavorQCD', 'CMS_ak8jet_jesEC2_2016', 'UEPS_FSR', 'QCDscale_Higgs_gg', 'CMS_ak8jet_jesEC2', 'CMS_ak4jet_jesHF', 'CMS_ak4jet_jesFlavorQCD', 'CMS_ak8jet_jesHF', 'CMS_eff_e_2016', 'CMS_scale_electron_2016', 'CMS_eff_hww_sngele_trigger_2016', 'lumi_13TeV_XYFact', 'UEPS_ISR', 'CMS_ak4jet_jesRelativeSample_2016', 'CMS_ak8jet_jesAbsolute_2016', 'CMS_ak8jet_jesRelativeSample_2016', 'lumi_13TeV_2016', 'CMS_ak4jet_jesAbsolute', 'CMS_ak8jet_jesRelativeBal', 'lumi_13TeV_BBDefl', 'CMS_eff_hww_sngmu_trigger_2016', 'pdf_qq_ACCEPT', 'CMS_eff_Wtag_2016', 'CMS_PU_2016', 'CMS_btag_lfstats2_2016', 'CMS_eff_m_2016', 'pdf_Higgs_qqbar', 'CMS_ak4jet_jesEC2', 'CMS_eff_prefiring_2016', 'lumi_13TeV_DynBeta', 'MultiVnorm2016', 'pdf_ttbar_ACCEPT', 'CMS_btag_hfstats1_2016', 'pdf_Higgs_gg', 'CMS_ak4jet_jesBBEC1', 'CMS_ak4jet_jesBBEC1_2016', 'CMS_ak8jet_jer_2016', 'CMS_ak8jet_jms_2016', 'dynorm2016', 'CMS_btag_lfstats1_2016', 'CMS_ak8jet_jmr_2016', 'CMS_btag_cferr1', 'CMS_btag_cferr2', 'CMS_ak4jet_jesHF_2016', 'QCDscale_Higgs_qqbar', 'CMS_btag_hf', 'QCDscale_gg_ACCEPT', 'CMS_ak8jet_jesBBEC1_2016', 'CMS_scale_muon_2016', 'CMS_scale_met_2016']

print len(list2016)

NuisanceCategory2016={
    'lumionisty':{
        'alias':'Luminosity', 
        'type':'norm',
        'list':['lumi_13TeV_Ghosts', 'lumi_13TeV_XYFact', 'lumi_13TeV_2016', 'lumi_13TeV_BBDefl', 'lumi_13TeV_DynBeta']
    },
    'ak4jet_jes_jer':{
        'alias':'AK4Jet JES/JER',
        'type':'shape', 
        'list':['CMS_ak4jet_jesEC2_2016', 'CMS_ak4jet_jesRelativeBal', 'CMS_ak4jet_jer_2016', 'CMS_ak4jet_jesAbsolute_2016', 'CMS_ak4jet_jesHF', 'CMS_ak4jet_jesFlavorQCD', 'CMS_ak4jet_jesRelativeSample_2016', 'CMS_ak4jet_jesAbsolute', 'CMS_ak4jet_jesEC2', 'CMS_ak4jet_jesBBEC1', 'CMS_ak4jet_jesBBEC1_2016', 'CMS_ak4jet_jesHF_2016']
    },
    'ak8jet_jes_jer':{
        'alias':'AK8Jet JES/JER', 
        'type':'shape',
        'list':['CMS_ak8jet_jesBBEC1', 'CMS_ak8jet_jesHF_2016', 'CMS_ak8jet_jesAbsolute', 'CMS_ak8jet_jesFlavorQCD', 'CMS_ak8jet_jesEC2_2016', 'CMS_ak8jet_jesEC2', 'CMS_ak8jet_jesHF', 'CMS_ak8jet_jesAbsolute_2016', 'CMS_ak8jet_jesRelativeSample_2016', 'CMS_ak8jet_jesRelativeBal', 'CMS_ak8jet_jer_2016', 'CMS_ak8jet_jesBBEC1_2016'],
    },
    'wtag_jms_jmr':{
        'alias':'WtagAK8Jet JMSJMR',
        'type':'shape',
        'list':['CMS_ak8jet_jms_2016', 'CMS_ak8jet_jmr_2016']
    },
    'Wtag_eff':{
        'alias':'WtagAK8Jet Eff.',
        'type':'shape',
        'list':['CMS_eff_Wtag_2016']
    },
    'mjjshape':{
        'alias':'AK4Jet MjjShape',
        'type':'shape',
        'list':['mjjshape_2016'],
        },
    'btag':{
        'alias':'B-tagging',
        'type':'shape',
        'list':['CMS_btag_lf', 'CMS_btag_hfstats2_2016', 'CMS_btag_lfstats2_2016', 'CMS_btag_hfstats1_2016', 'CMS_btag_lfstats1_2016', 'CMS_btag_cferr1', 'CMS_btag_cferr2', 'CMS_btag_hf']
    },
    'MET':{
        'alias':'Missing Energy',
        'type':'shape',
        'list':['CMS_scale_met_2016']
    },
    'pdf_accept':{
        'alias':'PDF Acceptance',
        'type':'shape',
        'list':['pdf_gg_ACCEPT', 'pdf_qq_ACCEPT', 'pdf_ttbar_ACCEPT']
    },
    'qcdscale_accept':{
        'alias':'QCD scale Acceptance',
        'type':'shape',
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
        'type':'shape',
        'list':['UEPS_FSR', 'UEPS_ISR']
    },
    'bkgnorm':{
        'alias':'Background Norm.',
        'type':'norm',
        'list':['ggWWnorm', 'MultiVnorm2016', 'dynorm2016'],
    },
    'ElectronTrigger':{
        'alias':'ElectronTrigger Effieicny',
        'type':'shape',
        'list':['CMS_eff_hww_sngele_trigger_2016'],
    },
    'MuonTrigger':{
        'alias':'MuonTrigger Effieicny',
        'type':'shape',
        'list':['CMS_eff_hww_sngmu_trigger_2016']
    },
    'ElectronID':{
        'alias':'Electron Identification',
        'type':'shape',
        'list':['CMS_eff_e_2016'],
        },
    'MuonID':{
        'alias':'Muon Identification',
        'type':'shape',
        'list':['CMS_eff_m_2016'],
    },
    'ElectronEnergyScale':{
        'alias':'Electron Energy Scale',
        'type':'shape',
        'list':['CMS_scale_electron_2016']
    },
    'MuonEnergyScale':{
        'alias':'Muon Momentum Scale',
        'type':'shape',
        'list':['CMS_scale_muon_2016']
    },
    'Prefireing':{
        'alias':'Prefiring',
        'type':'shape',
        'list':['CMS_eff_prefiring_2016']
    },
    'pu':{
        'alias':'PileUp',
        'type':'shape',
        'list':['CMS_PU_2016']
    }
}

Vaidation(list2016,NuisanceCategory2016)
print [NuisanceCategory2016[nui]['alias'] for nui in NuisanceCategory2016]
