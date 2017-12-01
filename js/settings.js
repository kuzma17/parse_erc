/**
 * Created by kuzma on 30.11.17.
 */
$(document).ready(function(){

        $('#option').click(function() {
            $('#preloader').show();
            $("#info").hide();
            $.post("option_list.py",{},onResponse);
            return false;
        });
        $('#category').click(function() {
            $('#preloader').show();
            $("#info").hide();
            $.post("category_list.py",{},onResponse);
            return false;
        });
        $('#subcategory').click(function() {
            $('#preloader').show();
            $("#info").hide();
            $.post("subcategory_list.py",{},onResponse);
            return false;
        });
         $('#vendor').click(function() {
            $('#preloader').show();
            $("#info").hide();
            $.post("vendor_list.py",{},onResponse);
            return false;
        });
         $('#code').click(function() {
            $('#preloader').show();
            $("#info").hide();
            $.post("code_list.py",{},onResponse);
            return false;
        });


        $('#info').on("click", ".edit_cat", function(){
            $('#preloader').show();
            $("#info").hide();
            var page = $(this).attr('data-cat')+'.py';
            $.post(page,{data:$(this).attr('data-id')},onResponse);
            return false;
        });

         $('#info').on("click", "#edit-submit", function(){
             $('#preloader').show();
             var form_data = new FormData($('#cat_save')[0]);
             var page = $(this).attr('data-cat')+'_edit.py';
             $("#info").hide();
             $.ajax({
                 type: 'POST',
                 url: page,
                 data: form_data,
                 contentType: false,
                 cache: false,
                 processData: false,
                 async: false,
                 success: function(data) {
                     onResponse(data)
                 }
             });
        });

        $('#info').on("click", "#add_cat", function(){
            $('#preloader').show();
            $("#info").hide();
            var page = $(this).attr('data-cat')+'.py';
            $.post(page,{},onResponse);
            return false;
        });

        $('#info').on("click", "#add-submit", function(){
             $('#preloader').show();
             var form_data = new FormData($('#cat_save')[0]);
             var page = $(this).attr('data-cat')+'_add.py';
             $("#info").hide();
             $.ajax({
                 type: 'POST',
                 url: page,
                 data: form_data,
                 contentType: false,
                 cache: false,
                 processData: false,
                 async: false,
                 success: function(data) {
                     onResponse(data)
                     //alert(data);
                 }
             });
        });

        $('#info').on("click", ".dell_cat", function(){
            if(confirm('Вы действительно хотите удалить объект?')) {
                $('#preloader').show();
                $("#info").hide();
                var page = $(this).attr('data-cat')+'_dell.py';
                $.post(page, {data: $(this).attr('data-id')}, onResponse);
                return false;
            }else {
                return false;
            }
        });

        function onResponse(data){
            $('#preloader').hide();
            $("#info").html(data);
            $("#info").show(300);
        }

    });
