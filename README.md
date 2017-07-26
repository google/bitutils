# bitutils

This is a collection of scripts which make working with binary numbers a bit
easier.

-   `bin` converts its argument (or standard input) to binary.
-   `hex` converts its argument (or standard input) to hexadecimal.
-   `bitrule` displays a ruler below its standard input.

This is not an official Google product.

## Example

``` shellsession
$ bin 12345 | bitrule
0b11000000111001
  '|'''|'''|'''|
   12  8   4   0
```
