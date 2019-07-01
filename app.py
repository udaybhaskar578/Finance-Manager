import markdown
from flask import Flask, render_template
from flask import Flask, request
from flask_restful import Resource, Api

from fm import FinanceManager

app = Flask(__name__)
api = Api(app)


@app.route("/")
def index():
    # Open the README file
    with open('./README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)


class ExpensesByCategory(Resource):
    def get(self, num_days):
        fm = FinanceManager()
        results = fm.getExpensesGroupbyCategory(num_days)

        return results


class AllExpensesByCategory(Resource):
    def get(self):
        fm = FinanceManager()
        results = fm.getExpensesGroupbyCategory()

        return results

class AllExpenses(Resource):
    def get(self):
        fm = FinanceManager()
        results = fm.getExpenses()

        return results


api.add_resource(AllExpenses, '/expenses')
api.add_resource(AllExpensesByCategory, '/expenses/category')
api.add_resource(ExpensesByCategory, '/expenses/category/<int:num_days>')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
