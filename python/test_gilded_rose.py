# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        """Test Foo"""
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_sell_in_decrease(self):
        """Test that sell-in decreases by 1"""
        items = [Item("foo", 10, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)

    def test_quality_decrease(self):
        """Test that quality decreases by 1"""
        items = [Item("foo", 10, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].quality)

    def test_expired_quality_decrease(self):
        """Test that quality decreases by twice as fast after sell-in date"""
        items = [Item("foo", 0, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)

    def test_quality_never_below_zero(self):
        """Test that quality never decreases below zero"""
        items = [Item("foo", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_increases_in_quality(self):
        """Test that Aged Brie increases in quality"""
        items = [Item("Aged Brie", 10, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)

    def test_quality_does_not_increase_above_fifty(self):
        """Test quality does not increase above 50"""
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_sell_in_does_not_decrease(self):
        """Test that sulfuras sell-in does not decrease"""
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)

    def test_sulfuras_quality_is_always_eighty(self):
        """Test that sulfuras quality is always 80"""
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)


if __name__ == '__main__':
    unittest.main()
