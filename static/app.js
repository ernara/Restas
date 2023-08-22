function updateTaskList() {
    console.log('Updating task list...');
    fetch('/get_tasks')
        .then(response => response.json())
        .then(data => {
            console.log('Received data:', data);
            const taskListContainer = document.getElementById('taskList');
            taskListContainer.innerHTML = ""; // Clear the container

            data.forEach(task => {
                const taskElement = document.createElement('div');
                taskElement.textContent = task.title; // Display the task title
                taskListContainer.appendChild(taskElement);
            });
        })
        .catch(error => console.error('Error:', error));
}




// Function to create a task
function createTask() {
    var titleInput = document.getElementById("taskTitle");
    var title = titleInput.value;

    if (title) {
        fetch('/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 'title': title }),
        })
        .then(response => response.json())
        .then(data => {
            // Clear the input and update the task list
            titleInput.value = "";
            updateTaskList();
        })
        .catch(error => console.error('Error:', error));
    }
}

// Function to delete a task
function deleteTask(taskId) {
    fetch(`/tasks/${taskId}`, {
        method: 'DELETE'
    })
    .then(response => {
        if (response.ok) {
            updateTaskList(); // Update the task list after deleting a task
        } else {
            console.error('Error deleting task');
        }
    })
    .catch(error => console.error('Error:', error));
}

// Load the initial task list when the page is loaded
console.log('Page loaded. Initiating task list update.');
window.onload = updateTaskList;
