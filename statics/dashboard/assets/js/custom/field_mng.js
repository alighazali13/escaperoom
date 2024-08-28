function checkvalue(key_input, value_input) {
    var status = false;    

    if (key_input != '' && value_input != ''){
        status = true;
    }

    return status;
}

function inputhandler(id, type) {
    const inputvalue = document.getElementById('selectedinp') ;
    if (type == 'add') {
        inputvalue.value = inputvalue.value + '_' + id.toString();
    }else if(type == 'remove'){
        var selected_list = inputvalue.value.split('_');
        var selected_list = selected_list.slice(1);
        console.log(selected_list)
        var newvalue = '1'
        selected_list.forEach(input => {
            if(input != id.toString() && input != '1'){
                console.log('yes')
                newvalue += '_' + input
            }
        });
        inputvalue.value = newvalue;
        console.log(newvalue)
        

    }
    
}

function addfield_booking(id) {
    const this_id = id - 1
    var key_input = document.getElementById('from' + '_' + this_id.toString()).value;    
    var value_input = document.getElementById('to' + '_' + this_id.toString()).value;
    
    var status = checkvalue(key_input, value_input);
    if (status == true) {
        next_inputs_id = id + 1
        html = '<div id="field_'+id+'" class="form-row mb-4 mt-4">'+
                    '<div class="form-group col-md-4  d-flex align-items-center">'+
                        '<input id="from_'+id+'" name="from_'+id+'" type="text" class="form-control" placeholder="از ساعت" required>'+
                    '</div>'+
                    '<div class="form-group col-md-4 d-flex align-items-center">'+
                        '<input id="to_'+id+'" name="to_'+id+'" type="text" class="form-control" placeholder=" تا ساعت " required>'+
                    '</div>'+
                    '<div class="form-group col-md-1">'+
                        '<ul class="list-unstyled d-flex" style="font-size: 22px; margin: 0 auto;">'+
                            '<li onclick="addfield_booking('+next_inputs_id+')" id="plus_'+id+'" class="primary_hover bs-tooltip" data-toggle="tooltip" data-placement="top" title="" data-original-title="فیلد اضافه"><i class="fa-solid fa-circle-plus fa-fw"></i></li>'+
                            '<li onclick="removefield_booking('+id+')" id="minus_'+id+'" class="danger_hover bs-tooltip" data-toggle="tooltip" data-placement="top" title="" data-original-title="فیلد کم"><i class="fa-solid fa-circle-minus fa-fw"></i></li>'+
                        '</ul>'+    
                    '</div>'+
                '</div>'
        $('#booking').append(html);
        inputhandler(id, 'add');
    }else if (status == false) {
        alert('نمیتوانید قبل از پر کردن فیلد سانس فیلد اضافه کنید.')
    }
}

function removefield_booking(id) {
    $('#field_'+ id).remove();
    inputhandler(id, 'remove');

}


