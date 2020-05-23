# xfuck (working title)

Language inspired by this xkcd:

![https://imgs.xkcd.com/comics/x.png](https://imgs.xkcd.com/comics/x.png)

Input is a pdf file and is converted to brainfuck (by a python script)

## Random ideas / features

- Cross platform: pdf files can be created on all platforms. Use anything as an IDE: Word, Latex, ... The possibilities are truly endless.

## Language specification

An xfuck source files are PDF files. The first eight letters of the pdf should have eight different fonts, each corresponding to [one letter](https://en.wikipedia.org/wiki/Brainfuck#Commands) of brainfuck.

The only allowed text characters in the PDF are the letter `'X'` or whitespace. Other characters are a syntax error. An exception is the string `X Æ A-12`, which is the same as  a single `X`. Other content, such as images or embedded SWF files are ignored.
