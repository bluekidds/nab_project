import pymysql
import logging
import sqlite3

SQL_Schema = """
                    CREATE TABLE nab_ventures_events_board(
                      event_conference_name VARCHAR(250),                
                      board_meeting VARCHAR(1),     
                      event_date DATE,
                      speaker VARCHAR(50),
                      notes_organiser VARCHAR(250), 
                      country VARCHAR(150),
                      audience SMALLINT,         
                      website_context VARCHAR(250), 
                      asset VARCHAR(50),
                      person_name VARCHAR(250)  
                    ) ;
                """


class CreateVenturesTeamTableIfNotExist:
    def execute(self):
        try:
            logging.getLogger().info("Initialize Ventures team table.")

            BasicOperator().commit("""
                    CREATE TABLE NAB_VENTURES_TEAM
                        (
                            person_name    VARCHAR(100)
                        ) ;
            """)

        except Exception as e:
            logging.getLogger().error("Initialize NAB Deals table\
            failed. Please Check your connection")
            logging.getLogger().error(str(e))


class CreateDealsTableIfNotExist:
    def execute(self):
        try:
            logging.getLogger().info("Initialize NAB Deals table.")

            BasicOperator().commit("""
                    CREATE TABLE nab_deals_events_board(
                      event_date DATE,
                      company_name VARCHAR(250),                
                      invested_in VARCHAR(250),     
                      speaker VARCHAR(50),
                      notes_organiser VARCHAR(250), 
                      country VARCHAR(150),
                      audience SMALLINT,         
                      website_context VARCHAR(250), 
                      asset VARCHAR(50),
                      person_name VARCHAR(250)  
                    ) ;
                """)

        except Exception as e:
            logging.getLogger().error("Initialize NAB Deals table\
            failed. Please Check your connection")
            logging.getLogger().error(str(e))

class CreateDealsTableIfNotExist:
    def execute(self):
        try:
            logging.getLogger().info("Initialize NAB Deals table.")

            BasicOperator().commit("""
                    CREATE TABLE nab_deals_events_board(
                      event_date DATE,
                      company_name VARCHAR(250),                
                      invested_in VARCHAR(250),     
                      speaker VARCHAR(50),
                      notes_organiser VARCHAR(250), 
                      country VARCHAR(150),
                      audience SMALLINT,         
                      website_context VARCHAR(250), 
                      asset VARCHAR(50),
                      person_name VARCHAR(250)  
                    ) ;
                """)

        except Exception as e:
            logging.getLogger().error("Initialize NAB Deals table\
            failed. Please Check your connection")
            logging.getLogger().error(str(e))


class CreateEventsTableIfNotExist:
    def execute(self):
        try:
            logging.getLogger().info("Initialize nab ventures events board table.")

            BasicOperator().commit(SQL_Schema)

        except Exception as e:
            logging.getLogger().error("Initialize nab ventures events board\
             table failed. Please Check your connection")
            logging.getLogger().error(str(e))


class InsertEventRecord:
    def __init__(self, event_conference_name, board_meeting,
                 event_date, speaker,
                 notes_organiser, country, audience, website_context,
                 asset, person_name):
        self.__event_conference_name = event_conference_name
        self.__board_meeting = board_meeting
        self.__event_date = event_date
        self.__speaker = speaker
        self.__notes_organiser = notes_organiser
        self.__country = country
        self.__audience = audience
        self.__website_context = website_context
        self.__asset = asset
        self.__person_name = person_name

    def execute(self):
        BasicOperator().commit(
            "INSERT INTO nab_ventures_events_board \
            (event_conference_name, board_meeting, event_date, \
             speaker, notes_organiser, country, audience, \
             website_context, asset, person_name) \
             VALUES ('{}', '{}', '{}', '{}', '{}', '{}',\
                     '{}', '{}', '{}', '{}')".format(self.__event_conference_name,
                                                     self.__board_meeting,
                                                     self.__event_date,
                                                     self.__speaker,
                                                     self.__notes_organiser,
                                                     self.__country,
                                                     self.__audience,
                                                     self.__website_context,
                                                     self.__asset,
                                                     self.__person_name)
            )


class FetchEventsRecordAll:

    def execute(self):
        return BasicOperator().fetch_all(
            "SELECT * FROM nab_ventures_events_board "
        )


class FetchEventsRecordWithinSamePerson:
    def __init__(self, person_name):
        self.__person_name = person_name

    def execute(self):
        return BasicOperator().fetch_all(
            "SELECT * FROM nab_ventures_events_board WHERE \
            person_name='{}'".format(self.__person_name)
        )


class FetchEventsLatestRecordWithSamePerson:

    def execute(self):
        sql_query = \
            "SELECT t.event_conference_name, t.person_name, t.event_date \
             FROM nab_ventures_events_board t \
             INNER JOIN( SELECT person_name, max(event_date) as MaxDate \
             from nab_ventures_events_board \
             group by person_name \
             ) tm on t.person_name = tm.person_name and t.event_date = tm.MaxDate"

        return BasicOperator().fetch_all(sql_query)


class BasicOperator:
    @staticmethod
    def fetch_all(query_string):
        with DBSQLiteConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(query_string)
            result = cursor.fetchall()

        return result

    @staticmethod
    def fetch_one(query_string):
        with DBSQLiteConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(query_string)
            result = cursor.fetchone()

        return result

    @staticmethod
    def commit(query_string):
        with DBSQLiteConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(query_string)
            connection.commit()


class DBSQLiteConnection:
    __dbfile = str()

    @staticmethod
    def configure_connection_information(dbfile):
        DBSQLiteConnection.__dbfile = dbfile

    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(
            self.__dbfile
        )
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


class DBConnection:
    __host = str()
    __port = int()
    __user = str()
    __password = str()
    __database = str()

    @staticmethod
    def configure_connection_information(host, port, user, password, database):
        DBConnection.__host = host
        DBConnection.__port = port
        DBConnection.__user = user
        DBConnection.__password = password
        DBConnection.__database = database

    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = pymysql.connect(
            host=DBConnection.__host,
            port=DBConnection.__port,
            user=DBConnection.__user,
            password=DBConnection.__password,
            db=DBConnection.__database,
            cursorclass=pymysql.cursors.DictCursor
        )
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
