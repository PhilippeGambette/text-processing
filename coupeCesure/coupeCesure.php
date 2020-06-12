</html><head>
<meta charset="UTF-8">
<title>coupeCésure</title>
<style>
h1,h2,h3 {text-align:center}
.candidate {background-color:#FFCCCC;}
.replaced {background-color:#CCCCFF;}
</style>
<link rel="icon" href="ijuv.ico" />
</head>
<SCRIPT TYPE="text/javascript" SRC="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></SCRIPT>
<SCRIPT TYPE="text/javascript" SRC="./coupeCesure-resources.js"></SCRIPT>
<SCRIPT TYPE="text/javascript" SRC="./coupeCesure.js"></SCRIPT>

</body>
<div style="width:700px;margin:auto;font-family:Calibri">
<h1>coupeCésure</h1>
<h2>Résultat de la tentative de suppression des césures</h2>
<h3>Comment ça marche...</h3>
<p>
Cet outil, <b>coupeCésure</b>, utilise la liste des mots simples du 
<!--<a href="http://infolingu.univ-mlv.fr/DonneesLinguistiques/Dictionnaires/telechargement.html">Dictionnaire DELA fléchi du français</a>-->
<a href="http://www.labri.fr/perso/clement/lefff/">le<i>fff</i> (lexique des formes fléchies du français)</a>
(disponible sous licence <a href="http://infolingu.univ-mlv.fr/DonneesLinguistiques/Lexiques-Grammaires/lgpllr.html">LGPLLR</a>),
pour reconnaître si des mots se terminant en fin de ligne
par un trait d'union sont réellement suivis d'un trait d'union
ou constituent la première partie d'un mot découpé par une césure.
</p>
<p>
L'outil <b>coupeCésure</b> est un <a href="coupeCesure.js">code Javascript</a>
mis à disposition sous licence libre GPL v. 3.0.
</p>

<p>
<br/><br/>
Code couleur :
<ul>
<li><span class="replaced">mot dont la césure a été supprimée
car trouvé en entier dans le dictionnaire</span></li>
<li><span class="candidate">mot pour lequel le trait d'union a été gardé</span></li>
</ul>
</p>

<br/><br/>
<h3>Texte obtenu après remplacements...</h3>

<div id="theText">
<?php
echo $_POST["fullText"];
?>
</div>
</body>
</html>