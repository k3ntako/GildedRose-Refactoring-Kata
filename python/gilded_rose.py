# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_items_for_next_day(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                item.update_for_next_day()
                continue
            
            item.update_for_next_day()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemType:
    def __init__(self, name, sell_in, quality):
        self.item = Item(name=name, sell_in=sell_in, quality=quality)

    def subtract_sell_in(self):
        self.item.sell_in = self.item.sell_in - 1

    def set_quality_to_50_or_less(self):
        if self.item.quality > 50:
            self.item.quality = 50
        
    def get_name(self): 
        return self.item.name 
       
    def set_name(self, name): 
        self.item.name = name 
  
    def del_name(self): 
        del self.item.name

    def get_sell_in(self): 
        return self.item.sell_in 
       
    def set_sell_in(self, sell_in): 
        self.item.sell_in = sell_in 
  
    def del_sell_in(self): 
        del self.item.sell_in 

    def get_quality(self): 
        return self.item.quality 
       
    def set_quality(self, quality): 
        self.item.quality = quality 
  
    def del_quality(self): 
        del self.item.quality 

    name = property(get_name, set_name, del_name)
    sell_in = property(get_sell_in, set_sell_in, del_sell_in)
    quality = property(get_quality, set_quality, del_quality)

class AgedBrie(ItemType):
    def update_for_next_day(self):
        self.subtract_sell_in()
        self.item.quality = self.item.quality + 1

        if self.item.sell_in < 0:
            self.item.quality = self.item.quality + 1

        self.set_quality_to_50_or_less()

class BackstagePasses(ItemType):
    def update_for_next_day(self):
        self.subtract_sell_in()
        self.item.quality = self.item.quality + 1

        if self.item.sell_in < 10:
            self.item.quality = self.item.quality + 1
        if self.item.sell_in < 5:
            self.item.quality = self.item.quality + 1       
        if self.item.sell_in < 0:
            self.item.quality = 0

        self.set_quality_to_50_or_less()

class Sulfuras(ItemType):
    def update_for_next_day(self):
       pass

class GenericType(ItemType):
    def update_for_next_day(self):
        self.subtract_sell_in()
        self.item.quality = self.item.quality - 1

        if self.item.sell_in < 0:
            self.item.quality = self.item.quality - 1

        if self.item.quality < 0:
            self.item.quality = 0

        self.set_quality_to_50_or_less()
    
