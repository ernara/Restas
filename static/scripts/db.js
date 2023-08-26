function getItemsFromDb() {
    $.get("/api/items/fromdb", function(data) {
        console.log(data);
    });
}

function addItemToDb(itemName) {
    $.ajax({
        url: "/api/items",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({ "name": itemName }),
        success: function() {
            console.log("Item added to database");
        }
    });
}

function updateItemInDb(itemId, newName) {
    $.ajax({
        url: "/api/items/fromdb/" + itemId,
        type: "PUT",
        contentType: "application/json",
        data: JSON.stringify({ "name": newName }),
        success: function() {
            console.log("Item updated in database");
        }
    });
}

window.updateItemInDb = updateItemInDb;

window.getItemsFromDb = getItemsFromDb;
window.addItemToDb = addItemToDb;
