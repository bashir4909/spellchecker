# Azerbaijani Spellchecker
Firefox SpellChecker for Azerbaijani

Hunspell dictionary for Azerbaijani language.

Wordlist is provided by [azerdict.com](https://azerdict.com)

# Notes
Word marks:

* N - noun (isim) [aı]
* O - noun (incə isim) [eəiöü]
* V - verb (feil)
* E - verb (incə feil)
* A - adjective (sifət)
* J - adjective (incə sifət)
* P - pronoun (əvəzlik)
* R - pronoun (incə əvəzlik)
* U - numeral (say)
* M - numeral (incə say)
* D - adverb (zərf)
* B - adverb (incə zərf)
* F - conjunction (bağlayıcı)
* G - conjunction (incə bağlayıcı)

* 1 - qalın [a,ı] - dı
* 2 - qalın [e,ə,i] - di
* 3 - qalın [o,u] - du
* 4 - qalın [ö,ü] - dü

# For testing

To test dictionaries I plan to create list of correct words and see if they can be recognised. To do so,

* Install hunspell. On Linux relevant command is `sudo apt install hunspell hunspell-tools`
* `/test` directory contains txt files with correct word on each line
* *cd* into `/dictionaries` folder. Run `hunspell -a -d ../test/isim.txt`, it will print * for words it identifies as correct and # with suggestions otherwise.

You can also test words interactively by
`
cd dictionaries
hunspell -a -d az
`

# License
Project is licensed under MPLv2 License, copy of the license can be obtained within project source code (LICENSE file).

Project is created and maintained by Mozilla Azerbaijan.
