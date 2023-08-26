$(document).ready(function() {
    function loadItems() {
        $.get("/api/items", function(data) {
            $("#items-list").empty();
            data.forEach(function(item) {
                var listItem = `<li>${item.name} 
                    <button class="update-button" data-id="${item.id}">Update</button>
                    <button class="delete-button" data-id="${item.id}">Delete</button>
                </li>`;
                $("#items-list").append(listItem);
            });
        });
    }

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

     $("#items-list").on("click", ".update-button", function() {
        var itemId = $(this).data("id");
        var newName = prompt("Enter new item name:");
        if (newName !== null) {
            $.ajax({
                url: "/api/items/" + itemId,
                type: "PUT",
                contentType: "application/json",
                data: JSON.stringify({ "name": newName }),
                success: function() {
                    loadItems();
                }
            });
        }
    });

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

    $(document).ready(function() {
        getItemsFromDb();
    });

    loadItems();
});
