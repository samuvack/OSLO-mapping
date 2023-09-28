---
layout: default
title: Stap voor stap
parent: Documentatie
grand_parent: Brugge
nav_order: 2
---

# Context

De @context sleutel definieert de context waarin de termen in het document worden geïnterpreteerd. Hier worden zowel naar externe contexten (URL's) als codelijsten verwezen.

Externe contexten: De eerste twee URL's verwijzen naar applicatieprofielen die specifieke termen en definities bevatten voor sensoren, bemonstering, observaties en metingen.

Codelijsten: Dit is een lijst van prefixen die worden gebruikt om termen in het document korter en leesbaarder te maken. Bijvoorbeeld, time verwijst naar het W3C Time Ontology, en qudt-schema verwijst naar het QUDT schema voor eenheden en dimensies.

# Graph 

De @graph sleutel bevat een lijst van objecten die de daadwerkelijke data van het document vertegenwoordigen. Elk object heeft een @type dat het type van het object aangeeft.

## Bemonstering

Beschrijft een bemonsteringsgebeurtenis. Het bevat details zoals het tijdstip van bemonstering, het object dat is bemonsterd, de organisatie die de bemonstering heeft uitgevoerd, de gebruikte procedure en het resultaat van de bemonstering.

## Monster

Dit object vertegenwoordigt een fysiek monster dat is genomen tijdens de bemonstering. Het bevat details zoals het type materiaal, het tijdstip van bemonstering en een unieke identificator.

## Meetpunt/Bemonsteringspunt

Dit object beschrijft een specifiek punt waar metingen of bemonsteringen worden uitgevoerd. Het bevat een identificator, geometrische gegevens en beschrijvende informatie.

## Observatieverzameling

Dit object groepeert meerdere observaties. Er zijn twee soorten observatieverzamelingen in dit document: één voor metingen ter plaatse en één voor weerobservaties.

## Observatie

Dit object beschrijft een specifieke observatie of meting. Het bevat details zoals het type observatie, het kenmerk dat wordt gemeten, en het resultaat van de observatie.