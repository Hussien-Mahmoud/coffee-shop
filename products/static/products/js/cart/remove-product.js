function remove_product(slug) {
    let product_cart_element = document.getElementById(slug)
    let quantity_element = product_cart_element.getElementsByClassName('value')[0]
    let index = cart_items.findIndex((item) => {return item.slug === slug})
    let quantity = cart_items[index].quantity
    if (quantity > 1){
        // update the elements
        quantity_element.textContent = (quantity - 1).toString()
        //update cart_items
        cart_items[index].quantity -= 1
    }else{
        product_cart_element.remove()
        cart_items.splice(index, 1)
    }

    let url = '/api/products/remove/' + slug + '/'
    let method = 'DELETE'

    let csrftoken = getCookie('csrftoken')

    fetch(url, {
        method: method,
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        mode: 'same-origin',
    })
    .then((resp) => resp.json())
    .then(function (data) {})
}