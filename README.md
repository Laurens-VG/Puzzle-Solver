# Project multimedia
Dit is een project van multimedia waarbij afzonderlijke puzzelstukken tot één puzzel worden gevormd. 


Universiteit Gent \
Faculteit Ingenieurswetenschappen en architectuur \
Opleiding Industriële Wetenschappen Elektronica-ICT \
Academiejaar 2019-2020

Auteurs: Stephanie Maes, Laurens Van Goethem \
Project onder begeleiding van: Sanne Roegiers, Martin Dimitrievski

## Inhoud

- **images**: map met datasets van jigsaw, tiles, rotated, shuffled, scrambled puzzelstukken
- **main.py**: hoofdbestand om een puzzel naar keuze op te lossen
- **DEMO.py**: Demo bestand, toont mengeling van puzzels die opgelost worden
- **extraction_original.py**: Bestand om de parameters uit de originele gegeven afbeelding te nemen
- **segmentation.py**: Bestand dat de originele afbeelding onderverdeelt in een aantal kleine puzzelstukken 
- **extraction_single_image.py**: Bestand dat alle kleine individuele puzzelstukken bewerkt
- **matching.py**: Bestand dat de puzzelstukken met elkaar vergelijkt en er een match uit haalt
- **solution.py**: Algoritme dat de verschillende puzzelstukken op een gegeven manier met elkaar laat vergelijken en matchen
- **result.py**: Bestand dat de gevonden puzzelstukken naast elkaar plakt
- **music.py**: Bestand dat de muziek behandelt


## Gebruik

Het project gebruikt python 3.7 \
De packages (zie versie controle) kunnen geïnstalleerd worden met pip:

    pip install -r requirements.txt
    
**Main.py**

Hoofdbestand om de methoden te evalueren op de datasets. Enkel jigsaw stukken worden opgelost. 

argumenten:
- method: naam van de methode
    - shuffled
    - rotated
    - scrambled
- dataset: naam van de dataset in de mappen
    - 2x2
    - 2x3
    - 3x3
    - 4x4
    - 5x5 

gebruik:

    python main.py --method shuffled --dataset 2x2
    
**DEMO.py**

Laat enkele voorgekozen oplossingen afspelen.

gebruik:

    python DEMO.py
    
## Versie controle

OS: Windows 10

IDE: JetBrains Pycharm 2019.2.2 (Professional Edition)

Python 3.7.1

Packages
- numpy 1.17.4
- matplotlib 3.1.1
- opencv-python 4.1.2.30
- scipy 1.3.3
- simpleaudio 1.0.4
- imutils 0.5.3
- argparse 1.4.0

