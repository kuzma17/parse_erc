
def category_list(cat, title, categories):
    print('Status: 200 OK')
    print('Content-Type: text/plain')
    print('')

    print('<strong class="title">'+title+'</strong>')
    print('<button style="float:right; margin-top: -15px" id="add_cat" data-cat="' + cat + '" type="button" class="btn btn-default">Добавить</button>')
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
        print('<td><a title="редактировать" class="edit_cat" data-id="' + str(category[0]) + '" data-cat="' + cat + '" href="#"><span class="glyphicon glyphicon-edit green"></span></a> ')
        print('<a title="удалить" class="dell_cat" data-id="' + str(category[0]) + '"  data-cat="' + cat + '" href="#"><span class="glyphicon glyphicon-remove red"></span></a></td>')
        print('</tr>')
    print('<table>')

def code_list(cat, title, codes):
    print('Status: 200 OK')
    print('Content-Type: text/plain')
    print('')

    print('<strong class="title">' + title + '</strong>')
    print('<button style="float:right; margin-top: -15px" id="add_cat" data-cat="' + cat + '" type="button" class="btn btn-default">Добавить</button>')
    print("""<table class="table table-hover white_bg">
                <thead>
                    <tr>
                        <th>id</th><th>Категория</th><th>Субкатегория</th><th>Бренд</th><th>код PROM</th><th>status</th><th></th>
                    </tr>
                <thead>""")
    for code in codes:
        if code[6] == 1:
            style = 'green'
        else:
            style = 'red'

        print('<tr class="'+style+'">')
        print('<td>'+str(code[0])+'</td>')
        print('<td>' + str(code[1].decode()) + '</td>')
        print('<td>' + str(code[2].decode()) + '</td>')
        print('<td>' + str(code[3].decode()) + '</td>')
        print('<td>' + str(code[4]) + '</td>')
        #print('<td>' + str(code[5].decode()) + '</td>')
        print('<td>' + str(code[6]) + '</td>')
        print('<td nowrap><a title="редактировать" class="edit_cat" data-id="' + str(code[0]) + '" data-cat="' + cat + '" href="#"><span class="glyphicon glyphicon-edit green"></span></a> ')
        print('<a title="удалить" class="dell_cat" data-id="' + str(code[0]) + '"  data-cat="' + cat + '" href="#"><span class="glyphicon glyphicon-remove red"></span></a></td>')
        print('</tr>')
    print('<table>')

def option_list(cat, title, codes):
    print('Status: 200 OK')
    print('Content-Type: text/plain')
    print('')

    print('<strong class="title">' + title + '</strong>')
    print("""<table class="table table-hover white_bg">
                <thead>
                    <tr>
                        <th>Опция</th><th>значение</th></th>
                    </tr>
                <thead>""")
    for code in codes:
        print('<tr>')
        print('<td>'+str(code[3].decode())+'</td>')
        print('<td>' + str(code[2]) + '</td>')
        print('<td nowrap><a title="редактировать" class="edit_cat" data-id="' + str(code[0]) + '" data-cat="' + cat + '" href="#"><span class="glyphicon glyphicon-edit green"></span></a>')
        print('</td>')
        print('</tr>')
    print('<table>')

def prom_list(cat, title, prom_codes):
    print('Status: 200 OK')
    print('Content-Type: text/plain')
    print('')

    print('<strong class="title">' + title + '</strong>')
    print(
        '<button style="float:right; margin-top: -15px" id="add_cat" data-cat="' + cat + '" type="button" class="btn btn-default">Добавить</button>')
    print("""<table class="table table-hover white_bg">
                    <thead>
                        <tr>
                            <th>id</th><th>code</th><th>parent code</th><th>title</th><th></th>
                        </tr>
                    <thead>""")
    for prom in prom_codes:
        print('<tr>')
        print('<td>' + str(prom[0]) + '</td>')
        print('<td>' + str(prom[1]) + '</td>')
        print('<td>' + str(prom[2]) + '</td>')
        print('<td>' + str(prom[3].decode()) + '</td>')
        print('<td><a title="редактировать" class="edit_cat" data-id="' + str(prom[0]) + '" data-cat="' + cat + '" href="#"><span class="glyphicon glyphicon-edit green"></span></a> ')
        print('<a title="удалить" class="dell_cat" data-id="' + str(prom[0]) + '"  data-cat="' + cat + '" href="#"><span class="glyphicon glyphicon-remove red"></span></a></td>')
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

def code_view(cat, title, categories, subcategories, vendors, category_id, subcategory_id, vendor_id, id, code, parent_code, title_code, status):
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
        print('<option value="' + str(category[0]) + '"')
        if category_id and int(category_id) == int(category[0]):
            print(' selected ')
        print('>' + str(category[1].decode()) +'</option>')
    print('</select>')
    print("""</div>
               </div>
            <div class="form-group">
              <label for="name" class="control-label col-sm-2">Субкатегория</label>
        	  <div class="col-sm-10">""")
    print('<select name="subcategory" id="subcategory" >')
    for subcategory in subcategories:
        print('<option value="' + str(subcategory[0]) + '"')
        if subcategory_id and int(subcategory_id) == int(subcategory[0]):
            print(' selected ')
        print('>' + str(subcategory[1].decode()) + '</option>')
    print('</select>')
    print("""</div>
                   </div>
                <div class="form-group">
                  <label for="name" class="control-label col-sm-2">Бренд</label>
            	  <div class="col-sm-10">""")
    print('<select name="vendor" id="vendor" >')
    for vendor in vendors:
        print('<option value="' + str(vendor[0]) + '"')
        if vendor_id and int(vendor_id) == int(vendor[0]):
            print(' selected ')
        print('>' + str(vendor[1].decode()) + '</option>')
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
    print('<select name="status" id="status" >')
    print('<option value="0"')
    if int(status) == 0:
        print(' selected ')

    print('>OFF</option>')
    print('<option value="1"')
    if int(status) == 1:
        print(' selected ')

    print('>ON</option>')
    print('</select>')
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

def option_view(cat, title, id, key, name, value):
    print('Status: 200 OK')
    print('Content-Type: text/plain')
    print('')

    print('<h4>' + title + '</h4>')
    print('<form method="post" name="cat_save" id="cat_save" action="category_save.py" >')
    print('<input type="hidden" name="id_cat" id="id_cat" value="' + id + '">')
    print('<input type="hidden" name="key" id="id_cat" value="' + key + '">')

    print('<div class="form-group">')
    print('<label for="name" class="control-label col-sm-2">' + name + '</label>')
    print('<div class="col-sm-10">')
    print('<input type="text" name="value_cat" id="value_cat" value="' + value + '">')
    print("""</div>
       </div>
       <div class="form-group">
          <div class="col-sm-offset-2 col-sm-10">""")
    print('<button id="edit-submit" data-cat="' + cat + '" type="button" class="btn btn-primary">Сохранить</button>')
    print("""</div>
       </div>
       </form>""")

def prom_view(cat, title, id, code, parent_code, title_code, list_code):
    print('Status: 200 OK')
    print('Content-Type: text/plain')
    print('')

    print('<h4>' + title + '</h4>')
    print('<form method="post" name="cat_save" id="cat_save" action="category_save.py" >')
    print('<input type="hidden" name="id_cat" id="id_cat" value="' + id + '">')

    print('<div class="form-group">')
    print('<label for="name" class="control-label col-sm-2">Code</label>')
    print('<div class="col-sm-10">')
    print('<input type="text" name="code" id="code" value="' + code + '">')
    print('</div></div>')
    print('<div class="form-group">')
    print('<label for="name" class="control-label col-sm-2">Parent Code</label>')
    print('<div class="col-sm-10">')
    #print('<input type="text" name="parent_code" id="parent_code" value="' + parent_code + '">')
    print('<select name="parent_code" id="parent_code" >')
    print('<option value="0"> 0 root </option>')
    for list in list_code:
        print('<option value="' + str(list[1]) + '"')
        if parent_code and int(parent_code) == int(list[1]):
            print(' selected ')
        print('>' + str(int(list[1])) + ' ' + str(list[3].decode()) + '</option>')
    print('</select>')
    print('</div></div>')
    print('<div class="form-group">')
    print('<label for="name" class="control-label col-sm-2">Title</label>')
    print('<div class="col-sm-10">')
    print('<input type="text" name="title_prom" id="title_prom" value="' + title_code + '">')
    print('</div></div>')

    if id:
        print(
            '<button id="edit-submit" data-cat="' + cat + '" type="button" class="btn btn-primary">Сохранить</button>')
    else:
        print('<button id="add-submit" data-cat="' + cat + '" type="button" class="btn btn-primary">Сохранить</button>')
    print("""</div>
              </div>
              </form>""")