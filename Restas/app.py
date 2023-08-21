import uuid
import traceback
import logging
from flask import Flask, jsonify, request, render_template

app = Flask(__name__, template_folder='templates')

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

tasks = []

# Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.json
        title = data.get('title')
        
        if title is None:
            app.logger.error("Title is missing in request data.")
            return jsonify({'error': 'Title is required'}), 400
        
        new_task = {
            'id': str(uuid.uuid4()),  # Generate a unique ID
            'title': title,
            'done': False
        }
        
        tasks.append(new_task)
        app.logger.info(f"New task created: {new_task}")
        return jsonify(new_task), 201
    except Exception as e:
        error_message = str(e)  # Get the exception class and message
        app.logger.error(error_message)  # Log the exception class and message
        
        return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500
    
# Create a new route to render the task list template
@app.route('/view_tasks', methods=['GET'])
def view_tasks():
    return render_template('tasks.html', tasks=tasks)

@app.route('/tasks/<string:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task_to_delete = None
    for task in tasks:
        if task['id'] == task_id:
            task_to_delete = task
            break
    if task_to_delete:
        tasks.remove(task_to_delete)
        app.logger.info(f"Task deleted: {task_to_delete}")
        return jsonify({'message': 'Task deleted successfully'}), 200
    else:
        return jsonify({'error': 'Task not found'}), 404

# Run the app on port 8001
if __name__ == '__main__':
    app.run(port=8001, debug=True)


