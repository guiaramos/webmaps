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
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)


<!-- ABOUT THE PROJECT -->
## About The Project

![webmaps-volcanoes][product-screenshot]

This is a program in Python that creats a HTML file with Folium and Pandas containing two layers:

    * Markers: Vulcanoes in USA;
    * Polygon: Population by country in the World.

The markers are based on TXT file with the information of the location and the name of each Volcano, also it has a link for the Volcano information on Google. It colors are defined according the height level, as follows:
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

### Built With
This is the list of the tech stack:


#### Code editor
[![VS Code][VSCode-shield]][VScode-url]


#### Back-End
[![Python][Python-shield]][Python-url]
[![Json][Json-shield]][Json-url]


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running just follow the [Prerequisites](#prerequisites).

Excute the program and then enter the desired word:
```sh
Please, inform the word: USA
```


### Prerequisites
* Python 3
* Visual Code Studio

### Installation

1. Clone the repo
```sh
git clone https://github.com/guiaramos/webmaps.git
```
2. Open the terminal/CMD
3. Enter
```sh
python3 dictionary.py
```

<!-- CONTACT -->
## Contact

[![Gui][Gui-shield]][Gui-url]
[![LinkedIn][linkedin-shield]][linkedin-url]





<!-- MARKDOWN LINKS & IMAGES -->

[build-shield]: https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat-square
[contributors-shield]: https://img.shields.io/badge/contributors-1-orange.svg?style=flat-square
[license-shield]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/guilhermearamos/
[product-screenshot]: https://github.com/guiaramos/webmaps/tree/master/src/project.png
[VSCode-shield]:https://img.shields.io/badge/-Visual%20Studio%20Code-blue.svg?logo=visual-studio-code
[VScode-url]:https://code.visualstudio.com/docs
[Python-shield]:https://img.shields.io/badge/-Python-blueviolet.svg?logo=Python
[Python-url]:https://docs.python.org/3/
[Json-shield]:https://img.shields.io/badge/-JSON-blueviolet.svg?logo=JSON
[Json-url]:https://www.json.org/
[Gui-shield]:https://img.shields.io/badge/Guilherme%20Ramos-e--Mail-lightgrey.svg
[Gui-url]:gui_aramos@outlook.com

