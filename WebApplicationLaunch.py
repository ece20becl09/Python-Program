from flask import Flask, render_template_string, request

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modern Calculator</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
        }
        .calculator-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
            width: 100%;
            max-width: 450px;
        }
        .btn-calculate {
            background: #764ba2;
            color: white;
            border: none;
            width: 100%;
            padding: 12px;
            border-radius: 10px;
            font-size: 1.1rem;
            font-weight: 600;
            transition: all 0.3s ease;
            margin-top: 10px;
        }
        .btn-calculate:hover {
            background: #5a3a8a;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            color: white;
        }
        .result-display {
            background: #eef2ff;
            border-radius: 12px;
            padding: 20px;
            margin-top: 25px;
            text-align: center;
            border-left: 6px solid #764ba2;
            animation: fadeIn 0.5s ease-in-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        h2 {
            color: #333;
            margin-bottom: 30px;
            text-align: center;
            font-weight: 700;
            letter-spacing: -1px;
        }
        .form-label {
            font-weight: 600;
            color: #555;
            margin-bottom: 8px;
        }
        .form-control, .form-select {
            border-radius: 10px;
            padding: 12px;
            border: 1px solid #ddd;
        }
        .form-control:focus, .form-select:focus {
            border-color: #764ba2;
            box-shadow: 0 0 0 0.25rem rgba(118, 75, 162, 0.25);
        }
    </style>
</head>
<body>
    <div class="calculator-card">
        <h2>Calculator App</h2>
        <form method="post">
            <div class="mb-3">
                <label class="form-label">First Number</label>
                <input type="number" step="any" name="num1" class="form-control" placeholder="e.g. 10" required>
            </div>
            <div class="mb-3">
                <label class="form-label">Second Number</label>
                <input type="number" step="any" name="num2" class="form-control" placeholder="e.g. 5" required>
            </div>
            <div class="mb-4">
                <label class="form-label">Operation</label>
                <select name="choice" class="form-select">
                    <option value="1">Addition (+)</option>
                    <option value="2">Subtraction (-)</option>
                    <option value="3">Multiplication (*)</option>
                    <option value="4">Division (/)</option>
                </select>
            </div>
            <button type="submit" class="btn btn-calculate">Calculate Now</button>
        </form>

        {% if result %}
        <div class="result-display">
            <h4 class="mb-0" style="color: #764ba2;">{{ result }}</h4>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            choice = int(request.form["choice"])

            if choice == 1:
                result = f"Answer = {num1 + num2}"
            elif choice == 2:
                result = f"Answer = {num1 - num2}"
            elif choice == 3:
                result = f"Answer = {num1 * num2}"
            elif choice == 4:
                if num2 == 0:
                    result = "Cannot divide by zero!"
                else:
                    result = f"Answer = {num1 / num2}"
            else:
                result = "Invalid choice!"

        except ValueError:
            result = "Invalid input! Please enter valid numbers."

    return render_template_string(html_code, result=result)

if __name__ == "__main__":
    app.run(debug=True)
