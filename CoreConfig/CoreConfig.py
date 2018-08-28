import configparser
import sys
import os


class ApplicationDirPathGetter:
    def execute(self):
        if getattr(sys, 'frozen', False):
            application_path = sys.executable

        elif hasattr(sys.modules['__main__'], "__file__"):
            application_path = os.path.abspath(sys.modules['__main__'].__file__)

        else:
            application_path = sys.executable

        return os.path.dirname(application_path)


class CoreConfig:
    __configs = None

    @staticmethod
    def initialize_core_config():
        CoreConfig.__configs = configparser.RawConfigParser()
        CoreConfig.__configs.read("NAB_form.ini")


    @staticmethod
    def get_db_connection_info():
        return {
            "host": CoreConfig.__configs.get("DB", "host"),
            "port": CoreConfig.__configs.getint("DB", "port"),
            "user": CoreConfig.__configs.get("DB", "user"),
            "password": CoreConfig.__configs.get("DB", "password"),
            "database": CoreConfig.__configs.get("DB", "database")
        }

    @staticmethod
    def get_sqlite3_db_connection_info():
        return {
            "dbfile": CoreConfig.__configs.get("DB", "dbfile")
        }

