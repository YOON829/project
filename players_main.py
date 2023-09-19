import pymysql


conn = pymysql.connect(host='localhost', user='root', password='',
                       db='new_schema', charset='utf8')

curs = conn.cursor()

sql = "select * from new_schema.`stats21-22`"
curs.execute(sql)
rows_21_22 = curs.fetchall()

sql = "select * from new_schema.`stats22-23`"
curs.execute(sql)
rows_22_23 = curs.fetchall()

print(rows_21_22[1])
print(rows_22_23[1])



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



# player_stats_obj = [Player2122(id=row[0], player_Name=row[1], Nation=row[2], Position=row[3], Squad=row[4],
#                                        Age=row[5], Goals=row[6], Assist=row[7], Goal_Assist=row[8],
#                                        Goal_without_PK=row[9], Expected_Goals=row[10],
#                                        Expected_Goals_without_PK=row[11], Expected_Assist_Goal=row[12])
#                         for row in rows]

# player_stats_obj = []
# for row in rows:
#     if row[6] > 20 and row[7] > 5:
#         player_stats = Player2122(id=row[0], player_Name=row[1], Nation=row[2], Position=row[3], Squad=row[4],
#                                   Age=row[5], Goals=row[6], Assist=row[7], Goal_Assist=row[8],
#                                   Goal_without_PK=row[9], Expected_Goals=row[10],
#                                   Expected_Goals_without_PK=row[11], Expected_Assist_Goal=row[12])
#         player_stats_obj.append(player_stats)

# for obj in player_stats_obj:
#     print(f"Player Name: {obj.player_Name}, Goals: {obj.Goals}, Expected Goals: {obj.Expected_Goals}")






# def fetch_data_form_data_base():
#     conn = pymysql.connect(host='localhost', user='root', password='akrsod12',
#                            db='new_schema', charset='utf8')

#     curs = conn.cursor()



# conn.close()

# if __name__ == '__main__':
#     main()