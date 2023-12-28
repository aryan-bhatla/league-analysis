#----------------------------------------------------------------------------------------------------- # 
# Modules
#----------------------------------------------------------------------------------------------------- # 
from flask import Flask, render_template

# Set up instance of Flask so can be used by other modules 
app = Flask(__name__)

from team_construction import calculate_team_ratings, LCK_teams, LCS_teams, LEC_teams


#----------------------------------------------------------------------------------------------------- # 
# App main
#----------------------------------------------------------------------------------------------------- # 
@app.route('/')
def index(): 
    
    # Decide normalisation
    LCS_normalisation = 1.25
    LEC_normalisation = 1.15
    LCK_normalisation = 1.0

    # Calculate team ratings
    lck_team_ratings = calculate_team_ratings(LCK_teams, LCK_normalisation)
    lcs_team_ratings = calculate_team_ratings(LCS_teams, LCS_normalisation)
    lec_team_ratings = calculate_team_ratings(LEC_teams, LEC_normalisation)

    # Collapse the data into a single variable
    lck_data = zip(LCK_teams, lck_team_ratings)
    lcs_data = zip(LCS_teams, lcs_team_ratings)
    lec_data = zip(LEC_teams, lec_team_ratings)

    return render_template('index.html', lck_data = lck_data, 
                                         lcs_data = lcs_data, 
                                         lec_data = lec_data)

if __name__ == '__main__': 
    app.run(debug = True)

