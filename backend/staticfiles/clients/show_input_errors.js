document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");

    form.addEventListener("submit", function(e) {
        let valid = true;

        // Xóa lỗi cũ trước khi kiểm tra
        form.querySelectorAll(".text-danger.custom-error").forEach(div => div.remove());

        form.querySelectorAll("input, textarea, select").forEach(function(input) {
            const isRequired = input.getAttribute("data-required");
            const label = input.getAttribute("data-label");

            if (isRequired && !input.value.trim()) {
                valid = false;

                // tạo div hiển thị lỗi ngay dưới input
                const error = document.createElement("div");
                error.classList.add("text-danger", "small", "custom-error");
                error.textContent = "Vui lòng nhập " + label + "!";

                // append vào parent (div col-md-6)
                input.parentNode.appendChild(error);
            }
        });

        if (!valid) {
            e.preventDefault(); // ngăn form submit nếu có lỗi
        }
    });
});
