# xfuck

`xfuck` (pronounced 'crossfuck') is an esoteric programming language based on fonts. It is revolutionary, portable and minimal - an interpreter can be written in less than 300 lines of Python.
The source code of an xfuck program is the fonts embedded in a PDF, interpreted as brainfuck commands. This provides incredible flexibility, and a rich ecosystem of literally billions of already existing valid programs.
In addition, PDF output is so ubiquitous that xfuck enables the user to write their program in a wide range of development environments, which were previously unsuitable for coding. These include (but are no limited to) Microsof Word, Excel, LaTeX, HTML files (via printing to PDF), or even by hand on a plain piece of paper and the help of an OCR program.

For example, a program that prints 'hello world' looks like this:

![hello-x](doc/screenshot-hello-x.png)

You can see the full source code for this example in [`examples/hello-x.pdf`](examples/hello-x.pdf).

xfuck was inspired by [this xkcd](https://xkcd.com/2309/):

![https://imgs.xkcd.com/comics/x.png](https://imgs.xkcd.com/comics/x.png)


## Random ideas / features

- Cross platform: pdf files can be created on all platforms. Use anything as an IDE: Word, Latex, ... The possibilities are truly endless.

## TODO:

- example fies in latex, word, libreoffice, html (export to pdf using e.g. browser)

## Language specification

xfuck source files are PDF files. The first eight characters of the pdf should have eight different fonts, each corresponding to [one letter](https://en.wikipedia.org/wiki/Brainfuck#Commands) of brainfuck.

The only allowed text characters in the PDF are the character `'X'` or whitespace. Other characters are a syntax error. An exception is the string `X Æ A-12`, which is the same as  a single `X`. Other content, such as images or embedded SWF files are ignored.

## Usage instructions

Install dependencies (python 3):
```
pip install -r requirements.txt
```

Compile (in the repository root folder):
```
./xfk inputfile.pdf [--compile]
```
By default, this command executes the code in `inputfile.pdf`. If the `--compile` flag is given, it instead outputs the contents of the input file as brainfuck source code to stdout.
