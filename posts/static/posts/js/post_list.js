/*
var pageNo = 1;
var pageHasNext = true;
var url = 'post_api/'

// Scroll function
$(window).on("scroll", function(){
    var scrollHeight = $(document).height();
    var scrollPosition = $(window).height() + $(window).scrollTop();
    if ((scrollHeight - scrollPosition) / scrollHeight === 0){
        getData()
    }
});


// load data from json and hook to the html document
function getData(){
    if (pageHasNext === false){
        return false;
    };

    pageNo = pageNo + 1;
    var requestUrl = url + pageNo;

    $.ajax({
        type: 'GET',
        url: requestUrl,
        dataType: 'json',
        success: function(response){
            // update the page has next from response object
            pageHasNext = response.pageHasNext

            // Collect data from the response object to update our template
            var newPosts = []

            $.each(response.newPostList, function(index, post){

            });
        }
    });
};

<div class="row post-card no-gutters">
    <div class="col-md-4">
        <img class="card-img rounded-0" src="post.cover" alt="post.title">
    </div>
    <div class="col-md-8">
        <div class="card-block pl-md-3">
            <a href="post.url" class="unstyled-link">
                <h3>post.title</h3>
            </a>
            <p>post.content</p>
            <span class="mr-3">
                <i class="fa fa-calendar" aria-hidden="true"></i>&nbsp;post.updated
            </span>
            <span class="mr-3">
                <i class="fa fa-tag" aria-hidden="true"></i>
            </span>
        </div>
    </div>
    <hr/>
</div>
*/

/*
$.each(post.category, function(tagIndex, tag) {
    console.log(tag)
    // <a href="`, tag.url `" class="unstyled-link">&nbsp;`, tag.type, `</a>
});
*/