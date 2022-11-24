
async function like(elem) {
    const url = '/feed/api/like/'
    const post_elem = elem.closest('.card')

    const response = await requestPost(url, {post_id: post_elem.getAttribute('data-post')});
    console.log(response.status);
}
async function dislike(elem) {
    const url = '/feed/api/dislike/'
    const post_elem = elem.closest('.card')

    const response = await requestPost(url, {post_id: post_elem.getAttribute('data-post')});
    console.log(response.status);
}

async function get_comments(elem) {
    const url = '/feed/api/getcomments/';
    const post_elem = elem.closest('.card')
    const data = {
        post_id: post_elem.getAttribute('data-post')
    }
    const response = await requestPost(url, data);
    console.log(response);
}

async function add_comment(elem) {
    const url = '/feed/api/addcomment/';
    const post_elem = elem.closest('.card')
    const data = {
        post_id: post_elem.getAttribute('data-post')
    }
    const response = await requestPost(url, data);
    console.log(response);
}