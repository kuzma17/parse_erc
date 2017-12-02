/**
 * Created by kuzma on 30.11.17.
 */
$(document).ready(function () {
    $('#preloader').show();
    $.ajax({
        type: 'POST',
        url: 'currency.py',
        success: function (data) {
            $('#preloader').hide();
            $("#currency").val(data);
        }
    });

    var filesExt = ['xml', 'XML', 'Xml'];
    $('#upload-file-btn').click(function () {
        var parts = $('#file').val().split('.');
        if (filesExt.join().search(parts[parts.length - 1]) == -1) {
            alert('Не корректный исходный файл!');
            return false;
        }
        $('#info_myForm').hide()
        $("#info").hide();
        $('#preloader').show();
        var form_data = new FormData($('#myForm')[0]);
        $.ajax({
            type: 'POST',
            url: 'readxml.py',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function (data) {
                onResponse(data)
            }
        });
    });

    $('#info').on("click", "#edit-param", function () {
        $('#preloader').show();
        var form_data = new FormData($('#category_save')[0]);
        $('#info_myForm').hide();
        $("#info").hide();
        $.ajax({
            type: 'POST',
            url: 'readxml.py',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function (data) {
                onResponse(data)
            }
        });
    });

    $('#info').on("click", "#create_xml", function () {
        $('#preloader').show();
        var form_data = new FormData($('#category_save')[0]);
        $('#info_myForm').hide();
        $("#info").hide();
        $.ajax({
            type: 'POST',
            url: 'create_xml.py',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function (data) {
                //onResponse(data)
                $('#preloader').hide();
                $("#info").html(data);
                //$("#info").show(300);
                $("#info").slideDown(400);
                ;
            }
        });
    });

    function onResponse(data) {
        $('#preloader').hide();
        $("#info").html(data);
        //$("#info").show(300);
        $("#info").slideDown(1000);
        ;
    }

    $('#info').on("mouseover", ".code_prom", function () {
        $(this).css({marginTop: '1px'});
        $(this).children("span").css({fontSize: '12px'});
    });
    $('#info').on("mouseout", ".code_prom", function () {
        $(this).css({marginTop: '-1px'});
        $(this).children("span").css({fontSize: '8px'});
    });
    $('#info').on("click", "#all_checkbox", function () {
        if ($(this).prop("checked")) {
            $('#all_checkbox_text').html('Снять все');
            $('.xml_check').prop("checked", true);
        } else {
            $('#all_checkbox_text').html('Выбрать все');
            $('.xml_check').prop("checked", false);
        }
    });
});
