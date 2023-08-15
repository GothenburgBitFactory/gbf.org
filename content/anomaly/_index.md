---
title: "Anomaly"
lang: en
layout: single
description: "A data anomaly detection utility. "
source: "https://github.com/GothenburgBitFactory/anomaly"
rank: 1
menu: main
aliases:
    - /projects/anomaly
---
# Anomaly

Anomaly can detect anomalous data in a numeric stream.

{{< project_facts anomaly >}}

## About

In order to do this, anomaly needs to see a stream of numeric data, and apply one of its detection methods.
If an anomaly is detected, a response is made, chosen from one or more built in methods.

## Numeric Stream

Anomaly works best in a pipe, and will read only numeric data from its input.
As a simple example, suppose you wish to monitor load average and look for unusual spikes.
The load average can be obtained from the 'uptime' command:

```
$ uptime
11:40  up 15 days,  4:04, 6 users, load averages: 0.38 0.32 0.32
```

We can extract the 5-minute load (the second of the three numbers) using this:

```
$ uptime | cut -f 13 -d ' '
0.29
```

That number can be extracted once a minute, using this:

```
$ while [ 1 ]; do uptime | cut -f 13 -d ' '; sleep 60; done
0.29
0.26
0.19
```

That is the kind of data stream that anomaly monitors.
White space (spaces, tabs, newlines) between the numbers are ignored, so we can simulate the above stream like this:

```
$ echo 0.29 0.26 0.19
```

This is a convenient way to demonstrate anomaly, shown below.

## Detection - Threshold

The simplest detection method is threshold, which compares the data to an absolute value.
This method can use a minimum and a maximum value for comparison.
These alternatives are all valid, and make use of `--min`, `--max` or both:

```
anomaly --threshold --min 1.22 --max 9.75
anomaly --threshold --min 1.22
anomaly --threshold --max 9.75
```

In the following example, the values '1' and '10' would be detected as anomalies:

```
$ echo 2 1 3 6 10 5 | anomaly --threshold --min 1.5 --max 8
Anomalous data detected.  The value 1 is below the minimum of 1.5.
Anomalous data detected.  The value 10 is above the maximum of 8.
```

## Detection - Standard Deviation

Standard deviation measures differences from the mean value of a sample of data, and is useful for detecting extraordinary values.
The sample size can be chosen such that there is enough data to determine a good mean value.
The limited sample size means that a rolling window of data is used, and therefore the mean and standard deviation is updated for the current window.
This makes the monitoring somewhat adaptive.
Here is an example:

```
anomaly --stddev --sample 20
```

This uses a sample size of the 20 most recent values, and will detect any values that are +/- 1 standard deviation from the mean.
An example:

```
$ echo 1 2 3 4 5 6 | anomaly --stddev --sample 5
Anomalous  data detected.  The value 6 is more than 1
sigma(s) above the mean value 3, with a sample size of 5. 
```

With a sample size of 5, comparisons begin only after the 6th value is seen.
In the example, the mean value of \[1 2 3 4 5\] is 3, and the standard deviation is 1.58.
This means that the 6th value is considered an anomaly if it is outside the range (3 +/- 1.58), which is from 1.42 to 4.58.

To make this less sensitive, a coefficient is introduced, which defaults to 1.0 (as above) but can be overridden:

```
$ echo 1 2 3 4 5 6 | anomaly --stddev --sample 5 --coefficient 1.9
$
```

In this example, the 6th value is not considered an anomaly because it is within the range (3 +/- (1.9 * 1.58)), which is between -0.002 and 6.002.

## Response - Message

The message response is the default, and consists of a single line of printed text.
It is a description of why the data value is considered an anomaly.
Here is an example:

```
$ echo 1 2 3 | anomaly --threshold --max 2.5
Anomalous data detected.  The value 3 is above the maximum of 2.5. 
```

The message can be suppressed, but another response must be specified:

```
$ echo 1 2 3 | anomaly --threshold --max 2.5 --quiet ... 
```

## Response - Execute

Anomaly can execute a program in response to detection.
Here an example uses the 'date' command, but any program can be used:

```
$ echo 1 2 3 | anomaly --threshold --max 2.5 --quiet --execute '/bin/date +%s'
1361727327
```

## Response - Signal

Anomaly can send a USR1 signal to a program in response to detection:

```
$ echo 1 2 3 | anomaly --threshold --max 2.5 --quiet --pid 12345
```

This sends the USR1 signal to the process with PID 12345.
The receiving program would need to respond accordingly.
