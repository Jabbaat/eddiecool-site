# generate_site.py

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Eddiecool - AI Art Platform</title>
    <style>
        body {
            background-color: #111;
            color: #eee;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        h1 {
            color: #00ffd5;
        }
        p {
            max-width: 600px;
            margin: auto;
        }
    </style>
</head>
<body>
    <h1>Welcome to Eddiecool</h1>
    <p>A platform for self-made AI art including videos and images.</p>
    <p>More coming soon!</p>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Website created! Check the 'index.html' file.")
