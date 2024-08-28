// Checks if a string contains only numbers
function containsOnlyNumbers(str) {
    return /^\d+$/.test(str);
};

document.getElementById('regdialogbtn').addEventListener('click', function() {
    const phonenumber = document.getElementById('phonenumber').value;
    if (containsOnlyNumbers(phonenumber) && (phonenumber.length == 10  || phonenumber.length == 11)) {
        console.log(phonenumber.length, ' is true')
        const data = {
            'protocol' : 'validation',
            'length' : phonenumber.length,
            'phonenumber' : phonenumber,
        };

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                // if not safe, set csrftoken
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken",  getCookie('csrftoken'));
                };
            }
        });
        // Sending data from validation
        $.ajax({
            url : '/v1/player/login/valvalidation/' ,
            type : "POST" ,
            data : {
                'getdata' : JSON.stringify(data)
            } ,
            dataType : 'json' ,
            success : function (res , status) {
                if (res.status == 200){
                    console.log(res.status)
                    var form_log = document.getElementById('form_log')
                    form_log.innerHTML = '';
                    var form_code = '<input type="hidden" id="p" value="'+res.phonenumber+'">'+
                                    '<div id="codeO" class="flex flex-col justify-between gap-2">'+
                                        '<input autocomplete="off" type="text" id="code" class="input input-bordered w-full" placeholder=" کد ارسال شده را وارد کنید " />'+
                                        '<small class="w-full text-red-500 none" id="cmsg"></small>'+
                                    '</div>'+
                                    '<div class="p-0">'+
                                        '<button data-ripple-dark="true" onclick="loginbtn()" id="loginbtn" class="w-full select-none rounded-lg bg-[#5c8374] py-3 px-6 text-center align-middle font-YekanBakh-Regular text-xs uppercase text-white shadow-md shadow-[#044040] transition-all hover:shadow-lg hover:shadow-gray-900/20 active:opacity-[0.85] disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">'+
                                            ' ورود به حساب'+
                                        '</button>'+
                                    '</div>';
                    document.getElementById('form_log').innerHTML = form_code;

                }if (res.status == 404) {
                    console.log(res.status)
                    var form_log = document.getElementById('form_log')
                    form_log.innerHTML = '';
                    var form_reg = '<input type="hidden" id="p" value="'+res.phonenumber+'">'+
                                    '<div class="flex flex-col md:flex-row justify-between gap-2">'+
                                        '<input autocomplete="off" type="text" id="first_name" class="input input-bordered w-full md:w-1/2" placeholder=" *نام" />'+
                                        '<input autocomplete="off" type="text" id="last_name" class="input input-bordered w-full md:w-1/2" placeholder=" *نام خانوادگی" />'+
                                    '</div>'+
                                    '<div class="flex flex-col md:flex-row justify-between gap-2">'+
                                        '<input autocomplete="off" type="email" id="mail" class="input input-bordered w-full md:w-1/2" placeholder=" *پست الکترونیک" />'+
                                        '<input autocomplete="off" type="text" id="password" class="input input-bordered w-full md:w-1/2" placeholder=" *رمز عبور" />'+
                                    '</div>'+
                                    '<div class="p-0">'+
                                        '<button data-ripple-dark="true" onclick="createaccgbtn()" id="createaccgbtn" class="w-full select-none rounded-lg bg-[#5c8374] py-3 px-6 text-center align-middle font-YekanBakh-Regular text-xs uppercase text-white shadow-md shadow-[#044040] transition-all hover:shadow-lg hover:shadow-gray-900/20 active:opacity-[0.85] disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" type="button">'+
                                       ' ساخت حساب کاربری'+
                                        '</button>'+
                                    '</div>';
                    document.getElementById('form_log').innerHTML = form_reg;
                }
            } ,
            error : function () {
                console.log('er')
                
            } ,
        });
    }
    // else{
    //     var msg = 'مقدار رمز عبور نمی توانند خالی باشد .'
    //     var alert = '<div class="alert alert-outline-danger mb-4" role="alert"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-x close" data-dismiss="alert"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></button><i class="flaticon-cancel-12 close" data-dismiss="alert"></i> <strong id="msg">خطا!</strong> ' + msg + '</div>'
    //     $('#validation_msg').append(alert);
    // }
});

function loginbtn() {
    const code = document.getElementById('code').value;
    console.log('code')
    const phonenumber = document.getElementById('p').value;
    if (containsOnlyNumbers(code) && code.length == 6) {
        console.log(code.length, ' is true')
        const data = {
            'protocol' : 'code',
            'code' : code,
            'phonenumber' : phonenumber,
        };

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                // if not safe, set csrftoken
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken",  getCookie('csrftoken'));
                };
            }
        });
        // Sending data from validation
        $.ajax({
            url : '/v1/player/login/valvalidation/' ,
            type : "POST" ,
            data : {
                'getdata' : JSON.stringify(data)
            } ,
            dataType : 'json' ,
            success : function (res , status) {
                console.log(res.status);
                if (res.status == 200){
                    location.reload()

                }if (res.status == 500) {
                    var cmsg = document.getElementById('cmsg')
                    cmsg.classList.remove('none')
                    cmsg.innerHTML = res.msg;
                }
            } ,
            error : function () {
                console.log('er')
                
            } ,
        });
    }
    // else{
    //     var msg = 'مقدار رمز عبور نمی توانند خالی باشد .'
    //     var alert = '<div class="alert alert-outline-danger mb-4" role="alert"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-x close" data-dismiss="alert"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></button><i class="flaticon-cancel-12 close" data-dismiss="alert"></i> <strong id="msg">خطا!</strong> ' + msg + '</div>'
    //     $('#validation_msg').append(alert);
    // }
};


function createaccgbtn() {
    const first_name = document.getElementById('first_name').value;
    const last_name = document.getElementById('last_name').value;
    const mail = document.getElementById('mail').value;
    const password = document.getElementById('password').value;
    const phonenumber = document.getElementById('p').value;
    console.log(phonenumber)
    
    const data = {
        'first_name' : first_name,
        'last_name' : last_name,
        'mail' : mail,
        'password' : password,
        'phonenumber' : phonenumber
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            // if not safe, set csrftoken
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken",  getCookie('csrftoken'));
            };
        }
    });
    // Sending data from validation
    $.ajax({
        url : '/v1/player/login/crtacc/' ,
        type : "POST" ,
        data : {
            'getdata' : JSON.stringify(data)
        } ,
        dataType : 'json' ,
        success : function (res , status) {
            console.log(res.status);
            if (res.status == 200){
                location.reload();

            }
        } ,
        error : function () {
            console.log('er')
            
        } ,
    });
    // else{
    //     var msg = 'مقدار رمز عبور نمی توانند خالی باشد .'
    //     var alert = '<div class="alert alert-outline-danger mb-4" role="alert"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-x close" data-dismiss="alert"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></button><i class="flaticon-cancel-12 close" data-dismiss="alert"></i> <strong id="msg">خطا!</strong> ' + msg + '</div>'
    //     $('#validation_msg').append(alert);
    // }
};

