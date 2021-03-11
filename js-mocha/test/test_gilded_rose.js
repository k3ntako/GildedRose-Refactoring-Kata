var { expect } = require("chai");
var { Shop, Item } = require("../src/gilded_rose.js");
describe("Gilded Rose", function () {
  describe("updateQuality", function () {
    it("should return foo", function () {
      const gildedRose = new Shop([new Item("foo", 0, 0)]);
      const items = gildedRose.updateQuality();
      expect(items[0].name).to.equal("foo");
    });

    it("should reduce sell in date by 1", function () {
      const gildedRose = new Shop([new Item("foo", 2, 0)]);
      const items = gildedRose.updateQuality();
      expect(items[0].sellIn).to.equal(1);
    });

    it("should reduce quality by 1", function () {
      const gildedRose = new Shop([new Item("foo", 2, 3)]);
      const items = gildedRose.updateQuality();
      expect(items[0].quality).to.equal(2);
    });

    it("should reduce quality by 2 if sell-in date is 0", function () {
      const gildedRose = new Shop([new Item("foo", 0, 10)]);
      const items = gildedRose.updateQuality();
      expect(items[0].quality).to.equal(8);
    });

    it("should not set quality below 0", function () {
      const gildedRose = new Shop([new Item("foo", 3, 0)]);
      const items = gildedRose.updateQuality();
      expect(items[0].quality).to.equal(0);
    });
  });
});
