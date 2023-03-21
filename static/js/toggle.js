let cartItem = document.querySelector('.cart-items-container');
let navbar = document.querySelector('.navbar');
let searchForm = document.querySelector('.search-form');

function cart_toggle(){
    cartItem.classList.toggle('active');
    navbar.classList.remove('active');
    searchForm.classList.remove('active');
}

document.querySelector('#menu-btn').onclick = () =>{
    navbar.classList.toggle('active');
    searchForm.classList.remove('active');
    cartItem.classList.remove('active');
}

document.querySelector('#search-btn').onclick = () =>{
    searchForm.classList.toggle('active');
    navbar.classList.remove('active');
    cartItem.classList.remove('active');
}

document.querySelector('#cart-btn').onclick = cart_toggle

// window.onscroll = () =>{
//     navbar.classList.remove('active');
//     searchForm.classList.remove('active');
//     cartItem.classList.remove('active');
// }