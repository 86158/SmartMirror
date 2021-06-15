<?php  
include('style.php');
include('function.php');
include('scripts.php');
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php $f = 1; ?>
    <div id="Clock">
    <?php Date_show(); ?>
    <div id="Time">
        <?php $time = date("H:i:s");
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
    </div>
    <!-- Code voor de random zinnetjes uit de database -->
    <span class="randomZin">
        <?php 
        $randZinnen = randomZin(); 
        ?>
            <?php foreach($randZinnen as $randZin) { ?>
                <div id="fitin"> 
                <?php echo($randZin['zinTekst']); ?> 
                </div> <?php
            }  ?>
    </span>
    <div id="rooster">
        <img src="images/rooster.png" alt="" width="100%">
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