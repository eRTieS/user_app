function getCSRF() {
    return {"X-CSRFToken": "{{ csrf_token }}"}
}

function users() {
    dynamicSearchAjaxRef = $.ajax({
        type: "GET",
        url: '/list-users',
        beforeSend: function() {
            if (dynamicSearchAjaxRef != null && dynamicSearchAjaxRef.readyState !== 4) {
                dynamicSearchAjaxRef.abort();
            }
        },
        complete: function(data) {
            console.log(data);
            console.log($(".list"))
            $(".list").html(data.responseText);
        }
    });
}
