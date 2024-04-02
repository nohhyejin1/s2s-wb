const baseURL = 'http://127.0.0.1:8000/'

function addToCart(item_id) {
    fetch(baseURL + "add/cart", {
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