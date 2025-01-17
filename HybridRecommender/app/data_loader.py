import pandas as pd
from sqlalchemy import create_engine
import cryptography
from app.config import host, port, user, password, database, charset

# SQLAlchemy 엔진 생성
engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset={charset}"
)

def load_data():
    
    Recipe = pd.read_sql("SELECT * FROM recipe", engine)
    User_Cuisine = pd.read_sql_query("SELECT * FROM user_cuisine", engine)
    User_FoodType = pd.read_sql_query("SELECT * FROM user_foodtype", engine)
    User_CookingStyle = pd.read_sql_query("SELECT * FROM user_cookingstyle", engine)
    User_Scrap = pd.read_sql_query("SELECT * FROM user_scrap", engine)
    
    return Recipe, User_Cuisine, User_FoodType, User_CookingStyle, User_Scrap


'''
import os

def load_data():
    
    DATA_PATH = "data/"
    Recipe_PATH = os.path.join(DATA_PATH, "Recipe.csv")
    User_Cuisine_PATH = os.path.join(DATA_PATH, "User_Cuisine.csv")
    User_FoodType_PATH = os.path.join(DATA_PATH, "User_FoodType.csv")
    User_CookingStyle_PATH = os.path.join(DATA_PATH, "User_CookingStyle.csv")
    User_Scrap_PATH = os.path.join(DATA_PATH, "User_Scrap.csv")

    Recipe = pd.read_csv(Recipe_PATH)
    User_Cuisine = pd.read_csv(User_Cuisine_PATH)
    User_FoodType = pd.read_csv(User_FoodType_PATH)
    User_CookingStyle = pd.read_csv(User_CookingStyle_PATH)
    User_Scrap = pd.read_csv(User_Scrap_PATH)
    
    return Recipe, User_Cuisine, User_FoodType, User_CookingStyle, User_Scrap
'''
