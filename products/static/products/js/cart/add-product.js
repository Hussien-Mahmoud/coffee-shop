function add_product(slug) {

    let product_cart_element = document.getElementById(slug)
    if (product_cart_element != null){
        let quantity_element = product_cart_element.getElementsByClassName('value')[0]
        let item = cart_items.find((item) => {return item.slug === slug})
        if (item !== undefined){
            let quantity = item.quantity
            // update the elements
            quantity_element.textContent = (quantity + 1).toString()
            //update cart_items
            item.quantity += 1
        }
        if (!cartItem.classList.contains('active')) {
            cart_toggle()
        }
    }


    let url = '/api/products/add/' + slug + '/'
    let method = 'POST'
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
    .then(function (data) {
        let product = data.selected_product
        if (product != null){
            if (product.quantity === 1) {
                add_product_elements(product)
                cart_items.push(product)

                if (!cartItem.classList.contains('active')) {
                    cart_toggle()
                }
            }
                // else if (product.quantity > 1) {
            //     // selected_product = cart_items.find((product) => { return product.slug === slug; })
            //     // console.log(selected_product)
            //     let product_cart_element = document.getElementById(slug)
            //     product_cart_element.getElementsByClassName('value')[0].textContent = product.quantity
            // }

        }
    })
}
