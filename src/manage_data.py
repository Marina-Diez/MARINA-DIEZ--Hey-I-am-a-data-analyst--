import pandas as pd
from src.config import collection

def carga_data():
    data = pd.read_csv("Output/Abb_NY_clean_output.csv")
    return data

def grafico_barras_st():
    data = carga_data()
    data = data.groupby("neighbourhood_group").agg({"neighbourhood_group":'count'}).rename(columns={"neighbourhood_group":"character_name", "neighbourhood_group":"number of reservations"}).reset_index().set_index("neighbourhood_group", drop=True)
    return data

def lista_bh():
    data = carga_data()
    return list(data.neighbourhood_group.unique())

def grafico(neighbourhood):
    data = carga_data()
    data = data[(data["neighbourhood_group"] == f"{neighbourhood}")]
    return data