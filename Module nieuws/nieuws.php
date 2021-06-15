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