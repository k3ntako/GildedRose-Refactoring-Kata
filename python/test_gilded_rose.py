# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        """Test Foo"""
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items_for_next_day()
        self.assertEqual("foo", items[0].name)

    def test_sell_in_decrease(self):
        """Test that sell-in decreases by 1"""
        items = [Item("foo", 10, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items_for_next_day()
        self.assertEqual(9, items[0].sell_in)

    def test_quality_decrease(self):
        """Test that quality decreases by 1"""
        items = [Item("foo", 10, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items_for_next_day()
        self.assertEqual(10, items[0].quality)

    def test_expired_quality_decrease(self):
        """Test that quality decreases by twice as fast after sell-in date"""
        items = [Item("foo", 0, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items_for_next_day()
        self.assertEqual(9, items[0].quality)

    def test_quality_never_below_zero(self):
        """Test that quality never decreases below zero"""
        items = [Item("foo", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items_for_next_day()
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_increases_in_quality(self):
        """Test that Aged Brie increases in quality"""
        items = [Item("Aged Brie", 10, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items_for_next_day()
        self.assertEqual(12, items[0].quality)

    def test_quality_does_not_increase_above_fifty(self):
        """Test quality does not increase above 50"""
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items_for_next_day()
        self.assertEqual(50, items[0].quality)

    def test_aged_brie_sell_in_decreases(self):
        """Test Aged Brie sell-in decreases by 1"""
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items_for_next_day()
        self.assertEqual(9, items[0].sell_in)

    def test_aged_brie_quality_after_sell_in(self):
        """Test Aged Brie quality increases by 2 after sell-in date"""
        items = [Item("Aged Brie", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items_for_next_day()
        self.assertEqual(12, items[0].quality)

    def test_sulfuras_sell_in_does_not_decrease(self):
        """Test that sulfuras sell-in does not decrease"""
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items_for_next_day()
        self.assertEqual(10, items[0].sell_in)

    def test_sulfuras_quality_is_always_eighty(self):
        """Test that sulfuras quality is always 80"""
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items_for_next_day()
        self.assertEqual(80, items[0].quality)

    def test_backstage_pass_quality_increases(self):
        """Test that backstage pass quality increases by 1"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items_for_next_day()
        self.assertEqual(12, items[0].quality)

    def test_backstage_pass_quality_increases_ten_days(self):
        """Test that backstage pass quality increases by 2 when 10 days away"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items_for_next_day()
        self.assertEqual(13, items[0].quality)

    def test_backstage_pass_quality_increases_six_days(self):
        """Test that backstage pass quality increases by 2 when 6 days away"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items_for_next_day()
        self.assertEqual(13, items[0].quality)

    def test_backstage_pass_quality_increases_five_days(self):
        """Test that backstage pass quality increases by 3 when 5 days away"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items_for_next_day()
        self.assertEqual(14, items[0].quality)

    def test_backstage_pass_quality_increases_one_day(self):
        """Test that backstage pass quality increases by 3 when 1 day away"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items_for_next_day()
        self.assertEqual(14, items[0].quality)

    def test_backstage_pass_quality_is_zero_after_event(self):
        """Test that backstage pass quality is zero after the event"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items_for_next_day()
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
