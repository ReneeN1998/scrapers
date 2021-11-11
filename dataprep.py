import pandas as pd
games1 = pd.read('1a_games.csv')

updates1 = pd.read('1a_updatesdata.csv')

# SteamSpy 
#data read in per genre (11) merged into 1 dataset 
spy_act = pd.read('actionsteamspy.csv')
spy_adv = pd.read('Adventuresteamspy.csv')
spy_ear = pd.read('earlyaccesssteamspy.csv')
spy_exe = pd.read('exearlyaccesssteamspy.csv')
spy_fre = pd.read('freesteamspy.csv')
spy_ind = pd.read('Indiesteamspy.csv')
spy_mmo = pd.read('massivelysteamspy.csv')
spy_rpg = pd.read('RPGsteamspy.csv')
spy_sim = pd.read('Simulationsteamspy.csv')
spy_spo = pd.read('Sportssteamspy.csv')
spy_str = pd.read('strategysteamspy.csv')

#Add genre to the data before merging? 

#Data merged into 1 dataset for steamspy data
data_steamspy = pd.concat(spy_act, spy_adv, spy_ear, spy_exe, spy_fre, spy_ind, spy_mmo, spy_rpg, spy_sim, spy_spo, spy_str)
