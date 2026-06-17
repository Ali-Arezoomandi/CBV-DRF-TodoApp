todoContainer = document.getElementById("todoList");

async function getTodos() {
    const response = await fetch("/api/v1/task/");
    const data = await response.json();

    data.forEach((task) => {
        if (task.completed) {
            todoContainer.innerHTML += `
                <li class="todo-item">
                    <div class="todo-left">
                        <h3>${task.title}</h3>
                    </div>
                    <div class="todo-right">
                        <div class="change-task">
                            <a href="/delete/${task.id}/" class="delete-btn"><i class="fas fa-trash-alt"></i></a>
                            <a href="/update/${task.id}/" class="edit-btn"><i class="fas fa-edit"></i></a>
                        </div>
                        <div class="status-container">
                            <span class="status">Completed</span>
                            <i class="fa-regular fa-circle-check" style="color: #22c55e; font-size: 1   rem; filter: drop-shadow(0 0 8px #22c55e);"></i>
                        </div>
                    </div>
                </li>
            `;
        } else {
            todoContainer.innerHTML += `
                <li class="todo-item">
                    <div class="todo-left">
                        <h3>${task.title}</h3>
                    </div>
                    <div class="todo-right">
                        <div class="change-task">
                            <a href="/delete/${task.id}/" class="delete-btn"><i class="fas fa-trash-alt"></i></a>
                            <a href="/update/${task.id}/" class="edit-btn"><i class="fas fa-edit"></i></a>
                        </div>
                        <div class="status-container">
                            <span class="status">InCompleted</span>
                            <i class="fa-regular fa-circle-xmark" style="color: #ef4444; font-size: 1rem; filter: drop-shadow(0 0 8px #ef4444);"></i>
                        </div>
                    </div>
                </li>
            `;
        }
    });
}

getTodos();
