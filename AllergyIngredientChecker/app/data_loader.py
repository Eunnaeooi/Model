import pandas as pd
from sqlalchemy import create_engine
from app.config import host, port, user, password , database, charset

# SQLAlchemy 엔진 생성
engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset={charset}"
)

# 데이터 로드 함수 (MySQL에서 불러오기)
def load_data():
    Ingredient = pd.read_sql("SELECT * FROM Ingredient", engine)
    Recipe_Ingredient = pd.read_sql("SELECT * FROM Recipe_Ingredient", engine)
    User_Ingredient = pd.read_sql("SELECT * FROM User_Ingredient", engine)
    return Ingredient, Recipe_Ingredient, User_Ingredient




'''
import os

def load_data():
    DATA_PATH = "data/"
    INGREDIENT_PATH = os.path.join(DATA_PATH, "Ingredient.csv")
    RECIPE_INGREDIENT_PATH = os.path.join(DATA_PATH, "Recipe_Ingredient.csv")
    USER_INGREDIENT_PATH = os.path.join(DATA_PATH, "User_Ingredient.csv")

    Ingredient = pd.read_csv(INGREDIENT_PATH)
    Recipe_Ingredient = pd.read_csv(RECIPE_INGREDIENT_PATH)
    User_Ingredient = pd.read_csv(USER_INGREDIENT_PATH)

    return Ingredient, Recipe_Ingredient, User_Ingredient
    '''