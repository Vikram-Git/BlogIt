function getCategory(){

    getUrl = "/posts/category/"
    $.ajax({
        type: 'GET',
        url: getUrl,
        dataType: 'json',
        success: function(response){
            $.each(response.categoryList, function(index, category){
                var menu = "<a href='" + category.url + "'>" + category.type + "</a>"
                var menuDiv = "<div class='col-sm-4'>" + menu + "</div>"
                $('.my-menu').append(menuDiv);
            });
        },
    });
};

$(document).ready(function(){
    getCategory();
});
