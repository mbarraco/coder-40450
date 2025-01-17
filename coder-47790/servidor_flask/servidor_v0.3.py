from flask import Flask

app = Flask("mi_servidor")


@app.route("/")
def home():
    return """
                    <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Welcome Message</title>
            <style>
                /* Basic styling for centered content and font */
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #f5f5f5;
                }
                .welcome-container {
                    background-color: #ffffff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                }
            </style>
        </head>
        <body>
            <div class="welcome-container">
                <h1>Welcome to Our Page!</h1>
                <p>This is a simple welcome message for beginner students learning HTML.</p>
            </div>
        </body>
        </html>

        """


app.run(debug=True, port=8182)
