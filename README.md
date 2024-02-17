# HackUDC: electrodatos

<p align="center">
    <a href="https://github.com/agr17/hackudc-electrodatos/" alt="hackudc-electrodatos">
        <img src="https://github.com/agr17/hackudc-electrodatos/blob/main/assets/electrodatos-high-resolution-logo.svg.png"/>
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

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png

## _Your electric bill easier than ever_

Electrodatos is an electric bill visualizer.

## TOC

- [Tech](#tech)
- [Development](#development)
  * [GitHub](#github)
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

### GitHub

In addition to a repository, GitHub offers a range of features, including a Kanban board for project planning. We have a simple approach where we use issues to plan new features. We create branches from these issues and merge them through pull requests. There are no specific requirements for naming or other related aspects, simply use English.


## Instalation

````
pip install -r requirements.txt
````


## Usage

### Bokeh

````
bokeh serve bokeh-vis --show --args .\data\cups\electrodatos_0.csv
````


## License

GNU General Public License v3.0


[hack-udc-electrodatos]: <https://github.com/agr17/hackudc-electrodatos>
[git-repo-url]: <https://github.com/agr17/hackudc-electrodatos.git>

[Black]: <https://github.com/psf/black>
[Bokeh]: <https://github.com/bokeh/bokeh>
[Pandas]: <https://github.com/pandas-dev/pandas>
[pvpc]: <https://github.com/David-Lor/python-pvpc>
