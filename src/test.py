import psycopg2


def create_db_employers_vacancy():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="9530",
        host="localhost"
    )
    cursor = conn.cursor()
    cursor.execute(f'DROP DATABASE IF EXISTS EMPLOYERS_VACANCY')
    conn.autocommit = True
    # команда для создания базы данных metanit
    sql = "CREATE DATABASE EMPLOYERS_VACANCY"
    # выполняем код sql
    cursor.execute(sql)
    print("База данных успешно создана")

    cursor.close()
    conn.close()


def fill_table_employers(employers):
    conn = psycopg2.connect(
        dbname="employers_vacancy",
        user="postgres",
        password="9530",
        host="localhost"
    )

    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS employers")
    conn.commit()
    cursor.execute("CREATE TABLE employers(employee_id VARCHAR(100) PRIMARY KEY NOT NULL, company_name VARCHAR(100)"
                   "NOT NULL, type VARCHAR(100) NOT NULL,area VARCHAR(100), open_vacancies VARCHAR(100) NOT NULL);")
    conn.commit()
    for row in employers:
        print(row)
        query = (f"INSERT INTO employers (employee_id, company_name, type, area, open_vacancies) VALUES (%s, %s, %s, "
                 f"%s, %s)")
        print(query)
        cursor.execute(query, row)

    conn.commit()
    cursor.close()
    conn.close()


# create_db_employers_vacancy()

a = [('174070', 'Яндекс', 'company', 'Москва', '1270')]
fill_table_employers(a)
