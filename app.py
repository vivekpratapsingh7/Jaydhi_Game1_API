from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the dataset
df = pd.read_csv("ml101_cleaned_chatbot_dataset.csv")
df['Item'] = df['Item'].str.lower()  # Normalize item names

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("item", "").strip().lower()

    # Search for label
    match = df[df['Item'] == user_input]

    if not match.empty:
        label = match['Label'].values[0]
        return jsonify({"label": label})
    else:
        return jsonify({"item": user_input, "label": "Unknown item"}), 404

if __name__ == '__main__':
    app.run(debug=True)
