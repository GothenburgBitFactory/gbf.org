---
title: "Vramsteg"
lang: en
layout: single
description: "A CLI progress bar that can be used from any script language."
source: "https://github.com/GothenburgBitFactory/vramsteg"
rank: 3
menu: main
aliases:
    - /projects/vramsteg
---
# Vramsteg

Vramsteg, from the Swedish framsteg (progress), is a CLI progress bar that can be used from any script language.
It supports color, labels, percentage completion, elapsed time and estimates.
It is used in our test suites.

* `git clone https://github.com/GothenburgBitFactory/vramsteg.git`
* `brew install vramsteg`

## About

Vramsteg adds progress-bar capability to a script/program that otherwise does not have one.
If a program has a lengthy iterative operation, it may benefit from using vramsteg, which provides these features:

* Display, removes or leaves a progress bar on screen
* Allows an arbitrary range to be represented (1-10, or 34-52, or 1-1000000)
* Has color, monochrome, or colorless progress bars
* Can display elapsed time
* Can estimate remaining time
* Configurable bar width
* Can show a prefix label
* Can show percentage completion

## Command Usage

![Vramsteg command usage](/img/vramsteg.png)
