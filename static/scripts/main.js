$(document).ready(function() {
    // Load items on page load
    loadItems();

    // Add item button click event
    $("#add-button").click(function() {
        var itemName = $("#item-name").val();
        if (itemName !== "") {
            $.ajax({
                url: "/api/items",
                type: "POST",
                contentType: "application/json",
                data: JSON.stringify({ "name": itemName }),
                success: function() {
                    loadItems();
                    $("#item-name").val("");
                }
            });
        }
    });

    // Delete item event using event delegation
    $("#items-list").on("click", ".delete-button", function() {
        var itemId = $(this).data("id");
        $.ajax({
            url: "/api/items/" + itemId,
            type: "DELETE",
            success: function() {
                loadItems();
            }
        });
    });

    // Load items using AJAX
    function loadItems() {
        $.get("/api/items", function(data) {
            $("#items-list").empty();
            data.forEach(function(item) {
                var listItem = `<li>${item.name} <button class="delete-button" data-id="${item.id}">Delete</button></li>`;
                $("#items-list").append(listItem);
            });
        });
    }
});
