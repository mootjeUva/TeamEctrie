# TeamEctrie

In de provincies Noord- en Zuid-Holland liggen in totaal 118 treinstations, waarvan de 22 belangrijkste intercitystations met de tussenliggende spoorverbindingen, in een .csv-bestand zijn opgeslagen. De getallen die achter een verbinding staan zijn de reistijden in minuten. De lijst met de locaties van de 22 treinstations zijn ook in een .csv-bestand opgeslagen.

1. Maak een lijnvoering voor Noord- en Zuid-Holland met maximaal zeven trajecten binnen een tijdsframe van twee uur, waarbij alle verbindingen bereden worden.

RailNL heeft recentelijk een doelfunctie opgesteld voor de kwaliteit van de lijnvoering. Als 100% van van de verbindingen bereden wordt, levert dat 10000 punten op je lijnvoering op, anders krijg je een een gedeelte daarvan. Maar hoe minder trajecten voor dezelfde service, hoe goedkoper. En in hoe minder tijd er in al die trajecten samen verbruikt wordt, hoe beter. Dus die factoren worden ook meegewogen in de doelfunctie:

    $ K = p*10000 - (T*100 + Min) $

waarin $K$ de kwaliteit van de lijnvoering is, $p$ de fractie van de bereden verbindingen (dus tussen 0 en 1), $T$ het aantal trajecten en $Min$ het aantal minuten in alle trajecten samen.

Maak wederom een lijnvoering voor Noord- en Zuid-Holland met maximaal zeven trajecten binnen een tijdsframe van twee uur, en probeer nu $K$ zo hoog mogelijk te krijgen.

## Aan de slag

### Vereisten

Deze codebase is volledig geschreven in Python 3.8.11 In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. De volgende instructie:

```
pip install -r requirements.txt
```

Of via conda:

```
conda install --file requirements.txt
```

### Gebruik

Een voorbeeldje kan gerund worden door aanroepen van:

```
python main.py
```

Het bestand geeft een voorbeeld voor gebruik van de verschillende functies.

### Structuur

De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

- **/code**: bevat alle code van dit project
  - **/code/algorithms**: bevat de code voor algoritmes
  - **/code/classes**: bevat de vijf benodigde classes voor deze case
  - **/code/visualisation**: bevat de benodigde code voor de visualisatie van deze case
- **/data**: bevat de 4 verschillende databestanden die nodig zijn om de graaf te vullen en te visualiseren

## Auteurs
- Mohammed Wafelgha
- Rowan Schelvis
- Guido Eerdhuizen
