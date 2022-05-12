from flask import Flask, make_response, jsonify, request

# Configure application
from core.employee import Employee
from core.utils import read_database, add_record_to_database

app = Flask(__name__)

EMPLOYEES_DATA = {}


@app.before_first_request
def before_first_request():
    app.logger.info("before_first_request")
    global EMPLOYEES_DATA
    EMPLOYEES_DATA = read_database()
    app.logger.info("DATA:")
    app.logger.info(EMPLOYEES_DATA)


@app.route("/salary", methods=["GET"])
def get_annual_salary():
    """Get annual salary budget for an employee"""
    employee = request.args.get("name")
    global EMPLOYEES_DATA
    if employee in EMPLOYEES_DATA:
        employee = EMPLOYEES_DATA[employee]
        response = make_response(
            {"annual_salary_budget": employee.get_annual_salary_budget()},
            200
        )
        response.headers["Content-Type"] = "application/json"
        return response
    else:
        msg = f"ERROR. Employee {employee} does not found"
        return make_response(jsonify(msg), 404)


@app.route("/employee", methods=["POST"])
def add_new_employee():
    data = request.form
    try:
        name = data["name"]
        position = data["position"]
        salary = float(data["monthly_salary"])
    except KeyError:
        return make_response("ERROR. name, position, monthly_salary required", 400)
    except ValueError:
        return make_response("ERROR. monthly_salary should be a number", 400)

    global EMPLOYEES_DATA
    employee = Employee(name, position, salary)
    EMPLOYEES_DATA[name] = employee
    add_record_to_database(employee)
    return make_response({"message": "success"}, 201)


if __name__ == "__main__":
    app.run(debug=True)
