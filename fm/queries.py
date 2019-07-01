from . import const

# Transactions
OVERALL_DATE_RANGE = "select * from " + const.DB_NAME + " where date between '%s' AND '%s';"

# Expenses
_BASE_QUERY_SPEND_CATEGORY = "select Category as Category, sum(Amount) as Total_Amount from %s " % const.DB_NAME

# Query for getting spent group by category
EXPENSES_GROUPBY_CATEGORY_TOTAL = _BASE_QUERY_SPEND_CATEGORY + " where transaction_type=='debit' group by Category; "
EXPENSES_GROUPBY_CATEGORY_BW_DATE_RANGE = _BASE_QUERY_SPEND_CATEGORY + " where transaction_type=='debit' and date between '%s' AND '%s' group by Category; "

# Expenses
_BASE_QUERY_TRANSACTIONS = "select Description, Original_Description, Amount, Category, Account_Name, Date from %s " % const.DB_NAME

# Query for getting spent per category
TRANSACTIONS_PER_CATEGORY_TOTAL = _BASE_QUERY_TRANSACTIONS + " where transaction_type=='debit' and Category=='%s'; "
TRANSACTIONS_PER_CATEGORY_BW_DATE_RANGE = _BASE_QUERY_TRANSACTIONS + " where transaction_type=='debit' and category=='%s' and date between '%s' AND '%s'; "

# Query for getting spent per category
TRANSACTIONS_ALL = _BASE_QUERY_TRANSACTIONS + " where transaction_type=='debit'; "
TRANSACTIONS_BW_DATE_RANGE = _BASE_QUERY_TRANSACTIONS + " where transaction_type=='debit' and date between '%s' AND '%s'; "
