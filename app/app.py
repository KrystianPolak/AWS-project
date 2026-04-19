from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

todos = ["Nauczyć się CI/CD", "Skonfigurować GitHub Actions"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        new_task = request.form.get('task')
        if new_task:
            todos.append(new_task)
        return redirect(url_for('index'))
    
    delete_id = request.args.get('delete')
    if delete_id is not None and delete_id.isdigit():
        idx = int(delete_id)
        if 0 <= idx < len(todos):
            todos.pop(idx)
        return redirect(url_for('index'))

    html = """
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <title>GitOps To-Do App</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f7f9fc; color: #333; display: flex; justify-content: center; padding-top: 50px; }
            .container { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); width: 100%; max-width: 400px; }
            h1 { text-align: center; color: #2c3e50; font-size: 24px; }
            form { display: flex; gap: 10px; margin-bottom: 20px; }
            input[type="text"] { flex: 1; padding: 10px; border: 1px solid #ddd; border-radius: 6px; outline: none; }
            input[type="text"]:focus { border-color: #13ba3c; }
            button { background-color: #13ba3c; color: white; border: none; padding: 10px 15px; border-radius: 6px; cursor: pointer; transition: 0.3s; }
            button:hover { background-color: #16a639; }
            ul { list-style-type: none; padding: 0; margin: 0; }
            li { background: #fdfdfd; border: 1px solid #eee; margin-bottom: 10px; padding: 12px; border-radius: 6px; display: flex; justify-content: space-between; align-items: center; }
            a.delete { color: #e74c3c; text-decoration: none; font-weight: bold; padding: 5px 10px; border-radius: 4px; }
            a.delete:hover { background-color: #ffeaea; }
            .footer { text-align: center; margin-top: 20px; font-size: 12px; color: #aaa; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Moja Lista Zadań</h1>
            
            <form method="POST" action="/">
                <input type="text" name="task" placeholder="Co jest do zrobienia?" autocomplete="off" required>
                <button type="submit">Dodaj</button>
            </form>

            <ul>
                {% for i in range(todos|length) %}
                    <li>
                        {{ todos[i] }}
                        <a href="/?delete={{ i }}" class="delete">✕</a>
                    </li>
                {% else %}
                    <li style="justify-content: center; color: #888;">Brak zadań. Brawo! 🎉</li>
                {% endfor %}
            </ul>
            
            <div class="footer">Działa w kontenerze Docker! 🐳</div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, todos=todos)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)