import sqlite3

conn = sqlite3.connect('Test.db')
cursor_obj = conn.cursor()


def createTable(self):
    conn = sqlite3.connect('Test.db')
    cursor_obj = conn.cursor()
    cursor_obj.execute(
        "CREATE TABLE if not exists TESTED(DRYBULBTEMPF FLOAT,	WETBULBTEMPF FLOAT,DewPointTempF FLOAT,RelativeHumidity FLOAT,WindSpeed FLOAT,WindDirection INT,StationPressure FLOAT,SeaLevelPressure FLOAT,Precip STRING)");
    print("Table created successfully!")
    conn.close()


# cursor_obj.execute(" select * from TESTED")
# op = cursor_obj.fetchall()

# print(op)


def enterTable(self, DRYBULBTEMPF, WETBULBTEMPF, DewPointTempF, RelativeHumidity, WindSpeed, WindDirection,
               StationPressure, SeaLevelPressure, Precip):
    conn = sqlite3.connect('Test.db')
    cursor_obj = conn.cursor()
    cursor_obj.execute(
        "insert into TESTED values({} , {} , {} , {} , {} , {}  ,{} , {} , {} , {}".foramt(DRYBULBTEMPF, WETBULBTEMPF,
                                                                                           DewPointTempF,
                                                                                           RelativeHumidity, WindSpeed,
                                                                                           WindDirection,
                                                                                           StationPressure,
                                                                                           SeaLevelPressure, Precip))
    conn.close()