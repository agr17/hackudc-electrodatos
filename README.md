# hackudc-electrodatos

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
- [Demo](#demo)
- [License](#license)


## Tech

Electrodatos uses a number of open source projects to work properly:

- [Black] - An uncompromising Python code formatter.
- [Bokeh] - A library used to make highly interactive graphs and visualizations.
- [pvpc] - A library that provides information about PVPC costs in Spain from the REE API.

And of course Electrodatos itself is open source with a [public repository][hackudc-electrodatos] on GitHub.

## Development

Want to contribute? Great!

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
[pvpc]: <https://github.com/David-Lor/python-pvpc>
