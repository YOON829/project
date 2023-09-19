import pymysql

conn = pymysql.connect(host='localhost', user='root', password='akrsod12',
                       db='new_schema', charset='utf8')

curs = conn.cursor()

# SQL 쿼리 실행 (예: 목표가 20개 이상이고 어시스트가 5개 이상인 경우)
sql = "SELECT * FROM player_stats4 WHERE Goals >= 20 AND Assist >= 5"  # 필터링 조건을 수정하세요
curs.execute(sql)

# 데이터 가져오기
rows = curs.fetchall()

# Player2122 클래스 정의 (앞서 정의한 클래스 활용)
class Player2122:
    def __init__(self, id, player_Name, Nation, Position, Squad, Age, Goals, Assist, Goal_Assist,
                 Goal_without_PK, Expected_Goals, Expected_Goals_without_PK, Expected_Assist_Goal):
        self.id = id
        self.player_Name = player_Name
        self.Nation = Nation
        self.Position = Position
        self.Squad = Squad
        self.Age = Age
        self.Goals = Goals
        self.Assist = Assist
        self.Goal_Assist = Goal_Assist
        self.Goal_without_PK = Goal_without_PK
        self.Expected_Goals = Expected_Goals
        self.Expected_Goals_without_PK = Expected_Goals_without_PK
        self.Expected_Assist_Goal = Expected_Assist_Goal

# 데이터베이스에서 가져온 데이터를 Player2122 객체로 변환
player_stats_obj = []
for row in rows:
    player_stats = Player2122(id=row[0], player_Name=row[1], Nation=row[2], Position=row[3], Squad=row[4],
                              Age=row[5], Goals=row[6], Assist=row[7], Goal_Assist=row[8],
                              Goal_without_PK=row[9], Expected_Goals=row[10],
                              Expected_Goals_without_PK=row[11], Expected_Assist_Goal=row[12])
    player_stats_obj.append(player_stats)

for obj in player_stats_obj:
    print(f"Player Name: {obj.player_Name}, Goals: {obj.Goals}, Assist: {obj.Assist}")