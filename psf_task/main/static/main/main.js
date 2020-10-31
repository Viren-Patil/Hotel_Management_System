const SpinnerBox = document.getElementById('spinner-box')
const DataBox = document.getElementById('data-box')

// console.log(SpinnerBox)
// console.log(DataBox)

var urls = ['/main/welcome/','/main/home-customer/', '/main/booking/', '/main/table-booking/',
			'/main/my-bookings/', '/main/payment/', '/main/gallery/', '/main/contact/'];

$.each(urls, function(i,u){
	$.ajax(u,
		{
			type: 'GET',
			success: function(response){
				SpinnerBox.classList.add('not-visible')
				// console.log('response',response)
			},
			error: function(error){
				console.log(error)
			}
		}
	);
});
