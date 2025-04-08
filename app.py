from flask import Flask
import subprocess
import os
import datetime
import pytz  # to handle IST conversion, install with 'pip install pytz' if needed

app = Flask(__name__)

@app.route('/htop')
def htop():
    
    full_name = "Adithya M"
    system_username = os.environ.get("USER", "codespace")

    tz_ist = pytz.timezone("Asia/Kolkata")
    server_time_ist = datetime.datetime.now(tz_ist).strftime("%Y-%m-%d %H:%M:%S %Z")

    try:
        top_process = subprocess.Popen(["top", "-b", "-n", "1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        top_output, top_error = top_process.communicate()
        if top_error:
            top_output_str = "Error retrieving top data: " + top_error.decode()
        else:
            top_output_str = top_output.decode()
    except Exception as e:
        top_output_str = str(e)

    html = f"""
    <html>
      <body>
        <h1>Htop Endpoint</h1>
        <p><b>Name:</b> {full_name}</p>
        <p><b>Username:</b> {system_username}</p>
        <p><b>Server Time (IST):</b> {server_time_ist}</p>
        <pre>{top_output_str}</pre>
      </body>
    </html>
    """
    return html

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000)