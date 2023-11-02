from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_payment', methods=['POST'])
def process_payment():
    # Simulate payment processing
    data = request.get_json()
    amount = data.get('amount')
    card_number = data.get('card_number')
    # You would typically use a payment gateway API here.
    # Implement real payment processing logic with a payment provider like Stripe.

    # In this example, we'll simply return a success message.
    response = {
        "status": "success",
        "message": f"Payment of ${amount:.2f} processed successfully."
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)