<!-- PROJECT SHIELDS -->
[![Build Status][build-shield]]()
[![Contributors][contributors-shield]]()
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/guiaramos/webmaps.git>
    <img src="" alt="Logo" width="80" height="80">
  </a>

  <h1 align="center">Webmaps - Volcanoes</h1>

  <p align="center">
    A webmap created with Python that shows the volcanoes of USA
    <br />
    <a href="https://github.com/guiaramos/webmaps.git"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/guiaramos/webmaps.git">View Demo</a>
    ·
    <a href="https://github.com/guiaramos/webmaps.git/issues">Report Bug</a>
    ·
    <a href="https://github.com/guiaramos/webmaps.git/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Contact](#contact)


<!-- ABOUT THE PROJECT -->
## **About The Project**
___

![webmaps-volcanoes][product-screenshot]

This is a program in Python that creats a HTML file with Folium and Pandas containing two layers:

    * Markers: Vulcanoes in USA;
    * Polygon: Population by country in the World.

The markers are based on CSV file with the information of the location and the name of each Volcano, also it has a link for the Volcano information on Google. It colors are defined according the height level, as follows:
```
    if Height < 1K:
        Color = 'green'
    elif 1K <= Height < 3K:
        Color = 'orange'
    else:
        Color = 'red'
```

The polygon layer are referred to the population by each country, based on JSON file that contains the detail information from 2005, it colors are defined by the population size, as follows:

```
    if Population < 10M:
        Color = 'green'
    elif 10M <= Population < 20M:
        Color = 'orange'
    else:
        Color = 'red'
```

## Built With
___
This is the list of the tech stack:


#### __Code editor__
[![VS Code][VSCode-shield]][VScode-url]

#### ___Front-End___
[![HTML][HTML-shield]][HTML-url]

#### ___Back-End___
[![Python][Python-shield]][Python-url]

#### ___Library___
[![Folium][Folium-shield]][Folium-url]
[![Pandas][Pandas-shield]][Pandas-url]

##### ___Database___
[![Json][Json-shield]][Json-url]
[![TXT][TXT-shield]][TXT-url]


<!-- GETTING STARTED -->
## Getting Started
___

To get a local copy up and running just follow the [Prerequisites](#prerequisites).

#### Excute the program:
```sh
python3 webmaps\map.py
```
#### Open the file:
```
webmaps\Map_html_popup_simple.html
```


### Prerequisites
* Python 3
    * Folium
    * Pandas


### Installation

1. Clone the repo
```sh
git clone https://github.com/guiaramos/webmaps.git
```

<!-- CONTACT -->
## Contact
___

[![Gui][Gui-shield]][Gui-url]
[![LinkedIn][linkedin-shield]][linkedin-url]





<!-- MARKDOWN LINKS & IMAGES -->

[build-shield]: https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat-square
[contributors-shield]: https://img.shields.io/badge/contributors-1-orange.svg?style=flat-square
[license-shield]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/guilhermearamos/
[product-screenshot]: src/project.png
[VSCode-shield]:https://img.shields.io/badge/-Visual%20Studio%20Code-lightgrey.svg?logo=visual-studio-code
[VScode-url]:https://code.visualstudio.com/docs
[Python-shield]:https://img.shields.io/badge/-Python-9cf.svg?logo=Python
[Python-url]:https://docs.python.org/3/
[Json-shield]:https://img.shields.io/badge/-JSON-yellow.svg?logo=JSON
[Json-url]:https://www.json.org/
[Gui-shield]:https://img.shields.io/badge/Guilherme%20Ramos-e--Mail-lightgrey.svg
[Gui-url]:gui_aramos@outlook.com
[HTML-shield]:https://img.shields.io/badge/-HTML-blue.svg?logo=HTML5
[HTML-url]:https://www.w3schools.com/html/html5_intro.asp
[TXT-shield]:https://img.shields.io/badge/-TXT-yellow.svg?logo=sublime-text
[TXT-url]: https://en.wikipedia.org/wiki/Comma-separated_values
[Folium-shield]:https://img.shields.io/badge/-Folium-green.svg?logo=Python
[Folium-url]:https://pypi.org/project/folium/
[Pandas-shield]:https://img.shields.io/badge/-Pandas-green.svg?logo=Python
[Pandas-url]:https://pandas.pydata.org/