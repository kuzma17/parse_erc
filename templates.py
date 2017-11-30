
def category_list(cat, title, categories):
    print('Status: 200 OK')
    print('Content-Type: text/plain')
    print('')

    print('<h4>'+title+'</h4>')
    print('<button id="add_cat" data-cat="' + cat + '" type="button" class="btn btn-default">Добавить</button><br>')
    print("""<table class="table table-hover white_bg">
                <thead>
                    <tr>
                        <th>id</th><th>name</th><th></th>
                    </tr>
                <thead>""")
    for category in categories:
        print('<tr>')
        print('<td>' + str(category[0]) + '</td>')
        print('<td>' + str(category[1].decode()) + '</td>')
        print('<td><a class="edit_cat" data-id="' + str(category[0]) + '" data-cat="' + cat + '" href="#"><span class="glyphicon glyphicon-edit green"></span></a> ')
        print('<a class="dell_cat" data-id="' + str(category[0]) + '"  data-cat="' + cat + '" href="#"><span class="glyphicon glyphicon-remove red"></span></a></td>')
        print('</tr>')
    print('<table>')

def code_list(cat, title, codes):
    print('Status: 200 OK')
    print('Content-Type: text/plain')
    print('')

    print('<h4>'+title+'</h4>')
    print('<button id="add_cat" data-cat="' + cat + '" type="button" class="btn btn-default">Добавить</button><br>')
    print("""<table class="table table-hover white_bg">
                <thead>
                    <tr>
                        <th>id</th><th>Категория</th><th>Субкатегория</th><th>Бренд</th><th>код</th><th>parent</th><th>title</th><th>status</th><th></th>
                    </tr>
                <thead>""")
    for code in codes:
        if code[7] == 1:
            style = 'green'
        else:
            style = 'red'

        print('<tr class="'+style+'">')
        print('<td>'+str(code[0])+'</td>')
        print('<td>' + str(code[1].decode()) + '</td>')
        print('<td>' + str(code[2].decode()) + '</td>')
        print('<td>' + str(code[3].decode()) + '</td>')
        print('<td>' + str(code[4].decode()) + '</td>')
        print('<td>' + str(code[5].decode()) + '</td>')
        print('<td>' + str(code[6].decode()) + '</td>')
        print('<td>' + str(code[7]) + '</td>')
        print('<td nowrap><a class="edit_cat" data-id="' + str(code[0]) + '" data-cat="' + cat + '" href="#"><span class="glyphicon glyphicon-edit green"></span></a> ')
        print('<a class="dell_cat" data-id="' + str(code[0]) + '"  data-cat="' + cat + '" href="#"><span class="glyphicon glyphicon-remove red"></span></a></td>')
        print('</tr>')

    print('<table>')

def category_view(cat, title, id, name):
    print('Status: 200 OK')
    print('Content-Type: text/plain')
    print('')

    print('<h4>' + title + '</h4>')
    print('<form method="post" name="cat_save" id="cat_save" action="category_save.py" >')
    print('<input type="hidden" name="id_cat" id="id_cat" value="' + id + '">')

    print("""<div class="form-group">
          <label for="name" class="control-label col-sm-2">Название</label>
    	  <div class="col-sm-10">""")
    print('<input type="text" name="name_cat" id="name_cat" value="' + name + '">')
    print("""</div>
       </div>
       <div class="form-group">
          <div class="col-sm-offset-2 col-sm-10">""")
    if id:
        print('<button id="edit-submit" data-cat="' + cat + '" type="button" class="btn btn-primary">Сохранить</button>')
    else:
        print('<button id="add-submit" data-cat="' + cat + '" type="button" class="btn btn-primary">Сохранить</button>')
    print("""</div>
       </div>
       </form>""")

def code_view(cat, title, categories, subcategories, vendors, id, code, parent_code, title_code, status):
    print('Status: 200 OK')
    print('Content-Type: text/plain')
    print('')

    print('<h4>' + title + '</h4>')
    print('<form method="post" name="cat_save" id="cat_save" action="category_save.py" >')
    print('<input type="hidden" name="id_cat" id="id_cat" value="' + id + '">')

    print("""<div class="form-group">
              <label for="name" class="control-label col-sm-2">Категория</label>
        	  <div class="col-sm-10">""")
    print('<select name="category" id="category" >')
    for category in categories:
        print('<option value="' + str(category[0]) + '" >' + str(category[1].decode()) +'</option>')
    print('</select>')
    print("""</div>
               </div>
            <div class="form-group">
              <label for="name" class="control-label col-sm-2">Субкатегория</label>
        	  <div class="col-sm-10">""")
    print('<select name="subcategory" id="subcategory" >')
    for subcategory in subcategories:
        print('<option value="' + str(subcategory[0]) + '" >' + str(subcategory[1].decode()) + '</option>')
    print('</select>')
    print("""</div>
                   </div>
                <div class="form-group">
                  <label for="name" class="control-label col-sm-2">Бренд</label>
            	  <div class="col-sm-10">""")
    print('<select name="vendor" id="vendor" >')
    for vendor in vendors:
        print('<option value="' + str(vendor[0]) + '" >' + str(vendor[1].decode()) + '</option>')
    print('</select>')
    print("""</div>
                  </div>
               <div class="form-group">
                 <label for="name" class="control-label col-sm-2">Код</label>
           	  <div class="col-sm-10">""")
    print('<input type="text" name="code" id="code" value="' + code + '">')
    print("""</div>
                     </div>
                  <div class="form-group">
                    <label for="name" class="control-label col-sm-2">parent code</label>
              	  <div class="col-sm-10">""")
    print('<input type="text" name="parent_code" id="parent_code" value="' + parent_code + '">')
    print("""</div>
                     </div>
                  <div class="form-group">
                    <label for="name" class="control-label col-sm-2">Title</label>
              	  <div class="col-sm-10">""")
    print('<input type="text" name="title" id="title" value="' + title_code + '">')
    print("""</div>
                        </div>
                     <div class="form-group">
                       <label for="name" class="control-label col-sm-2">Status</label>
                 	  <div class="col-sm-10">""")
    print('<input type="text" name="status" id="status" value="' + status + '">')
    print("""</div>
           </div>
           <div class="form-group">
              <div class="col-sm-offset-2 col-sm-10">""")
    if id:
        print(
            '<button id="edit-submit" data-cat="' + cat + '" type="button" class="btn btn-primary">Сохранить</button>')
    else:
        print('<button id="add-submit" data-cat="' + cat + '" type="button" class="btn btn-primary">Сохранить</button>')
    print("""</div>
           </div>
           </form>""")