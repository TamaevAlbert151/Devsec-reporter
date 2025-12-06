import json
from datetime import datetime

def main():
    with open("report.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    issues = data.get("issues", [])

    html = "<html><body>"
    html += "<h1>Отчёт проверки</h1>"
    html += f"<p>Сгенерирован: {datetime.now()}</p>"
    html += "<table border='1' cellpadding='5'>"
    html += "<tr><th>Tool</th><th>Severity</th><th>Message</th><th>File</th><th>Line</th></tr>"

    for i in issues:
        html += f"<tr><td>{i['tool']}</td><td>{i['severity']}</td>"
        html += f"<td>{i['message']}</td><td>{i['file']}</td><td>{i['line']}</td></tr>"

    html += "</table></body></html>"

    with open("report.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("Готово! Файл report.html создан.")

if __name__ == "__main__":
    main()
