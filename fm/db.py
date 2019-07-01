import sqlite3


class Database:
    '''
        Generic class to create, connect and execute queries on a sqlite
        database
    '''

    def __init__(self, dbName, dbPath, dataFile):
        self.dbName = dbName
        self.dbPath = dbPath
        self.dataFile = dataFile
        self.connection = None

    def createDatabaseFromDataFrame(self, tableName, dataFrame):
        if self.connection is None:
            self.connect()
        dataFrame.to_sql(name=tableName, if_exists='replace', con=self.connection)

    def connect(self):
        self.connection = sqlite3.connect(self.dbName)

        def make_dicts(cursor, row):
            return dict((cursor.description[idx][0], value)
                        for idx, value in enumerate(row))

        self.connection.row_factory = make_dicts

    def close(self):
        self.connection.close()

    def execute(self, query):
        '''
            Executes query and retruns response in dictionary format
        '''
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        return results
