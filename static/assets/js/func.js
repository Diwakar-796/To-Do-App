console.log("Testing...");

$(document).ready(function () {
    $("#filterPanel form").on("submit", function (e) {
        e.preventDefault();  // STOP normal form submission

        let id = $("#filterOption").val(); // get selected category id

        console.log("Id:", id);

        $.ajax({
            url: "/filter-task/",
            type: "GET",   // match your Django view (uses request.GET)
            data: {
                "id": id
            },
            dataType: "json",
            beforeSend: function () {
                console.log("Filtering...");
            },
            success: function (response) {
                console.log("Filtered...");
                console.log(response);

                // Update the task list dynamically
                $("#tod0-list").html(response.data);
            }
        });
    });
});