window.onload = function () {
    $('.product_list').on('click', 'button', function () {
        let target = event.target;
        let productID = target.name;
        console.log(target);
        $.ajax({
            url: '/baskets/basket-add/' + productID + '/',
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        })
    })
}