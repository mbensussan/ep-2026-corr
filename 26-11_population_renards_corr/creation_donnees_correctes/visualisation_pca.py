# programme pour afficher la géométrie des données car je suspecte que le
# jeu de données est incorrect en raison des résultats foireux obtenus à la
# dernière question : quelque soit la valeur de k le diagnostic est présence de
# renard.
# Conclusion après visualisation : les données sont pourries, on n'arrive pas
# à distinguer des nuages de points séparés. Il faut générer de nouvelles
# données.

# https://plotly.com/python/pca-visualization/

from donnees_habitats_original_foireux import zones_connues
import plotly.express as px
import pandas as pd
from sklearn.decomposition import PCA

def visualisation(habitats, composantes_principales=False):
    """Prend en paramètre une liste de dictionnaires. Chaque dictionnaire
    a pour clé des noms de variables et pour valeurs les valeurs respectives
    associées. La variable expliquée doit être placée en dernier et les
    variables explicatives en premier. Ouvre une fenêtre dans le navigateur
    Web pour affficher la représentation matricielle des graphiques par
    couple de variables explicatives ou par couple de composantes principales
    si le paramètre composantes_principales est choisi à True."""
    df = pd.DataFrame(habitats)
    variables_explicatives = df.columns[:-1] # tout sauf la varibale expliquée
    variable_expliquee = df.columns[-1] # variable expliquée (ici présence renard)
    if not composantes_principales:
        # figure à partir des variables explicatives
        fig = px.scatter_matrix(
            df,
            dimensions=variables_explicatives,
            color=variable_expliquee
        )
        fig.update_traces(diagonal_visible=False)
        fig.show()
    else:
        # figure à partir des composantes principales
        pca = PCA()
        components = pca.fit_transform(df[variables_explicatives])
        labels = {
            str(i): f"PC {i+1} ({var:.1f}%)"
            for i, var in enumerate(pca.explained_variance_ratio_ * 100)
        }
        fig = px.scatter_matrix(
            components,
            labels=labels,
            dimensions=range(4),
            color=df[variable_expliquee]
        )
        fig.update_traces(diagonal_visible=False)
        fig.show()


if __name__ == '__main__':
    visualisation(zones_connues)
    visualisation(zones_connues, composantes_principales=True)