from app.content_recommender import ContentBasedRecommenderEmbedding
from app.collaborative_filtering import UserBasedCollaborativeFiltering
from app.config import HYBRID_WEIGHT
import pandas as pd

class HybridRecommender:
    def __init__(self, hybrid_weight=HYBRID_WEIGHT):
        self.hybrid_weight = hybrid_weight
        self.content_model = ContentBasedRecommenderEmbedding()
        self.collab_model = UserBasedCollaborativeFiltering()

    def recommend(self, user_id, User_Cuisine, User_FoodType, User_CookingStyle, User_Scrap, Recipe):
        # 콘텐츠 기반 추천 점수 계산
        content_scores = self.content_model.recommend(user_id, User_Cuisine, User_FoodType, User_CookingStyle, Recipe)
        
        # 협업 필터링 추천 점수 계산
        collab_scores = self.collab_model.recommend(user_id, User_Cuisine, User_FoodType, User_CookingStyle, User_Scrap, Recipe)

        # 점수 병합 및 최종 점수 계산
        combined_scores = content_scores.merge(collab_scores, on='recipe_id', how='outer').fillna(0)
        combined_scores['final_score'] = (combined_scores['content_score'] * self.hybrid_weight +
                                          combined_scores['collab_score'] * (1 - self.hybrid_weight))

        # 중복 제거 및 점수 기준 정렬
        combined_scores = combined_scores.drop_duplicates(subset='recipe_id')
        combined_scores_sorted = combined_scores.sort_values(by='final_score', ascending=False).reset_index(drop=True)

        # 최상위 레시피 추천
        return combined_scores_sorted.iloc[0]['recipe_id']
    