Object subclass: #GildedRose instanceVariableNames: '' classVariableNames: ''
poolDictionaries: '' category: 'GildedRose'! !GildedRose commentStamp:
'AndreasLeidig 4/21/2012 15:38' prior: 0! This Kata was originally created by
Terry Hughes (http://twitter.com/#!!/TerryHughes). It is already on GitHub as
"GildedRose", a sample project for C#. I could have forked it again, but I
thought other language users might not want to download a whole C# project
environment. In this repository are starting code samples for Java, Python,
Ruby, C# and C++. See also
http://iamnotmyself.com/2011/02/13/refactor-this-the-gilded-rose-kata/
==================== How to use this Kata ==================== The simplest way
is to just clone the code and start hacking away improving the design. You'll
want to look at the "Gilded Rose Background Reading" (below) which explains what
the code is for. I strongly advise you that you'll also need some tests if you
want to make sure you don't break the code while you refactor. You could write
some unit tests yourself, using the Kata Background Reading (below) to identify
suitable test cases. I've provided a failing unit test in a popular test
framework as a starting point for most languages. Alternatively, use the
"Text-Based" tests provided in this repository. (Read more about that in the
next section) Whichever testing approach you choose, the idea of the exercise is
to do some deliberate practice, and improve your Refactoring skills. The idea is
not to re-write the code from scratch, but rather to practice taking small
steps, running the tests often, and incrementally improving the design.
================== Text-Based Testing ================== This is a testing
approach which is very useful when refactoring legacy code. The basic idea is to
create tests that use the text which the code produces. Before you change the
code, you run it, and save the output as a "Golden Copy". Then after you change
the code, you run it again, and compare the output against the Golden Copy. Any
differences, and the test fails. It's basically the same idea as
"assertEquals(expected, actual)" in a unit test, except the text you are
comparing is typically much longer, and the "expected" value is saved from
actual output, rather than being defined in advance. Typically a piece of legacy
code may not produce suitable textual output from the start, so you may need to
modify it before you can write your first text-based test. That could involve
inserting log statements into the code, or just writing a "main" method that
executes the code and prints out what the result is afterwards. It's this latter
approach we are using here to test GildedRose. The Text-Based tests in this
repository are designed to be used with the tool "TextTest"
(http://texttest.org). This tool helps you to organize and run text-based tests.
There is more information in the README file in the "texttests" subdirectory.
=================================== Gilded Rose Kata Background Reading
=================================== Hi and welcome to team Gilded Rose. As you
know, we are a small inn with a prime location in a prominent city ran by a
friendly innkeeper named Allison. We also buy and sell only the finest goods.
Unfortunately, our goods are constantly degrading in quality as they approach
their sell by date. We have a system in place that updates our inventory for us.
It was developed by a no-nonsense type named Leeroy, who has moved on to new
adventures. Your task is to add the new feature to our system so that we can
begin selling a new category of items. First an introduction to our system: -
All items have a SellIn value which denotes the number of days we have to sell
the item - All items have a Quality value which denotes how valuable the item is
- At the end of each day our system lowers both values for every item Pretty
simple, right? Well this is where it gets interesting: - Once the sell by date
has passed, Quality degrades twice as fast - The Quality of an item is never
negative - "Aged Brie" actually increases in Quality the older it gets - The
Quality of an item is never more than 50 - "Sulfuras", being a legendary item,
never has to be sold or decreases in Quality - "Backstage passes", like aged
brie, increases in Quality as it's SellIn value approaches; Quality increases by
2 when there are 10 days or less and by 3 when there are 5 days or less but
Quality drops to 0 after the concert We have recently signed a supplier of
conjured items. This requires an update to our system: - "Conjured" items
degrade in Quality twice as fast as normal items Feel free to make any changes
to the UpdateQuality method and add any new code as long as everything still
works correctly. However, do not alter the Item class or Items property as those
belong to the goblin in the corner who will insta-rage and one-shot you as he
doesn't believe in shared code ownership (you can make the UpdateQuality method
and Items property static if you like, we'll cover for you). Just for
clarification, an item can never have its Quality increase above 50, however
"Sulfuras" is a legendary item and as such its Quality is 80 and it never
alters.! !GildedRose methodsFor: 'API' stamp: 'AndreasLeidig 4/21/2012 17:02'!
updateQualityFor: items items do: [:item | (item name ~= 'Aged Brie' and: [item
name ~= 'Backstage passes to a TAFKAL80ETC concert']) ifTrue: [item quality > 0
ifTrue: [item name ~= 'Sulfuras, Hand of Ragnaros' ifTrue: [item quality: item
quality - 1]]] ifFalse: [item quality < 50 ifTrue: [item quality: item quality +
1. item name = 'Backstage passes to a TAFKAL80ETC concert' ifTrue: [item sellIn
< 11 ifTrue: [item quality < 50 ifTrue: [item quality: item quality + 1]]. item
sellIn < 6 ifTrue: [item quality < 50 ifTrue: [item quality: item quality +
1]]]]]. item name ~= 'Sulfuras, Hand of Ragnaros' ifTrue: [item sellIn: item
sellIn - 1]. item sellIn < 0 ifTrue: [item name ~= 'Aged Brie' ifTrue: [item
name ~= 'Backstage passes to a TAFKAL80ETC concert' ifTrue: [item quality > 0
ifTrue: [item name ~= 'Sulfuras, Hand of Ragnaros' ifTrue: [item quality: item
quality - 1]]] ifFalse: [item quality: item quality - item quality]] ifFalse:
[item quality < 50 ifTrue: [item quality: item quality + 1]]]]! ! "-- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- "! GildedRose class
instanceVariableNames: ''! !GildedRose class methodsFor: 'run Example' stamp:
'AndreasLeidig 4/21/2012 20:26'! runExamples "GildedRose runExamples" | items
gildedRose | items := OrderedCollection new add: (Item new name: '+5 Dexterity
Vest'; sellIn: 10; quality: 20; yourself); add: (Item new name: 'Aged Brie';
sellIn: 2; quality: 0; yourself); add: (Item new name: 'Elixir of the Mongoose';
sellIn: 5; quality: 7; yourself); add: (Item new name: 'Sulfuras, Hand of
Ragnaros'; sellIn: 0; quality: 80; yourself); add: (Item new name: 'Sulfuras,
Hand of Ragnaros'; sellIn: -1; quality: 80; yourself); add: (Item new name:
'Backstage passes to a TAFKAL80ETC concert'; sellIn: 15; quality: 20; yourself);
add: (Item new name: 'Backstage passes to a TAFKAL80ETC concert'; sellIn: 10;
quality: 49; yourself); add: (Item new name: 'Backstage passes to a TAFKAL80ETC
concert'; sellIn: 5; quality: 49; yourself); add: (Item new name: 'Conjured Mana
Cake'; sellIn: 3; quality: 6; yourself); "this conjured item does not work
properly yet" yourself. gildedRose := GildedRose new. Transcript show:
'OMGHAI!!'; cr. 0 to: 30 do: [:idx | Transcript show: '-------- day ' , idx
printString , ' --------'; cr; show: 'name, sellIn, quality'; cr. items do:
[:item | Transcript show: item name , ', ' , item sellIn printString , ', ' ,
item quality printString; cr]. Transcript cr. gildedRose updateQualityFor:
items]. Transcript cr! ! Object subclass: #Item instanceVariableNames: 'name
sellIn quality' classVariableNames: '' poolDictionaries: '' category:
'GildedRose'! !Item methodsFor: 'accessing' stamp: 'AndreasLeidig 4/21/2012
15:40'! name ^name! ! !Item methodsFor: 'accessing' stamp: 'AndreasLeidig
4/21/2012 15:41'! name: aString name := aString! ! !Item methodsFor: 'accessing'
stamp: 'AndreasLeidig 4/21/2012 15:41'! quality ^quality! ! !Item methodsFor:
'accessing' stamp: 'AndreasLeidig 4/21/2012 15:42'! quality: aNumber quality :=
aNumber! ! !Item methodsFor: 'accessing' stamp: 'AndreasLeidig 4/21/2012 15:41'!
sellIn ^sellIn! ! !Item methodsFor: 'accessing' stamp: 'AndreasLeidig 4/21/2012
15:42'! sellIn: aNumber sellIn := aNumber ! !
