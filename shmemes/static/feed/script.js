
async function like(elem) {
    const url = '/feed/api/like/'
    const post_elem = elem.closest('.card')

    const response = await requestPost(url, {post_id: post_elem.getAttribute('data-post')});
    console.log(response.status);
}
async function dislike(elem) {
    console.log(elem)
    const url = '/feed/api/dislike/'
    const post_elem = elem.closest('.card')

    const response = await requestPost(url, {post_id: post_elem.getAttribute('data-post')});
    console.log(response.status);
}