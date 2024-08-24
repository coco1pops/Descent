
# Load up items into item_lookup

init python:

    import datetime

    #   Initialize the date
    gClock = datetime.datetime(2020,6,1)
    gDow = gClock.strftime('%A')
    gDay_cnt = 1

    # Cash amounts
    gPizzaCash = 100 # Weekly wage
    gGameCost = 5 # Amount player spends daily on games
    gGameMinCash = 40 # Amount player needs to game
    gPartyCost = 20 # Cost for a night out. Doubles if player parties at the weekend
    gPartyMinCash = 120 # Amount player needs to party

    gPlayerCosts = 50 # Weekly living costs
    gKasRent = 400

    # Timers
    gKasTrigger = 20 # Number of days between Kasumi events
    gMakTrigger = 30 # Number of days between Maki events

    # Indira values
    gIndAvailable = 5 # Trigger to enable Indira's councilling
    gIndEvents = []
    gIndEvents = [False for i in range(10)]

    # Chihura values
    gChiStudy = None
    gChiMax = 0
    gChiDict = {}
    gChiFlag = True

    class Kit(object):
        def __init__(self, earrings, necklace, left_ring, right_ring):
            self.earrings = None
            self.necklace = None
            self.left_ring = None
            self.right_ring = None

    class Player(object):
        def __init__(self, character, description, top, trousers, underwear, shoes, hair, bodyhair, kit = Kit(None, None, None, None),
        items = [], cash = 200):
            self.c = character
            self.description = description
            self.top = top
            self.trousers = trousers
            self.underwear = underwear
            self.shoes = shoes
            self.hair = hair
            self.bodyhair = bodyhair
            self.kit = kit
            self.loathing = 0
            self.libido = 0
            self.knowledge = 0
            self.cash = cash
            self.items = items
            self.attributes = []
            self.books = 0
            self.clothes = 0
            self.dress = 0
            self.toys = 0
            self.oname = ""
            self.hair_cnt = 0
            self.smooth = 3
            self.fem = False

        def wear(self, item, finger):
            if item.type == "earrings":
                if self.kit.earrings != None:
                    self.update_stats(self.kit.earrings, -1)
                    self.items.append(self.kit.earrings)
                self.kit.earrings = item
            elif item.type == "necklace":
                if self.kit.necklace != None:
                    self.update_stats(self.kit.necklace, -1)
                    self.items.append(self.kit.necklace)
                self.kit.necklace = item
            elif item.type == "ring" and finger == "left":
                if self.kit.left_ring != None:
                    self.update_stats(self.kit.left_ring, -1)
                    self.items.append(self.kit.left_ring)
                self.kit.left_ring = item
            else:
                if self.kit.right_ring != None:
                    self.update_stats(self.kit.right_ring, -1)
                    self.items.append(self.kit.right_ring)
                self.kit.right_ring = item

            self.update_stats(item, 1)

        def takeoff(self, jewel):
            if jewel == "earrings":
                self.update_stats(self.kit.earrings, -1)
                self.items.append(self.kit.earrings)
                self.kit.earrings = None
            elif jewel == "necklace":
                self.update_stats(self.kit.necklace, -1)
                self.items.append(self.kit.necklace)
                self.kit.necklace = None
            elif jewel == "left ring":
                self.update_stats(self.kit.left_ring, -1)
                self.items.append(self.kit.left_ring)
                self.kit.left_ring = None
            else:
                self.update_stats(self.kit.right_ring, -1)
                self.items.append(self.kit.right_ring)
                self.kit.right_ring = None


        def dec_value(self, val, dec):
            val -= dec
            if val < 0:
                val = 0
            return(val)

        def update_stats(self, foc, chg):
            if foc == "Study": # Player works hard but needs a distraction
                self.knowledge += chg
                self.libido += 1
            elif foc == "Chill": # Player feels bad about wasting time
                self.loathing += 1
            elif foc == "Game": # Player feels bad about wasting time but is distracted
                self.loathing += 1
                self.libido = self.dec_value(self.libido, 1)
                self.cash -= (gGameCost * chg)
            elif foc == "Exercise": # Player feels good about himself but has more energy
                self.loathing = self.dec_value(self.loathing, chg)
                self.libido += chg
            else: #foc == "Party", costly way to reduce lib and loses knowledge too
                self.knowledge = self.dec_value(self.knowledge, chg)
                self.libido = self.dec_value(self.libido, chg)
                self.cash -= (gPartyCost * chg)

        def reject(self, val):
            self.libido += val

        def accept(self, val):
            self.libido = self.dec_value(self.libido, val)
            self.loathing += val

        def filterbytype(self, typ):
            filtered_objs = [obj for obj in self.items if obj.type == typ]
            return filtered_objs

        def get_obj(self, typ, cnt):
            ix = renpy.random.randint(1, cnt)
            objs = self.filterbytype(typ)
            return objs[ix-1]

        def add_item(self, item):
            self.items.append(item)
            item.owned = True
            if item.type == "Dress":
                self.dress += 1
            elif item.type == "Clothes":
                self.clothes += 1
            elif item.type == "Toy":
                self.toys += 1
            else: # item type = Book
                self.books += 1

        def loath_desc(self):
            cnt = 0
            while self.loathing > loath_lookup[cnt]["ix"] and cnt < len(loath_lookup) - 1:
                cnt += 1

            if self.loathing < loath_lookup[cnt]["ix"]:
                cnt -= 1

            return (loath_lookup[cnt]["val"])

        def lib_desc(self):
            cnt = 0
            while self.libido > lib_lookup[cnt]["ix"] and cnt < len(lib_lookup) - 1:
                cnt += 1

            if self.libido < lib_lookup[cnt]["ix"]:
                cnt -= 1

            return (lib_lookup[cnt]["val"])


    class NPC(object):
        def __init__(self, character, description, body, attitude, dress, id, gap):
            self.c = character
            self.description = description
            self.body = body
            self.attitude = attitude
            self.dress = dress
            self.level = -1
            self.id = id
            self.gap = gap
            self.countdown = -1
            self.gapcnt = -1
            self.attributes = []

    class Item(object):
        def __init__(self, name, description, usage, type, libido_mod, \
        loathing_mod, chiitem):
            self.name = name
            self.description = description
            self.usage = usage
            self.type = type
            self.libido_mod = libido_mod
            self.loathing_mod = loathing_mod
            self.chiitem = chiitem
            self.owned = False

    class ChiItem(Item):
        def __init__(self, name, description, usage, type, libido_mod, \
        loathing_mod, desire, level, knowledge):
            super().__init__(name, description, usage, type, libido_mod, loathing_mod, True)
            self.desire = desire
            self.level = level
            self.knowledge = knowledge


    import csv

    fn = f"{config.basedir}\\game\\csv\\Game Assets - Objects.csv"
    with open(fn, "r") as file:
        reader = csv.reader(file)
        csv_data = [row for row in reader]

        item_lookup = []
        for row in csv_data[1:]:
            row[1] = row[1].replace("|", ",")
            row[2] = row[2].replace("|", ",")
            if row[7] == "FALSE": # Normal Item
                item_lookup.append(Item(row[0], row[1], row[2], row[3], int(row[4]), int(row[5]), False))
            else: # Chi Item
                item_lookup.append(ChiItem(row[0], row[1], row[2], row[3], int(row[4]), int(row[5]), row[8], int(row[9]), int(row[10])))
                gChiMax += 1
                if row[8] not in gChiDict:
                    gChiDict[row[8]] = {"count": 1, "max" : 1}
                else:
                    gChiDict[row[8]]["max"] += 1


    fn = f"{config.basedir}\\game\\csv\\Game Assets - Lib.csv"
    with open(fn, "r") as file:
        reader = csv.reader(file)
        csv_data = [row for row in reader]

        lib_lookup = []
        for row in csv_data[1:]:
            lib_lookup.append({"ix": int(row[0]), "val": row[1]})

    fn = f"{config.basedir}\\game\\csv\\Game Assets - Loath.csv"
    with open(fn, "r") as file:
        reader = csv.reader(file)
        csv_data = [row for row in reader]

        loath_lookup = []
        for row in csv_data[1:]:
            loath_lookup.append({"ix": int(row[0]), "val": row[1]})

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default i = Player(Character("p"), "fresh-faced young student with blue eyes", \
    "teeshirt", "jeans", "boxer shorts", "trainers", "neatly cut, quite short and light-brown", "soft, sparse")

default k = NPC(Character("Kasumi"), "pretty oriental girl, with long, straight black hair, a cute nose and big, black eyes", \
    "slender with gentle curves and nicely shaped legs", "Shy and Sweet", \
    "a denim dress that hugs her slim figure", "k", 4)
$ k.attributes = ["Pain Slut", "Femboy"]

default m = NPC(Character("Maki"), "a striking girl with a round face, piercing blue eyes and long, straight, silky ginger hair", \
    "very round, with big breasts, a huge bum, thick thighs and a roll of fat around her middle ", \
    "Sensual and Naughty", \
    "a long, blue dress that is stretched across her ample folds", "m", 7)
$ m.attributes = ["Chubby Chaser", "Femboy", "Cock Sucker", "Anal Whore"]

default y = NPC(Character("Yuki"), "a slobby, 38 year old woman with a pretty, chubby face, brown eyes and long, messy, greasy dark-brown hair", \
    "very large, saggy breasts, a huge bum, thick thighs and big, soft buttocks", \
    "Dominant and Filthy", \
    "a tight teeshirt with food stains down the front and sweaty armpits as well as too tight jeans that don't contain her flabby stomach and fat arse", "y", 7)
$ y.attributes = ["Chubby Chaser", "Sweat Rag", "Toilet Slave", "Hairy Worshiper", "Ass Licker"]

default c = NPC(Character("Chihura"), "a severe face with long, blond, wavy hair and glasses", \
    "big, firm breasts, a large bum and strong thighs", \
    "Overbearing and Demanding", \
    "a smart white blouse, black pencil skirt, fine tights and high heels", "c", 3)
$ c.attributes = ["Hairy Worshiper", "Ass Licker"]

default d = NPC(Character("Indira"), "a mature Indian woman with a round face, big brown eyes and long, curly black hair", \
    "overweight with large, soft breasts, a thick waist and a very large bottom and chubby thighs", \
    "Caring, Loving and Gentle", \
    "a dark blouse unbuttoned at the top to show her cleavage, gold necklace, loose, flowery trousers and low heels", "d", 10)
$ d.attributes = ["Chubby Chaser","Femboy", "Hairy Worshiper", "Ass Licker", "Anal Whore"]

default s = NPC(Character("Satomi"), "a 30 year old woman with blue eyes and long, wavy blond hair in a pony-tail", \
    "tall, athletic and strong with big breasts, a thick waist, a firm bottom and strong legs", \
    "Rough and Overbearing", \
    "sports gear, a tight, sweaty grey running top, shorts, white socks and training shoes", "s", 7)
$ s.attributes = ["Sweat Rag", "Pain Slut", "Ass Licker"]

default n = Character("", kind=nvl, color="#030303", what_prefix="{size=-2}", what_suffix="{/size}")


label after_load:
    python:
        for item in i.items:
            gChiDict[item.desire]["count"] += 1

    return
