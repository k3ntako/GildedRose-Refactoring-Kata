# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_items_for_next_day(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            elif item.name == "Aged Brie":
                self.update_age_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_backstage_passes(item)
            else:
                self.update_generic(item)

    def update_age_brie(self, item):
        item.quality = item.quality + 1

        item.sell_in = item.sell_in - 1

        if item.sell_in < 0:
            item.quality = item.quality + 1

        if item.quality > 50:
            item.quality = 50

    def update_backstage_passes(self, item):
        item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1

        if item.sell_in < 10:
            item.quality = item.quality + 1
        if item.sell_in < 5:
            item.quality = item.quality + 1
        if item.quality > 50:
            item.quality = 50        
        if item.sell_in < 0:
            item.quality = 0

    def update_generic(self, item):
        item.quality = item.quality - 1
        item.sell_in = item.sell_in - 1

        if item.sell_in < 0:
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
