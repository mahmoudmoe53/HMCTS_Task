const form = document.getElementById('task-form');
const taskList = document.getElementById('task-list');


async function loadTasks() {
  taskList.innerHTML = '';
  const res = await fetch('/api/tasks');
  const tasks = await res.json();
  tasks.forEach(task => {
    const li = document.createElement('li');
    li.innerHTML = `
      <strong>${task.title}</strong> [${task.status}]
      <button onclick="deleteTask(${task.id})">Delete</button>
      <button onclick="markDone(${task.id})">Done</button>
    `;
    taskList.appendChild(li);
  });
}


form.addEventListener('submit', async e => {
  e.preventDefault();
  const data = {
    title: document.getElementById('title').value,
    description: document.getElementById('description').value,
    status: document.getElementById('status').value || 'todo',
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


async function markDone(id) {
  await fetch(`/api/tasks/${id}`, {
    method: 'PATCH',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({status: 'done'})
  });
  loadTasks();
}

loadTasks();
