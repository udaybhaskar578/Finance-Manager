import pandas as pd


class DataProcessor:
    def __init__(self, dataFileName, cleanData=True, processData=True):
        self.dataFileName = dataFileName
        self._dataFrame = None
        self._cleanData = cleanData
        self._processData = processData

    def readCsv(self, *args, **kwargs):
        self._dataFrame = pd.read_csv(self.dataFileName, *args, **kwargs)
        if self._cleanData:
            self.__clean()

        if self._processData:
            self.preProcess()

    def __clean(self):
        if self._dataFrame is None:
            return

        self._dataFrame.columns = self._dataFrame.columns.str.strip()
        self._dataFrame.columns = self._dataFrame.columns.str.replace(' ', '_')

    def preProcess(self):
        self._dataFrame.loc[self._dataFrame.Description ==
                            'Xoom', ['Category']] = 'Transfer to INDIA'

    @property
    def dataFrame(self):
        return self._dataFrame
