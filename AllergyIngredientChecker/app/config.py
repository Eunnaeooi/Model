# MySQL 연결 정보
host = 'localhost'
port = 3306
user = 'root'
password = 'danchoo12'
database = 'RECIGUARD'
charset = 'utf8mb4'

# FastText 모델 하이퍼파라미터
VECTOR_SIZE = 300
WINDOW_SIZE = 5
MIN_COUNT = 1
SG = 1
EPOCHS = 10

# 하이퍼파라미터
SIMILARITY_THRESHOLD = 0.15
SAME_CLASS_WEIGHT = 1.4
DIFF_CLASS_WEIGHT = 0.7