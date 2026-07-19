from flask import Flask, render_template_string, request, jsonify
import math
from datetime import datetime

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced Calculator Pro</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding: 20px;
        }
        
        .main-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            width: 100%;
            max-width: 1200px;
            align-items: start;
        }
        
        @media (max-width: 1024px) {
            .main-container {
                grid-template-columns: 1fr;
            }
        }
        
        .card-wrapper {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 25px;
            padding: 35px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            animation: slideIn 0.6s ease-out;
        }
        
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .card-title {
            color: #333;
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 25px;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .card-title i {
            color: #764ba2;
            font-size: 2rem;
        }
        
        .form-group-custom {
            margin-bottom: 18px;
        }
        
        .form-label {
            font-weight: 600;
            color: #555;
            margin-bottom: 8px;
            display: block;
            font-size: 0.95rem;
        }
        
        .form-control, .form-select {
            border-radius: 12px;
            padding: 12px 15px;
            border: 2px solid #e0e0e0;
            font-size: 1rem;
            transition: all 0.3s ease;
        }
        
        .form-control:focus, .form-select:focus {
            border-color: #764ba2;
            box-shadow: 0 0 0 0.25rem rgba(118, 75, 162, 0.15);
            outline: none;
        }
        
        .btn-calculate {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
            color: white;
            border: none;
            border-radius: 12px;
            font-size: 1.05rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-top: 8px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .btn-calculate:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 25px rgba(118, 75, 162, 0.4);
        }
        
        .btn-calculate:active {
            transform: translateY(-1px);
        }
        
        .btn-clear {
            width: 100%;
            padding: 10px;
            background: #f0f0f0;
            color: #666;
            border: 2px solid #e0e0e0;
            border-radius: 12px;
            font-size: 0.95rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-top: 8px;
        }
        
        .btn-clear:hover {
            background: #e0e0e0;
            border-color: #999;
        }
        
        .result-display {
            background: linear-gradient(135deg, #eef2ff 0%, #f5f3ff 100%);
            border-radius: 16px;
            padding: 25px;
            margin-top: 25px;
            border-left: 5px solid #764ba2;
            animation: fadeIn 0.5s ease-in-out;
            box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.05);
        }
        
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .result-label {
            font-size: 0.85rem;
            color: #999;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
        }
        
        .result-value {
            font-size: 2.2rem;
            color: #764ba2;
            font-weight: 700;
            word-break: break-all;
            font-family: 'Courier New', monospace;
        }
        
        .error-display {
            background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
            border-radius: 16px;
            padding: 20px;
            margin-top: 25px;
            border-left: 5px solid #e53935;
            color: #c62828;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .error-display i {
            font-size: 1.5rem;
        }
        
        .success-display {
            background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
            border-radius: 16px;
            padding: 20px;
            margin-top: 25px;
            border-left: 5px solid #2e7d32;
            color: #1b5e20;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .success-display i {
            font-size: 1.5rem;
        }
        
        .history-item {
            background: #f8f9fa;
            padding: 12px 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            border-left: 4px solid #764ba2;
            font-size: 0.95rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            animation: slideInLeft 0.3s ease-out;
        }
        
        @keyframes slideInLeft {
            from {
                opacity: 0;
                transform: translateX(-20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        .history-item:hover {
            background: #e9ecef;
            transform: translateX(5px);
        }
        
        .history-expression {
            color: #666;
            font-weight: 600;
        }
        
        .history-result {
            color: #764ba2;
            font-weight: 700;
            font-family: 'Courier New', monospace;
        }
        
        .history-empty {
            color: #999;
            text-align: center;
            padding: 20px;
            font-style: italic;
        }
        
        .advanced-ops {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 15px;
        }
        
        .btn-advanced {
            padding: 10px 12px;
            background: #f5f5f5;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            cursor: pointer;
            font-weight: 600;
            font-size: 0.9rem;
            transition: all 0.3s ease;
            color: #666;
        }
        
        .btn-advanced:hover {
            background: #764ba2;
            color: white;
            border-color: #764ba2;
            transform: translateY(-2px);
        }
        
        .info-box {
            background: #f0f4ff;
            border-radius: 12px;
            padding: 15px;
            margin-top: 15px;
            border-left: 4px solid #667eea;
            font-size: 0.9rem;
            color: #555;
        }
        
        .info-box i {
            color: #667eea;
            margin-right: 8px;
        }
        
        .copy-btn {
            cursor: pointer;
            color: #764ba2;
            margin-left: 8px;
            transition: all 0.3s ease;
        }
        
        .copy-btn:hover {
            color: #667eea;
            transform: scale(1.1);
        }
    </style>
</head>
<body>
    <div class="main-container">
        <!-- Main Calculator Card -->
        <div class="card-wrapper">
            <h3 class="card-title">
                <i class="fas fa-calculator"></i>
                Advanced Calculator
            </h3>
            
            <form id="calculatorForm" method="post">
                <!-- First Number -->
                <div class="form-group-custom">
                    <label class="form-label" for="num1">
                        <i class="fas fa-hash"></i> First Number
                    </label>
                    <input type="number" step="any" id="num1" name="num1" class="form-control" 
                           placeholder="Enter first number" required>
                </div>
                
                <!-- Second Number -->
                <div class="form-group-custom">
                    <label class="form-label" for="num2">
                        <i class="fas fa-hash"></i> Second Number
                    </label>
                    <input type="number" step="any" id="num2" name="num2" class="form-control" 
                           placeholder="Enter second number" required>
                </div>
                
                <!-- Operation Selection -->
                <div class="form-group-custom">
                    <label class="form-label" for="choice">
                        <i class="fas fa-stream"></i> Select Operation
                    </label>
                    <select id="choice" name="choice" class="form-select">
                        <option value="1">➕ Addition (+)</option>
                        <option value="2">➖ Subtraction (-)</option>
                        <option value="3">✖️ Multiplication (*)</option>
                        <option value="4">➗ Division (/)</option>
                        <option value="5">📊 Modulus (%)</option>
                        <option value="6">🔢 Power (^)</option>
                    </select>
                </div>
                
                <!-- Advanced Operations -->
                <div class="form-group-custom">
                    <label class="form-label">
                        <i class="fas fa-flask-vial"></i> Quick Operations
                    </label>
                    <div class="advanced-ops">
                        <button type="button" class="btn-advanced" onclick="calculateAdvanced('square')">
                            x²
                        </button>
                        <button type="button" class="btn-advanced" onclick="calculateAdvanced('sqrt')">
                            √x
                        </button>
                        <button type="button" class="btn-advanced" onclick="calculateAdvanced('sin')">
                            sin(x)
                        </button>
                        <button type="button" class="btn-advanced" onclick="calculateAdvanced('cos')">
                            cos(x)
                        </button>
                    </div>
                </div>
                
                <!-- Buttons -->
                <button type="submit" class="btn-calculate" id="submitBtn">
                    <i class="fas fa-check-circle"></i> Calculate
                </button>
                <button type="button" class="btn-clear" onclick="clearForm()">
                    <i class="fas fa-trash"></i> Clear All
                </button>
            </form>
            
            <!-- Result Display -->
            <div id="resultContainer"></div>
            
            <!-- Info Box -->
            <div class="info-box">
                <i class="fas fa-lightbulb"></i>
                <strong>Pro Tip:</strong> Use keyboard Enter to calculate instantly!
            </div>
        </div>
        
        <!-- History & Info Panel -->
        <div class="card-wrapper">
            <h3 class="card-title">
                <i class="fas fa-history"></i>
                Calculation History
            </h3>
            
            <div id="historyContainer" class="history-empty">
                <i class="fas fa-inbox"></i><br>No calculations yet
            </div>
            
            <button type="button" class="btn-clear" onclick="clearHistory()">
                <i class="fas fa-broom"></i> Clear History
            </button>
            
            <!-- Stats Panel -->
            <div class="info-box" style="margin-top: 25px;">
                <i class="fas fa-chart-bar"></i>
                <strong>Statistics</strong>
                <div style="margin-top: 10px; font-size: 0.9rem;">
                    <div><strong>Total Calculations:</strong> <span id="totalCalcs">0</span></div>
                    <div style="margin-top: 5px;"><strong>Last Operation:</strong> <span id="lastOp">None</span></div>
                </div>
            </div>
            
            <!-- Features List -->
            <div class="info-box" style="margin-top: 15px; background: #fff3e0; border-left-color: #ff9800;">
                <i class="fas fa-star" style="color: #ff9800;"></i>
                <strong>Features:</strong>
                <ul style="margin: 10px 0 0 0; padding-left: 25px; font-size: 0.85rem;">
                    <li>Basic & Advanced Operations</li>
                    <li>Full Calculation History</li>
                    <li>Keyboard Support</li>
                    <li>Error Handling</li>
                    <li>Real-time Validation</li>
                </ul>
            </div>
        </div>
    </div>
    
    <script>
        let calculationHistory = [];
        const MAX_HISTORY = 10;
        
        // Load history from localStorage
        window.onload = function() {
            const saved = localStorage.getItem('calcHistory');
            if (saved) {
                calculationHistory = JSON.parse(saved);
                updateHistoryDisplay();
            }
            
            // Keyboard Enter support
            document.getElementById('num1').addEventListener('keypress', handleEnter);
            document.getElementById('num2').addEventListener('keypress', handleEnter);
            document.getElementById('choice').addEventListener('keypress', handleEnter);
        };
        
        function handleEnter(e) {
            if (e.key === 'Enter') {
                document.getElementById('calculatorForm').dispatchEvent(new Event('submit'));
            }
        }
        
        document.getElementById('calculatorForm').addEventListener('submit', function(e) {
            e.preventDefault();
            performCalculation();
        });
        
        async function performCalculation() {
            const num1 = parseFloat(document.getElementById('num1').value);
            const num2 = parseFloat(document.getElementById('num2').value);
            const choice = document.getElementById('choice').value;
            
            if (isNaN(num1) || isNaN(num2)) {
                showError('Please enter valid numbers!');
                return;
            }
            
            const formData = new FormData();
            formData.append('num1', num1);
            formData.append('num2', num2);
            formData.append('choice', choice);
            
            try {
                const response = await fetch('/', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.text();
                const parser = new DOMParser();
                const doc = parser.parseFromString(data, 'text/html');
                
                const result = doc.querySelector('[data-result-value]');
                if (result) {
                    const resultValue = result.dataset.resultValue;
                    const expression = result.dataset.expression;
                    
                    addToHistory(expression, resultValue);
                    displayResult(expression, resultValue);
                }
            } catch (error) {
                showError('Calculation failed! Please try again.');
            }
        }
        
        function calculateAdvanced(operation) {
            const num1 = parseFloat(document.getElementById('num1').value);
            
            if (isNaN(num1)) {
                showError('Please enter a number in the first field!');
                return;
            }
            
            let result, expression;
            
            try {
                switch(operation) {
                    case 'square':
                        result = num1 * num1;
                        expression = `${num1}²`;
                        break;
                    case 'sqrt':
                        if (num1 < 0) throw new Error('Cannot calculate square root of negative number!');
                        result = Math.sqrt(num1);
                        expression = `√${num1}`;
                        break;
                    case 'sin':
                        result = Math.sin(num1);
                        expression = `sin(${num1})`;
                        break;
                    case 'cos':
                        result = Math.cos(num1);
                        expression = `cos(${num1})`;
                        break;
                    default:
                        throw new Error('Unknown operation');
                }
                
                addToHistory(expression, result);
                displayResult(expression, result);
            } catch (error) {
                showError(error.message);
            }
        }
        
        function displayResult(expression, resultValue) {
            const container = document.getElementById('resultContainer');
            const formattedResult = typeof resultValue === 'number' ? resultValue.toFixed(6).replace(/\.?0+$/, '') : resultValue;
            
            container.innerHTML = `
                <div class="result-display" data-result-value="${formattedResult}" data-expression="${expression}">
                    <div class="result-label">Calculation Result</div>
                    <div class="result-value">
                        ${expression} = ${formattedResult}
                        <span class="copy-btn" onclick="copyToClipboard('${formattedResult}')" title="Copy result">
                            <i class="fas fa-copy"></i>
                        </span>
                    </div>
                </div>
            `;
        }
        
        function showError(message) {
            const container = document.getElementById('resultContainer');
            container.innerHTML = `
                <div class="error-display">
                    <i class="fas fa-exclamation-circle"></i>
                    <span>${message}</span>
                </div>
            `;
        }
        
        function addToHistory(expression, result) {
            const timestamp = new Date().toLocaleTimeString();
            calculationHistory.unshift({
                expression,
                result: typeof result === 'number' ? result.toFixed(6).replace(/\.?0+$/, '') : result,
                timestamp
            });
            
            if (calculationHistory.length > MAX_HISTORY) {
                calculationHistory.pop();
            }
            
            localStorage.setItem('calcHistory', JSON.stringify(calculationHistory));
            updateHistoryDisplay();
        }
        
        function updateHistoryDisplay() {
            const container = document.getElementById('historyContainer');
            
            if (calculationHistory.length === 0) {
                container.innerHTML = '<div class="history-empty"><i class="fas fa-inbox"></i><br>No calculations yet</div>';
                document.getElementById('totalCalcs').textContent = '0';
                return;
            }
            
            container.innerHTML = calculationHistory.map((item, index) => `
                <div class="history-item">
                    <div>
                        <div class="history-expression">${item.expression}</div>
                        <small style="color: #999;">${item.timestamp}</small>
                    </div>
                    <div class="history-result">${item.result}</div>
                </div>
            `).join('');
            
            document.getElementById('totalCalcs').textContent = calculationHistory.length;
            if (calculationHistory.length > 0) {
                document.getElementById('lastOp').textContent = calculationHistory[0].expression;
            }
        }
        
        function clearForm() {
            document.getElementById('calculatorForm').reset();
            document.getElementById('resultContainer').innerHTML = '';
            document.getElementById('num1').focus();
        }
        
        function clearHistory() {
            if (confirm('Are you sure you want to clear all history?')) {
                calculationHistory = [];
                localStorage.removeItem('calcHistory');
                updateHistoryDisplay();
            }
        }
        
        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(() => {
                alert('Result copied to clipboard! ✓');
            });
        }
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1", 0))
            num2 = float(request.form.get("num2", 0))
            choice = int(request.form.get("choice", 1))
            
            result = None
            expression = ""
            
            if choice == 1:
                result = num1 + num2
                expression = f"{num1} + {num2}"
            elif choice == 2:
                result = num1 - num2
                expression = f"{num1} - {num2}"
            elif choice == 3:
                result = num1 * num2
                expression = f"{num1} × {num2}"
            elif choice == 4:
                if num2 == 0:
                    return render_template_string(html_code, error="Cannot divide by zero!")
                result = num1 / num2
                expression = f"{num1} ÷ {num2}"
            elif choice == 5:
                if num2 == 0:
                    return render_template_string(html_code, error="Modulus by zero is not allowed!")
                result = num1 % num2
                expression = f"{num1} % {num2}"
            elif choice == 6:
                result = num1 ** num2
                expression = f"{num1} ^ {num2}"
            else:
                return render_template_string(html_code, error="Invalid choice!")
            
            # Format result to avoid floating point errors
            if isinstance(result, float):
                result_str = f"{result:.6f}".rstrip('0').rstrip('.')
            else:
                result_str = str(result)
            
            # Return a response that includes data attributes
            response_html = f"""
            {html_code.replace('</body>', f'''
                <div style="display:none;">
                    <div data-result-value="{result_str}" data-expression="{expression}"></div>
                </div>
            </body>''')}
            """
            return response_html
            
        except ValueError:
            return render_template_string(html_code, error="Invalid input! Please enter valid numbers.")
        except Exception as e:
            return render_template_string(html_code, error=f"An error occurred: {str(e)}")
    
    return render_template_string(html_code)

if __name__ == "__main__":
    print("🚀 Advanced Calculator App is running...")
    print("📊 Visit http://127.0.0.1:5000/")
    app.run(debug=True, host='127.0.0.1', port=5000)
