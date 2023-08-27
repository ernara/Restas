$(document).ready(function() {
    function loadItems() {
        $.get("/api/items/fromdb", function(data) {
            $("#items-list").empty();
            data.forEach(function(item) {
                var listItem = createListItem(item);
                $("#items-list").append(listItem);
            });
        });
    }

    function createListItem(item) {
        return `<li>${item.name} 
            <button class="update-button" data-id="${item.id}">Update</button>
            <button class="delete-button" data-id="${item.id}">Delete</button>
        </li>`;
    }

    function addItem() {
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
    }

    function updateItem(itemId) {
        var newName = prompt("Enter new item name:");
        if (newName !== null) {
            $.ajax({
                url: "/api/items/fromdb/" + itemId,
                type: "PUT",
                contentType: "application/json",
                data: JSON.stringify({ "name": newName }),
                success: function() {
                    loadItems();
                }
            });
        }
    }

    function deleteItem(itemId) {
        $.ajax({
            url: "/api/items/fromdb/" + itemId,
            type: "DELETE",
            success: function() {
                loadItems();
            }
        });
    }

    $("#add-button").click(function() {
        addItem();
    });

    $("#items-list").on("click", ".update-button", function() {
        var itemId = $(this).data("id");
        updateItem(itemId);
    });

    $("#items-list").on("click", ".delete-button", function() {
        var itemId = $(this).data("id");
        deleteItem(itemId);
    });

    loadItems();
});
