# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_items_for_next_day(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            if item.name == "Aged Brie":
                item.quality = item.quality + 1
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.quality = item.quality + 1
                if item.sell_in < 11:
                    item.quality = item.quality + 1
                if item.sell_in < 6:
                    item.quality = item.quality + 1
            else:
                item.quality = item.quality - 1

            item.sell_in = item.sell_in - 1

            if item.sell_in < 0:
                if item.name == "Aged Brie":
                    item.quality = item.quality + 1
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = 0
                else:
                    item.quality = item.quality - 1

            if item.quality < 0:
                item.quality = 0

            if item.quality > 50:
                item.quality = 50


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
