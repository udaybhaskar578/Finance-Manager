# Finance Manager

Built using Python, Flask, SQLLite, Pandas

Quick start
-----------

All dependencies can be installed using the following command

    $ pip install -r requirements.txt

To run the Application please use the following command

    $ python app.py


## Input Data format

The raw_data that we used for this has been imported from Mint financial software

If you do not have an account with Mint, you can format all your expenses as a csv below and save it as transactions.csv under raw_data folder

| Date | Description | Original Description | Amount | Transaction Type | Category | Account Name | Labels | Notes |
| ------------- | ------------- | ----- | ------------- | ------------- | ----- | ------------- | ------------- | ----- |
| 2019-04-02      | ABC | ABC*DEF |   $12 | Debit | Gym | Discover | Null | Null |

## API's Exposed

### List all expenses

**Definition**

`GET /expenses`

**Response**

- `200 OK` on success

```json
[
    {
        "Description": "Abc Westca",
        "Original_Description": "ABC*WESTCA",
        "Amount": 49,
        "Category": "Gym",
        "Account_Name": "Cash rewards credit card ",
        "Date": "2019-01-24 00:00:00"
    },
    {
        "Description": "Uber.com",
        "Original_Description": "UBR* PENDING.UBER.COM",
        "Amount": 6.65,
        "Category": "Rental Car & Taxi",
        "Account_Name": "Cash rewards credit card ",
        "Date": "2019-01-24 00:00:00"
	}
]
```

### List expenses grouped by category

**Definition**

`GET /expenses/category`

**Response**

- `200 OK` on success

```json
[
    {
        "Category": "XYZ",
        "Total_Amount": 2
    },
    {
        "Category": "ABC",
        "Total_Amount": 220
	}
]
```

### List expenses grouped by category within last N days

**Definition**

`GET /expenses/category/<int:num_days>`

**Response**

- `200 OK` on success

```json
[
    {
        "Category": "XYZ",
        "Total_Amount": 2
    },
    {
        "Category": "ABC",
        "Total_Amount": 220
	}
]
```