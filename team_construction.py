#----------------------------------------------------------------------------------------------------- # 
# Modules
#----------------------------------------------------------------------------------------------------- # 
import data_preparation
import pandas as pd
import rating_calculation as rating 


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
# Data preprocessing
#----------------------------------------------------------------------------------------------------- # 
# Load data 
final_data = data_preparation.prepare_data("LCK_Player_Data",             # Korean main league
                                           "LCKCL_Player_Data",           # Korean sub league  
                                           "LCS_Player_Data",             # North American main league 
                                           "LCSA_Player_Data",            # North American sub league 
                                           "LEC_Player_Data",             # European main league 
                                           "LFL_Player_Data",             # European sub league
                                           "PRM_Player_Data",             # European sub league 
                                           "NLC_Player_Data",             # European sub league
                                           "MSI_Player_Data",             # Mid year tournament 
                                           "Worlds_Player_Data")          # World championship tournament 

# Clean up final row containing NaN
final_data.drop(final_data.tail(1).index, inplace = True)


#----------------------------------------------------------------------------------------------------- #
# Load results 
#----------------------------------------------------------------------------------------------------- # 
model_results = pd.read_csv('results.csv', index_col = 0)


#----------------------------------------------------------------------------------------------------- #
# Elo normalisation factor
#----------------------------------------------------------------------------------------------------- # 
LCS_normalisation = 1.25
LEC_normalisation = 1.15
LCK_normalisation = 1.0


#----------------------------------------------------------------------------------------------------- # 
# LCK total team elo
#----------------------------------------------------------------------------------------------------- # 
team_ratings = []

# Iterate through each team in the LCK
for team_name, team_data in LCK_teams.items():
   
    # Reset player_ratings for each team
    player_ratings = []  

    for position, player in team_data.items():
        ratings = rating.calc_player_rating(player, model_results, final_data, "importance")
        player_ratings.append(ratings)

    total_team_rating = sum(player_ratings)
    team_ratings.append(total_team_rating)

    print(f"{team_name} has a rating of {total_team_rating}")


#----------------------------------------------------------------------------------------------------- # 
# LCS total team elo
#----------------------------------------------------------------------------------------------------- #
team_ratings = []

# Iterate through each team in the LCS
for team_name, team_data in LCS_teams.items():
   
    # Reset player_ratings for each team
    player_ratings = []  

    for position, player in team_data.items():
        ratings = rating.calc_player_rating(player, model_results, final_data, "importance")
        player_ratings.append(ratings)

    total_team_rating = sum(player_ratings) / LCS_normalisation
    team_ratings.append(total_team_rating)

    print(f"{team_name} has a rating of {total_team_rating}")


#----------------------------------------------------------------------------------------------------- # 
# LEC total team elo
#----------------------------------------------------------------------------------------------------- #
team_ratings = []

# Iterate through each team in the LEC
for team_name, team_data in LEC_teams.items():
   
    # Reset player_ratings for each team
    player_ratings = []  

    for position, player in team_data.items():
        ratings = rating.calc_player_rating(player, model_results, final_data, "importance")
        player_ratings.append(ratings)

    total_team_rating = sum(player_ratings) / LEC_normalisation
    team_ratings.append(total_team_rating)

    print(f"{team_name} has a rating of {total_team_rating}")