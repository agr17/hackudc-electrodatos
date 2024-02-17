<!--
SPDX-FileCopyrightText: 2024 Manuel Corujo
SPDX-FileCopyrightText: 2024 María López
SPDX-FileCopyrightText: 2024 Pablo Boo
SPDX-FileCopyrightText: 2024 Ángel Regueiro

SPDX-License-Identifier: MIT
-->

# HackUDC: electrodatos

<p align="center">
    <a href="https://github.com/agr17/hackudc-electrodatos/" alt="hackudc-electrodatos">
        <img src="https://github.com/agr17/hackudc-electrodatos/blob/main/assets/electrodatos-high-resolution-logo.png"/>
    </a>
</p>

<p align="center">
    <a href="https://github.com/agr17/hackudc-electrodatos/blob/develop/LICENSE" alt="License">
        <img src="https://img.shields.io/github/license/agr17/hackudc-electrodatos" />
    </a>
    <a href="https://github.com/agr17/hackudc-electrodatos/graphs/contributors" alt="Contributors">
        <img src="https://img.shields.io/github/contributors/agr17/hackudc-electrodatos" />
    </a>
    <a href="https://github.com/agr17/hackudc-electrodatos/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/agr17/hackudc-electrodatos" />
    </a>
    <a href="#stars" alt="Stars">
        <img src="https://img.shields.io/github/stars/agr17/hackudc-electrodatos" />
    </a>
</p>

This work is licensed under a [MIT license](https://opensource.org/license/mit/).

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png

## _Your electric bill easier than ever_

Electrodatos is an electric bill visualizer.

## TOC

- [Tech](#tech)
- [Development](#development)
  * [Git-Flow](#git-flow)
- [Usage](#usage)
- [License](#license)


## Tech

Electrodatos uses a number of open source projects to work properly:

- [Black] - An uncompromising Python code formatter.
- [Bokeh] - A library used to make interactive data visualization in the browser.
- [Pandas] - A flexible and powerful data analysis / manipulation library for Python.
- [pvpc] - A library that provides information about PVPC costs in Spain from the REE API.

And of course Electrodatos itself is open source with a [public repository](https://github.com/agr17/hackudc-electrodatos) on GitHub.

## Development

Want to contribute? Great!

### Git-Flow

Carggregator uses git-flow to structure its repository! Open your favorite Terminal and run these commands.

Initialize git-flow:
```sh
bash .bin/git_gitflow.sh init
```

Start a new feature:
```sh
git flow feature start Issue-X
```

Finish a feature:
```sh
git flow feature finish Issue-X
```

## Instalation

````
pip install -r requirements.txt
````


## Usage

### Bokeh

````
bokeh serve bokeh-vis --show --args .\data\cups\electrodatos_0.csv 2022
````


## License
The MIT License (MIT)

[hack-udc-electrodatos]: <https://github.com/agr17/hackudc-electrodatos>
[git-repo-url]: <https://github.com/agr17/hackudc-electrodatos.git>

[Black]: <https://github.com/psf/black>
[Bokeh]: <https://github.com/bokeh/bokeh>
[Pandas]: <https://github.com/pandas-dev/pandas>
[pvpc]: <https://github.com/David-Lor/python-pvpc>
