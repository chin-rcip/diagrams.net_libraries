[*Le français suit*](https://github.com/chin-rcip/diagrams.net_libraries#biblioth%C3%A8ques-logicielles-diagramsnet)

# diagrams.net Libraries

An overview of diagrams.net libraries and instructions on how to use them.

**Version**: 2.0

**Created date**: 2021-04-22

**Last update**: 2024-10-02

**Contact**: For any questions and/or feedback, please contact us at pch.RCIP-CHIN.pch@canada.ca, indicating “diagrams.net libraries” in the subject line of the email.

- [Main Use](#main-use)
- [Context](#context)
- [Essential Vocabularies and Prior Knowledge](#essential-vocabularies-and-prior-knowledge)
- [Intended Audience(#s) and Section Description](#intended-audiences-and-section-description)
- [Instructions](#instructions) 
	- [Loading the Libraries](#loading-the-libraries)
		- [Opening a Library File](#opening-a-library-file)
		- [Loading a Library via a URL](#loading-a-library-via-a-url)
	- [Using the Libraries](#using-the-libraries)
- [Memory Aids](#memory-aids)
- [To Know More](#to-know-more)
- [Licence](#licence)
- [Bibliography](#bibliography)

## Main Use

  - To facilitate the visualization of data models based on [CIDOC CRM](http://www.cidoc-crm.org/) and [its extensions](http://www.cidoc-crm.org/collaborations) when using the diagrams.net tool.

## Context

**[diagrams.net](https://www.diagrams.net/) libraries** is a collection of custom shape library files (.xml) of ontologies used to represent semantic patterns through [diagrams.net](https://www.diagrams.net/). It is maintained by the Canadian Heritage Information Network (CHIN) and used to generate diagrams in the context of its Linked Open Data projects. Currently, CHIN provides eight libraries for the following CIDOC CRM ontologies (i.e. the ones that are officially released in RDFS format). The libraries are of benefit to users who design diagrams for data models that are based on CIDOC CRM.

  - CIDOC CRM base (version 7.1.3): includes two libraries, one with properties' quantification, and one without.

  - LRMoo (version 1.0)

  - PRESSoo (version 1.0)

  - CRMdig (version 3.2.2)

  - CRMpc (version 7.1.3)

  - CRMarchaeo (version 2.1.1)

  - CRMgeo (version 1.2)

*This work is inspired by the [work of Nicola Carboni](https://github.com/ncarboni/Shapes_CIDOC-CRM).*

## Essential Vocabularies and Prior Knowledge

A custom library is a set of pre-designed shapes that can be easily dragged and dropped in the drawing canvas to facilitate the drawing process. It is usually found on the left side panel of the diagrams.net editor.

Each library contains the shapes of all the [classes](https://chin-rcip.github.io/collections-model/en/resources/current/glossary#class-noun) as well as the connectors for the [properties](https://chin-rcip.github.io/collections-model/en/resources/current/glossary#property-noun) of each ontology. The colour scheme (see below) is based on a proposal by CIDOC CRM SIG for [CIDOC CRM](http://www.cidoc-crm.org/).

![](/images/color_en.png)

## Intended Audience(s) and Section Description

The tool can be used by anyone who wants to visualize data models that are based on CIDOC CRM and its extensions. There are two methods of loading the libraries depending on the version of diagrams.net being used:

  - [Desktop version](#opening-a-library-file)

  - [Online version](#loading-a-library-via-a-url)

The [Using the libraries](#using-the-libraries) section provides a more detailed description and guide to the usage of the libraries themselves.

## Instructions

### Loading the Libraries

To use the libraries, there are two options:

  - Opening a library XML file directly to the editor, or

  - Loading a library via URL.

#### Opening a Library File

*This option is most suitable for the diagrams.net desktop version.*

Launch the diagrams.net editor, click **File Open Library from**, then:

1.  If the Github repository or the XML file(s) are downloaded:
    
    1.  Select the service or device where the file(s) are stored;
    
    2.  Locate and select the library (the file extension will be
        .xml), and click **Choose**.

OR

2.  Directly use the Github URL for each library file in the folder **/cidoc-crm**:
    
    1.  CIDOC CRM base

        a. Without properties' quantification
           (https://raw.githubusercontent.com/chin-rcip/diagrams.net_libraries/main/cidoc-crm/crm_library.xml)

        b. With properties' quantification
           (https://raw.githubusercontent.com/chin-rcip/diagrams.net_libraries/main/cidoc-crm/crm_quantifications_library.xml)
    
    2.  LRMoo
        (https://raw.githubusercontent.com/chin-rcip/diagrams.net_libraries/main/cidoc-crm/lrmoo_library.xml)
    
    3.  PRESSoo
        (https://raw.githubusercontent.com/chin-rcip/diagrams.net_libraries/main/cidoc-crm/pressoo_library.xml)
    
    4.  CRMdig
        (https://raw.githubusercontent.com/chin-rcip/diagrams.net_libraries/main/cidoc-crm/crmdig_library.xml)
    
    5.  CRMpc
        (https://raw.githubusercontent.com/chin-rcip/diagrams.net_libraries/main/cidoc-crm/crmpc_library.xml)
    
    6.  CRMarchaeo
        (https://raw.githubusercontent.com/chin-rcip/diagrams.net_libraries/main/cidoc-crm/crmpc_library.xml)
    
    7.  CRMgeo
        (https://raw.githubusercontent.com/chin-rcip/diagrams.net_libraries/main/cidoc-crm/crmpc_library.xml)

![](/images/diagrams_net_en_1.png)

#### Loading a Library via a URL

*This option is most suitable for the diagrams.net online version.*

Click on the following URLs to open the diagrams.net editor with:

  - [CRM base library (without properties' quantification)](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrm_library.xml)

  - [CRM base library (with properties' quantification)](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrm_quantifications_library.xml)

  - [LRMoo library](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Flrmoo_library.xml)

  - [PRESSoo library](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fpressoo_library.xml)

  - [CRMdig library](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmdig_library.xml)

  - [CRMpc library](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmpc_library.xml)

  - [CRMarchaeo library](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmarchaeo_library.xml)

  - [CRMgeo library](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmgeo_library.xml)

  - [All libraries](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrm_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrm_quantifications_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Flrmoo_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmdig_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmpc_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fpressoo_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmarchaeo_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmgeo_library.xml)

Once loaded, the library is usually cached by the browser, so there is no need to load it every time, unless the browser data has been cleared.

### Using the Libraries

Each library contains two types of shapes:

1. Rounded rectangle shapes for classes (each shape is filled with colour, per the colour scheme described above).

    - Shape:

        - Rounded rectangle

        - Border:

            - solid 
            
            - black
            
            - 1 pt
        
        - Width: 140

        - Height: 70 

        - Fill: per the colour scheme described above

    - Text:

        - Font: Helvetica

        - Size: 16

        - Color: black

        - Horizontal align: center

        - Vertical align: middle

        - Weight: bold

        - Word wrap

        - Value: entity name without underscore

    - Data:

        - URI
        
        - Labels in available languages
        
        - No scope note
        
        - Link (clickable)


2. Black arrows for properties.

    - Shape:

        - One-way arrow

        - Stroke width: 2 pt
        
        - Color: black

    - Text:

        - Font: Helvetica

        - Size: 14

        - Color: black

        - Horizontal align: center

        - Vertical align: middle

        - Weight: bold

        - Background color: white

        - Value: entity name without underscore, quantifications

    - Data:

        - URI
        
        - Labels in available languages
        
        - No scope note
        
        - Link (clickable)

![](/images/diagrams_net_en_2.png)

To search for any shape, either classes or properties, enter its CIDOC CRM code and/or label.

![](/images/diagrams_net_en_3.png)

## Memory Aids

  - Use [this link](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrm_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrm_quantifications_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Flrmoo_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmdig_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmpc_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fpressoo_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmarchaeo_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmgeo_library.xml) to load all libraries at once in the diagrams.net online version.

  - Use the Search tool to find an entity, either by code and/or label.

## For More Information

Consult the following resources for further information on how to generate, share and load diagrams.net’s custom libraries in general:

  - [https://desk.draw.io/support/solutions/articles/16000067790](https://desk.draw.io/support/solutions/articles/16000067790)

  - [http://jgraph.github.io/drawio-libs/](http://jgraph.github.io/drawio-libs/)

## Licence

Files in this repository are made available under the MIT License. To meet the attribution requirements of this license, you must indicate the copyright holder using the following:

> Copyright (c) 2021-2022 Canadian Heritage Information Network, Canadian Heritage, Government of Canada - Réseau Canadien d'information sur le patrimoine, Patrimoine canadien, Gouvernement du Canada

> diagrams.net is distributed under [Apache License 2.0](https://github.com/jgraph/drawio/blob/dev/LICENSE).
> Copyright 2021 diagrams.net (JGraph)

## Bibliography

Benson, David. 2020. “Work with Custom Shape Libraries.” Legacy Desk - Do Not Use. September 15, 2020. [https://drawio.freshdesk.com/support/solutions/articles/16000067790-work-with-custom-shape-libraries](https://drawio.freshdesk.com/support/solutions/articles/16000067790-work-with-custom-shape-libraries).

Canadian Heritage Information Network (CHIN). 2021a. “class (noun).” In *Glossary*. Ottawa, ON: Government of Canada / Gouvernement du Canada. [https://chin-rcip.github.io/collections-model/en/resources/current/glossary#class-noun](https://chin-rcip.github.io/collections-model/en/resources/current/glossary#class-noun)

———. 2021b. “property (noun).” In *Glossary*. Ottawa, ON: Government of Canada / Gouvernement du Canada. [https://chin-rcip.github.io/collections-model/en/resources/current/glossary#property-noun](https://chin-rcip.github.io/collections-model/en/resources/current/glossary#property-noun)

Carboni, Nicola. (2020) 2021. Shapes_CIDOC-CRM. [https://github.com/ncarboni/Shapes_CIDOC-CRM](https://github.com/ncarboni/Shapes_CIDOC-CRM)

jgraph. n.d. “Diagrams.Net Libraries.” Drawio-Libs. Accessed May 13, 2021. [http://jgraph.github.io/drawio-libs/](http://jgraph.github.io/drawio-libs/)

---

# Bibliothèques logicielles diagrams.net

Un aperçu des bibliothèques logicielles diagrams.net et explique comment les utiliser.

**Version** : 2.0

**Créé le** : 2021-04-22

**Mis à jour le** : 2024-10-02

**Des questions?** : Veuillez adresser vos questions et commentaires par courriel à l’adresse [pch.RCIP-CHIN.pch@canada.ca](mailto:pch.RCIP-CHIN.pch@canada.ca). Précisez « Bibliothèques diagrams.net » dans l’objet.

- [Utilisation principale](#utilisation-principale)
- [Contexte](#contexte)
- [Vocabulaire de base et connaissances préalables](#vocabulaire-de-base-et-connaissances-préalables)
- [Auditoire visé et description des sections](#auditoire-visé-et-description-des-sections)
- [Instructions](#instructions)
	- [Chargement des bibliothèques](#chargement-des-bibliothèques)
		- [Ouverture d’une bibliothèque](#ouverture-dune-bibliothèque)
		- [Chargement d’une bibliothèque par son URL](#chargement-dune-bibliothèque-par-son-URL)
	- [Utilisation des bibliothèques](#utilisation-des-bibliothèques)
- [Aide-mémoire](#aide-mémoire)
- [Pour en savoir plus](#pour-en-savoir-plus)
- [Licence](#licence)
- [Bibliographie](#bibliographie)

## Utilisation principale

  - Simplifier la visualisation de modèles de données fondés sur [CIDOC CRM](http://www.cidoc-crm.org/) et [ses extensions](http://www.cidoc-crm.org/collaborations) lorsque ceux-ci sont réalisés par l’intermédiaire de l’outil [diagrams.net](https://www.diagrams.net/).

## Contexte

Les bibliothèques [diagrams.net](https://www.diagrams.net/) constituent un ensemble de fichiers XML d’ontologies qui sert à représenter des patrons conceptuels à l’aide du logiciel [diagrams.net](https://www.diagrams.net/). Tenu à jour par le Réseau canadien d’information sur le patrimoine (RCIP), ces bibliothèques logicielles permettent de créer des diagrammes dans le cadre de projets de données ouvertes et liées. Le RCIP a jusqu’à maintenant créé huit bibliothèques destinées aux ontologies du Modèle conceptuel de référence du Comité international pour la Documentation (CIDOC CRM); celles-ci sont diffusées officiellement en format RDFS et répertoriées ci-dessous. Elles seront utiles aux utilisateurs qui créent des diagrammes de modèles de données fondés sur le CIDOC CRM.

  - CIDOC CRM base (version 7.1.3) : comprend deux bibliothèques logicielles, une avec la quantification des propriétés et l'autre sans.

  - LRMoo (version 1.0)

  - PRESSoo (version 1.0)

  - CRMdig (version 3.2.2)

  - CRMpc (version 7.1.3)

  - CRMarchaeo (version 2.1.1)

  - CRMgeo (version 1.2)

*Ces travaux ont été inspirés par le [travail de Nicola Carboni](https://github.com/ncarboni/Shapes_CIDOC-CRM).*

## Vocabulaire de base et connaissances préalables

Une bibliothèque consiste en un ensemble de formes qu’on peut simplement glisser et déposer dans un diagramme pour en faciliter la création. Elle se trouve habituellement dans le volet gauche du logiciel diagrams.net.

Chaque bibliothèque contient les formes de toutes les [classes](https://chin-rcip.github.io/collections-model/en/resources/current/glossary#class-noun) et les connecteurs correspondant aux [propriétés](https://chin-rcip.github.io/collections-model/en/resources/current/glossary#property-noun) de chaque ontologie. La palette de couleurs choisie (voir ci-dessous) est fondée sur une proposition du CIDOC CRM SIG pour le [CIDOC CRM](http://www.cidoc-crm.org/).

![](/images/color_fr.png)

## Auditoire visé et description des sections 

Quiconque voulant visualiser des modèles de données fondés sur le CIDOC CRM et ses extensions peut utiliser cet outil. Selon la version de diagrams.net utilisée, deux versions permettent de charger les bibliothèques :

  - [version bureau (version locale)](#ouverture-dune-bibliothèque)

  - [version en ligne](#chargement-dune-bibliothèque-par-son-url)

Vous trouverez à la rubrique [Utilisation des bibliothèques](#utilisation-des-bibliothèques) une description plus approfondie des bibliothèques et des conseils sur leur utilisation.

## Instructions

### Chargement des bibliothèques 

Vous pouvez accéder à l’une ou l’autre des bibliothèques de deux façons :

  - vous ouvrez une bibliothèque XML directement dans le logiciel;

  - vous chargez la bibliothèque voulue par son URL.

#### Ouverture d’une bibliothèque 

*Cette option est la plus appropriée à l’usage local du logiciel diagrams.net.*

Lancez le logiciel diagrams.net, cliquez dans l’ordre sur **Fichier** puis **Ouvrir une librairie depuis**, et :

1.  si le répertoire Github ou les fichiers XML sont déjà téléchargés :
    
    1.  choisissez le service ou l’appareil où se trouvent les
        fichiers;
    
    2.  localisez le fichier voulu et sélectionnez-le (l’extension est
        .xml), puis cliquez sur **Ouvrir**.

OU

2.  entrez directement l’URL Github de chaque bibliothèque, dans le répertoire **/cidoc-crm** :
    
    1.  CIDOC CRM base
        
        a. Sans la quantification des propriétés
           (https://raw.githubusercontent.com/chin-rcip/diagrams.net_libraries/main/cidoc-crm/crm_library.xml)

        b. Avec la quantification des propriétés
           (https://raw.githubusercontent.com/chin-rcip/diagrams.net_libraries/main/cidoc-crm/crm_quantifications_library.xml)        
    
    2.  LRMoo
        (https://raw.githubusercontent.com/chin-rcip/diagrams.net_libraries/main/cidoc-crm/lrmoo_library.xml)
    
    3.  PRESSoo
        (https://raw.githubusercontent.com/chin-rcip/diagrams.net_libraries/main/cidoc-crm/pressoo_library.xml)
    
    4.  CRMdig
        (https://raw.githubusercontent.com/chin-rcip/diagrams.net_libraries/main/cidoc-crm/crmdig_library.xml)
    
    5.  CRMpc
        (https://raw.githubusercontent.com/chin-rcip/diagrams.net_libraries/main/cidoc-crm/crmpc_library.xml)
    
    6.  CRMarchaeo
        (https://raw.githubusercontent.com/chin-rcip/diagrams.net_libraries/main/cidoc-crm/crmpc_library.xml)
    
    7.  CRMgeo
        (https://raw.githubusercontent.com/chin-rcip/diagrams.net_libraries/main/cidoc-crm/crmpc_library.xml)

![](/images/diagrams_net_fr_1.PNG)

#### Chargement d’une bibliothèque par son URL 

*Cette option est la plus appropriée à l’usage en ligne du logiciel diagrams.net.*

Cliquez sur l’une des adresses suivantes pour ouvrir diagrams.net et y charger la bibliothèque voulue :

  - [Bibliothèque CRM base (sans la quantification des propriétés)](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrm_library.xml)

  - [Bibliothèque CRM base (avec la quantification des propriétés)](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrm_quantifications_library.xml)

  - [Bibliothèque LRMoo](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Flrmoo_library.xml)

  - [Bibliothèque PRESSoo](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fpressoo_library.xml)

  - [Bibliothèque CRMdig](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmdig_library.xml)

  - [Bibliothèque CRMpc](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmpc_library.xml)

  - [Bibliothèque CRMarchaeo](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmarchaeo_library.xml)

  - [Bibliothèque CRMgeo](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmgeo_library.xml)

  - [Toutes les bibliothèques](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrm_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrm_quantifications_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Flrmoo_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmdig_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmpc_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fpressoo_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmarchaeo_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmgeo_library.xml)

Une fois chargée, la bibliothèque est habituellement gardée dans la mémoire cache du navigateur Web; il est donc inutile de la charger de nouveau à moins d’avoir vidé la mémoire cache.

### Utilisation des bibliothèques 

Les bibliothèques contiennent deux types de formes :

1. des rectangles arrondis colorés selon la palette de couleurs décrite ci-dessus et qui représentent les classes;

    - Forme:

        - Rectangle arrondi

        - Bordure:

            - pleine 
            
            - noire
            
            - 1 pt
        
        - Largeur: 140

        - Hauteur: 70 

        - Remplissage: selon la palette de couleurs décrite ci-dessus

    - Texte:

        - Police: Helvetica

        - Taille: 16

        - Couleur: noir

        - Alignement horizontal: centré

        - Alignement vertical: milieu

        - Poids de la police: gras

        - Retour à la ligne

        - Valeur: nom de l'entité sans barre de soulignement

    - Donnée:

        - URI
        
        - Étiquettes dans les langues disponibles
        
        - Pas de note d'application
        
        - Lien (cliquable)

2. des flèches noires qui représentent les propriétés.

    - Forme:

        - Flèche unidirectionnelle

        - Largeur du trait: 2 pt
        
        - Couleur: noire

    - Texte:

        - Police: Helvetica

        - Taille: 14

        - Couleur: noir

        - Alignement horizontal: centré

        - Alignement vertical: milieu

        - Poids de la police: gras

        - Couleur de l'arrière-plan: blanc
          
        - Valeur: nom de l'entité sans barre de soulignement, quantifications

    - Donnée:

        - URI
        
        - Étiquettes dans les langues disponibles
        
        - Pas de note d'application
        
        - Lien (cliquable)

![](/images/diagrams_net_fr_2.png)

Pour trouver une forme en particulier (classes ou propriétés), entrez son code CIDOC CRM ou son titre dans le champ de recherche.

![](/images/diagrams_net_fr_3.png)

## Aide-mémoire 

  - Cliquez [ici](https://app.diagrams.net/?splash=0&clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrm_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrm_quantifications_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Flrmoo_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmdig_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmpc_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fpressoo_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmarchaeo_library.xml;Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fchin-rcip%2Fdiagrams.net_libraries%2Fmain%2Fcidoc-crm%2Fcrmgeo_library.xml) pour charger toutes les bibliothèques dans la version en ligne de diagrams.net.

  - Interrogez l’outil de recherche pour trouver une entité par son code ou son titre.

## Pour plus d'informations

Pour en savoir plus sur la création, l’échange et le chargement des bibliothèques de formes dans diagrams.net, consultez les ressources documentaires suivantes (en anglais seulement) :

  - [https://desk.draw.io/support/solutions/articles/16000067790](https://desk.draw.io/support/solutions/articles/16000067790)

  - [http://jgraph.github.io/drawio-libs/](http://jgraph.github.io/drawio-libs/)

## Licence

Les fichiers de ce répertoire sont distribués en vertu de la licence MIT. Pour satisfaire aux exigences relatives à son attribution, vous devez préciser comme suit le détenteur du droit d’auteur :

> Copyright (c) 2021-2022 Canadian Heritage Information Network, Canadian Heritage, Government of Canada - Réseau canadien d'information sur le patrimoine, Patrimoine canadien, Gouvernement du Canada

> diagrams.net est distribué sous la licence [Apache License 2.0](https://github.com/jgraph/drawio/blob/dev/LICENSE).
> Copyright 2021 diagrams.net (JGraph)

## Bibliographie

Benson, David. 2020. « *Work with Custom Shape Libraries* ». Legacy desk – do not use. 15 septembre 2020. [https://drawio.freshdesk.com/support/solutions/articles/16000067790-work-with-custom-shape-libraries](https://drawio.freshdesk.com/support/solutions/articles/16000067790-work-with-custom-shape-libraries). (En anglais seulement)

Carboni, Nicola. (2020) 2021. Shapes_CIDOC-CRM. [https://github.com/ncarboni/Shapes_CIDOC-CRM](https://github.com/ncarboni/Shapes_CIDOC-CRM) (en anglais seulement)

jgraph. n.d. « Diagrams.Net Libraries ». Drawio-Libs. Consulté le 13 mai 2021. [http://jgraph.github.io/drawio-libs/](http://jgraph.github.io/drawio-libs/) (en anglais seulement)

Réseau canadien d’information sur le patrimoine (RCIP). 2021a. « classe (nom féminin) ». Dans le *Glossaire*. Ottawa, ON : Government of Canada / Gouvernement du Canada. [https://chin-rcip.github.io/collections-model/fr/ressources/actuel/glossaire#classe-nom-feminin](https://chin-rcip.github.io/collections-model/fr/ressources/actuel/glossaire#classe-nom-feminin)

Réseau canadien d’information sur le patrimoine (RCIP). 2021a. « propriété (nom féminin) ». Dans le *Glossaire*. Ottawa, ON : Government of Canada / Gouvernement du Canada. [https://chin-rcip.github.io/collections-model/fr/ressources/actuel/glossaire#propriete-nom-feminin](https://chin-rcip.github.io/collections-model/fr/ressources/actuel/glossaire#propriete-nom-feminin)





