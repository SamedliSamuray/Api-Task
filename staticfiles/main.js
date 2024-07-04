let cards=document.getElementById('cards');


fetch('http://127.0.0.1:8000/blog-api/list/')
.then(response => response.json())
.then(response => {
    console.log(response)
})