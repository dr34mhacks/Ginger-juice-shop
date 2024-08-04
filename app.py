from flask import Flask, request, render_template_string

app = Flask(__name__)
app.secret_key = "VjJGeklHbDBJSEpsWVd4c2VTQnpkWEJ3YjNObFpDQjBieUJpWlNCelpXTnlaWFJwZG1VLw=="

# Simple SSTI vulnerability at /greet path
@app.route('/')
def index():
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ginger Juice Shop</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #f2f2f2;
                    color: #333;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-size: cover;
                    background-position: center;
                }
                .container {
                    background-color: rgba(255, 255, 255, 0.9);
                    padding: 40px;
                    border-radius: 15px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    text-align: center;
                }
                h1 {
                    color: #3498db;
                    font-size: 2em;
                    margin-bottom: 20px;
                }
                input[type="text"] {
                    padding: 12px;
                    width: 80%;
                    margin-bottom: 20px;
                    border: 2px solid #ccc;
                    border-radius: 5px;
                    font-size: 1em;
                }
                input[type="submit"], .btn-hard {
                    background-color: #3498db;
                    color: white;
                    border: none;
                    padding: 12px 25px;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 1em;
                    transition: background-color 0.3s, transform 0.3s;
                    display: block;
                    margin: 10px auto;
                    width: 80%;
                    position: relative;
                    overflow: hidden;
                    z-index: 0;
                }
                input[type="submit"]:hover, .btn-hard:hover {
                    background-color: #2980b9;
                    transform: scale(1.05);
                }
                input[type="submit"]::before, .btn-hard::before {
                    content: '';
                    position: absolute;
                    top: 0;
                    left: -100%;
                    width: 200%;
                    height: 100%;
                    background: linear-gradient(90deg, rgba(255,255,255,0.1), rgba(255,255,255,0.5), rgba(255,255,255,0.1));
                    transition: left 0.5s ease-in-out;
                    z-index: -1;
                }
                input[type="submit"]:hover::before, .btn-hard:hover::before {
                    left: 100%;
                }
                .greeting-container {
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <div class="container" id="form-container">
                <h1>Welcome to Ginger Juice Shop!</h1>
                <form method="POST" action="/greet">
                    <input type="text" name="name" placeholder="Enter your name" required>
                    <input type="submit" value="Greet">
                </form>
                <button class="btn-hard" onclick="window.location.href='/hard'">Go to Hard Challenge</button>
            </div>
            <div class="greeting-container" id="greeting-container" style="display: none;">
            </div>
        </body>
        </html>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', '')
    template = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ginger Juice Shop</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #f2f2f2;
                    color: #333;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-image: url('https://images.unsplash.com/photo-1682530016867-6fcc63df0cfb?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
                    background-size: cover;
                    background-position: center;
                }
                .container {
                    background-color: #FFFFFF;
                    padding: 40px;
                    border-radius: 15px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    text-align: center;
                }
                h2 {
                    color: #3498db;
                    font-size: 2em;
                }
                a {
                    text-decoration: none;
                    color: #3498db;
                    font-weight: bold;
                    display: inline-block;
                    margin-top: 20px;
                    font-size: 1.2em;
                }
                a:hover {
                    color: #2980b9;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Hello, ''' + name + '''! Welcome to Ginger Juice Shop!</h2>
                <a href="/">Back to Home</a>
            </div>
        </body>
        </html>
    '''
    return render_template_string(template)

# More complex SSTI challenge at /hard
@app.route('/hard', methods=['GET', 'POST'])
def hard():
    if request.method == 'POST':
        name = request.form.get('name', '')
        
        # Basic input validation to block common SSTI patterns
        blacklist = ['__', 'class', 'mro', 'subclasses', 'eval', 'exec', 'import', 'os', 'sys', '.', '_', 'config']
        if any(keyword in name for keyword in blacklist):
            return "Invalid input detected! You might need to Try Hard!!", 400

        template = '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Advanced Ginger Juice Shop</title>
                <style>
                    body {
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        background-color: #f2f2f2;
                        color: #333;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        background-image: url('https://images.unsplash.com/photo-1709477992494-34e084eb1779?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
                        background-size: cover;
                        background-position: center;
                    }
                    .container {
                        background-color: #ffffff;
                        padding: 40px;
                        border-radius: 15px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                        text-align: center;
                    }
                    h2 {
                        color: #3498db;
                        font-size: 2em;
                    }
                    a {
                        text-decoration: none;
                        color: #3498db;
                        font-weight: bold;
                        display: inline-block;
                        margin-top: 20px;
                        font-size: 1.2em;
                    }
                    a:hover {
                        color: #2980b9;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h2>Hello, ''' + name + '''! Was it this hard?</h2>
                    <a href="/hard">Back to Hard Challenge</a>
                </div>
            </body>
            </html>
        '''
        return render_template_string(template)

    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Advanced Ginger Juice Shop</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #f2f2f2;
                    color: #333;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-size: cover;
                    background-position: center;
                }
                .container {
                    background-color: rgba(255, 255, 255, 0.9);
                    padding: 40px;
                    border-radius: 15px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    text-align: center;
                }
                h1 {
                    color: #3498db;
                    font-size: 2em;
                    margin-bottom: 20px;
                }
                input[type="text"] {
                    padding: 12px;
                    width: 80%;
                    margin-bottom: 20px;
                    border: 2px solid #ccc;
                    border-radius: 5px;
                    font-size: 1em;
                }
                input[type="submit"] {
                    background-color: #3498db;
                    color: white;
                    border: none;
                    padding: 12px 25px;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 1em;
                    transition: background-color 0.3s, transform 0.3s;
                    display: block;
                    margin: 10px auto;
                    width: 80%;
                    position: relative;
                    overflow: hidden;
                    z-index: 0;
                }
                input[type="submit"]:hover {
                    background-color: #2980b9;
                    transform: scale(1.05);
                }
                input[type="submit"]::before {
                    content: '';
                    position: absolute;
                    top: 0;
                    left: -100%;
                    width: 200%;
                    height: 100%;
                    background: linear-gradient(90deg, rgba(255,255,255,0.1), rgba(255,255,255,0.5), rgba(255,255,255,0.1));
                    transition: left 0.5s ease-in-out;
                    z-index: -1;
                }
                input[type="submit"]:hover::before {
                    left: 100%;
                }
                .greeting-container {
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <div class="container" id="form-container">
                <h1>Welcome to the Advanced Ginger Juice Shop!</h1>
                <form method="POST" action="/hard">
                    <input type="text" name="name" placeholder="Enter your name" required>
                    <input type="submit" value="Submit">
                </form>
            </div>
            <div class="greeting-container" id="greeting-container" style="display: none;">
            </div>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
