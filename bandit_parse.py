import os
import json


def check_report():
    with open('test.json') as report:
        json_rep = json.load(report)
        if json_rep["metrics"]["_totals"]["SEVERITY.HIGH"] > 0:
            os.system('cat test.json')
            raise Exception("Severity check failed!")


try:
    check_report()
except FileNotFoundError:
    os.system('bandit -r webapp -n 3 -ii -lll -f json -o test.json')
    check_report()
