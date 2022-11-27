
async function like(elem) {
    const url = '/feed/api/like/'
    const post_elem = elem.closest('.card')

    const response = await requestPost(url, {post_id: post_elem.getAttribute('data-post')});
    if (response.status === 'ok') {
        let likes_number = elem.querySelector('.likes-number');
        likes_number.textContent = +likes_number.textContent + 1; 
    }
}
async function dislike(elem) {
    const url = '/feed/api/dislike/'
    const post_elem = elem.closest('.card')

    const response = await requestPost(url, {post_id: post_elem.getAttribute('data-post')});
    if (response.status === 'ok') {
        let dislikes_number = elem.querySelector('.dislikes-number');
        dislikes_number.textContent = +dislikes_number.textContent + 1; 
    }
}

async function get_comments(elem) {
    const url = '/feed/api/getcomments/';
    const post_elem = elem.closest('.card')
    const data = {
        post_id: post_elem.getAttribute('data-post')
    }
    const response = await requestPost(url, data);
    if (response.status === 'ok') location.reload();
}


async function add_comment(elem) {
    const url = '/feed/api/addcomment/';
    const post_elem = elem.closest('.modal')
    const comment_text = elem.closest('.input-group').querySelector('.form-control');

    const data = {
        post_id: post_elem.getAttribute('data-post'), 
        text: comment_text.value
    }
    const response = await requestPost(url, data);
    
    if (response.status === 'ok') location.reload();
}

document.querySelectorAll('.post-toggler').forEach(btn => {
    btn.addEventListener('click', async function() {
        const post_id = btn.closest('.card').getAttribute('data-post');
        const commentContainer = document.getElementById(`postModal_${post_id}`).querySelector('.commentContainer'); 

        if (commentContainer.children.length > 0) return;
        
        const response = await get_comments(btn);
        for (let comment of response.comments) {
            let commentElem = document.createElement('div');
            commentElem.classList.add('comment-block');

            let commentAuthor = document.createElement('a'); 
            commentAuthor.setAttribute('href', `/user/${comment.author.id}`);
            commentAuthor.textContent = `${comment.author.name}: `;

            let commentContent = document.createElement('span'); 
            commentContent.textContent = comment.text

            commentElem.append(commentAuthor);
            commentElem.append(commentContent);

            commentContainer.append(commentElem);
        };
    })
});