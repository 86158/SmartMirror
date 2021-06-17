<?php
	include "roosterExport.php";
	foreach ($roosterArray as $day){
		echo "<table id='eduarteAgenda'>";

		echo "<th class='agendaDag'>", $day['day'], "</th>";
		foreach ($day['subjects'] as $subject){
			echo "<tr><td class='agendaVak'>", $subject['vak'], "</td>";
			echo "<td class='agendaBegintijd'>van: ", $subject['begintijd'], "</td><td class='agendaEindtijd'> tot: ", $subject["eindtijd"], "</td></tr>";
		}
		echo "</table>";
	}
?>
<!DOCTYPE html>
<html lang="en">
<head>
	<link rel="stylesheet" href="style.css">
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
</html>