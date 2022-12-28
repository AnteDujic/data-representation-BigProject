    function getAll(){
        $.ajax({
            "url": "http://127.0.0.1:5000/visited",
            "method":"GET",
            "data":"",
            "dataType": "JSON",
            "success":function(result){
                //console.log(result);
                for (details of result){
					addToTable(details)
				}
     
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });

    }
	
	function createDestination(destination){
		$.ajax({
            "url": "http://127.0.0.1:5000/visited",
            "method":"POST",
            "data":JSON.stringify(destination),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                console.log(result);
                destination.id = result.id
                addToTable(destination)
				clearForm()

            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });
    }
	
	function updateDestination(destination){
        console.log(JSON.stringify(destination));
        $.ajax({
            "url": "http://127.0.0.1:5000/visited/"+encodeURI(destination.id),
            "method":"PUT",
            "data":JSON.stringify(destination),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
               // console.log(result);
			      updateTableRow(destination)
                  clearForm()
                  
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });
	}
	
	function deleteDestination(id){
        
        //console.log(JSON.stringify('deleting '+id));
        $.ajax({
            "url": "http://127.0.0.1:5000/visited/"+encodeURI(id),
            "method":"DELETE",
            "data":"",
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                //console.log(result);
                  
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });
    }