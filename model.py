import pickle
import pandas as pd

## Load the user recommendation model and sentiment classification model
import requests

recommendation_model = pd.read_pickle("./models/user_recommendation.pkl")
sentiment_model = pd.read_pickle("./models/sentiment_model.pkl")

def recommendation(user_name):

    Product_prediction = pd.DataFrame(recommendation_model.loc[user_name].sort_values(ascending=False)[0:20]).reset_index()
    Product_predct_senti = pd.merge(Product_prediction, sentiment_model, how='left', on=['name', 'name'])
    Res_df = Product_predct_senti.sort_values(by='Positive', ascending=False)[0:5]
    Res_df_final = Res_df['name'].to_frame()
    return Res_df_final

## function to check if the user_name is validate or not
def validate_user(user_name):

    if user_name in list(recommendation_model.index):
        return True
    else:
        return False

