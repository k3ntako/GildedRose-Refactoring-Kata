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

  "Backstage passes to a TAFKAL80ETC concert": {
    updateQuality: (sellIn, quality) => {
      quality = quality + 1;

      if (sellIn < 11) {
        quality = quality + 1;
      }
      if (sellIn < 6) {
        quality = quality + 1;
      }

      sellIn--;

      if (quality > 50) {
        quality = 50;
      } else if (sellIn < 0) {
        quality = 0;
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
      let { sellIn, quality } = item;

      if (spec) {
        [sellIn, quality] = spec.updateQuality(sellIn, quality);
      } else {
        quality--;
        sellIn--;

        if (sellIn < 0) {
          quality--;
        }

        if (quality > 50) {
          quality = 50;
        } else if (quality < 0) {
          quality = 0;
        }
      }

      item.sellIn = sellIn;
      item.quality = quality;
    }

    return this.items;
  }
}
module.exports = {
  Item,
  Shop,
};
