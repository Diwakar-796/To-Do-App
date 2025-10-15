const todoList = document.getElementById('todo-list');
const alertBox = document.getElementById('update-alert');
const addTaskBtn = document.getElementById('add-task-btn');
const newTaskInput = document.getElementById('new-task-input');

// Function to create a new task item
function createTaskItem(taskText) {
  const li = document.createElement('li');
  li.className = "list-group-item bg-transparent text-light d-flex justify-content-between align-items-center";
  li.innerHTML = `
    <div class="d-flex align-items-center flex-grow-1">
      <input type="checkbox" class="form-check-input me-2">
      <span class="task-label flex-grow-1">${taskText}</span>
      <input type="text" class="form-control edit-input d-none flex-grow-1" value="${taskText}">
    </div>
    <div class="btn-group btn-group-sm">
      <button type="button" class="btn btn-outline-primary edit-btn">
        <i class="bi bi-pencil"></i>
      </button>
      <button type="button" class="btn btn-outline-success save-btn d-none">
        <i class="bi bi-check"></i>
      </button>
      <button type="button" class="btn btn-outline-danger delete-btn">
        <i class="bi bi-trash"></i>
      </button>
    </div>
  `;
  return li;
}

// Add task functionality
addTaskBtn.addEventListener('click', () => {
  const taskText = newTaskInput.value.trim();
  if (taskText !== "") {
    const newTask = createTaskItem(taskText);
    todoList.appendChild(newTask);
    newTaskInput.value = "";
  }
});

// Allow Enter key to add task
newTaskInput.addEventListener('keypress', (e) => {
  if (e.key === "Enter") {
    addTaskBtn.click();
  }
});

// Handle edit, save, delete
todoList.addEventListener('click', function(event) {
  const editBtn = event.target.closest('.edit-btn');
  const saveBtn = event.target.closest('.save-btn');
  const deleteBtn = event.target.closest('.delete-btn');

  if (editBtn) {
    const li = editBtn.closest('li');
    const label = li.querySelector('.task-label');
    const input = li.querySelector('.edit-input');
    const editButton = li.querySelector('.edit-btn');
    const saveButton = li.querySelector('.save-btn');
    label.classList.add('d-none');
    input.classList.remove('d-none');
    input.value = label.textContent.trim();
    input.focus();
    editButton.classList.add('d-none');
    saveButton.classList.remove('d-none');
  }
  if (saveBtn) {
    const li = saveBtn.closest('li');
    const label = li.querySelector('.task-label');
    const input = li.querySelector('.edit-input');
    const editButton = li.querySelector('.edit-btn');
    const saveButton = li.querySelector('.save-btn');
    label.textContent = input.value.trim();
    input.classList.add('d-none');
    label.classList.remove('d-none');
    saveButton.classList.add('d-none');
    editButton.classList.remove('d-none');
    alertBox.classList.remove('d-none');
    alertBox.classList.add('show');
  }
  if (deleteBtn) {
    deleteBtn.closest('li').remove();
  }
});