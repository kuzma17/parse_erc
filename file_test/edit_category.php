<?php
$host = '127.0.0.1';
$user = 'root';
$password = '170270';
$database = 'parse_erc';

$link = mysqli_connect($host, $user, $password, $database)
or die("Ошибка " . mysqli_error($link));
$link->set_charset('utf8');

$id = $_GET['id'];
$action = $_GET['action'];

if($action == 'edit') {
    $query = "SELECT * FROM erc_categories WHERE id = " . $id;
    $result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link));

    $category = mysqli_fetch_object($result);
}else{
    $category = $_POST['category'];
    $query = "UPDATE erc_categories SET name = '".$category."' WHERE id = " . $id;
    $result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link));

    
}

?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <meta charset="utf-8">
    <link href="/css/style.css" rel="stylesheet"/>
    <link rel="stylesheet" href="/css/bootstrap.min.css" >
    <link rel="stylesheet" href="/css/font-awesome.min.css">
</head>
<body style="background-color: #e0ebeb;">
<div class="container" >
    <div class="row">
        <div class="rcol-sm-3 col-md-3 col-lg-3">
            <div class="panel panel-default">
                <div class="panel-heading">Заголовок</div>
                <div class="panel-body">
                    Общие настройки
                </div>
                <div class="panel-body">
                    Категории
                </div>
                <div class="panel-body">
                    Сиб категории
                </div>
                <div class="panel-body">
                    Бренды
                </div>
                <div class="panel-body">
                    Коды
                </div>
            </div>
        </div>
        <div class="rcol-sm-9 col-md-9 col-lg-9">
            
            <form method="post" action="edit_category.php?type=category&action=save&id=1">
                <div class="form-group">
                    <label  class="col-md-3 control-label">Name<span class="red">*</span></label>
                    <div class="col-md-9">
                        <input type="text" class="form-control" name="category" value="<?=$category->name?>">
                    </div>
                </div>
                <div class="form-group">
                    <input type="submit" value="Save">
                </div>
            </form>

        </div>
    </div>
</div>


</body>
</html>
