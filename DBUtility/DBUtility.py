import pymysql
import psycopg2
import logging
import sqlite3
import datetime


class DropTable:
    def __init__(self, table_name):
        self.__table_name = table_name

    def execute(self):
        BasicOperator().commit("DROP TABLE {}".format(self.__table_name))


class FetchVenturesDealLeadsRecordAll:

    def execute(self):
        return BasicOperator().fetch_all(
            "SELECT * FROM nab_ventures_deals_leads LIMIT 5"
        )


class CreateVenturesDealLeadsIfNotExist:
    def execute(self):
        try:
            logging.getLogger().info("Initialize Ventures Deals Leads table")

            BasicOperator().commit("""
                    CREATE TABLE nab_ventures_deals_leads
                    (
                        person_name    VARCHAR(100)
                        deals_leads_date Date
                        number_of_leads Integer
                    ) ;
            """
                                   )
        except Exception as e:
            logging.getLogger().error("Initialize  Ventures Deals Leads table\
            failed. Please Check your connection")
            logging.getLogger().error(str(e))


class InsertVenturesDealLeadsRecord:
    def __init__(self, person_name, deals_leads_date, number_of_leads):

        self.__person_name = person_name
        self.__deals_leads_date = deals_leads_date
        self.__number_of_leads = number_of_leads

    def execute(self):
        BasicOperator().commit(
            "INSERT INTO nab_ventures_deals_leads \
            (person_name, deals_leads_date, number_of_leads) \
             VALUES ('{}','{}', '{}')".format(self.__person_name,
                                              self.__deals_leads_date,
                                              self.__number_of_leads)
            )


class FetchNABRecordAll:

    def execute(self):
        return BasicOperator().fetch_all(
            "SELECT * FROM nab_labs_initiatives_cycle LIMIT 5"
        )


class CreateNABTableIfNotExist:
    def execute(self):
        try:
            logging.getLogger().info("Initialize NAB Labs table")

            BasicOperator().commit("""
                    CREATE TABLE nab_labs_initiatives_cycle
                        (
                            initiative_name VARCHAR(200),
                            decision_made   VARCHAR(100),
                            reason          VARCHAR(200),
                            comments        VARCHAR(500),
                            experiment_flag VARCHAR(1),
                            experiment_date DATE,
                            hacks_flag      VARCHAR(1),
                            hacks_date      DATE,
                            poc_flag        VARCHAR(1),
                            poc_date        DATE,
                            incubated_flag  VARCHAR(1),
                            incubated_date  DATE,
                            exited_flag     VARCHAR(1),
                            exited_date     DATE,
                            system_date     timestamp
                        ) ;

            """
                                   )
        except Exception as e:
            logging.getLogger().error("Initialize NAB Labs table\
            failed. Please Check your connection")
            logging.getLogger().error(str(e))


class InsertNABTableRecord:
    def __init__(self, initiative_name, decision_made, reason,
                 comments, experiment_flag, experiment_date, hacks_flag,
                 hacks_date, poc_flag, poc_date, incubated_flag,
                 incubated_date, exited_flag, exited_date, system_date):

        self.__initiative_name = initiative_name
        self.__decision_made = decision_made
        self.__reason = reason
        self.__comments = comments
        self.__experiment_flag = experiment_flag
        self.__experiment_date = experiment_date
        self.__hacks_flag = hacks_flag
        self.__hacks_date = hacks_date
        self.__poc_flag = poc_flag
        self.__poc_date = poc_date
        self.__incubated_flag = incubated_flag
        self.__incubated_date = incubated_date
        self.__exited_flag = exited_flag
        self.__exited_date = exited_date
        self.__system_date = system_date

    def execute(self):
        BasicOperator().commit(
            "INSERT INTO nab_labs_initiatives_cycle \
            (initiative_name, decision_made, reason, \
             comments, experiment_flag, experiment_date, hacks_flag, \
             hacks_date, poc_flag, poc_date, incubated_flag, \
            incubated_date, exited_flag, exited_date, system_date) \
             VALUES ('{}','{}', '{}', '{}','{}', '{}', \
                    '{}','{}', '{}', '{}','{}', '{}', \
                    '{}','{}', '{}' )".format(self.__initiative_name,
                                              self.__decision_made,
                                              self.__reason,
                                              self.__comments,
                                              self.__experiment_flag,
                                              self.__experiment_date,
                                              self.__hacks_flag,
                                              self.__hacks_date,
                                              self.__poc_flag,
                                              self.__poc_date,
                                              self.__incubated_flag,
                                              self.__incubated_date,
                                              self.__exited_flag,
                                              self.__exited_date,
                                              self.__system_date)
            )


class CreateVenturesEngagementTableIfNotExist:
    def execute(self):
        try:
            logging.getLogger().info("Initialize Ventures engagement table.")

            BasicOperator().commit("""
                    CREATE TABLE nab_ventures_engagement_types
                        (
                            Engagement_type    VARCHAR(250)
                        ) ;
            """)
            BasicOperator().commit(
                """

                        INSERT INTO nab_ventures_engagement_types
                        VALUES 
                         ('Speaking Event'),
                         ('Event Attended'),
                         ('Board Meeting');

                """
            )
        except Exception as e:
            logging.getLogger().error("Initialize Ventures engagement table\
            failed. Please Check your connection")
            logging.getLogger().error(str(e))


class FetchVenturesEngagement:
    def execute(self):
        engagement_list = BasicOperator().fetch_all(
            "SELECT * FROM nab_ventures_engagement_types")

        return engagement_list


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

            BasicOperator().commit("""
                                      CREATE TABLE nab_ventures_events_board
                                    (
                                        event_conference_name    VARCHAR(250),             
                                        event_date         DATE,
                                        engagement_type          VARCHAR(50),
                                        notes_organiser          VARCHAR(250),
                                        location        VARCHAR(250),  
                                        country            VARCHAR(150),
                                        Quality               SMALLINT,
                                        audience      SMALLINT, 
                                        website_context          VARCHAR(250),  
                                        asset              VARCHAR(50),
                                        person_name        VARCHAR(250)   
                                    ) ;
                                  """)

        except Exception as e:
            logging.getLogger().error("Initialize nab ventures events board\
             table failed. Please Check your connection")
            logging.getLogger().error(str(e))


class InsertEventRecord:
    def __init__(self, event_conference_name,
                 event_date, engagement_type,
                 notes_organiser, location,
                 country, Quality, audience, website_context,
                 asset, person_name):
        self.__event_conference_name = event_conference_name
        self.__event_date = event_date
        self.__engagement_type = engagement_type
        self.__notes_organiser = notes_organiser
        self.__location = location
        self.__country = country
        self.__Quality = Quality
        self.__audience = audience
        self.__website_context = website_context
        self.__asset = asset
        self.__person_name = person_name

    def execute(self):
        BasicOperator().commit(
            "INSERT INTO nab_ventures_events_board \
            (event_conference_name, event_date, engagement_type,\
             notes_organiser, location, country, Quality, audience, \
             website_context, asset, person_name) \
             VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}',\
                     '{}', '{}', '{}', '{}')".format(self.__event_conference_name,
                                                     self.__event_date,
                                                     self.__engagement_type,
                                                     self.__notes_organiser,
                                                     self.__location,
                                                     self.__country,
                                                     self.__Quality,
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
            BasicOperator().commit("""
                                      CREATE TABLE nab_poc_status(
                                        poc_name VARCHAR(50),
                                        poc_status VARCHAR(50)  
                                      ) ;
                                  """)

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
            BasicOperator().commit("""
                                      CREATE TABLE nab_mobile_nps(
                                        date DATE,
                                        channel VARCHAR(50),
                                        score SMALLINT,         
                                        thoughts VARCHAR(250), 
                                        comments VARCHAR(250)  
                                      ) ;
                                  """ )

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




class CreateNPSTableIfNotExist:
    def execute(self):
        try:
            logging.getLogger().info("Initialize nab NPS table.")
            BasicOperator().commit("""
                                      CREATE TABLE nab_mobile_nps(
                                        date DATE,
                                        channel VARCHAR(50),
                                        score SMALLINT,         
                                        thoughts VARCHAR(250), 
                                        comments VARCHAR(250)  
                                      ) ;
                                  """ )

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

    
# ----------------------------------------


class CreateExecutionTableIfNotExist:
    def execute(self):
        try:
            logging.getLogger().info("Initialize nab execution table.")
            BasicOperator().commit("""
                                      CREATE TABLE nab_Partnership_executed_initiatives(
                                            initiative_name VARCHAR(150),
                                            initiative_short_description  VARCHAR(250),
                                            initiative_category VARCHAR(100),
                                            creation_date DATE,
                                            type  VARCHAR(100),
                                            stakeholder VARCHAR(50),
                                            execution VARCHAR(1),
                                            execution_date  Date,
                                            system_creation_date Timestamp
                                       ) ;
                                  """ )

        except Exception as e:
            logging.getLogger().error("Initialize nab execution table failed. Please check your connection")
            logging.getLogger().error(str(e))

class InsertExecutionRecord:
    def __init__(self, initiative_name, initiative_short_description, initiative_category, creation_date, type, stakeholder, execution, execution_date):
        self.__initiative_name = initiative_name
        self.__initiative_short_description = initiative_short_description
        self.__initiative_category = initiative_category
        self.__creation_date = creation_date
        self.__type = type
        self.__stakeholder = stakeholder
        self.__execution = execution
        self.__execution_date = execution_date
        self.__system_creation_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    def execute(self):
        BasicOperator().commit(
            "INSERT INTO nab_Partnership_executed_initiatives \
            (initiative_name, initiative_short_description, initiative_category, creation_date, type, stakeholder, team_recommendation, execution, execution_date, endorsement_body, system_creation_date) \
             VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.__initiative_name,
                                                            self.__initiative_short_description,
                                                            self.__initiative_category,
                                                            self.__creation_date,
                                                            self.__type,
                                                            self.__stakeholder,
                                                            self.__execution,
                                                            self.__execution_date,
                                                            self.__system_creation_date)
            )

class FetchExecutionRecordAll:

    def execute(self):
        return BasicOperator().fetch_all(
            "SELECT * FROM nab_Partnership_executed_initiatives "
        )

class FetchExecutionRecordRecent:

    def execute(self):
        return BasicOperator().fetch_all(
            "SELECT top 10 * FROM nab_Partnership_executed_initiatives order by system_creation_date DESC"
        )



# -----------------------------------------------------------

class CreateEndorsementTableIfNotExist:
    def execute(self):
        try:
            logging.getLogger().info("Initialize nab endorsement table.")
            BasicOperator().commit("""
                                      CREATE TABLE nab_Partnership_endorsed_initiatives(
                                            initiative_name VARCHAR(150),
                                            initiative_short_description  VARCHAR(250),
                                            initiative_category VARCHAR(100),
                                            creation_date DATE,
                                            type  VARCHAR(100),
                                            stakeholder VARCHAR(50),
                                            team_recommendation VARCHAR(5),
                                            endorsement VARCHAR(1),
                                            endorsement_date  Date,
                                            endorsement_body  VARCHAR(200),
                                            system_creation_date Timestamp
                                       ) ;
                                  """ )

        except Exception as e:
            logging.getLogger().error("Initialize nab endorsement table failed. Please check your connection")
            logging.getLogger().error(str(e))

class InsertEndorsementRecord:
    def __init__(self, initiative_name, initiative_short_description, initiative_category, creation_date, type, stakeholder, team_recommendation, endorsement, endorsement_date, endorsement_body):
        self.__initiative_name = initiative_name
        self.__initiative_short_description = initiative_short_description
        self.__initiative_category = initiative_category
        self.__creation_date = creation_date
        self.__type = type
        self.__stakeholder = stakeholder
        self.__team_recommendation = team_recommendation
        self.__endorsement = endorsement
        self.__endorsement_date = endorsement_date
        self.__endorsement_body = endorsement_body
        self.__system_creation_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    def execute(self):
        BasicOperator().commit(
            "INSERT INTO nab_Partnership_endorsed_initiatives \
            (initiative_name, initiative_short_description, initiative_category, creation_date, type, stakeholder, team_recommendation, endorsement, endorsement_date, endorsement_body, system_creation_date) \
             VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.__initiative_name,
                                                            self.__initiative_short_description,
                                                            self.__initiative_category,
                                                            self.__creation_date,
                                                            self.__type,
                                                            self.__stakeholder,
                                                            self.__team_recommendation,
                                                            self.__endorsement,
                                                            self.__endorsement_date,
                                                            self.__endorsement_body,
                                                            self.__system_creation_date)
            )

class FetchEndorsementRecordAll:

    def execute(self):
        return BasicOperator().fetch_all(
            "SELECT * FROM nab_Partnership_endorsed_initiatives "
        )

class FetchEndorsementRecordRecent:

    def execute(self):
        return BasicOperator().fetch_all(
            "SELECT top 10 * FROM nab_Partnership_endorsed_initiatives order by system_creation_date DESC"
        )



  
    
    

class BasicOperator:
    @staticmethod
    def fetch_all(query_string):
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(query_string)
            result = cursor.fetchall()

        return result

    @staticmethod
    def fetch_one(query_string):
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(query_string)
            result = cursor.fetchone()

        return result

    @staticmethod
    def commit(query_string):
        with DBConnection() as connection:
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
        self.connection = psycopg2.connect(
            host=DBConnection.__host,
            port=DBConnection.__port,
            user=DBConnection.__user,
            password=DBConnection.__password,
            database=DBConnection.__database
            #,
            #cursorclass=pymysql.cursors.DictCursor
        )
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
