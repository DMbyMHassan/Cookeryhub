from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# configurations
app.config['UPLOAD_FOLDER'] = 'static/images'

''' Load the recipes data from into pandas DataFrame'''
csv_file = 'recipes.csv'
df_recipes = pd.read_csv(csv_file)


@app.route('/')
def homepage():
    return render_template('hmomepage.html')


@app.route('/recipes')
# test line to check git hub
def recipes():
    return render_template('recipes.html', recipes=df_recipes.to_dict(orient='records'))


@app.route('/upload', methods=['GET', 'POST'])
def uplod_form():
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        ingredients = request.form['ingredients']
        preparation_instructions = request.form['preperation_instructions']
        serving_instructions = request.form['serving_instrucyios']
        image = request.files['image']
        """Validation the form data and process the image upload"""
        if recipe_name and ingredients and preparation_instructions and serving_instructions and image:
            image.save(os.path.join(app.config['UPLOAD_FOLDER']))
            new_recipe = {
                'Recipe_Name': recipe_name,
                'Preparation_Instructions': preparation_instructions,
                'Serving_Instructions' :serving_instructions,
                'Image_URL': f'static/images/{image.filename}'
            }
            df_recipes.append(new_recipe,ignore_index =True)
            df_recipes.to_csv(csv_file,index=False)
        return
    else:
        return


if __name__ == '__main__':
    app.run(debug=True)
