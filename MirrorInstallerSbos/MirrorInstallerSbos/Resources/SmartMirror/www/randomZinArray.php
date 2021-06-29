
<?php
$randomzin = array(
  array('De manier waarop jij dit varkentje hebt gewassen is inspirerend voor iedereen.'),
  array('Jouw benadering is verfrissend.'),
  array('Je mag trots zijn op jezelf.'),
  array('Jij brengt de zonnestralen in mijn dag.'),
  array('Dank je wel dat jij er voor me bent.'),
  array('Zonder jouw was ik niks <3'),
  array('Wat heb je een mooie trui aan.'),
  array('Jouw lach is betoverend.'),
  array('Je bent geweldig, prachtig, uniek!'),
  array('Je bent mooi zoals je bent.'),
  array( 'Jij bent hartverwarmend.'),
  array('Ik hoop dat je inziet hoe bijzonder je bent.'),
  array('Jij bent zo prachtig. (van binnen en van buiten)'),
  array('Dank je wel voor wie jij bent.'),
  array('Je mag er zijn. Ik geloof in jou.'),
  array('Did you sleep well?'),
  array('Failure Will Never Overtake Me If My Determination To Succeed Is Strong Enough.'),
  array('People Who Are Crazy Enough To Think They Can Change The World, Are The Ones Who Do.'),
  array('If You Are Working On Something That You Really Care About, You Don’t Have To Be Pushed. The Vision Pulls You.'),
  array('It’s Not Whether You Get Knocked Down, It’s Whether You Get Up.'),
  array('You Learn More From Failure Than From Success. Don’t Let It Stop You. Failure Builds Character.'),
  array('Don’t Let Yesterday Take Up Too Much Of Today.'),
  array('The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty.'),
  array('The Best Way To Get Started Is To Quit Talking And Begin Doing.')
);

$num = count($randomzin);

$rand = rand(0, ($num - 1));

$selectedZin = $randomzin[$rand];
?>