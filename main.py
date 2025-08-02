from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)

# Each task: {'id', 'title', 'description', 'due_date', 'status'}
tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        task = {
            'id': str(uuid.uuid4()),
            'title': title,
            'description': description,
            'due_date': due_date,
            'status': 'Pending'
        }
        tasks.append(task)
        return redirect(url_for('index'))

    search = request.args.get('search', '').lower()
    status_filter = request.args.get('status', '')

    filtered = tasks
    if search:
        filtered = [t for t in filtered if search in t['title'].lower()]
    if status_filter == 'done':
        filtered = [t for t in filtered if t['status'] == 'Done']
    elif status_filter == 'pending':
        filtered = [t for t in filtered if t['status'] == 'Pending']

    return render_template('index.html', tasks=filtered, search=search, status=status_filter)

@app.route('/done/<task_id>')
def mark_done(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'Done' if task['status'] != 'Done' else 'Pending'
            break
    return redirect(url_for('index'))

@app.route('/delete/<task_id>')
def delete(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
