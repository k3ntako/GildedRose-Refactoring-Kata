class Item {
  constructor(name, sellIn, quality) {
    this.name = name;
    this.sellIn = sellIn;
    this.quality = quality;
  }
}

const ITEM_SPECS = {
  "Sulfuras, Hand of Ragnaros": {
    updateQuality: (sellIn, quality) => {
      return [sellIn, quality];
    },
  },

  "Aged Brie": {
    updateQuality: (sellIn, quality) => {
      sellIn--;

      quality++;

      sellIn--;

      if (sellIn < 0) {
        quality++;
      }

      if (quality > 50) {
        quality = 50;
      }

      return [sellIn, quality];
    },
  },
};

class Shop {
  constructor(items = []) {
    this.items = items;
  }
  updateQuality() {
    for (var i = 0; i < this.items.length; i++) {
      const item = this.items[i];

      const spec = ITEM_SPECS[item.name];
      if (spec) {
        const { sellIn, quality } = item;
        const [updatedSellIn, updatedQuality] = spec.updateQuality(
          sellIn,
          quality
        );

        item.sellIn = updatedSellIn;
        item.quality = updatedQuality;
        continue;
      }

      if (item.name === "Backstage passes to a TAFKAL80ETC concert") {
        item.quality = item.quality + 1;

        if (item.sellIn < 11) {
          item.quality = item.quality + 1;
        }
        if (item.sellIn < 6) {
          item.quality = item.quality + 1;
        }
      } else {
        item.quality = item.quality - 1;
      }

      item.sellIn = item.sellIn - 1;

      if (item.sellIn < 0) {
        if (item.name === "Backstage passes to a TAFKAL80ETC concert") {
          item.quality = 0;
        } else {
          item.quality = item.quality - 1;
        }
      }

      if (item.quality > 50) {
        item.quality = 50;
      } else if (item.quality < 0) {
        item.quality = 0;
      }
    }

    return this.items;
  }
}
module.exports = {
  Item,
  Shop,
};
