---
title: "Taskshell"
lang: en
layout: single
description: "A shell command that wraps Taskwarrior commands."
source: "https://github.com/GothenburgBitFactory/taskshell"
rank: 45
aliases:
    - /projects/tasksh
---
# Taskshell

Taskshell is a shell command that wraps Taskwarrior commands.
It is intended to provide simpler Taskwarrior access, and add a few new features of its own.
The project is new, bear with us please.

Taskshell replaces the built-in `shell` command of older releases, and the bundled `tasksh` program of version `2.3.0`.
The former was very limited and the latter unsupported, buggy and flawed.
This project represents GBF taking control of this project.

* `git clone --recursive https://github.com/GothenburgBitFactory/taskshell.git`
* `brew install tasksh`

## About

Taskshell is a shell that implements a review feature, and integrates `libreadline`.
It is on its own release schedule that is unhampered by lengthy Taskwarrior development cycles.
