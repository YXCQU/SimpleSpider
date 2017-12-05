import pymysql


def mysql_insert(sql_data):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='lagou', charset='utf8')
    cursor = conn.cursor()
    insert_sql = """INSERT INTO lagou(companyId,positionName,workYear,education,jobNature,positionId,createTime,
    city,industryField,positionAdvantage,salary,companySize,score,companyFullName, financeStage) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    try:
        for item in sql_data:
            cursor.execute(insert_sql, item)
            conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    sql_data = [
        ["11111111", "11111111", "11111111", "11111111", "11111111", "11111111", "11111111", "11111111", "11111111",
         "11111111",
         "11111111", "11111111", "", None, "11111111"]]
    mysql_insert(sql_data)
