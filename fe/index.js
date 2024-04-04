const baseURL = 'https://be.rosieshop.domain.aws-team-demo.link'
// const baseURL = 'http://127.0.0.1:8000'

function addToCart(item_id) {
    fetch(baseURL + "/add/cart", {
        method: "POST",
        body: JSON.stringify({
            "user_id": "tester",
            "item_id": item_id
        }),
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
}

function getCart(item_id) {
    fetch(baseURL + "/cart", {
        method: "GET",
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
}
