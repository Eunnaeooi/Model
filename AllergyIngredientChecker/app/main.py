from fastapi import FastAPI
from pydantic import BaseModel
from app.data_loader import load_data
from app.ingredient_classifier import IngredientClassifier
from app.allergy_checker import AllergyIngredientChecker

app = FastAPI(title="Allergy Ingredient Checker API")

# 요청 데이터 모델 정의
class AllergyRequest(BaseModel):
    user_id: int
    recipe_id: int

# 데이터 로드 및 모델 초기화
Ingredient, Recipe_Ingredient, User_Ingredient = load_data()
classifier = IngredientClassifier('app/rules.pkl')
Ingredient_Label = classifier.generate_ingredient_label(Ingredient)
checker = AllergyIngredientChecker(
    ingredient_label=Ingredient_Label,
    recipe_ingredient=Recipe_Ingredient,
    user_ingredient=User_Ingredient,
    model_path='app/fasttext_model.model'
)

# 헬스 체크 API
@app.get("/")
def health_check():
    return {"status": "API is running smoothly!"}

# 알레르기 유발 가능성 체크 API
@app.post("/check_allergy")
def check_allergy(request: AllergyRequest):
    result = checker.find_similar_ingredients_by_category(request.user_id, request.recipe_id)
    return {"ingredient": result.tolist()}
