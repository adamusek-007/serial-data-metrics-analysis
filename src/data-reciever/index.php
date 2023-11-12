<?php
include("db-config.php");
include("connection.php");

$temperature = $_GET["temperature"];
$humidity = $_GET["humidity"];

if ($temperature != null && $humidity != null) {
    $tempSql = "INSERT INTO `data` (`value`, `sensor_id`) VALUES ({$temperature}, 1);";
    $humiditySql = "INSERT INTO `data` (`value`, `sensor_id`) VALUES ({$humidity}, 2);";

    $connection = getDatabaseConnection();
    $connection->query($tempSql);
    $connection->query($humiditySql);
}