var total_amt = 0;
var all_items_price = 0;

cart = JSON.parse(localStorage.getItem('cart'));
if (cart != null){cart_products = Object.keys(cart);} else {cart_products = [];}
console.log(cart_products)

product_card = document.getElementById('product-card');
review_products = document.getElementById('review-products');

function showProducts(){
  if(cart_products.length != 0){
    cart_products.forEach((value)=>{
      value = value.slice(2) // get only id
      products_list.forEach((product)=>{

        if(product[0] == value){
			if(product_card != null){
				console.log('inside cart');
				document.querySelector('.cart-is-empty-text').style.visibility = 'hidden';
				dis = (product[2]*product[4])/100 + product[2];
				let node = document.createElement('div');
				node.id = 'pr' + value;
				node.classList.add('row')
				node.innerHTML = `<div class='col-12 col-md-2'>
								<div class='img-container'>
								<img style='height: 100%;' src='/media/${product[3]}' alt='product image'>
							</div>
							<div class='quantity'>
								<i class='fas fa-plus plus-btn'></i>
								<input class='quant-input  mx-2' type='text' name='name' value='${cart["pr"+value]}'>
								<i class='fas fa-minus minus-btn'></i>
							</div>
							</div>
							<div class='col-12 col-md-7'>
								<p id='name'>${product[1]}</p>
								<p class='seller'>Seller: Truecom</p>
								<h5 class='price my-2'><b>₹${product[2]}</b></h5><span class='fprice px-2 my-2'>₹${dis}</span><span class='discount my-2'>${product[4]}% off</span>
								<br class='mb-3'><a id='add-to-wish' class='secondary-txt' href='#'>SAVE FOR LATER</a><a id='remove-item-pr${value}' class='secondary-txt remove-item' href='#'>REMOVE</a>
							</div>
							<div class='col-12 col-md-3'>
								Delivery in 3-4 days | 
								7 days replacement policy
							</div>`;
				product_card.appendChild(node);
			}

			else if(review_products != null){
				console.log(product[1]);
				document.querySelector('.cart-is-empty-text').style.visibility = 'hidden';
				let node = document.createElement('li');
				node.classList.add('list-group-item');
				node.classList.add('d-flex');
				node.classList.add('justify-content-between');
				node.classList.add('align-items-center');
				node.innerHTML = `${product[1]}<span class="badge bg-light text-dark" style="font-size:14px;">x  ${cart["pr"+value]}</span>`;
				review_products.appendChild(node);
			}
			all_items_price += product[2];
			let quantity = cart["pr"+value];
			let one_item_price = product[2] * quantity;
			total_amt += one_item_price;
			return;
			
        }
        
      });
      

    });
	document.querySelector('#total-amt').innerText += all_items_price;
	document.querySelector('.total-amount-num').innerText += total_amt;
    // document.getElementById('product-card').innerHTML = inner_html;
  }
}
console.log('script working finne')
document.getElementById('total-item').innerText = cart_products.length;