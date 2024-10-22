import pprint as pp
import str_ex2 as Fa


snip = input("Donnez votre chaine: ").lower()
words = set(snip.split(" "))

dicto = {a:Fa.findAll(snip,a) for a in words}