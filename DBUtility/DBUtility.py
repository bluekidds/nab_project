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

SQL_Schema_nps = """
                    CREATE TABLE nab_mobile_nps(
                      date DATE,
                      channel VARCHAR(50),
                      score SMALLINT,         
                      thoughts VARCHAR(250), 
                      comments VARCHAR(250)  
                    ) ;
                """ 

SQL_Schema_poc = """
                    CREATE TABLE nab_poc_status(
                      poc_name VARCHAR(50),
                      poc_status VARCHAR(50)  
                    ) ;
                """    

class DropTable:
    def __init__(self, table_name):
        self.__table_name = table_name

    def execute(self):
        BasicOperator().commit("DROP TABLE {}".format(self.__table_name))



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
            BasicOperator().commit(
                """

                        INSERT INTO NAB_VENTURES_TEAM 
                        VALUES 
                         ( 'Todd Forest'),
                         ('Melissa Widner'),
                         ( 'Lucinda Hankin'),
                         ( 'Jaquelyne Vulligns') ;

                """
            )
        except Exception as e:
            logging.getLogger().error("Initialize Ventures team table\
            failed. Please Check your connection")
            logging.getLogger().error(str(e))


class CreateDealsLeverageTableIfNotExist:

    @staticmethod
    def execute():
        try:
            logging.getLogger().info("Initialize NAB Done Leverage \
            Deals table.")

            BasicOperator().commit("""
                    CREATE TABLE nab_ventures_deals_leveraged(
                         company_name            VARCHAR(250),
                         deal_dleveraged_Date    DATE,
                         leverage_desc           VARCHAR(1000)
                    ) ;
                """)

        except Exception as e:
            logging.getLogger().error("Initialize NAB Done Leverage \
            Deals table\
            failed. Please Check your connection")
            logging.getLogger().error(str(e))


class InsertDealLeverageRecord:
    def __init__(self, date, company_name,
                 leverage_desc):

        self.__date = date
        self.__company_name = company_name
        self.__leverage_desc = leverage_desc

    def execute(self):
        BasicOperator().commit(
            "INSERT INTO nab_ventures_deals_leveraged \
            (deal_dleveraged_Date, company_name, leverage_desc) \
             VALUES ('{}','{}', '{}')".format(self.__date,
                                              self.__company_name,
                                              self.__leverage_desc)
            )


class FetchDealsLeverageRecordLastThree:

    def execute(self):
        return BasicOperator().fetch_all(
            "SELECT * FROM nab_ventures_deals_leveraged ORDER BY \
             deal_dleveraged_Date DESC LIMIT 5"
        )


class CreateDealsTableIfNotExist:

    @staticmethod
    def execute():
        try:
            logging.getLogger().info("Initialize NAB Done Deals table.")

            BasicOperator().commit("""
                    CREATE TABLE nab_deals_events_board(
                        company_name    VARCHAR(250),
                        deal_done_Date  DATE,
                        invested_in     VARCHAR(1000),
                        aud_invested    REAL
                    ) ;
                """)

        except Exception as e:
            logging.getLogger().error("Initialize NAB Done Deals table\
            failed. Please Check your connection")
            logging.getLogger().error(str(e))


class InsertDealDoneRecord:
    def __init__(self, date, company_name,
                 invested_in, invested):

        self.__date = date
        self.__company_name = company_name
        self.__invested_in = invested_in
        self.__invested = invested

    def execute(self):
        BasicOperator().commit(
            "INSERT INTO nab_deals_events_board \
            (deal_done_Date, company_name, invested_in, aud_invested) \
             VALUES ('{}','{}', '{}', '{}')".format(self.__date,
                                                          self.__company_name,
                                                          self.__invested_in,
                                                          self.__invested)
            )


class FetchDealsDoneRecordLastThree:

    def execute(self):
        return BasicOperator().fetch_all(
            "SELECT * FROM nab_deals_events_board ORDER BY \
             deal_done_Date DESC LIMIT 5"
        )


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


class InsertVenturesPerson:
    def __init__(self, person):
        self.__person = person

    def execute(self):
        BasicOperator().commit(
            "INSERT INTO NAB_VENTURES_TEAM values \
            ('{}')".format(self.__person)
        )


class FetchVenturesPerson:
    def execute(self):
        team_list = BasicOperator().fetch_all(
            "SELECT * FROM NAB_VENTURES_TEAM")

        return team_list


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


class CreatePOCTableIfNotExist:
    def execute(self):
        try:
            logging.getLogger().info("Initialize nab POC table.")
            BasicOperator().commit(SQL_Schema_poc)

        except Exception as e:
            logging.getLogger().error("Initialize nab POC table failed. Please check your connection")
            logging.getLogger().error(str(e))


class InsertPOCRecord:
    def __init__(self, poc_name, poc_status):
        self.__poc_name = poc_name
        self.__poc_status = poc_status

    def execute(self):
        BasicOperator().commit(
            "INSERT INTO nab_poc_status \
            (poc_name, poc_status) \
             VALUES ('{}', '{}')".format(self.__poc_name,
                                         self.__poc_status))

class UpdatePOCRecord:
    def __init__(self, poc_name, new_status):
        self.__poc_name = poc_name
        self.__new_status = new_status

    def execute(self):
        BasicOperator().commit(
            "UPDATE nab_poc_status \
             SET poc_status = '{}' \
             WHERE poc_name = '{}'".format(self.__new_status,
                                         self.__poc_name))

class GetPOCStatus:
    def __init__(self, poc_name):
        self.__poc_name = poc_name

    def execute(self):
        return BasicOperator().fetch_one(
            "SELECT poc_status FROM nab_poc_status WHERE poc_name = '{}'".format(self.__poc_name)
        )[0]


class FetchPOCRecordAll:

    def execute(self):
        return BasicOperator().fetch_all(
            "SELECT * FROM nab_poc_status "
        )


class CreateNPSTableIfNotExist:
    def execute(self):
        try:
            logging.getLogger().info("Initialize nab NPS table.")
            BasicOperator().commit(SQL_Schema_nps)

        except Exception as e:
            logging.getLogger().error("Initialize nab NPS table failed. Please check your connection")
            logging.getLogger().error(str(e))

class InsertNPSRecord:
    def __init__(self, date, channel, score, thoughts, comments):
        self.__date = date
        self.__channel = channel
        self.__score = score
        self.__thoughts = thoughts
        self.__comments = comments

    def execute(self):
        BasicOperator().commit(
            "INSERT INTO nab_mobile_nps \
            (date, channel, score, thoughts, comments) \
             VALUES ('{}', '{}', '{}', '{}', '{}')".format(self.__date,
                                                      self.__channel,
                                                      self.__score,
                                                      self.__thoughts,
                                                      self.__comments)
            )

class FetchNPSRecordAll:

    def execute(self):
        return BasicOperator().fetch_all(
            "SELECT * FROM nab_mobile_nps "
        )




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
