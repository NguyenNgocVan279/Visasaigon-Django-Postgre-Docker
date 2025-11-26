document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('contactForm');
    const messageDiv = document.getElementById('contact_message');

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const formData = new FormData(form);
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        fetch(form.action, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Accept': 'application/json',
            },
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            messageDiv.textContent = data.message || 'Gửi thành công!';
            messageDiv.style.color = 'green';
            form.reset();
        })
        .catch(error => {
            messageDiv.textContent = 'Đã có lỗi xảy ra. Vui lòng thử lại.';
            messageDiv.style.color = 'red';
            console.error('Fetch error:', error);
        });
    });
});
