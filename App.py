from flask impotr Flask
import pandas as pd
import os

app = Flask(__name__)

#configurations
app.config['UPLOA_FOLDER'] ='static/images'

''' Load the recipes data from into pandas DataFrame'''
csv_file = 'recipes.csv'
df_recipes =pd.read_csv(csv_file)

def hompage():
    return render_template('hmomepage.html')

#test line to check git hub
def recipes():
    return render_template('recipes.html')

def uplod_form():
    if
        return
    else:
        return

if __name__ == '__main__':
    app.run()