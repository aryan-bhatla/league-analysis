#----------------------------------------------------------------------------------------------------- # 
# Modules
#----------------------------------------------------------------------------------------------------- # 
import data_functions as data
import logistics_functions as logistic
import pandas as pd 


#----------------------------------------------------------------------------------------------------- #
# Roles for each team
#----------------------------------------------------------------------------------------------------- # 
Support = "Support"
ADC = "ADC"
Middle = "Middle"
Jungle = "Jungle"
Top = "Top"

Support_Sub = "Support_Sub"
ADC_Sub = "ADC_Sub"
Middle_Sub = "Middle_Sub"
Jungle_Sub = "Jungle_Sub"
Top_Sub = "Top_Sub"


#----------------------------------------------------------------------------------------------------- # 
# LCK teams 
#----------------------------------------------------------------------------------------------------- # 
Dplus_KIA = {Support: "Kellin", 
             ADC: "Aiming", 
             Middle: "ShowMaker", 
             Jungle: "Lucid", 
             Top: "Kingen"}

DRX = {Support: "Pleata", 
       ADC: "Teddy", 
       Middle: "SeTab", 
       Jungle: "Sponge", 
       Top: "Rascal"}

Gen_G = {Support: "Lehends", 
         ADC: "Peyz", 
         Middle: "Chovy", 
         Jungle: "Canyon", 
         Top: "Kiin"}

Hanwha_Life_Esports = {Support: "Delight", 
                       ADC: "Viper", 
                       Middle: "Zeka", 
                       Jungle: "Peanut", 
                       Top: "Doran"}

KT_Rolster = {Support: "BeryL", 
              ADC: "Deft", 
              Middle: "Bdd", 
              Jungle: "Pyosik", 
              Top: "PerfecT"}

Kwangdong_Freecs = {Support: "Andil", 
                    ADC: "Taeyoon", 
                    Middle: "BuLLDoG", 
                    Jungle: "Cuzz", 
                    # Jungle_Sub: 'YoungJae', 
                    Top: "DuDu"}

Nongshim_RedForce = {Support: "Peter", 
                    ADC: "Jiwoo", 
                    Middle: "FIESTA", 
                    Jungle: "Sylvie", 
                    Top: "DnDn"}

BRION = {Support: "Effort", 
         ADC: "Envyy", 
         Middle: "Karis", 
         Jungle: "gideon", 
         Top: "Morgan"}

T1 = {Support: "Keria", 
      ADC: "Gumayusi", 
      Middle: "Faker", 
      Jungle: "Oner", 
      Top: "Zeus"}

Liiv_SANDBOX = {Support: "Execute", 
                ADC: "Hena", 
                Middle: "Clozer", 
                Jungle: "Willer", 
                Top: "Clear"}

LCK_teams = {'Dplus_KIA': Dplus_KIA,
             'DRX': DRX,
             'Gen_G': Gen_G,
             'Hanwha_Life_Esports': Hanwha_Life_Esports,
             'KT_Rolster': KT_Rolster,
             'Kwangdong_Freecs': Kwangdong_Freecs,
             'Nongshim_RedForce': Nongshim_RedForce,
             'BRION': BRION,
             'T1': T1,
             'Liiv_SANDBOX': Liiv_SANDBOX}


#----------------------------------------------------------------------------------------------------- # 
# LCS teams 
#----------------------------------------------------------------------------------------------------- # 
_100_Thieves = {Support: "Hide",
                ADC: "Sniper",
                Middle: "River",
                Jungle: "Quid",
                Top: "Meech"}

Cloud9 = {Support: "VULCAN",
          ADC: "Fudge",
          Middle: "jojopyun",
          Jungle: "Blaber",
          Top: "Berserker"}

Dignitas = {Support: "Isles",
            ADC: "Tomo",
            Middle: "Dove",
            Jungle: "eXyu",
            Top: "Rich"}

FlyQuest = {Support: "Massu",
            ADC: "Busio",
            Middle: "Jensen",
            Jungle: "Inspired",
            Top: "Bwipo"}

Immortals = {Support: "Olleh",
             ADC: "Tactical",
             Middle: "Mask",
             Jungle: "Armao",
             Top: "Castle"}

NRG = {Support: "huhi",
       ADC: "FBI",
       Middle: "Palafox",
       Jungle: "Contractz",
       Top: "Dhokla"}

Shopify_Rebellion = {Support: "Zeyzal",
                     ADC: "Bvoy",
                     Middle: "Insanity",
                     Jungle: "Bugi",
                     Top: "FakeGod"}

Team_Liquid = {Support: "CoreJJ",
               ADC: "Yeon",
               Middle: "APA",
               Jungle: "UmTi",
               Top: "Impact"}

LCS_teams = {'100_Thieves': _100_Thieves,
             'Cloud9': Cloud9,
             'Dignitas': Dignitas,
             'FlyQuest': FlyQuest,
             'Immortals': Immortals,
             'NRG': NRG,
             'Shopify_Rebellion': Shopify_Rebellion,
             'Team_Liquid': Team_Liquid}


#----------------------------------------------------------------------------------------------------- # 
# LEC teams 
#----------------------------------------------------------------------------------------------------- # 
Fnatic = {Support: "Jun",
          ADC: "Noah",
          Middle: "Humanoid",
          Jungle: "Razork",
          Top: "Oscarinin"}

G2_Esports = {Support: "Mikyx",
              ADC: "Hans Sama",
              Middle: "Caps",
              Jungle: "Yike",
              Top: "BrokenBlade"}

GIANTX = {Support: "IgNar",
          ADC: "Patrik",
          Middle: "Jackies",
          Jungle: "Peach",
          Top: "Odoamne"}

Rogue = {Support: "Zoelys",
         ADC: "Comp",
         Middle: "Larssen",
         Jungle: "Markoon",
         Top: "Szygenda"}

SK_Gaming = {Support: "Doss",
             ADC: "Exakick",
             Middle: "Nisqy",
             Jungle: "Isma",
             Top: "Irrelevant"}

Team_BDS = {Support: "Labrov",
            ADC: "Ice",
            Middle: "nuc",
            Jungle: "Sheo",
            Top: "Adam"}

Team_Heretics = {Support: "Kaiser",
                 ADC: "Flakked",
                 Middle: "Perkz",
                 Jungle: "Jankos",
                 Top: "Wunder"}

Team_Vitality = {Support: "Hylissang",
                 ADC: "Carzzy",
                 Middle: "Vetheo",
                 Jungle: "Daglas",
                 Top: "Photon"}

LEC_teams = {'Fnatic': Fnatic,
             'G2_Esports': G2_Esports,
             'GIANTX': GIANTX,
             'Rogue': Rogue,
             'SK_Gaming': SK_Gaming,
             'Team_BDS': Team_BDS,
             'Team_Heretics': Team_Heretics,
             'Team_Vitality': Team_Vitality}


#----------------------------------------------------------------------------------------------------- # 
# All teams 
#----------------------------------------------------------------------------------------------------- # 
all_teams = {
    'LCK': {'Dplus_KIA': Dplus_KIA,
            'DRX': DRX,
            'Gen_G': Gen_G,
            'Hanwha_Life_Esports': Hanwha_Life_Esports,
            'KT_Rolster': KT_Rolster,
            'Kwangdong_Freecs': Kwangdong_Freecs,
            'Nongshim_RedForce': Nongshim_RedForce,
            'BRION': BRION,
            'T1': T1,
            'Liiv_SANDBOX': Liiv_SANDBOX},

    'LCS': {'100_Thieves': _100_Thieves,
            'Cloud9': Cloud9,
            'Dignitas': Dignitas,
            'FlyQuest': FlyQuest,
            'Immortals': Immortals,
            'NRG': NRG,
            'Shopify_Rebellion': Shopify_Rebellion,
            'Team_Liquid': Team_Liquid},

    'LEC': {'Fnatic': Fnatic,
            'G2_Esports': G2_Esports,
            'GIANTX': GIANTX,
            'Rogue': Rogue,
            'SK_Gaming': SK_Gaming,
            'Team_BDS': Team_BDS,
            'Team_Heretics': Team_Heretics,
            'Team_Vitality': Team_Vitality}
}


#----------------------------------------------------------------------------------------------------- # 
# Data preprocessing
#----------------------------------------------------------------------------------------------------- # 
# Load data 
player_data = data.prepare_data("data/LCK_Player_Data",             # Korean main league
                                "data/LCKCL_Player_Data",           # Korean sub league  
                                "data/LCS_Player_Data",             # North American main league 
                                "data/LCSA_Player_Data",            # North American sub league 
                                "data/LEC_Player_Data",             # European main league 
                                "data/LFL_Player_Data",             # European sub league
                                "data/PRM_Player_Data",             # European sub league 
                                "data/NLC_Player_Data",             # European sub league
                                "data/MSI_Player_Data",             # Mid year tournament 
                                "data/Worlds_Player_Data")          # World championship tournament 

# Clean up final row containing NaN
player_data.drop(player_data.tail(1).index, inplace = True)


#----------------------------------------------------------------------------------------------------- #
# Load results 
#----------------------------------------------------------------------------------------------------- # 
model_results = pd.read_csv('model_results.csv', index_col = 0)


#----------------------------------------------------------------------------------------------------- #
# Elo normalisation factor
#----------------------------------------------------------------------------------------------------- # 
LCS_normalisation = 1.0
LEC_normalisation = 1.0
LCK_normalisation = 1.0


#----------------------------------------------------------------------------------------------------- #
# LCK, LCS, LEC ratings
#----------------------------------------------------------------------------------------------------- # 
model_method = "rf_importance"
# model_method = "coefficient"
# model_method = "xg_importance"

lck_team_ratings = logistic.calculate_team_ratings(LCK_teams, model_results, player_data, model_method)
lcs_team_ratings = logistic.calculate_team_ratings(LCS_teams, model_results, player_data, model_method, LCS_normalisation)
lec_team_ratings = logistic.calculate_team_ratings(LEC_teams, model_results, player_data, model_method, LEC_normalisation)

lck_data = zip(LCK_teams, lck_team_ratings)
lcs_data = zip(LCS_teams, lcs_team_ratings)
lec_data = zip(LEC_teams, lec_team_ratings)

lck_data_dict = dict(zip(LCK_teams.keys(), lck_team_ratings))
lcs_data_dict = dict(zip(LCS_teams.keys(), lcs_team_ratings))
lec_data_dict = dict(zip(LEC_teams.keys(), lec_team_ratings))


#----------------------------------------------------------------------------------------------------- #
# LCK, LCS, LEC ratings tables
#----------------------------------------------------------------------------------------------------- # 
lck_ratings = logistic.ratings_table(LCK_teams, lck_team_ratings)
lcs_ratings = logistic.ratings_table(LCS_teams, lcs_team_ratings)
lec_ratings = logistic.ratings_table(LEC_teams, lec_team_ratings)


#----------------------------------------------------------------------------------------------------- #
# LCK, LCS, LEC winrates tables 
#----------------------------------------------------------------------------------------------------- # 
best_of_one_lck_winrates = logistic.winrates_table(LCK_teams, lck_data_dict, 1)
best_of_one_lcs_winrates = logistic.winrates_table(LCS_teams, lcs_data_dict, 1)
best_of_one_lec_winrates = logistic.winrates_table(LEC_teams, lec_data_dict, 1)

best_of_three_lck_winrates = logistic.winrates_table(LCK_teams, lck_data_dict, 3)
best_of_three_lcs_winrates = logistic.winrates_table(LCS_teams, lcs_data_dict, 3)
best_of_three_lec_winrates = logistic.winrates_table(LEC_teams, lec_data_dict, 3)

best_of_five_lck_winrates = logistic.winrates_table(LCK_teams, lck_data_dict, 5)
best_of_five_lcs_winrates = logistic.winrates_table(LCS_teams, lcs_data_dict, 5)
best_of_five_lec_winrates = logistic.winrates_table(LEC_teams, lec_data_dict, 5)


#----------------------------------------------------------------------------------------------------- #
# LCK, LCS, LEC odds tables 
#----------------------------------------------------------------------------------------------------- # 
best_of_one_lck_odds = logistic.odds_table(LCK_teams, lck_data_dict, 1)
best_of_one_lcs_odds = logistic.odds_table(LCS_teams, lcs_data_dict, 1)
best_of_one_lec_odds = logistic.odds_table(LEC_teams, lec_data_dict, 1)

best_of_three_lck_odds = logistic.odds_table(LCK_teams, lck_data_dict, 3)
best_of_three_lcs_odds = logistic.odds_table(LCS_teams, lcs_data_dict, 3)
best_of_three_lec_odds = logistic.odds_table(LEC_teams, lec_data_dict, 3)

best_of_five_lck_odds = logistic.odds_table(LCK_teams, lck_data_dict, 5)
best_of_five_lcs_odds = logistic.odds_table(LCS_teams, lcs_data_dict, 5)
best_of_five_lec_odds = logistic.odds_table(LEC_teams, lec_data_dict, 5)