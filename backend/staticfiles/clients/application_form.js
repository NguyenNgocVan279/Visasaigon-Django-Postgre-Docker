document.addEventListener("DOMContentLoaded", function() {
    const addButton = document.getElementById("add-file-row");
    const tableBody = document.querySelector("#file-upload-table tbody");

    // Lấy tổng số form hiện tại
    let totalForms = document.querySelector('#id_form-TOTAL_FORMS');
    
    addButton.addEventListener("click", function() {
        // index mới = TOTAL_FORMS
        const newIndex = parseInt(totalForms.value);

        // Clone dòng đầu tiên
        const emptyRow = tableBody.querySelector('tr').cloneNode(true);

        // Reset input value
        emptyRow.querySelectorAll('input, select').forEach(function(input) {
            if (input.type === 'file') {
                input.value = "";
            } else if (input.type === 'checkbox') {
                input.checked = false;
            } else {
                input.value = "";
            }

            // Update name & id theo index mới
            input.name = input.name.replace(/\d+/, newIndex);
            input.id = input.id.replace(/\d+/, newIndex);
        });

        // Append row mới
        tableBody.appendChild(emptyRow);

        // Update TOTAL_FORMS
        totalForms.value = newIndex + 1;
    });
});
