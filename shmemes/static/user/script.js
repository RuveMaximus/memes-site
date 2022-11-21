async function login() {
    const user_login = document.getElementById('username');
    const user_password = document.getElementById('password'); 

    const response = await requestPost('/user/api/login/', {'username': user_login.value, 'password': user_password.value});

    if (response.status === 'fail') alert('Ошибка выполнения запроса')
}


async function register() {
    const user_login = document.getElementById('username');
    const user_password = document.getElementById('password'); 
    
    const response = await requestPost('/user/api/register/', {'username': user_login.value, 'password': user_password.value});

    if (response.status === 'fail') alert('Ошибка выполнения запроса')
}