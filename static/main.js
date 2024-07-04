let cards=document.getElementById('cards');


fetch('http://127.0.0.1:8000/blog-api/list/')
.then(response => response.json())
.then(response => {
    response.map((details)=> 
    {
        let card=document.createElement('div')
        card.classList.add('card')
        cards.append(card)
        let username=document.createElement('h2')
        username.classList.add('username')
        username.textContent=details.user_name
        let img=document.createElement('img')
        img.setAttribute('src',details.img)
        img.classList.add('card-img-top')
        let card_body=document.createElement('div')
        card_body.classList.add('card-body')
        let title=document.createElement('h5')
        title.classList.add('card-title')
        title.textContent=details.title
        let content=document.createElement('p')
        content.classList.add('card-text')
        content.textContent=details.content
        let button=document.createElement('a')
        button.classList.add('btn-primary')
        button.classList.add('btn')
        button.innerHTML='Buy'
        let datetime=document.createElement('h6')
        datetime.classList.add('card-date')
        if(details.formatted_createDate==details.formatted_updateDate){
            datetime.textContent=details.formatted_createDate
        }
        else{
            datetime.textContent=details.formatted_updateDate+' Düzəliş edildi'
        }
        card_body.append(username,title,content,button,datetime)
        card.append(img,card_body)
    })
})