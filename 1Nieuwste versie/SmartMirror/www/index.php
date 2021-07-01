<?php  
include('style.php');
include('function.php');
include('scripts.php');

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <!--<meta http-equiv="refresh" content="10"> -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php $f = 1; ?>
    <div id="Clock">
        <div id="weer">
            <ul> 
                <li>
                Weersverwachting:
                </li>
                <?php
                    include "weersVerwachtingexport.php";
                    foreach ($weersVerwachtingArray as $day) {
                    echo "<li class='agendaDag'>", $day, "</li>";;
                    }   
                ?>
            </ul>
        </div>
        <div class="datum"><?php Date_show(); ?></div>
        <div id="Time">
        <?php $time = date("G:i:s");
              echo $time; ?>
        <script type="text/javascript">
            setInterval(function() {
                        var currentTime = new Date ( );    
                        var currentHours = currentTime.getHours ( );   
                        var currentMinutes = currentTime.getMinutes ( );   
                        var currentSeconds = currentTime.getSeconds ( );
                        currentMinutes = ( currentMinutes < 10 ? "0" : "" ) + currentMinutes;   
                        currentSeconds = ( currentSeconds < 10 ? "0" : "" ) + currentSeconds;    
                        var currentTimeString = currentHours + ":" + currentMinutes + ":" + currentSeconds;
                        document.getElementById("Time").innerHTML = currentTimeString;
                    }, 1000);
            </script>
        </div>
        <div class="feestdagen">
        <?php
	        include "feestdagExport.php";
            foreach ($feestdagenArray as $feestdag){ ?>
                <div class="feestdag">
                <?php
                echo $feestdag['desc'];
                echo " "; ?> 
                <div class="datum"><?php
                echo $feestdag['datum'];
                ?></div>
                </div> <?php
            }
        ?>
        </div>
    </div>
    <!-- Code voor de random zinnetjes uit de database -->
    <span class="randomZin">
        <?php 
        include "randomZinArray.php";
        ?>
            <div id="fitin"> 
            <?php echo($selectedZin[0]); ?> 
            </div>
    </span> 
    <div id="rooster">
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
    </div>
    <div id="stocks">
    <div class="crypto">Crypto</div><div class="data">Muntwaarde DagVerschil Marktwaarde</div>
    <?php
        include "cryptoExport.php";
        foreach ($cryptoArray as $crypto){ ?>
            <div class="crypto">
            <?php
                echo $crypto['naam'];
                echo " "; 
            ?> </div>
            <div class="data">
            <?php
                echo $crypto['desc'];
            ?>
            </div> <?php
        }
    ?>
    </div>
    <div id="cijfers">
        <img src="images/cijfers.png" alt="" width="100%">
    </div>

    <div id="News">
        <?php
        //suppercooleschoolprojectenBV-INC.
        //BY: Sebastiaan Verhappen
        //function: Display random news article from nu.nl
        //get full array from nu.nl
        $feed = "https://www.nu.nl/rss/Algemeen";
        $feed_to_array = (array) simplexml_load_file($feed);
        //goto news articles in full feed array
        $feed_channel = (array) $feed_to_array['channel'];
        $feed_item = (array) $feed_channel['item'];
        //pick random article
        $feed_nmr = rand(0, count($feed_item)-1);
        $feed_article = (array) $feed_item[$feed_nmr];
        //print random article
        echo "<div id='news_article'>";
        echo "<h2 id='news_title'>",$feed_article['title'], "</h2>";
        echo "<p id='news_description'>", $feed_article['description'], "</p>";
        echo "<p id='news_date'>", substr($feed_article['pubDate'], 0, -5), "<a id='news_readmore' href='$feed_article[guid]'>read more</a>", "</p>";
        echo "</div>";
        ?>
    </div>
</body>
</html>