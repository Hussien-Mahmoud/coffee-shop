let cookie = document.cookie;
let cart_items = [];
let myHeaders = new Headers();
myHeaders.append("Cookie", cookie);
myHeaders.append("Accept", "application/json");

let requestOptions = {
    method: 'GET',
    headers: myHeaders,
    redirect: 'follow'
};

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function add_product_elements(selectedProduct) {
        let cartItem = document.createElement('div');
        cartItem.setAttribute('class', 'cart-item');
        cartItem.setAttribute('id', selectedProduct.slug);


        let span = document.createElement('span');
        span.setAttribute('class', 'fas fa-times');
        span.addEventListener('click', function () {
            remove_product(selectedProduct.slug)
        });

        let image = document.createElement('img');
        image.setAttribute('src', selectedProduct.image);
        image.setAttribute('alt', selectedProduct.name)

        let content = document.createElement('div');
        content.setAttribute('class', 'content');

        let name = document.createElement('h3');
        const nameText = document.createTextNode(selectedProduct.name);
        name.appendChild(nameText);
        
        let price_quantity_container = document.createElement('div');
        price_quantity_container.setAttribute('class', 'price-quantity-container');


        let price = document.createElement('div');
        price.setAttribute('class', 'price');
        const priceText = document.createTextNode(selectedProduct.price);
        price.appendChild(priceText);


        let quantity = document.createElement('div');
        quantity.setAttribute('class', 'quantity');

        let increase = document.createElement('button');
        increase.appendChild(document.createTextNode('+'));
        increase.addEventListener('click', function () {
            add_product(selectedProduct.slug)
        });

        let decrease = document.createElement('button');
        decrease.appendChild(document.createTextNode('-'));
        decrease.addEventListener('click', function () {
            remove_product(selectedProduct.slug)
        });

        let value = document.createElement('span');
        value.setAttribute('class', 'value')
        value.appendChild(document.createTextNode(selectedProduct.quantity));

        quantity.append(decrease)
        quantity.append(value)
        quantity.append(increase)

        price_quantity_container.append(price)
        price_quantity_container.append(quantity)

        content.append(name);
        content.append(price_quantity_container);

        cartItem.append(span);
        cartItem.append(image);
        cartItem.append(content);

        let container = document.querySelector('div.cart-items-container');
        let target = document.querySelector('div.cart-items-container > a.btn');
        container.insertBefore(cartItem, target)
}

fetch("/api/products/", requestOptions)
.then(response => response.json())
.then(value => {
    cart_items = value
    for (const selectedProduct of value) {
        add_product_elements(selectedProduct)
    }
})
.catch(error => console.log('error', error));

