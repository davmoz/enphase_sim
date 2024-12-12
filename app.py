# app.py
from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/api/v1/production/inverters', methods=['GET'])
def inverters():
    return jsonify(
        {
            "inverters": [
                {
                    "id": 1,
                    "name": "Inverter 1"
                },
                {
                    "id": 2,
                    "name": "Inverter 2"
                }   
            ]
        }
    )

@app.route('/ivp/meters/reports/consumption', methods=['GET'])
def consumption():
    return jsonify({
        "consumption": [
            {
                "id": 1,
                "name": "Meter 1"
            },
            {
                "id": 2,
                "name": "Meter 2"
            }
        ] 
    })
    
@app.route('/ivp/pdm/energy', methods=['GET'])
def energy():
    return jsonify({
        "energy": [
            {
                "id": 1,
                "name": "Meter 1",
                "value": 1000
            },
            {
                "id": 2,
                "name": "Meter 2",
                "value": 2000
            }
        ] 
    })

@app.route('/production.json', methods=['GET'])
def production_json():
    current_time = int(datetime.datetime.now().timestamp())
    return jsonify({
        "production": {
            "production": [
                {
                    "type": "inverters",
                    "activeCount": 21,
                    "readingTime": 0,
                    "wNow": 0,
                    "whLifetime": 22174104
                },
                {
                    "type": "eim",
                    "activeCount": 1,
                    "measurementType": "production",
                    "readingTime": current_time,
                    "wNow": 0,
                    "whLifetime": 23996277.788,
                    "varhLeadLifetime": 5303014.034,
                    "varhLagLifetime": 4845749.198,
                    "vahLifetime": 29670375.023,
                    "rmsCurrent": 3.859,
                    "rmsVoltage": 252.478,
                    "reactPwr": 474.234,
                    "apprntPwr": 487.2,
                    "pwrFactor": 0,
                    "whToday": 0.788,
                    "whLastSevenDays": 131945.788,
                    "vahToday": 545.023,
                    "varhLeadToday": 1.034,
                    "varhLagToday": 530.198
                }
            ],
            "consumption": [
                {
                    "type": "eim",
                    "activeCount": 1,
                    "measurementType": "total-consumption",
                    "readingTime": current_time,
                    "wNow": 272.007,
                    "whLifetime": 23872360.47,
                    "varhLeadLifetime": 189660.377,
                    "varhLagLifetime": 623700.162,
                    "vahLifetime": 39466404.883,
                    "rmsCurrent": 9.942,
                    "rmsVoltage": 252.407,
                    "reactPwr": -152.089,
                    "apprntPwr": 1254.698,
                    "pwrFactor": 0.21,
                    "whToday": 876.47,
                    "whLastSevenDays": 150.47,
                    "vahToday": 1220.883,
                    "varhLeadToday": 569.377,
                    "varhLagToday": 0
                },
                {
                    "type": "eim",
                    "activeCount": 1,
                    "measurementType": "net-consumption",
                    "readingTime": current_time,
                    "wNow": 272.007,
                    "whLifetime": -121977.358,
                    "varhLeadLifetime": 5492674.411,
                    "varhLagLifetime": 5469449.36,
                    "vahLifetime": 39466404.883,
                    "rmsCurrent": 6.082,
                    "rmsVoltage": 252.407,
                    "reactPwr": -626.323,
                    "apprntPwr": 767.63,
                    "pwrFactor": 0.34,
                    "whToday": 0,
                    "whLastSevenDays": 0,
                    "vahToday": 0,
                    "varhLeadToday": 0,
                    "varhLagToday": 0
                }
            ],
            "storage": [
                {
                    "type": "acb",
                    "activeCount": 0,
                    "readingTime": 0,
                    "wNow": 0,
                    "whNow": 0,
                    "state": "idle"
                }
            ]
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)