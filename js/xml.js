/**
 * Created by kuzma on 30.11.17.
 */
$(document).ready(function() {
               var filesExt = ['xml', 'XML', 'Xml'];
               $('#upload-file-btn').click(function() {
                   var parts = $('#file').val().split('.');
                   if(filesExt.join().search(parts[parts.length - 1]) == -1){
                       alert('Не корректный исходный файл!');
                       return false;
                   }
                   $('#myForm').hide()
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
                       success: function(data) {
                           $('#preloader').hide();
                           $('#info').html(data);
                           $("#info").show(300);
                           //alert(data);
                       }
                   });
               });

               $('#info').on("click", "#edit-param", function() {
                   $('#preloader').show();
                   var form_data = new FormData($('#category_save')[0]);
                   $('#myForm').hide();
                    $("#info").hide();
                   $.ajax({
                       type: 'POST',
                        url: 'readxml.py',
                        data: form_data,
                        contentType: false,
                        cache: false,
                        processData: false,
                        async: false,
                       success: function(data) {
                           $('#preloader').hide();
                           $('#info').html(data);
                           $("#info").show(300);
                           //alert(data);
                       }
                   });
               });

              $('#info').on("click", "#create_xml", function() {
                   $('#preloader').show();
                   $('#myForm').hide();
                    $("#info").hide();
                   $.ajax({
                       type: 'POST',
                        url: 'create_xml.py',
                        contentType: false,
                        cache: false,
                        processData: false,
                        async: false,
                       success: function(data) {
                           $('#preloader').hide();
                           $('#info').html(data);
                           $("#info").show(300);
                           //alert(data);
                       }
                   });
               });


               $('#info').on("mouseover", ".code_prom", function(){
                   $(this).css({marginTop: '1px'});
                   $(this).children("span").css({fontSize: '12px'});
               })
               $('#info').on("mouseout", ".code_prom", function(){
                   $(this).css({marginTop: '-1px'});
                   $(this).children("span").css({fontSize: '8px'});
               })
           });
