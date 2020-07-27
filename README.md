# Proportional Navigation
![Test](https://github.com/iwishiwasaneagle/proportional_navigation/workflows/Python%20package/badge.svg) [![PyPI version](https://badge.fury.io/py/proportional-navigation.svg)](https://badge.fury.io/py/proportional-navigation) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/proportional_navigation) [![Coverage Status](https://coveralls.io/repos/github/iwishiwasaneagle/proportional_navigation/badge.svg?branch=master)](https://coveralls.io/github/iwishiwasaneagle/proportional_navigation?branch=master) [![Downloads](https://pepy.tech/badge/proportional-navigation)](https://pepy.tech/project/proportional-navigation)

A package to easily do [proportional navigation](https://en.wikipedia.org/wiki/Proportional_navigation). This navigation equation is popular for target-persuader Line-of-Sight applications, such as missiles. The popularity stems partially from it's simple implementation, and effectiveness.

## Explanation on notation

From the below figure, it is clear that we are using velocity/heading model for each body. Such that V is the magnitude of velocity, psi is heading relative to world x-axis, and x and y of the body is relative to the world axes.

![Axes](images/axes.png)

## Installation

```bash
git clone https://github.com/iwishiwasaneagle/proportional_navigation
cd proportional_navigation
python setup.py install
```
```bash
pip install proportional_navigation
```
