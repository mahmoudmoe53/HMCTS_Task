const form = document.getElementById('task-form');
const taskList = document.getElementById('task-list');


function renderTask(task) {
  return `
    <div class="flex items-center justify-between p-4 bg-gray-50 rounded-xl shadow-sm">
      <div>
        <h3 class="text-lg font-semibold
          ${task.status === 'done' ? 'line-through text-gray-400' : ''}
          ${task.status === 'in-progress' ? 'text-yellow-600' : ''}">
          ${task.title}
        </h3>
        ${task.description ? `<p class="text-sm text-gray-600">${task.description}</p>` : ""}
        ${task.due_date ? `<p class="text-xs text-gray-500">Due: ${task.due_date}</p>` : ""}
      </div>

      <div class="flex gap-2">
        ${task.status !== "done"
          ? `<button onclick="updateTask(${task.id}, 'done')" class="px-3 py-1 text-xs bg-green-500 text-white rounded-lg hover:bg-green-600">Done</button>`
          : ""}
        <button onclick="deleteTask(${task.id})" class="px-3 py-1 text-xs bg-red-500 text-white rounded-lg hover:bg-red-600">Delete</button>
      </div>
    </div>
  `;
}




async function loadTasks() {
  taskList.innerHTML = '';
  const res = await fetch('/api/tasks');
  const tasks = await res.json();
  tasks.forEach(task => {
    const div = document.createElement('div');
    div.innerHTML = renderTask(task);
    taskList.appendChild(div);
  });
}





form.addEventListener('submit', async e => {
  e.preventDefault();
  const data = {
    title: document.getElementById('title').value,
    description: document.getElementById('description').value,
    status: document.getElementById('status').value,
    due_date: document.getElementById('due_date').value || null
  };

  await fetch('/api/tasks', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data)
  });

  form.reset();
  loadTasks();
});


async function deleteTask(id) {
  await fetch(`/api/tasks/${id}`, {method: 'DELETE'});
  loadTasks();
}

async function updateTask(id, status) {
  await fetch(`/api/tasks/${id}`, {
    method: 'PATCH',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({status})
  });
  loadTasks();
}


loadTasks();
