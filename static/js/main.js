document.addEventListener('DOMContentLoaded', function() {
document.querySelectorAll('.delete-btn').forEach(btn => {
    btn.addEventListener('click', function() {
    if (!confirm('Are you sure you want to delete this student?')) return;
    const url = this.dataset.url;

    fetch(url, {
        method: 'POST',
        headers: {
        'X-CSRFToken': csrftoken,
        'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
        const row = this.closest('tr');
        if (row) row.remove();
        showMessage('Student deleted successfully.', 'success');
        const tbody = document.querySelector('tbody');
        if (!tbody.querySelector('tr')) {
            tbody.innerHTML = '<tr><td colspan="5">No students found.</td></tr>';
        }

        } else {
        showMessage('Delete failed.', 'error');
        }
    })
    .catch(err => {
        console.error(err);
        showMessage('Server error while deleting student.', 'error');
    });
    });
});

function showMessage(msg, type="success") {
    let container = document.querySelector('.messages');
    if (!container) {
    container = document.createElement('ul');
    container.className = 'messages';
    document.querySelector('.container').prepend(container);
    }
    const li = document.createElement('li');
    li.className = type;
    li.innerText = msg;
    container.appendChild(li);
    setTimeout(() => li.remove(), 3000);
}
});
