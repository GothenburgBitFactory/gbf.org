---
title: "Taskshell"
lang: en
layout: single
description: "A shell command that wraps Taskwarrior commands."
source: "https://github.com/GothenburgBitFactory/taskshell"
rank: 45
menu: main
aliases:
    - /projects/tasksh
---
# Taskshell

Taskshell is a shell command that wraps Taskwarrior commands.

{{< project_facts tasksh >}}

## About

Taskshell replaces the built-in `shell` command of older Taskwarrior releases, and the bundled `tasksh` program of version `2.3.0`.
The former was very limited and the latter unsupported, buggy and flawed.

Taskshell is a shell that implements a review feature, and integrates `libreadline`.
It is on its own release schedule that is unhampered by lengthy Taskwarrior development cycles.
