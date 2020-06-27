</html><head>
<meta charset="UTF-8">
<title>fs - Correction des erreurs d'OCR ſ &rarrow; s</title>
<style>
h1,h2,h3 {text-align:center}
.candidate {background-color:#FFCCCC;}
.replaced {background-color:#CCCCFF;}
</style>
<link rel="icon" href="ijuv.ico" />
</head>
<SCRIPT TYPE="text/javascript" SRC="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></SCRIPT>
<SCRIPT TYPE="text/javascript" SRC="./fs-resources<?php 
if(sizeof($_POST["nc"])==1){
  echo '-nc';
}
?>.js"></SCRIPT>
<SCRIPT TYPE="text/javascript" SRC="./fs.js"></SCRIPT>

</body>
<div style="width:350px;margin:auto;font-family:Calibri">
<h1>fs</h1>
<h2>Résultat de l’aide à la correction d'OCR des "f" en "ſ"</h2>
<h3>Comment ça marche...</h3>
<p>
Cet outil, <b>fs</b>, utilise une liste de termes potentiellement erronés contenant un "f" au lieu d'un "s" construite à partir :
<ol>
<li>de la liste des mots simples du <a href="http://infolingu.univ-mlv.fr/DonneesLinguistiques/Dictionnaires/telechargement.html">Dictionnaire DELA fléchi du français</a>
(disponible sous licence <a href="http://infolingu.univ-mlv.fr/DonneesLinguistiques/Lexiques-Grammaires/lgpllr.html">LGPLLR</a>) ;</li>
<li>de la base de données <a href="http://www.lexique.org">Lexique 3.83</a>
(disponible sous licence <a href="https://creativecommons.org/licenses/by-sa/4.0">CC BY SA 4.0</a>) ;</li>
<?php 
if(sizeof($_POST["nc"])==1){
  echo '<li>d’une liste de mots construite par Simon Gabay à partir du LGeRM (disponible sous licence <a href="https://creativecommons.org/licenses/by-nc-sa/3.0/fr/">CC BY NC SA 3.0</a>) ;</li>';
}
?></ol>
pour obtenir la liste contenue dans <a href="fs-resources<?php 
if(sizeof($_POST["nc"])==1){
  echo '-nc';
}
?></ol>
.js">ce fichier</a>.
</p>
<p>
L'outil <b>fs</b> est un <a href="fs.js">code Javascript</a>
(mis à disposition <a href="https://github.com/PhilippeGambette/text-processing">sous licence libre GPL v. 3.0</a>) qui réalise les actions suivantes :
<ul>
<li>tout mot correspondant à un mot présent dans la liste ci-dessus avec une seule explication possible remplaçant des f par des s est remplacé par sa version corrigée
puis colorée <span class="replaced">en bleu</span>,</li>
<li>tout mot correspondant à un mot présent dans la liste ci-dessus avec des ambigüités est remplacé par la première version corrigée possible, mais
coloré <span class="candidate">en rouge pâle</span>, au cas où il devrait être remplacé manuellement par une autre version possible.</li>
</ul>
</p>

<p>
<br/><br/>
Code couleur :
<ul>
<li><span class="replaced">mot remplacé par un mot du dictionnaire contenant un "s" à la place d'un "f", sans ambigüité trouvée</span></li>
<li><span class="candidate">mot remplacé par un mot du dictionnaire contenant un "s" à la place d'un "f", avec ambigüité possible</span></li>
</ul>
</p>

<br/><br/>
<h3>Texte obtenu après remplacements...</h3>

<div id="theText">
<?php
   $fullText = explode(PHP_EOL, $_POST["fullText"]);
   foreach($fullText as $line){
      echo '<span class="line">'.str_replace("<","&lt;",str_replace(">","&gt;",$line)).'</span><br/>';
   }
?>
</div>
</body>
</html>