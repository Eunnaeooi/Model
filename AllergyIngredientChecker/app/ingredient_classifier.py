import pickle

class IngredientClassifier:
    def __init__(self, rules_path):
        with open(rules_path, 'rb') as file:
            self.rules = pickle.load(file)

    def classify_ingredient(self, ingredient):
        sorted_rules = {category: sorted(keywords, key=len, reverse=True) for category, keywords in self.rules.items()}
        matched_category, max_match_length = None, 0
        for category, keywords in sorted_rules.items():
            for keyword in keywords:
                if keyword in ingredient and len(keyword) > max_match_length:
                    matched_category, max_match_length = category, len(keyword)
        return matched_category if matched_category else "기타"

    def generate_ingredient_label(self, Ingredient):
        Ingredient["ingredient_classification"] = Ingredient["ingredient"].apply(self.classify_ingredient)
        return Ingredient[Ingredient['ingredient_classification'].notna()]