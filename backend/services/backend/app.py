from flask import Flask, jsonify, request
import pandas as pd
from services.recommendation_engine import recommend_schemes

app = Flask(__name__)

schemes = pd.read_csv("ml/data/schemes_dataset.csv")

@app.route("/recommend", methods=["POST"])
def recommend():
    user = request.json
    recommendations = recommend_schemes(user, schemes)
    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True)
