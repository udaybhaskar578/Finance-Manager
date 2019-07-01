from . import db
from . import data_processor
from . import utils, const, queries
import logging


class FinanceManager:
    def __init__(self):
        logging.basicConfig(
            format='%(asctime)s [%(levelname).4s] %(message)s',
            filename='app.log',
            level=logging.INFO)
        self.logger = logging.getLogger('FM')

        # Database details
        self._database = const.DATABASE
        self._dbName = const.DB_NAME
        self._dataFile = const.DATA_FILE
        self._tableName = const.TABLE_NAME

        self.logger.info('Creating database %s at %s' % (self._dbName, self._database))
        self.database = db.Database(self._dbName, self._database, self._dataFile)
        self.createDatabase()
        self.database.connect()

    def __del__(self):
        self.database.close()

    def createDatabase(self):
        if not utils.fileExists(self._database):
            self.logger.info(
                'DB %s does not exists. Creating DB' % self._database)
            dfTransactions = data_processor.DataProcessor(self._dbName)
            dfTransactions.readCsv(parse_dates=['Date'])
            self.database.createDatabaseFromDataFrame(self._dbName,
                                                      dfTransactions)

    def getExpensesGroupbyCategory(self, nDays=None):
        if nDays is None:
            results = self.database.execute(
                queries.EXPENSES_GROUPBY_CATEGORY_TOTAL)
        else:
            startDate, endDate = utils.getLastNdaysStartAndEndDate(nDays)
            q = queries.EXPENSES_GROUPBY_CATEGORY_BW_DATE_RANGE % (
                str(startDate), str(endDate))
            results = self.database.execute(q)

        return results
    
    def getExpenses(self,nDays=None):
        if nDays is None:
            results = self.database.execute(
                queries.TRANSACTIONS_ALL)
        else:
            startDate, endDate = utils.getLastNdaysStartAndEndDate(nDays)
            q = queries.TRANSACTIONS_BW_DATE_RANGE % (
                str(startDate), str(endDate))
            results = self.database.execute(q)
        return results


    def getExpensesPerCategory(self, category=None, nDays=None):
        if category == None:
            return None

        if nDays is None:
            results = self.database.execute(
                queries.TRANSACTIONS_PER_CATEGORY_TOTAL % category)
        else:
            startDate, endDate = utils.getLastNdaysStartAndEndDate(nDays)
            q = queries.EXPENSES_GROUPBY_PER_BW_DATE_RANGE % (str(startDate),
                                                              str(endDate))
            results = self.database.execute(q)

        return results
