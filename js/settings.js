/**
 * Created by kuzma on 30.11.17.
 */
$(document).ready(function () {

     function edit_(form_data, page) {
         $('#preloader').show();
         $("#info").hide();
         $.ajax({
            type: 'POST',
            url: page,
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function (data) {
                onResponse(data)
            }
        });
    }

    function checkCode(form_data, page) {
        var code = form_data.getAll('code_code');
        $.ajax({
            type: 'POST',
            url: 'check_code.py',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function (data) {
                if(data == 1){
                    edit_(form_data, page);
                }else{
                    alert('Код ' + code + ' не существует!');
                    return false;
                }
            }
        });
    }

    $('#option').click(function () {
        $('#preloader').show();
        $("#info").hide();
        $.post("option_list.py", {}, onResponse);
        return false;
    });
    $('#category').click(function () {
        $('#preloader').show();
        $("#info").hide();
        $.post("category_list.py", {}, onResponse);
        return false;
    });
    $('#subcategory').click(function () {
        $('#preloader').show();
        $("#info").hide();
        $.post("subcategory_list.py", {}, onResponse);
        return false;
    });
    $('#vendor').click(function () {
        $('#preloader').show();
        $("#info").hide();
        $.post("vendor_list.py", {}, onResponse);
        return false;
    });
    $('#code').click(function () {
        $('#preloader').show();
        $("#info").hide();
        $.post("code_list.py", {}, onResponse);
        return false;
    });
    $('#prom_code').click(function () {
        $('#preloader').show();
        $("#info").hide();
        $.post("prom_list.py", {}, onResponse);
        return false;
    });


    $('#info').on("click", ".edit_cat", function () {
        $('#preloader').show();
        $("#info").hide();
        var page = $(this).attr('data-cat') + '.py';
        $.post(page, {data: $(this).attr('data-id')}, onResponse);
        return false;
    });

    $('#info').on("click", "#edit-submit", function () {
        var form_data = new FormData($('#cat_save')[0]);
        var page = $(this).attr('data-cat') + '_edit.py';
        if ($(this).attr('data-cat') == 'code') {
            checkCode(form_data, page);
            return false;
        }
        edit_(form_data, page);
    });

    $('#info').on("click", "#add-submit", function () {
        var form_data = new FormData($('#cat_save')[0]);
        var page = $(this).attr('data-cat') + '_add.py';
        if ($(this).attr('data-cat') == 'code') {
            checkCode(form_data, page);
            return false;
        }
        edit_(form_data, page);
    });

    $('#info').on("click", "#add_cat", function () {
        $("#info").hide();
        var page = $(this).attr('data-cat') + '.py';
        $.post(page, {}, onResponse);
        return false;
    });

    $('#info').on("click", ".dell_cat", function () {
        if (confirm('Вы действительно хотите удалить объект?')) {
            $('#preloader').show();
            $("#info").hide();
            var page = $(this).attr('data-cat') + '_dell.py';
            $.post(page, {data: $(this).attr('data-id')}, onResponse);
            return false;
        } else {
            return false;
        }
    });

    function onResponse(data) {
        $('#preloader').hide();
        $("#info").html(data);
        //$("#info").show(300);
        $("#info").slideDown(600);
    }

});
