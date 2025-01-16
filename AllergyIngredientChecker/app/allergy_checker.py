import pandas as pd
from gensim.models import FastText
from config import SIMILARITY_THRESHOLD, SAME_CLASS_WEIGHT, DIFF_CLASS_WEIGHT

class AllergyIngredientChecker:
    def __init__(self, ingredient_label, recipe_ingredient, user_ingredient, model_path):
        self.ingredient_label = ingredient_label
        self.recipe_ingredient = recipe_ingredient
        self.user_ingredient = user_ingredient
        self.fasttext_model = FastText.load(model_path)

    def calculate_weighted_similarity(self, recipe_ing, allergy_ing, recipe_class, allergy_class):
        if recipe_ing in self.fasttext_model.wv and allergy_ing in self.fasttext_model.wv:
            similarity = self.fasttext_model.wv.similarity(recipe_ing, allergy_ing)
            weight = SAME_CLASS_WEIGHT if recipe_class == allergy_class else DIFF_CLASS_WEIGHT
            return similarity * weight
        return 0

    def compare_ingredients(self, recipe_row, user_allergies):
        recipe_ing = recipe_row['ingredient']
        recipe_class = recipe_row['ingredient_classification']
        for _, allergy_row in user_allergies.iterrows():
            allergy_ing = allergy_row['ingredient']
            allergy_class = allergy_row['ingredient_classification']
            similarity = self.calculate_weighted_similarity(recipe_ing, allergy_ing, recipe_class, allergy_class)
            if similarity >= SIMILARITY_THRESHOLD:
                return recipe_ing
        return None

    def find_similar_ingredients_by_category(self, user_id, recipe_id):
        user_allergy_ids = self.user_ingredient[self.user_ingredient['user_id'] == user_id]['ingredient_id'].tolist()
        user_allergies = self.ingredient_label[self.ingredient_label['ingredient_id'].isin(user_allergy_ids)]
        recipe_ingredient_ids = self.recipe_ingredient[self.recipe_ingredient['recipe_id'] == recipe_id]['ingredient_id'].tolist()
        recipe_ingredients = self.ingredient_label[self.ingredient_label['ingredient_id'].isin(recipe_ingredient_ids)]
        similar_ingredients_list = [
            {'recipe_id': recipe_id, 'ingredient': matched_ing}
            for _, recipe_row in recipe_ingredients.iterrows()
            if (matched_ing := self.compare_ingredients(recipe_row, user_allergies))
        ]
        return pd.DataFrame(similar_ingredients_list)['ingredient'] if similar_ingredients_list else pd.Series([pd.NA], name='ingredient')
