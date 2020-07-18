import pandas as pd
from bokeh.plotting import figure, output_file, show, output_notebook

#fonction pour creer le dashbord
def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)

#importer les données sur internet
links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',\
       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}

#lire le fichier  GDP.csv
path_gdp=links['GDP']
gdp=pd.read_csv(path_gdp) # read
#convertir en un DataFrame (un tableau pour facilliter l'accès au données)
print('le tableau de données GDP -US :')
gdp=pd.DataFrame(gdp)
gdp.head() # affiche que 5 lignes
print(gdp[0:40])

#lire le fichier  unemployment.csv
path_unemployment=links['unemployment']
unemployment=pd.read_csv(path_unemployment)
#convertir le fichier csv en un tableau de données
print('le tableau qui montre le taux du chômage -US :')
unemployment=pd.DataFrame(unemployment)
unemployment.head() #head shwos only 5 rows
print(unemployment[0:40])

#unemployment > 8,5 / affichier le taux de chômage le plus élevé
greater_unemployment=unemployment[unemployment['unemployment']>8.5]
print('le taux de chômage le plus élevé > 8.5% :\n',greater_unemployment)

#extraire le les données de la colonne 'change_current'
print('extraire les données de la colonne -change_current- :')
gdp_change =gdp.loc[:,'change-current'] # Create your dataframe with column change-current
gdp_change.head()
print(gdp_change[0:40])

#extraire le les données de la colonne 'unmeployment'
print('extraire les données de la colonne -unemployment- :')
unemployment =unemployment.loc[:,'unemployment']
unemployment.head()
print(unemployment[0:40])

#extraire le les données de la colonne 'date'
print('extraire les données de la colonne -unemployment- :')
x =gdp.loc[:,'date']# Create your dataframe with column date
x.head()
print(x[0:40])


title ='Analyzing US Economic Data and Building a Dashboard \n realized by :\n --KADI koussaila' # Give your dashboard a string title
file_name = "index.html"
#appel à la fonction pour creer le fichier html
make_dashboard(x, gdp_change, unemployment, title, file_name)

