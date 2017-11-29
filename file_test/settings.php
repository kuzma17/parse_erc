<?php
$host = '127.0.0.1';
$user = 'root';
$password = '170270';
$database = 'parse_erc';

$link = mysqli_connect($host, $user, $password, $database)
or die("Ошибка " . mysqli_error($link));
$link->set_charset('utf8');

$query ="SELECT * FROM erc_categories";
$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link));

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
                    Суб категории
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
            <table class="" cellpadding="1" cellspacing="1">
                <tr>
                    <th>id</th><th>name</th><th></th>
                </tr>
                <?php while ($category = mysqli_fetch_object($result)) {?>
                    <tr>
                        <td><?=$category->id?></td><td><?=$category->name?></td><td><a href="?type=category&action=edit&id=<?=$category->id?>" >edit</a> <a href="?type=category&action=delete&id=<?=$category->id?>" >delete</a></td></tr>
                    </tr>

                <?php } ?>
            </table>
        </div>
    </div>
</div>


</body>
</html>
