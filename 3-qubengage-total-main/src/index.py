from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def main():
    output = {
        "error": False,
        "items": "",
        "total": 0
    }

    item_1 = request.args.get('item_1')
    item_2 = request.args.get('item_2')
    item_3 = request.args.get('item_3')
    item_4 = request.args.get('item_4')
    attendance_1 = request.args.get('attendance_1')
    attendance_2 = request.args.get('attendance_2')
    attendance_3 = request.args.get('attendance_3')
    attendance_4 = request.args.get('attendance_4')

    items = [item_1, item_2, item_3, item_4]
    attendances = [attendance_1, attendance_2, attendance_3, attendance_4]

    total = getTotal(attendances)

    output['items'] = items
    output['total'] = total

    return jsonify(output)

def getTotal(attendances):
    attendances = [int(a) if a and a.isdigit() else 0 for a in attendances]
    total_attendance = sum(attendances)
    return total_attendance

if __name__ == '__main__':
    app.run(debug=True)
