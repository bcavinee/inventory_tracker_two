$('#department-form-button').click(function() {

	// Allows reagent name to be shown when button is clicked
	$('#reagent_name').delay("slow").show()



	// Moves reagent name down, then hides it, then moves it back to the top when hidden
	$('#reagent_name').delay("slow").animate({
	'marginTop' : "+=125px", //moves down
	},1100,function() {
		$('#reagent_name').hide()
		$("#reagent_name").css("margin-top", "0px")
	});


	// Opens lid
	$('#lid').delay("slow").animate(
		{deg: -90},
		{

			duration: 500,
			step: function(now) {
				$('#lid').css({transform: 'rotate(' + now + 'deg)'})
			}
		}


	)

	// Closes lid
	$('#lid').delay("slow").animate(
		{deg: 0},
		{

			duration: 500,
			step: function(now) {
				$('#lid').css({transform: 'rotate(' + now + 'deg)'})
			}
		}


	)



});
// $('#lid').css("transform", 'rotate(-80deg)')

// $("span").css({"transform": "rotate(-45deg)", "transition": "transform 250ms"});

$(document).on('submit','#user_reagent_selection', function(e) {

	e.preventDefault();

	// Same logic as GET request, using this to update table when user uses POST request

	// Getting the closest table data which would be the button itself, then getting the 
	// previous element which is the table data containing the amount.  From there getting the
	// id of that element
	var reagent_amount_from_table=$(".subtract-button").closest('td').prev().attr("id")

	// Taking the id of the element and prepending a # to be used for changing the reagent amount
	// Once updated
	var reagent_amount = "#" + reagent_amount_from_table
	
	$.ajax({


		type: 'POST',
		url:'',
		data: {

			reagent_choice: $('#id_reagent_choice').val(),
			amount_taken: $('#id_amount_taken').val(),
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

		},

		success:function(response) {


			
			if (response.reagent_exist == false) {

				$("#reagent_exist").text(response.reagent_name + " does not exist")
				$("#reagent_name").text("Sorry " + response.reagent_name + " Does Not Exist")
				$("#reagent_quantity").html('<img src="media/images/sad_resized.png">')
				$("#remaining").text('')
				$("#remove-success").text('')

			}

			else if (response.reagent_exist == true) {


				$("#reagent_exist").text("")
				$("#reagent_name").text(response.reagent_name)
				$("#reagent_quantity").text(response.updated_reagent_amount)
				$("#remaining").text('Remaining')
				$("#remove-success").text('Reagent Successfully Removed')		
		
			}

			if (response.updated_reagent_amount <= response.warning_level) {

				$('#reagent-modify-modal').modal("show")
			}
			
		}
	})


})





$(document).ready(function(){


	

	$(".subtract-button").click(function() {

		// Getting name of reagent to pass to view to be processed
		var reagent_lot_from_table= $(this).attr("value")

		// Getting the closest table data which would be the button itself, then getting the 
		// previous element which is the table data containing the amount.  From there getting the
		// id of that element
		var reagent_amount_from_table=$(this).closest('td').prev().attr("id")

		// Taking the id of the element and prepending a # to be used for changing the reagent amount
		// Once updated
		var reagent_amount = "#" + reagent_amount_from_table
		

		$.ajax({

			url: '',
			type: 'GET',
			data: {

				reagent_lot_from_table: reagent_lot_from_table

			},

			success: function(response) {
				// Passed in the id of the table data row for the reagent chosen.
				// Changing the text of that row to the updated amount
				$(reagent_amount).text(response.table_updated_reagent_amount)
				if (response.table_updated_reagent_amount <= response.reagent_warning_level) {
					$('#reagent-modify-modal').modal("show")
				}
				
			}			

		})
	})



})

$(document).on('submit','#modify-form', function(e) {



		// Getting name of reagent to pass to view to be processed
		var reagent_lot_from_table_specialist= $(this).attr("value")
		let cookie = document.cookie
		var csrfToken = cookie.substring(cookie.indexOf('=') + 1)

		$.ajax({

			url: '',
			type: 'POST',
			data: {
				csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
				reagent_lot_from_table_specialist: reagent_lot_from_table_specialist,
				
			},

			success: function(response) {
				
					
			}			

		})
	})


 


// Delete button AJAX call


$(document).ready(function(){

	$(".delete-button").click(function() {
		var reagent_lot_from_delete_button= $(this).attr("value")
		let cookie = document.cookie
		var csrfToken = cookie.substring(cookie.indexOf('=') + 1)
		
		$.ajax({

			url: '',
			type: 'GET',
			data: {

				reagent_lot_from_delete_button: reagent_lot_from_delete_button,

			},
			success: function(response) {

					$('#reagent-delete-modalLabel').html("<h3>Are you sure you want to delete</h3>")
					$('#delete-modal-body').html(`


						<form method="POST" action="/specialist_information" id="delete-form">
							<input type="hidden" name="reagent-lot-to-delete" id="hidden-name-to-delete">
							<input type="hidden" name="delete_equation_answer" id="delete_equation_answer">
							<input type="hidden" name="csrfmiddlewaretoken" value=`+ csrfToken  + `>

						
							<p>Enter answer to equation to remove:</p>
							<p>`+ response.equation_x+ ` `+ "+" + ` `+ response.equation_y +` `+ "=" + `</p>
							<p id="if_answer_is_wrong"></p>
							<input type="text" class="form-control" name="user_answer" id="user_equation_answer" placeholder="Enter Result">
							<input type="submit" value="Submit" class="mt-4">
														
						</form> 



						`)
					$('#hidden-name-to-delete').attr("value", response.reagent_lot_from_delete_button) 
					$('#delete_equation_answer').attr("value", response.delete_answer)

			}
		})
	})
})


$(document).on('submit', '#delete-form', function(e){

	var equation_answer= $("#delete_equation_answer").val()
	var user_answer= $("#user_equation_answer").val()

	if (equation_answer != user_answer) {

		$("#if_answer_is_wrong").text("Answer Incorrect")
		e.preventDefault()
	}

});



$(document).on('submit','#specialist_reagent_selection', function(e) {

	e.preventDefault();

	// Checking to see if user checked the Current Lot? box
	if ($('#specialist_current_lot_choice').is(":checked")) {
		var is_current_lot= "Current lot"
	}
	else {

		var is_current_lot= "Not current lot"
	}
	
	$.ajax({


		type: 'POST',
		url:'',
		data: {

			specialist_lot_choice: $('#specialist_lot_choice').val(),
			specialist_reagent_choice: $('#specialist_reagent_choice').val(),
			specialist_current_lot_choice: is_current_lot,
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

		},

		success:function(response) {

			// If the user did not select Current Lot? and the reagent exist, we loop through the returned array of lot numbers based on the reagent the user selected.
			// We then show the modal containing those lot numbers and add the values to the options to be selected
			if (response.specialist_current_lot_choice == "Not current lot" && response.reagent_exist == true){

				for (x=0; x < response.list_of_all_lot_numbers.length; x++) {

					$('#lot-selection-modal').modal("show")
					$("#lot_selection_dropdown").after(`<option class="dropdown-lot-choices" value="`+ response.list_of_all_lot_numbers[x] +`">`+ response.list_of_all_lot_numbers[x] + `</option>`)
				
				}

				//Adding the user selected reagent name to the id="chose-lot"
				$("#chose-lot").text(`Chose ` + response.reagent_name + ' Lot')
			}

			
			// If the selected reagent does not exist and the user did not check Current Lot?
			// We display to the user that the reagent does not exist
			else if (response.reagent_exist == false && response.specialist_current_lot_choice == "Not current lot") {
				
				$("#exist").text(response.specialist_reagent_choice + " does not exist")
 				$("#specialist_reagent_heading").html('<h1 class="text-dark bg-danger">' + response.specialist_reagent_choice  +' Does Not Exist</h1>')
 				$("#specialist_reagent_amount").text("")
 				$("#specialist_reagent_lot").text("")
 				$("#specialist_lot_date").text("")
 				$("#specialist_lot_current").text("")

			}
 			

			// Checking if user selected reagent exist and if the user selected Current Lot?
			// Displaying the lot information to the user  
			else if (response.reagent_exist == true && response.specialist_current_lot_choice == "Current lot") {
				$("#exist").text("")
 				$("#specialist_reagent_heading").text(response.reagent_name)
 				$("#specialist_reagent_amount").text(response.quantity)
 				$("#specialist_reagent_lot").text(response.lot)
 				$("#specialist_lot_date").text(response.expiration)
 				$("#specialist_lot_current").text(response.current)

			}


			else if (response.reagent_exist == false && response.specialist_current_lot_choice == "Current lot") {

				$("#exist").text(response.specialist_reagent_choice + " does not exist")
 				$("#specialist_reagent_heading").html('<h1 class="text-dark bg-danger">' + response.specialist_reagent_choice  +' Current Lot Does Not Exist</h1>')
 				$("#specialist_reagent_amount").text("")
 				$("#specialist_reagent_lot").text("")
 				$("#specialist_lot_date").text("")
 				$("#specialist_lot_current").text("")



			}
		}
	})


})


// There was an issue that if the user exited out of the modal it would run the for loop that adds to the selection options.
// If the user clicks the exit button in the modal the function below will fire
// The function clears the selection options
$(document).ready(function(){

  $("#lot-selection-close-button").click(function(){
    
  	$(".dropdown-lot-choices").remove()

  });
});







$(document).on('submit','#lot-selection-form', function(e) {


		e.preventDefault();
		

					
		
		$.ajax({

			url: '',
			type: 'POST',
			data: {
				specialist_lot_choice_from_modal: $('#lot-selection-dropdown-modal option:selected').val(),
				csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
				
			},

			success: function(response) {
				

				// When modal is submitted reagent information is displayed to the user
				$('#lot-selection-modal').modal('hide');
				$("#exist").text("")
 				$("#specialist_reagent_heading").text(response.reagent_name)
 				$("#specialist_reagent_amount").text(response.quantity)
 				$("#specialist_reagent_lot").text(response.lot)
 				$("#specialist_lot_date").text(response.expiration)
 				$("#specialist_lot_current").text(response.current)

 				// The selection option are then deleted so the options are not left everytime a user choses a reagent. 
 				$(".dropdown-lot-choices").remove()
 				


			}			

		})
	})






$(document).on('submit','#date_form', function(e) {


		e.preventDefault();
		
		// let cookie = document.cookie
		// var csrfToken = cookie.substring(cookie.indexOf('=') + 1)

		$.ajax({

			url: '',
			type: 'POST',
			data: {
				start_date: $('#start_date').val(),
				end_date: $('#end_date').val(),
				csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
				
			},

			success: function(response) {
			
				if (response.reagent_name_date_range == 'Does not exist') {

					$("#date_selection_results").text("Reagent has not been used")

				}

				else if (response.reagent_name_date_range != "Does not exist") {

				$("#date_selection_results").text(response.reagent_name_date_range + " " + response.reagent_lot_from_table + " Usage From:" )
				$("#dates").text(response.start_date_updated + " to " + response.end_date_updated)
				$("#range_usage").text(response.time_usage_range_total)

				}

				if (response.time_usage_range_total == null) {

				$("#date_selection_results").text(response.reagent_name_date_range + " " + response.reagent_lot_from_table + " Usage From:" )
				$("#dates").text(response.start_date_updated + " to " + response.end_date_updated)
				$("#range_usage").text("Reagent has not been used")
		
					
			}			
				}

		})
	})






  





$(document).ready(function () {
	$("#usage-table tr").click(function() {
	    var tableData = $(this).children("td").map(function() {
	        return $(this).attr("class");
	    }).get();

	   
	    y= $.trim(tableData[0])
	  
	   	z= "."+y
	   	
			var reagentNameArray = $(z).map(function() {
			    return this.innerHTML;
			}).get();

			var reagentLotArray = $(z).next().map(function() {
			    return this.innerHTML;
			}).get();

			console.log(reagentLotArray)

			var all = $(z).next().next().map(function() {
			    return this.innerHTML;
			}).get();

	

			var total_reagent_used= 0

			for (var i = 0; i < all.length; i++) {

				var reagent_used= parseInt(all[i])
				total_reagent_used += reagent_used

			}
			

			reagentUsedMessage= "Total " + reagentNameArray[0] + " Lot: " + reagentLotArray[0] + " used is " +  total_reagent_used
			
			$("#reagent-used-message").text(reagentUsedMessage)


	});
});











function sortTable(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("specialist-table");
  switching = true;
  //Set the sorting direction to ascending:
  dir = "asc"; 
  /*Make a loop that will continue until
  no switching has been done:*/
  while (switching) {
    //start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /*Loop through all table rows (except the
    first, which contains table headers):*/
    for (i = 1; i < (rows.length - 1); i++) {
      //start by saying there should be no switching:
      shouldSwitch = false;
      /*Get the two elements you want to compare,
      one from current row and one from the next:*/
      x = rows[i].getElementsByClassName("sort-alphabetically")[n];
      y = rows[i + 1].getElementsByClassName("sort-alphabetically")[n];
  
      /*check if the two rows should switch place,
      based on the direction, asc or desc:*/
      if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          //if so, mark as a switch and break the loop:
          shouldSwitch= true;
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          //if so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /*If a switch has been marked, make the switch
      and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      //Each time a switch is done, increase this count by 1:
      switchcount ++;      
    } else {
      /*If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again.*/
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}

function sortTableNum(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("specialist-table");
  switching = true;
  //Set the sorting direction to ascending:
  dir = "asc"; 
  /*Make a loop that will continue until
  no switching has been done:*/
  while (switching) {
    //start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /*Loop through all table rows (except the
    first, which contains table headers):*/
    for (i = 1; i < (rows.length - 1); i++) {
      //start by saying there should be no switching:
      shouldSwitch = false;
      /*Get the two elements you want to compare,
      one from current row and one from the next:*/
      x = rows[i].getElementsByClassName("sort-numerically")[n];
      y = rows[i + 1].getElementsByClassName("sort-numerically")[n];
  
      /*check if the two rows should switch place,
      based on the direction, asc or desc:*/
      if (dir == "asc") {
       if (Number(x.innerHTML) > Number(y.innerHTML)) {
          //if so, mark as a switch and break the loop:
          shouldSwitch= true;
          break;
        }
      } else if (dir == "desc") {
        if (Number(x.innerHTML) < Number(y.innerHTML))  {
          //if so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /*If a switch has been marked, make the switch
      and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      //Each time a switch is done, increase this count by 1:
      switchcount ++;      
    } else {
      /*If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again.*/
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}



