from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn='https://2be3d8351378b6d0c6510633d9129969@o4509681749786624.ingest.us.sentry.io/4509681763090432',
    send_default_pii=True,
)

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Flask + Sentry"

@app.route('/err')
def trigger_err():
    division_by_zero = 1 / 0
    return str(division_by_zero)

if __name__ == '__main__':
    app.run(debug=True)
