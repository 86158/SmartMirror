<?php
function db_connect(){
 $servername    ="localhost";
 $username      ="root";
 $password  	="";
 $dbname        ="smartmirror";

 $conn = new mysqli($servername, $username, $password, $dbname);

 if($conn->connect_error)
 {
     die("Connection failed: ". $conn->connect_error);
 }
 return $conn;
}

function randomZin(){
    $conn = db_connect();

    $sql = "SELECT * FROM `randomzin` WHERE `zinId` ORDER BY RAND() LIMIT 1";
    $result = $conn->query($sql) or die($conn->error);
    $posts = $result->fetch_all(MYSQLI_ASSOC);


    $randZinnen = [];

    if ($result->num_rows > 0) {
        // output data of each row
        while($row = $result->fetch_assoc()) 
            {
            $randZinnen[] = $row;
            }
        }
    else {
        print($posts);
    }
    return $posts;
    $result = $conn->query($sql);
}
function Date_show()
{
  $WeekDay = array(
    "Zondag",
    "Maandag",
    "Dinsdag",
    "Woensdag",
    "Donderdag",
    "Vrijdag",
    "Zaterdag"
);
$dayOfWeek = $WeekDay[date("w")];
$month = array(
    "Januari",
    "Februari",
    "Maart",
    "April",
    "Mei",
    "Juni",
    "Juli",
    "Augustus",
    "September",
    "Oktober",
    "November",
    "December"
);
$date = date("d") . " " . $month[date("n") - 1] . " " . date("Y");
echo $dayOfWeek . " " . $date;
}


?>