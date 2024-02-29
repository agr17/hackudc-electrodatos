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

- [Installation and usage](#installation-and-usage)
- [Tech](#tech)
- [Development](#development)
- [License](#license)

## Installation and usage

````
pip install -r requirements.txt
````

````
bokeh serve bokeh-vis --show --args .\data\cups\electrodatos_0.csv 2022
````

## Tech

Electrodatos uses a number of open source projects to work properly:

- [Black] - An uncompromising Python code formatter.
- [Bokeh] - A library used to make interactive data visualization in the browser.
- [Pandas] - A flexible and powerful data analysis / manipulation library for Python.
- [pvpc] - A library that provides information about PVPC costs in Spain from the REE API.

And of course Electrodatos itself is open source with a [public repository](https://github.com/agr17/hackudc-electrodatos) on GitHub.

## Development

Here are several ways you can contribute to the Electrodatos project:

- Propose Pull Requests (PRs) to rectify bugs or introduce new features.
- Offer feedback and report bugs concerning the software or documentation.
- Improve our documentation.

## Demo

https://github.com/agr17/hackudc-electrodatos/assets/29493377/dd309cb9-2433-4c6c-93cd-3764e64a536f



## License
The MIT License (MIT).

[hack-udc-electrodatos]: <https://github.com/agr17/hackudc-electrodatos>
[git-repo-url]: <https://github.com/agr17/hackudc-electrodatos.git>

[Black]: <https://github.com/psf/black>
[Bokeh]: <https://github.com/bokeh/bokeh>
[Pandas]: <https://github.com/pandas-dev/pandas>
[pvpc]: <https://github.com/David-Lor/python-pvpc>
