import os
import socket

from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "local")
POD_NAME = os.getenv("HOSTNAME", socket.gethostname())


@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>EKS Kubernetes Platform</title>

      <style>
        body {{
          margin: 0;
          font-family: Arial, Helvetica, sans-serif;
          background: linear-gradient(135deg, #020617, #0f172a);
          color: #e2e8f0;
          min-height: 100vh;
          display: flex;
          justify-content: center;
          align-items: center;
        }}

        .card {{
          width: min(800px, 90%);
          background: #0f172a;
          border: 1px solid #334155;
          border-radius: 18px;
          padding: 40px;
          box-shadow: 0 20px 60px rgba(0,0,0,.35);
        }}

        h1 {{
          font-size: 48px;
          margin-bottom: 10px;
        }}

        .accent {{
          color: #38bdf8;
        }}

        .status {{
          display: inline-block;
          margin: 20px 0;
          padding: 8px 14px;
          border-radius: 999px;
          background: rgba(34,197,94,.1);
          color: #86efac;
          border: 1px solid rgba(34,197,94,.3);
        }}

        .grid {{
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
          gap: 16px;
          margin-top: 30px;
        }}

        .item {{
          background: #111827;
          border: 1px solid #1e293b;
          border-radius: 12px;
          padding: 20px;
        }}

        .label {{
          color: #94a3b8;
          font-size: 13px;
          text-transform: uppercase;
        }}

        .value {{
          margin-top: 8px;
          font-size: 18px;
          font-weight: bold;
          word-break: break-word;
        }}
      </style>
    </head>

    <body>
      <div class="card">
        <h1>AWS EKS <span class="accent">Kubernetes Platform</span></h1>

        <p>
          Containerized application running on Kubernetes and designed
          for deployment to Amazon EKS.
        </p>

        <div class="status">● Application Healthy</div>

        <div class="grid">
          <div class="item">
            <div class="label">Version</div>
            <div class="value">{APP_VERSION}</div>
          </div>

          <div class="item">
            <div class="label">Pod</div>
            <div class="value">{POD_NAME}</div>
          </div>

          <div class="item">
            <div class="label">Platform</div>
            <div class="value">Kubernetes</div>
          </div>
        </div>
      </div>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(
        status="healthy",
        version=APP_VERSION,
        pod=POD_NAME,
    )


@app.route("/ready")
def ready():
    return jsonify(status="ready")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)