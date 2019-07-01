import pytest
import unittest

from fm import FinanceManager


class TestFinanceManager(unittest.TestCase):
    def setUp(self):
        self.fm = FinanceManager()

    def test_getExpensesGroupbyCategory(self):
        tests = [{
            'desc': 'Get all expenses group by category',
            'args': [None],
            'expected': []
        },
                 {
                     'desc': 'Get all expenses group by category past ndays',
                     'args': [30],
                     'expected': []
                 }]
        self.fm = FinanceManager()
        for test in tests:
            res = self.fm.getExpensesGroupbyCategory(test['args'][0])
            # For now just checking type of return valu
            self.assertEqual(type(res), type(test['expected']), test['desc'])

    def test_getExpensesPerCategory(self):
        results = self.fm.getExpensesPerCategory(category=None, nDays=None)
        assert results == None
        results = self.fm.getExpensesPerCategory(
            category='Utilities', nDays=None)
        assert results != None
        print(results)

    def test_getTransactionForCategory(self):
        pass
