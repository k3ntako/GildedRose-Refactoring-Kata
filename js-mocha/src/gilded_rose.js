class Item {
  constructor(name, sellIn, quality) {
    this.name = name;
    this.sellIn = sellIn;
    this.quality = quality;
  }
}

const validateQuality = (quality) => {
  if (quality > 50) {
    return 50;
  } else if (quality < 0) {
    return 0;
  }
  return quality;
};

const ITEM_SPECS = {
  "Sulfuras, Hand of Ragnaros": {
    updateQuality: (item) => {
      return [item.sellIn, 80];
    },
  },

  "Aged Brie": {
    updateQuality: (item) => {
      let { quality, sellIn } = item;
      quality++;
      sellIn--;

      if (sellIn < 0) {
        quality++;
      }

      quality = validateQuality(quality);

      return [sellIn, quality];
    },
  },

  "Backstage passes to a TAFKAL80ETC concert": {
    updateQuality: (item) => {
      let { quality, sellIn } = item;
      quality++;

      if (sellIn < 11) {
        quality = quality + 1;
      }
      if (sellIn < 6) {
        quality = quality + 1;
      }

      sellIn--;

      if (sellIn < 0) {
        quality = 0;
      }

      quality = validateQuality(quality);

      return [sellIn, quality];
    },
  },

  generic_spec: {
    updateQuality: (item) => {
      let { quality, sellIn } = item;
      quality--;
      sellIn--;

      if (sellIn < 0) {
        quality--;
      }

      quality = validateQuality(quality);

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

      let spec = ITEM_SPECS[item.name];

      if (!spec) {
        spec = ITEM_SPECS.generic_spec;
      }

      const [sellIn, quality] = spec.updateQuality(item);

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
