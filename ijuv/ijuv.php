</html><head>
<meta charset="UTF-8">
<title>ijuv - Aide à la transcription en "j" et "v" des graphies "i" et "u" ayant valeur de consonne</title>
<style>
h1,h2,h3 {text-align:center}
.candidate {background-color:#FFEEEE;}
.replaced {background-color:#CCCCFF;}
</style>
<link rel="icon" href="ijuv.ico" />
</head>
<SCRIPT TYPE="text/javascript" SRC="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></SCRIPT>
<SCRIPT TYPE="text/javascript" SRC="./ijuv-resources.js"></SCRIPT>
<SCRIPT TYPE="text/javascript" SRC="./ijuv.js"></SCRIPT>

</body>
<div style="width:350px;margin:auto;font-family:Calibri">
<h1>ijuv</h1>
<h2>Résultat de l'aide à la transcription par "j" et "v" des graphies "i" et "u" ayant valeur de consonne</h2>
<h3>Comment ça marche...</h3>
<p>
Cet outil, <b>ijuv</b>, utilise la liste des termes en moyen et ancien français, contenant des "j" ou des "v", réunis dans ce
<a href="https://fr.wikisource.org/wiki/Wikisource:Dictionnaire">dictionnaire Wikisource de modernisation orthographique</a>
(disponible sous <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.fr">licence Creative Commons Attribution-partage dans les mêmes conditions</a> ;
la liste de ses contributeurs et contributrices se trouve <a href="https://fr.wikisource.org/w/index.php?title=Wikisource:Dictionnaire&action=history">ici</a>),
et la liste des mots simples du <a href="http://infolingu.univ-mlv.fr/DonneesLinguistiques/Dictionnaires/telechargement.html">Dictionnaire DELA fléchi du français</a>
(disponible sous licence <a href="http://infolingu.univ-mlv.fr/DonneesLinguistiques/Lexiques-Grammaires/lgpllr.html">LGPLLR</a>),
complétées de quelques ajouts (voir <a href="ijuv-resources.js">ce fichier</a>).
</p>
<p>
L'outil <b>ijuv</b> est un <a href="ijuv.js">code Javascript</a>
(mis à disposition sous licence libre GPL v. 3.0) qui réalise les actions suivantes :
<ul>
<li>tout mot correspondant à un mot présent dans une des listes évoquées ci-dessus, mais dont les "j" ont été remplacés par des "i"
et les "v" ont été remplacés par des "u" (par exemple "<i>aduantage</i>"), est remplacé par sa version corrigée ("<i>advantage</i>"),
puis colorée <span class="replaced">en bleu</span>,</li>
<li>quelques remplacements automatiques de mots contenant "V" à la place de "U" (par exemple "<i>NOVS</i>", "<i>QVAND</i>"),
ou mixant les "u" et les "v" à remplacer ou garder intacts (par exemple "Viuants", "vsurpateur"),
sont aussi effectués (en fonction également de <a href="ijuv-resources.js">ce fichier</a>), suivis également d'une coloration <span class="replaced">en bleu</span>,</li>
<li>les mots contenant des "i" ou des "u" mais n'ayant pas subi de remplacement car ne correspondant pas aux cas précédents sont
colorés <span class="candidate">en rouge pâle</span>, au cas où ils devraient être corrigés manuellement.</li>
</ul>
</p>

<p>
<br/><br/>
Code couleur :
<ul>
<li><span class="replaced">mot remplacé par un mot du dictionnaire contenant "j" à la place de "i" ou "v" à la place de "u"</span></li>
<li><span class="candidate">mot contenant "i" ou "u" non remplacé</span></li>
</ul>
</p>

<br/><br/>
<h3>Texte obtenu après remplacements...</h3>

<div id="theText">
<?php
if($_POST["type"] == "html"){
   if($_POST["pwd"] != "fabulanumerica"){
      echo "<b>Mot de passe incorrect : demandez-le à l'adresse philippe.gambette@u-pem.fr</b>";
   } else {
      echo $_POST["fullText"];
   }
} else {
   $fullText = explode(PHP_EOL, $_POST["fullText"]);
   foreach($fullText as $line){
      echo '<span class="line">'.str_replace("<","&lt;",str_replace(">","&gt;",$line)).'</span><br/>';
   }
}
?>
</div>
</body>
</html>