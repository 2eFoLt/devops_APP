import os
import json


def check_report():
    with open('test.json') as report:
        json_rep = json.load(report)
        if json_rep["metrics"]["_totals"]["SEVERITY.HIGH"] > 0:
            os.system('cat test.json')
            raise Exception("Severity check failed!")


check_report()
