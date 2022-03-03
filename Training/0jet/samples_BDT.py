import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # inclusive BDT Training 0j merged
configurations = os.path.dirname(configurations) # Merged Training 
configurations = os.path.dirname(configurations) # FullRunII
configurations = os.path.dirname(configurations) # WW
configurations = os.path.dirname(configurations) # Configurations


from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, getBaseWnAOD, addSampleWeight
def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return []
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

# samples
try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()


################################################
################# SKIMS ########################
################################################

mcProduction_2016 = 'Summer16_102X_nAODv7_Full2016v7'
mcSteps_2016 = 'MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7{var}'

mcProduction_2017 = 'Fall2017_102X_nAODv7_Full2017v7'
mcSteps_2017 = 'MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7{var}'

mcProduction_2018 = 'Autumn18_102X_nAODv7_Full2018v7'
mcSteps_2018 = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7{var}'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'

def makeMCDirectory_2016(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction_2016, mcSteps_2016.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction_2016, mcSteps_2016.format(var=''))
		
def makeMCDirectory_2017(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction_2017, mcSteps_2017.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction_2017, mcSteps_2017.format(var=''))
		
def makeMCDirectory_2018(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction_2018, mcSteps_2018.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction_2018, mcSteps_2018.format(var=''))

mcDirectory_2016 = makeMCDirectory_2016()
mcDirectory_2017 = makeMCDirectory_2017()
mcDirectory_2018 = makeMCDirectory_2018()

################################################
############### Lepton WP ######################
################################################

eleWP_2016 = 'mva_90p_Iso2016_tthmva_70'
muWP_2016 = 'cut_Tight80x_tthmva_80'

eleWP_2017 = 'mvaFall17V1Iso_WP90_tthmva_70'	
muWP_2017 = 'cut_Tight_HWWW_tthmva_80'

eleWP_2018 = 'mvaFall17V1Iso_WP90_tthmva_70'
muWP_2018 = 'cut_Tight_HWWW_tthmva_80'

LepWPCut_2016 = 'LepCut2l__ele_' + eleWP_2016 + '__mu_' + muWP_2016
LepWPCut_2017 = 'LepCut2l__ele_' + eleWP_2017 + '__mu_' + muWP_2017
LepWPCut_2018 = 'LepCut2l__ele_' + eleWP_2018 + '__mu_' + muWP_2018

################################################
############### b-tag WPs ######################
################################################

# 2016
btagWP_2016 = '0.6321' # Deep CSV medium WP for 2016
bVeto_2016 = 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > '+btagWP_2016+') == 0'
bVetoSF_2016 = 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))'
bReq_2016 = 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > '+btagWP_2016+') >= 1'
bReqSF_2016 = 'mtw2>30 && mll>50 && ((Sum$(CleanJet_pt > 30.) == 0 && !bVeto_2016) || bReq_2016)'
topcr_2016 = 'mtw2>30 && mll>50 && ((Sum$(CleanJet_pt > 30.) == 0 && !bVeto_2016) || bReq_2016)'
btagSF_2016 = '(bVeto_2016 || (topcr_2016 && Sum$(CleanJet_pt > 30.) == 0))*bVetoSF_2016 + (topcr_2016 && Sum$(CleanJet_pt > 30.) > 0)*bReqSF_2016'

# 2017
btagWP_2017 = '0.4941' # Deep CSV medium WP for 2017
bVeto_2017 = 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > '+btagWP_2017+') == 0'
bVetoSF_2017 = 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))'
bReq_2017 = 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > '+btagWP_2017+') >= 1'
bReqSF_2017 = 'mtw2>30 && mll>50 && ((Sum$(CleanJet_pt > 30.) == 0 && !bVeto_2017) || bReq_2017)'
topcr_2017 = 'mtw2>30 && mll>50 && ((Sum$(CleanJet_pt > 30.) == 0 && !bVeto_2017) || bReq_2017)'
btagSF_2017 = '(bVeto_2017 || (topcr_2017 && Sum$(CleanJet_pt > 30.) == 0))*bVetoSF_2017 + (topcr_2017 && Sum$(CleanJet_pt > 30.) > 0)*bReqSF_2017'

# 2018
btagWP_2018 = '0.4184' # Deep CSV medium WP for 2018
bVeto_2018 = 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > '+btagWP_2018+') == 0'
bVetoSF_2018 = 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))'
bReq_2018 = 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > '+btagWP_2018+') >= 1'
bReqSF_2018 = 'mtw2>30 && mll>50 && ((Sum$(CleanJet_pt > 30.) == 0 && !bVeto_2018) || bReq_2018)'
topcr_2018 = 'mtw2>30 && mll>50 && ((Sum$(CleanJet_pt > 30.) == 0 && !bVeto_2018) || bReq_2018)'
btagSF_2018 = '(bVeto_2018 || (topcr_2018 && Sum$(CleanJet_pt > 30.) == 0))*bVetoSF_2018 + (topcr_2018 && Sum$(CleanJet_pt > 30.) > 0)*bReqSF_2018'

################################################
############ BASIC MC WEIGHTS ##################
################################################

Jet_PUIDSF = 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose)))'

SFweight_2016 = ' * '.join(['SFweight2l', LepWPCut_2016, 'LepSF2l__ele_' + eleWP_2016 + '__mu_' + muWP_2016, btagSF_2016, 'PrefireWeight', 'Jet_PUIDSF']) 
SFweight_2017 = ' * '.join(['SFweight2l', LepWPCut_2017, 'LepSF2l__ele_' + eleWP_2017 + '__mu_' + muWP_2017, btagSF_2017, 'PrefireWeight', 'Jet_PUIDSF'])
SFweight_2018 = ' * '.join(['SFweight2l', LepWPCut_2018, 'LepSF2l__ele_' + eleWP_2018 + '__mu_' + muWP_2018, btagSF_2018, 'Jet_PUIDSF'])

PromptGenLepMatch2l = 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1], 0)'

mcCommonWeight_2016 = 'XSWeight*' + SFweight_2016 + '*PromptGenLepMatch2l*METFilter_MC'
mcCommonWeight_2017 = 'XSWeight*' + SFweight_2017 + '*PromptGenLepMatch2l*METFilter_MC'
mcCommonWeight_2018 = 'XSWeight*' + SFweight_2018 + '*PromptGenLepMatch2l*METFilter_MC'

###########################################
#############  BACKGROUNDS  ###############
###########################################

###### DY #######
useDYHT = True

#xxxxxxx 2016 xxxxxxx
files = nanoGetSampleFiles(mcDirectory_2016, 'DYJetsToLL_M-50_ext2') + \
    nanoGetSampleFiles(mcDirectory_2016, 'DYJetsToLL_M-10to50')

samples['DY_2016'] = {
    'name': files,
    'weight': mcCommonWeight_2016 + '*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 &&\
                                 Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )',
    'FilesPerJob': 4,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    }
	
# Add DY HT Samples
if useDYHT :
    samples['DY_2016']['name'] +=   nanoGetSampleFiles(mcDirectory_2016, 'DYJetsToLL_M-5to50_HT-70to100') \
                                + nanoGetSampleFiles(mcDirectory_2016, 'DYJetsToLL_M-5to50_HT-100to200') \
                                + nanoGetSampleFiles(mcDirectory_2016, 'DYJetsToLL_M-5to50_HT-200to400') \
                                + nanoGetSampleFiles(mcDirectory_2016, 'DYJetsToLL_M-5to50_HT-400to600_ext1') \
                                + nanoGetSampleFiles(mcDirectory_2016, 'DYJetsToLL_M-5to50_HT-600toinf') \
                                + nanoGetSampleFiles(mcDirectory_2016, 'DYJetsToLL_M-50_HT-70to100') \
                                + nanoGetSampleFiles(mcDirectory_2016, 'DYJetsToLL_M-50_HT-100to200_ext1') \
                                + nanoGetSampleFiles(mcDirectory_2016, 'DYJetsToLL_M-50_HT-200to400_ext1') \
				+ nanoGetSampleFiles(mcDirectory_2016, 'DYJetsToLL_M-50_HT-400to600_ext1') \
				+ nanoGetSampleFiles(mcDirectory_2016, 'DYJetsToLL_M-50_HT-600to800') \
				+ nanoGetSampleFiles(mcDirectory_2016, 'DYJetsToLL_M-50_HT-800to1200') \
				+ nanoGetSampleFiles(mcDirectory_2016, 'DYJetsToLL_M-50_HT-1200to2500') \
				+ nanoGetSampleFiles(mcDirectory_2016, 'DYJetsToLL_M-50_HT-2500toInf')

handle = open('%s/src/PlotsConfigurations/Configurations/patches/DYrew30.py' % os.getenv('CMSSW_BASE'),'r')
exec(handle)
handle.close()
DY_NLO_pTllrw_2016 = '('+DYrew['2016']['NLO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)'
DY_LO_pTllrw_2016 = '('+DYrew['2016']['LO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)'

addSampleWeight(samples,'DY_2016','DYJetsToLL_M-50_ext2', DY_NLO_pTllrw_2016)
addSampleWeight(samples,'DY_2016','DYJetsToLL_M-10to50', DY_NLO_pTllrw_2016)

if useDYHT :
    # Remove high HT from inclusive samples
    addSampleWeight(samples,'DY_2016','DYJetsToLL_M-50_ext2', 'LHE_HT<70.0')
    addSampleWeight(samples,'DY_2016','DYJetsToLL_M-10to50', 'LHE_HT<70.0')
    # pt_ll weight
    addSampleWeight(samples,'DY_2016','DYJetsToLL_M-5to50_HT-70to100'       ,DY_LO_pTllrw_2016)
    addSampleWeight(samples,'DY_2016','DYJetsToLL_M-5to50_HT-100to200'      ,DY_LO_pTllrw_2016)
    addSampleWeight(samples,'DY_2016','DYJetsToLL_M-5to50_HT-200to400'      ,DY_LO_pTllrw_2016)
    addSampleWeight(samples,'DY_2016','DYJetsToLL_M-5to50_HT-400to600_ext1' ,DY_LO_pTllrw_2016)
    addSampleWeight(samples,'DY_2016','DYJetsToLL_M-5to50_HT-600toinf'      ,DY_LO_pTllrw_2016)
    addSampleWeight(samples,'DY_2016','DYJetsToLL_M-50_HT-70to100'          ,DY_LO_pTllrw_2016)
    addSampleWeight(samples,'DY_2016','DYJetsToLL_M-50_HT-100to200_ext1'    ,DY_LO_pTllrw_2016)
    addSampleWeight(samples,'DY_2016','DYJetsToLL_M-50_HT-200to400_ext1'    ,DY_LO_pTllrw_2016)
    addSampleWeight(samples,'DY_2016','DYJetsToLL_M-50_HT-400to600_ext1'    ,DY_LO_pTllrw_2016)
    addSampleWeight(samples,'DY_2016','DYJetsToLL_M-50_HT-600to800'         ,DY_LO_pTllrw_2016)
    addSampleWeight(samples,'DY_2016','DYJetsToLL_M-50_HT-800to1200'        ,DY_LO_pTllrw_2016)
    addSampleWeight(samples,'DY_2016','DYJetsToLL_M-50_HT-1200to2500'       ,DY_LO_pTllrw_2016)
    addSampleWeight(samples,'DY_2016','DYJetsToLL_M-50_HT-2500toInf'        ,DY_LO_pTllrw_2016)
'''
#xxxxxxx 2017 xxxxxxx
files = nanoGetSampleFiles(mcDirectory_2017, 'DYJetsToLL_M-50_ext1') + \
        nanoGetSampleFiles(mcDirectory_2017, 'DYJetsToLL_M-10to50-LO_ext1')

samples['DY_2017'] = {
    'name': files,
    'weight': mcCommonWeight_2017 + "*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 &&\
                                     Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )",
    'FilesPerJob': 8,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    }

# Add DY HT Samples
if useDYHT :
    samples['DY_2017']['name'] +=     nanoGetSampleFiles(mcDirectory_2017, 'DYJetsToLL_M-4to50_HT-100to200_ext1') \
                               + nanoGetSampleFiles(mcDirectory_2017, 'DYJetsToLL_M-4to50_HT-200to400_newpmx') \
                               + nanoGetSampleFiles(mcDirectory_2017, 'DYJetsToLL_M-4to50_HT-400to600') \
                               + nanoGetSampleFiles(mcDirectory_2017, 'DYJetsToLL_M-4to50_HT-600toInf') \
                               + nanoGetSampleFiles(mcDirectory_2017, 'DYJetsToLL_M-50_HT-100to200') \
                               + nanoGetSampleFiles(mcDirectory_2017, 'DYJetsToLL_M-50_HT-200to400') \
                               + nanoGetSampleFiles(mcDirectory_2017, 'DYJetsToLL_M-50_HT-400to600_ext1') \
                               + nanoGetSampleFiles(mcDirectory_2017, 'DYJetsToLL_M-50_HT-600to800') \
                               + nanoGetSampleFiles(mcDirectory_2017, 'DYJetsToLL_M-50_HT-800to1200') \
                               + nanoGetSampleFiles(mcDirectory_2017, 'DYJetsToLL_M-50_HT-1200to2500') \
                               + nanoGetSampleFiles(mcDirectory_2017, 'DYJetsToLL_M-50_HT-2500toInf')

DY_NLO_pTllrw_2017 = '('+DYrew['2017']['NLO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)'
DY_LO_pTllrw_2017 = '('+DYrew['2017']['LO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)'

addSampleWeight(samples,'DY_2017','DYJetsToLL_M-50_ext1',        DY_NLO_pTllrw_2017)
addSampleWeight(samples,'DY_2017','DYJetsToLL_M-10to50-LO_ext1', DY_LO_pTllrw_2017)

if useDYHT :
    # Remove high HT from inclusive samples
    addSampleWeight(samples,'DY_2017','DYJetsToLL_M-50_ext1'       , 'LHE_HT<100.0')
    addSampleWeight(samples,'DY_2017','DYJetsToLL_M-10to50-LO_ext1', 'LHE_HT<100.0')
    # pt_ll weight
    addSampleWeight(samples,'DY_2017','DYJetsToLL_M-4to50_HT-100to200_ext1'   ,DY_LO_pTllrw_2017)
    addSampleWeight(samples,'DY_2017','DYJetsToLL_M-4to50_HT-200to400_newpmx' ,DY_LO_pTllrw_2017)
    addSampleWeight(samples,'DY_2017','DYJetsToLL_M-4to50_HT-400to600'        ,DY_LO_pTllrw_2017)
    addSampleWeight(samples,'DY_2017','DYJetsToLL_M-4to50_HT-600toInf'        ,DY_LO_pTllrw_2017)
    addSampleWeight(samples,'DY_2017','DYJetsToLL_M-50_HT-100to200'           ,DY_LO_pTllrw_2017)
    addSampleWeight(samples,'DY_2017','DYJetsToLL_M-50_HT-200to400'           ,DY_LO_pTllrw_2017)
    addSampleWeight(samples,'DY_2017','DYJetsToLL_M-50_HT-400to600_ext1'      ,DY_LO_pTllrw_2017)
    addSampleWeight(samples,'DY_2017','DYJetsToLL_M-50_HT-600to800'           ,DY_LO_pTllrw_2017)
    addSampleWeight(samples,'DY_2017','DYJetsToLL_M-50_HT-800to1200'          ,DY_LO_pTllrw_2017)
    addSampleWeight(samples,'DY_2017','DYJetsToLL_M-50_HT-1200to2500'         ,DY_LO_pTllrw_2017)
    addSampleWeight(samples,'DY_2017','DYJetsToLL_M-50_HT-2500toInf'          ,DY_LO_pTllrw_2017)

#xxxxxxx 2018 xxxxxxx
files = nanoGetSampleFiles(mcDirectory_2018, 'DYJetsToLL_M-50_ext2') + \
        nanoGetSampleFiles(mcDirectory_2018, 'DYJetsToLL_M-10to50-LO') + \
        nanoGetSampleFiles(mcDirectory_2018, 'DYJetsToLL_M-10to50-LO_ext1')

samples['DY_2018'] = {
    'name': files,
    'weight': mcCommonWeight_2018 + '*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 &&\
                                 Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )',
    'FilesPerJob': 6,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
}

# Add DY HT Samples
if useDYHT :
    samples['DY_2018']['name'] +=     nanoGetSampleFiles(mcDirectory_2018, 'DYJetsToLL_M-4to50_HT-100to200' ) \
                               + nanoGetSampleFiles(mcDirectory_2018, 'DYJetsToLL_M-4to50_HT-200to400' ) \
                               + nanoGetSampleFiles(mcDirectory_2018, 'DYJetsToLL_M-4to50_HT-400to600' ) \
                               + nanoGetSampleFiles(mcDirectory_2018, 'DYJetsToLL_M-4to50_HT-600toInf') \
                               + nanoGetSampleFiles(mcDirectory_2018, 'DYJetsToLL_M-50_HT-70to100') \
                               + nanoGetSampleFiles(mcDirectory_2018, 'DYJetsToLL_M-50_HT-100to200') \
                               + nanoGetSampleFiles(mcDirectory_2018, 'DYJetsToLL_M-50_HT-200to400') \
                               + nanoGetSampleFiles(mcDirectory_2018, 'DYJetsToLL_M-50_HT-400to600') \
                               + nanoGetSampleFiles(mcDirectory_2018, 'DYJetsToLL_M-50_HT-600to800') \
                               + nanoGetSampleFiles(mcDirectory_2018, 'DYJetsToLL_M-50_HT-800to1200')  \
                               + nanoGetSampleFiles(mcDirectory_2018, 'DYJetsToLL_M-50_HT-1200to2500') \
                               + nanoGetSampleFiles(mcDirectory_2018, 'DYJetsToLL_M-50_HT-2500toInf')

M10baseW = getBaseWnAOD(mcDirectory_2018,'Autumn18_102X_nAODv6_Full2018v6',['DYJetsToLL_M-10to50-LO','DYJetsToLL_M-10to50-LO_ext1'])
DY_NLO_pTllrw_2018 = '('+DYrew['2018']['NLO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)'
DY_LO_pTllrw_2018 = '('+DYrew['2018']['LO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)'

addSampleWeight(samples,'DY_2018','DYJetsToLL_M-50_ext2'        ,DY_NLO_pTllrw_2018)
addSampleWeight(samples,'DY_2018','DYJetsToLL_M-10to50-LO'      ,DY_LO_pTllrw_2018 +'*'+M10baseW+'/baseW')
addSampleWeight(samples,'DY_2018','DYJetsToLL_M-10to50-LO_ext1' ,DY_LO_pTllrw_2018 +'*'+M10baseW+'/baseW')

if useDYHT :
    # Remove high HT from inclusive samples
    addSampleWeight(samples,'DY_2018','DYJetsToLL_M-10to50-LO_ext1', '(LHE_HT<100)')
    addSampleWeight(samples,'DY_2018','DYJetsToLL_M-10to50-LO'     , '(LHE_HT<100)')
    addSampleWeight(samples,'DY_2018','DYJetsToLL_M-50_ext2'       , '(LHE_HT<70)')
    # pt_ll weight
    addSampleWeight(samples,'DY_2018','DYJetsToLL_M-4to50_HT-100to200',DY_LO_pTllrw_2018)
    addSampleWeight(samples,'DY_2018','DYJetsToLL_M-4to50_HT-200to400',DY_LO_pTllrw_2018)
    addSampleWeight(samples,'DY_2018','DYJetsToLL_M-4to50_HT-400to600',DY_LO_pTllrw_2018)
    addSampleWeight(samples,'DY_2018','DYJetsToLL_M-4to50_HT-600toInf',DY_LO_pTllrw_2018)
    addSampleWeight(samples,'DY_2018','DYJetsToLL_M-50_HT-70to100'    ,DY_LO_pTllrw_2018)
    addSampleWeight(samples,'DY_2018','DYJetsToLL_M-50_HT-100to200'   ,DY_LO_pTllrw_2018)
    addSampleWeight(samples,'DY_2018','DYJetsToLL_M-50_HT-200to400'   ,DY_LO_pTllrw_2018)
    addSampleWeight(samples,'DY_2018','DYJetsToLL_M-50_HT-400to600'   ,DY_LO_pTllrw_2018)
    addSampleWeight(samples,'DY_2018','DYJetsToLL_M-50_HT-600to800'   ,DY_LO_pTllrw_2018)
    addSampleWeight(samples,'DY_2018','DYJetsToLL_M-50_HT-800to1200'  ,DY_LO_pTllrw_2018)
    addSampleWeight(samples,'DY_2018','DYJetsToLL_M-50_HT-1200to2500' ,DY_LO_pTllrw_2018)
    addSampleWeight(samples,'DY_2018','DYJetsToLL_M-50_HT-2500toInf'  ,DY_LO_pTllrw_2018)
'''
###########################################
#############   SIGNALS  ##################
###########################################

###### WW ########

#xxxxxxx 2016 xxxxxxx
samples['WW_2016'] = {
    'name': nanoGetSampleFiles(mcDirectory_2016, 'WW-LO'),
    'weight': mcCommonWeight_2016+ '*nllW',
    'FilesPerJob': 4
}
'''
#xxxxxxx 2017 xxxxxxx
samples['WW_2017'] = {
    'name': nanoGetSampleFiles(mcDirectory_2017, 'WW-LO'),
    'weight': mcCommonWeight_2017 + '*nllW',
    'FilesPerJob': 1
}

#xxxxxxx 2018 xxxxxxx
samples['WW_2018'] = {
    'name': nanoGetSampleFiles(mcDirectory_2018, 'WW-LO'),
    'weight': mcCommonWeight_2018+'*nllW',
    'FilesPerJob': 2
}
'''
###### ggWW ########

#xxxxxxx 2016 xxxxxxx
samples['ggWW_2016'] = {
    'name': nanoGetSampleFiles(mcDirectory_2016, 'GluGluWWTo2L2Nu_MCFM'),
    'weight': mcCommonWeight_2016+'*1.53/1.4', # updating k-factor
    'FilesPerJob': 4
}
'''
#xxxxxxx 2017 xxxxxxx
files = nanoGetSampleFiles(mcDirectory_2017, 'GluGluToWWToENEN') + \
    nanoGetSampleFiles(mcDirectory_2017, 'GluGluToWWToENMN') + \
    nanoGetSampleFiles(mcDirectory_2017, 'GluGluToWWToENTN') + \
    nanoGetSampleFiles(mcDirectory_2017, 'GluGluToWWToMNEN') + \
    nanoGetSampleFiles(mcDirectory_2017, 'GluGluToWWToMNMN') + \
    nanoGetSampleFiles(mcDirectory_2017, 'GluGluToWWToMNTN') + \
    nanoGetSampleFiles(mcDirectory_2017, 'GluGluToWWToTNEN') + \
    nanoGetSampleFiles(mcDirectory_2017, 'GluGluToWWToTNMN') + \
    nanoGetSampleFiles(mcDirectory_2017, 'GluGluToWWToTNTN')

samples['ggWW_2017'] = {
    'name': files,
    'weight': mcCommonWeight_2017 + '*1.53/1.4', # updating k-factor
    'FilesPerJob': 10
}

#xxxxxxx 2018 xxxxxxx
samples['ggWW_2018'] = {
    'name': nanoGetSampleFiles(mcDirectory_2018, 'GluGluToWWToENEN') + \
            nanoGetSampleFiles(mcDirectory_2018, 'GluGluToWWToENMN') + \
            nanoGetSampleFiles(mcDirectory_2018, 'GluGluToWWToENTN') + \
            nanoGetSampleFiles(mcDirectory_2018, 'GluGluToWWToMNEN') + \
            nanoGetSampleFiles(mcDirectory_2018, 'GluGluToWWToMNMN') + \
            nanoGetSampleFiles(mcDirectory_2018, 'GluGluToWWToMNTN') + \
            nanoGetSampleFiles(mcDirectory_2018, 'GluGluToWWToTNEN') + \
            nanoGetSampleFiles(mcDirectory_2018, 'GluGluToWWToTNMN') + \
            nanoGetSampleFiles(mcDirectory_2018, 'GluGluToWWToTNTN'),
    'weight': mcCommonWeight_2018+'*1.53/1.4',
    'FilesPerJob': 2
}
'''
