# aws MySQL 연결 정보
host = "reciguard-db.czouas0eqnqo.ap-northeast-2.rds.amazonaws.com"
port = 3306
user = 'reciguard'
password = 'tavereciguard'
database = 'reciguard'
charset = 'utf8mb4'

'''
# MySQL 연결 정보
host = 'localhost'
port = 3306
user = 'root'
password = 'danchoo12'
database = 'RECIGUARD'
charset = 'utf8mb4'
'''

# 하이퍼파라미터
WEIGHT_CUISINE = 0.5
WEIGHT_FOODTYPE = 0.3
WEIGHT_COOKINGSTYLE = 0.2

TIME_WEIGHT = 0.3
DECAY_RATE = 7
SIMILARITY_THRESHOLD = 0.15

HYBRID_WEIGHT = 0.7
