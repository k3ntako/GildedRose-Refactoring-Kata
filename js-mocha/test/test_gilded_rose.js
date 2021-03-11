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

    it("should increase quality of Aged Brie", function () {
      const gildedRose = new Shop([new Item("Aged Brie", 10, 15)]);
      const items = gildedRose.updateQuality();
      expect(items[0].quality).to.equal(16);
    });
  });

  it("should not increase quality over 50", function () {
    const gildedRose = new Shop([new Item("Aged Brie", 10, 50)]);
    const items = gildedRose.updateQuality();
    expect(items[0].quality).to.equal(50);
  });

  it("should change sell-in date of Sulfuras, Hand of Ragnaros", function () {
    const gildedRose = new Shop([
      new Item("Sulfuras, Hand of Ragnaros", 10, 20),
    ]);
    const items = gildedRose.updateQuality();
    expect(items[0].sellIn).to.equal(10);
  });

  it("should change quality of Sulfuras, Hand of Ragnaros", function () {
    const gildedRose = new Shop([
      new Item("Sulfuras, Hand of Ragnaros", 10, 20),
    ]);
    const items = gildedRose.updateQuality();
    expect(items[0].quality).to.equal(20);
  });

  it("should increase backstage pass quality by 1 if sell-in is greater than 10", function () {
    const gildedRose = new Shop([
      new Item("Backstage passes to a TAFKAL80ETC concert", 25, 20),
    ]);
    const items = gildedRose.updateQuality();
    expect(items[0].quality).to.equal(21);
  });

  it("should increase backstage pass quality by 2 if sell-in is 10 or less", function () {
    const gildedRose = new Shop([
      new Item("Backstage passes to a TAFKAL80ETC concert", 10, 20),
    ]);
    const items = gildedRose.updateQuality();
    expect(items[0].quality).to.equal(22);
  });

  it("should increase backstage pass quality by 3 if sell-in is 5 or less", function () {
    const gildedRose = new Shop([
      new Item("Backstage passes to a TAFKAL80ETC concert", 5, 20),
    ]);
    const items = gildedRose.updateQuality();
    expect(items[0].quality).to.equal(23);
  });

  it("should set backstage pass quality to 0 after the concert", function () {
    const gildedRose = new Shop([
      new Item("Backstage passes to a TAFKAL80ETC concert", 0, 20),
    ]);
    const items = gildedRose.updateQuality();
    expect(items[0].quality).to.equal(0);
  });
});
