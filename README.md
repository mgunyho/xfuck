# xfuck

Esoteric programming language inspired by [this xkcd](https://xkcd.com/2309/):

![https://imgs.xkcd.com/comics/x.png](https://imgs.xkcd.com/comics/x.png)

An xfuck compiler takes a pdf file as input and converts to brainfuck (using a python script), where eight different fonts correspond to the eight symbols of brainfuck.

## Random ideas / features

- Cross platform: pdf files can be created on all platforms. Use anything as an IDE: Word, Latex, ... The possibilities are truly endless.

## TODO:

- Brainfuck to xfuck (typesetted pdf)
  - for testing: X (e.g. python) to brainfuck compiling workflow 
- xfuck to brainfuck to local binary executable
- xfuck to brainfuck ASCII
- example fies in latex, word, libreoffice, html (export to pdf using e.g. browser) 
- ???
- Profit.
- Ebin 2 min vidyo

## Language specification

xfuck source files are PDF files. The first eight characters of the pdf should have eight different fonts, each corresponding to [one letter](https://en.wikipedia.org/wiki/Brainfuck#Commands) of brainfuck.

The only allowed text characters in the PDF are the character `'X'` or whitespace. Other characters are a syntax error. An exception is the string `X Æ A-12`, which is the same as  a single `X`. Other content, such as images or embedded SWF files are ignored.
