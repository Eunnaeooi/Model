from gensim.models import FastText
from config import VECTOR_SIZE, WINDOW_SIZE, MIN_COUNT, SG, EPOCHS

def train_fasttext_model(Ingredient_Label, model_path):
    ingredient_sentences = Ingredient_Label['ingredient'].astype(str).apply(lambda x: [x]).tolist()
    model = FastText(sentences=ingredient_sentences, 
                     vector_size=VECTOR_SIZE, 
                     window=WINDOW_SIZE, 
                     min_count=MIN_COUNT, 
                     sg=SG, 
                     epochs=EPOCHS)
    model.save(model_path)
