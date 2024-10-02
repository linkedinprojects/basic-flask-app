from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Set default background color to 'skyblue' if no color is provided
    bg_color = request.args.get('color', 'skyblue')
    return render_template('index.html', color=bg_color)

if __name__ == '__main__':
    # Export the port from environment variables, default to 80 for exposure
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port, debug=True)
