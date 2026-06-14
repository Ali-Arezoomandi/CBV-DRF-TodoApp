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
                    <span>Completed</span>
                    <div>
                        <a href="/delete/${task.id}/" class="delete-btn"><i class="fas fa-trash-alt"></i></a>
                        <a href="/update/${task.id}/" class="edit-btn"><i class="fas fa-edit"></i></a>
                    </div>
                </li>
            `;
        } else {
            todoContainer.innerHTML += `
                <li class="todo-item">
                    <div class="todo-left">
                        <h3>${task.title}</h3>
                    </div>
                    <span>InCompleted</span>
                    <div>
                        <a href="/delete/${task.id}/" class="delete-btn"><i class="fas fa-trash-alt"></i></a>
                        <a href="/update/${task.id}/" class="edit-btn"><i class="fas fa-edit"></i></a>
                    </div>
                </li>
            `;
        }
    });
}

getTodos();
