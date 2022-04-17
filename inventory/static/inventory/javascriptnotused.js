

// This file contains ideas that were not used

$(document).ready(function(){


	// This function used a get request to pass the lot number from the table to the backend.  From there a form was made with a post request
	// to modify the reagent.

	// I decided to still use the get request but use that to direct the user to another page containing a model form.  

	$(".modify-button").click(function() {

		// Getting name of reagent to pass to view to be processed
		var reagent_lot_from_table_specalist= $(this).attr("value")
		let cookie = document.cookie
		var csrfToken = cookie.substring(cookie.indexOf('=') + 1)

		$.ajax({

			url: '',
			type: 'GET',
			data: {

				reagent_lot_from_table_specalist: reagent_lot_from_table_specalist,
				

			},

			success: function(response) {
				// Passed in the id of the table data row for the reagent chosen.
				// Changing the text of that row to the updated amount
				// $(reagent_amount).text(response.table_updated_reagent_amount)
				
				if (response.current == true){
					
					$('#reagent-modify-modalLabel').html(response.reagent_name)
					$('#modify-modal-body').html(`


						<form method="POST" action="/specialist_information">
							<input type="hidden" name="csrfmiddlewaretoken" value=`+ csrfToken  + `>
							<input type="hidden" name="reagent_lot" id="hidden-name">
							
							<div class="mb-3">
								<label for="form-reagent-quantity" class="form-label">Reagent Quantity</label>
								<input type="number" class="form-control" id="form-reagent-lot-number" name="form-reagent-quantity" placeholder=`+ response.quantity + `>
							</div>
							<div class="mb-3">
								<label for="form-lot-number" class="form-label">Lot Number</label>
								<input type="text" class="form-control" id="form-lot-number" name="form-lot-number" placeholder=`+ response.lot + `>
							</div>
							<div class="mb-3">
								<label for="lot-number-expiration" class="form-label">Lot Expiration</label>
								<input type="text" class="form-control" id="reagent-lot-number-expiration" name="form-lot-expiration" placeholder=`+ response.expiration + `
								onfocus="(this.type='date')" onblur="(this.type='text')">
							</div>
							<div class="form-check">
							  <input class="form-check-input" type="checkbox" value="True" id="flexCheckDefault" name="form-current-lot" checked>
							  <label class="form-check-label" for="flexCheckDefault">
							    Current Lot?
							  </label>
							</div>
							<input type="submit" value="Submit" class="mt-4">
						</form> 



						`)

					// Anything space after the first word in response.reagent_name was getting put outside the "" for the hidden field
					// Added hidded field value with block of code below
					$('#hidden-name').attr("value" , response.lot)

				}

				else if (response.current == false) {
					
					$('#reagent-modify-modalLabel').html(response.reagent_name)
					$('#modify-modal-body').html(`


						<form method="POST" action="/specialist_information">
							<input type="hidden" name="csrfmiddlewaretoken" value=`+ csrfToken  + `>
							<input type="hidden" name="reagent_lot" id="hidden-name">

							<div class="mb-3">
								<label for="form-reagent-quantity" class="form-label">Reagent Quantity</label>
								<input type="number" class="form-control" id="form-reagent-lot-number" name="form-reagent-quantity" placeholder=`+ response.quantity + `>
							</div>
							<div class="mb-3">
								<label for="form-lot-number" class="form-label">Lot Number</label>
								<input type="text" class="form-control" id="form-lot-number" name="form-lot-number" placeholder=`+ response.lot + `>
							</div>
							<div class="mb-3">
								<label for="lot-number-expiration" class="form-label">Lot Expiration</label>
								<input type="text" class="form-control" id="reagent-lot-number-expiration" name="form-lot-expiration" placeholder=`+ response.expiration + `
								onfocus="(this.type='date')" onblur="(this.type='text')">
							</div>
							<div class="form-check">
							  <input class="form-check-input" type="checkbox" value="True" id="flexCheckDefault" name="form-current-lot">
							  <label class="form-check-label" for="flexCheckDefault">
							    Current Lot?
							  </label>
							</div>
							<input type="submit" value="Submit" class="mt-4">
						</form> 



						`)


					$('#hidden-name').attr("value" , response.lot)

				}
			}			

		})
	})



})

// function sortTableNum(n) {
//   var table, rows, switching, i, x, y, shouldSwitch;
//   table = document.getElementById("specialist-table");
//   switching = true;
//   /*Make a loop that will continue until
//   no switching has been done:*/
//   while (switching) {
//     //start by saying: no switching is done:
//     switching = false;
//     rows = table.rows;
//     /*Loop through all table rows (except the
//     first, which contains table headers):*/
//     for (i = 1; i < (rows.length - 1); i++) {
//       //start by saying there should be no switching:
//       shouldSwitch = false;
//       // Get the two elements you want to compare,
//       one from current row and one from the next:
//       x = rows[i].getElementsByClassName("sort-numerically")[n];
//       y = rows[i + 1].getElementsByClassName("sort-numerically")[n];
//       //check if the two rows should switch place:
//       if (Number(x.innerHTML) > Number(y.innerHTML)) {
//         //if so, mark as a switch and break the loop:
//         shouldSwitch = true;
//         break;
//       }
//     }
//     if (shouldSwitch) {
//       /*If a switch has been marked, make the switch
//       and mark that a switch has been done:*/
//       rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
//       switching = true;
//     }
//   }
// }

// $(document).on('submit','#tech-usage-form', function() {


		
		

// 		$.ajax({

// 			url: '',
// 			type: 'POST',
// 			data: {
// 				technologist_user: $('#technologist-selection option:selected').val(),
// 				csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
				
// 			},

// 			success: function(response) {
				

				
 				


// 			}			

// 		})
// 	})



// $(document).ready(function(){
// 	$(document).on('click', ".subtract-button", function() {

			
// 			var reagent_name_from_table= $(this).attr("value")
// 			var reagent_amount_from_table=$(this).closest('td').prev()
// 			console.log(reagent_amount_from_table)
// 			$.ajax({

// 				url: '',
// 				type: 'GET',
// 				data: {
// 					reagent_name_from_table: reagent_name_from_table
// 				},
// 				success: function(response) {
// 					alert("it worked")
// 					$(reagent_name_from_table).text(response.table_updated_reagent_amount)
// 				}
// 			});



// 	})

// });



	// $('#reagent_name').animate(
	// 	{deg: 0},
	// 	{

	// 		duration: 500,
	// 		step: function(now) {
	// 			$('#reagent_name').css({transform: 'rotate(' + now + 'deg)'})
	// 		}
	// 	}


	// )	
	// $('#reagent_name').animate({
	// 'marginTop' : "0px" //moves down
	// });


		// $('#reagent_name').animate(
	// 	{deg: -90},
	// 	{

	// 		duration: 500,
	// 		step: function(now) {
	// 			$('#reagent_name').css({transform: 'rotate(' + now + 'deg)'})
	// 		}
	// 	}


	// )	


	// $(document).ready(function(){
// 	$("#tech_col").hover(function(){
// 		$(this).animate({marginTop: '-=1%'},"fast");
// 	},function(){
// 		$(this).animate({marginTop: "0%"},"fast")
// 	}
// 	);
// });

// $(document).ready(function(){
// 	$("#tech_spec_col").hover(function(){
// 		$(this).animate({marginTop: '-=1%'},"fast");
// 	},function(){
// 		$(this).animate({marginTop: "0%"},"fast")
// 	}
// 	);
// });


