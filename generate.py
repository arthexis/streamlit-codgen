import json
from json import dumps
import yaml
import random
import typer
from enum import Enum
from faker import Faker


def flat_values(source: dict) -> list:
    return [item for sublist in source.values() for item in sublist]


ATTRIBUTE_CATEGORIES = {
    "Mental": ("Intelligence", "Wits", "Resolve"),
    "Physical": ("Strength", "Dexterity", "Stamina"),
    "Social": ("Presence", "Manipulation", "Composure"),
}

ATTRIBUTES = flat_values(ATTRIBUTE_CATEGORIES)

CATEGORIES = list(ATTRIBUTE_CATEGORIES.keys())

RESISTANCE_ATTRIBUTES = ("Resolve", "Stamina", "Composure")

SKILL_CATEGORIES = {
    "Mental": (
        "Academics",
        "Computer",
        "Crafts",
        "Investigation",
        "Medicine",
        "Occult",
        "Politics",
        "Science",
    ),
    "Physical": (
        "Athletics",
        "Brawl",
        "Drive",
        "Firearms",
        "Larceny",
        "Stealth",
        "Survival",
        "Weaponry",
    ),
    "Social": (
        "Animal Ken",
        "Empathy",
        "Expression",
        "Intimidation",
        "Persuasion",
        "Socialize",
        "Streetwise",
        "Subterfuge",
    ),
}

SKILLS = flat_values(SKILL_CATEGORIES)

VIRTUES = [
    "Patient",
    "Loving",
    "Ambitious",
    "Generous",
    "Just",
    "Tolerant",
    "Hopeful",
    "Courageous",
    "Confident",
]

VICES = [
    "Hateful",
    "Cruel",
    "Greedy",
    "Lustful",
    "Cowardly",
    "Arrogant",
    "Gluttonous",
    "Deceitful",
    "Reckless",
]

COD_MERIT_DOTS = {
    "Anonymity": (1, 2, 3, 4, 5),
    "Fame": (1, 2, 3),
    "Barfly": (2,),
    "Alternate Identity": (1, 2, 3),
    "Small-Framed": (2,),
    "Giant": (3,),
    "Area of Expertise": (1,),
    "Common Sense": (3,),
    "Eye for the Strange": (2,),
    "Danger Sense": (2,),
    "Direction Sense": (1,),
    "Eidetic Memory": (2,),
    "Encyclopedic Knowledge": (2,),
    "Fast Reflexes": (1, 2, 3),
    "Good Time Management": (1,),
    "Holistic Awareness": (1,),
    "Indomitable": (2,),
    "Language": (1,),
    "Library": (1, 2, 3),
    "Meditative Mind": (1, 2, 3),
    "Multilingual": (1,),
    "Tolerance for Biology": (2,),
    "Trained Observer": (1, 3),
    "Crack Driver": (2,),
    "Demolisher": (1, 2, 3),
    "Double Jointed": (2,),
    "Fleet of Foot": (1, 2, 3),
    "Hardy": (1, 2, 3),
    "Iron Stamina": (1, 2, 3),
    "Parkour": (1, 2, 3, 4, 5),
    "Allies": (1, 2, 3, 4, 5),
    "Fast-Talking": (1, 2, 3, 4, 5),
    "Fixer": (2,),
    "Hobbyist Clique": (2,),
    "Inspiring": (3,),
    "Iron Will": (2,),
    "Mentor": (1, 2, 3, 4, 5),
    "Mystery Cult Initiation": (1, 2, 3, 4, 5),
    "Resources": (1, 2, 3, 4, 5),
    "Pusher": (1,),
    "Retainer": (1, 2, 3, 4, 5),
    "Safe Place": (1, 2, 3, 4, 5),
    "Status": (1, 2, 3, 4, 5),
    "Staff": (1, 2, 3, 4, 5),
    "Striking Looks": (1, 2),
    "Sympathetic": (2,),
    "Taste": (1,),
    "True Friend": (3,),
    "Untouchable": (1,),
}

COD_MERITS = list(COD_MERIT_DOTS.keys())

PROFESSION_SKILLS = {
    "Academic": ("Academics", "Science"),
    "Artist": ("Crafts", "Expression"),
    "Athlete": ("Athletics", "Medicine"),
    "Cop": ("Streetwise", "Firearms"),
    "Criminal": ("Larceny", "Streetwise"),
    "Detective": ("Empathy", "Investigation"),
    "Doctor": ("Empathy", "Medicine"),
    "Engineer": ("Crafts", "Science"),
    "Hacker": ("Computer", "Science"),
    "Hit Man": ("Firearms", "Stealth"),
    "Journalist": ("Expression", "Investigation"),
    "Laborer": ("Athletics", "Crafts"),
    "Occultist": ("Investigation", "Occult"),
    "Politician": ("Politics", "Subterfuge"),
    "Religious Leader": ("Academics", "Occult"),
    "Scientist": ("Investigation", "Science"),
    "Socialite": ("Politics", "Socialize"),
    "Stuntman": ("Athletics", "Drive"),
    "Survivalist": ("Animal Ken", "Survival"),
    "Soldier": ("Firearms", "Survival"),
    "Technician": ("Crafts", "Investigation"),
    "Thug": ("Brawl", "Intimidation"),
    "Vagrant": ("Streetwise", "Survival"),
}

PROFESSION_ATTRIBUTES = {
    "Academic": ("Intelligence",),
    "Artist": ("Dexterity",),
    "Athlete": ("Stamina",),
    "Cop": ("Wits",),
    "Criminal": ("Manipulation",),
    "Detective": ("Wits",),
    "Doctor": ("Intelligence",),
    "Engineer": ("Dexterity",),
    "Hacker": ("Intelligence",),
    "Hit Man": ("Dexterity",),
    "Journalist": ("Composure",),
    "Laborer": ("Stamina",),
    "Occultist": ("Composure",),
    "Politician": ("Manipulation",),
    "Religious Leader": ("Manipulation",),
    "Scientist": ("Intelligence",),
    "Socialite": ("Presence",),
    "Stuntman": ("Strength",),
    "Survivalist": ("Wits",),
    "Soldier": ("Resolve",),
    "Technician": ("Composure",),
    "Thug": ("Strength",),
    "Vagrant": ("Wits",),
}

PROFESSIONS = list(PROFESSION_SKILLS.keys())

PATH_REAGENT_ARCANA = {
    "Acanthus": ("Fate", "Time"),
    "Mastigos": ("Mind", "Space"),
    "Moros": ("Death", "Matter"),
    "Obrimos": ("Prime", "Forces"),
    "Thyrsus": ("Spirit", "Life"),
}

PATH_INFERIOR_ARCANUM = {
    "Acanthus": "Forces",
    "Mastigos": "Matter",
    "Moros": "Spirit",
    "Obrimos": "Death",
    "Thyrsus": "Mind",
}

ARCANA = flat_values(PATH_REAGENT_ARCANA)

PATHS = list(PATH_REAGENT_ARCANA.keys())

ORDER_CHANCE = {
    "Adamantine Arrow": 8,
    "The Mysterium": 8,
    "The Silver Ladder": 6,
    "Guardians of the Veil": 4,
    "The Free Council": 20,
    "Seers of the Throne": 10,
    "Apostate": 4,
    "Nameless": 5,
    "Scelesti": 1,
    "Tremere Lich": 1,
}

FACTIONS = list(ORDER_CHANCE.keys())

MTAW_MERIT_DOTS = {
    "Adamant Hand": (2,),
    "Artifact": (3, 4, 5),
    "Astral Adept": (3,),
    "Cabal Theme": (1,),
    "Concilium Status": (1, 2, 3, 4, 5),
    "Order Status": (1, 2, 3, 4, 5),
}


def shuffled(items) -> list:
    return random.sample(items, k=len(items))


def split(dots: int, traits: int, limit: int = 5) -> list:
    assert dots < traits * limit
    result = [0] * traits
    while sum(result) < dots:
        index = random.randint(0, traits - 1)
        if result[index] < limit:
            result[index] += 1
    return result


def assign(dots: int, traits, limit: int = 5) -> dict:
    values = split(dots, len(traits), limit)
    return dict(zip(traits, values))


def remove_zeroes(char: dict) -> dict:
    return {k: v for k, v in char.items() if v}


def reassign_dense(
    original: dict,
    density: int = 5,
    base: int = 0,
    limit: int = 5,
    protect: tuple = None,
) -> dict:
    result = dict(original)
    keys = list(result.keys())
    for _ in range(density):
        from_key = random.choice(keys)
        to_key = random.choice(keys)
        if protect and from_key in protect:
            continue
        if result[from_key] == 1 and limit > result[to_key] > base:
            if random.randint(0, result[to_key] * 2) >= 5:
                continue
            result[from_key] -= 1
            result[to_key] += 1
    return remove_zeroes(result)


fake = Faker()


def split_category(dot_sets: tuple, source: dict, base: int = 0, limit: int = 5):
    results = {}
    for category, dots in zip(shuffled(CATEGORIES), dot_sets):
        values = assign(dots, source[category], limit=(limit - base))
        for trait, value in values.items():
            results[trait] = value + base
    return results


def base_attributes(dot_sets=(5, 4, 3)) -> dict:
    return split_category(dot_sets, source=ATTRIBUTE_CATEGORIES, base=1)


def base_skills(dot_sets=(11, 7, 4)) -> dict:
    return split_category(dot_sets, source=SKILL_CATEGORIES)


def base_merits(dots: int = 7) -> dict:
    results = {}
    while (total := sum(results.values())) < dots:
        merit = random.choice(COD_MERITS)
        if merit not in results:
            cost = random.choice(COD_MERIT_DOTS[merit])
            if total + cost <= dots:
                results[merit] = cost
    return results


def base_arcana(path, dots: int = 6, limit: int = 3, loops: int = 10):
    reagents = PATH_REAGENT_ARCANA[path]
    arcana = {arcanum: 1 for arcanum in reagents}
    arcana[random.choice(reagents)] += 1
    while sum(arcana.values()) < dots:
        arcanum = random.choice(ARCANA)
        if arcanum == PATH_INFERIOR_ARCANUM[path]:
            continue
        if arcanum not in arcana:
            arcana[arcanum] = 1
        elif arcana[arcanum] < limit:
            arcana[arcanum] += 1
    return reassign_dense(arcana, density=loops, limit=limit, protect=reagents)


def add_trait(traits: dict, trait: str, dots: int = 1, limit: int = 5) -> dict:
    traits = dict(traits)
    if trait not in traits:
        traits[trait] = dots
    elif traits[trait] + dots <= limit:
        traits[trait] += dots
    return traits


def weighted_choice(options: dict) -> str:
    total = sum(options.values())
    target = random.randint(0, total)
    accumulated = 0
    for key, value in options.items():
        accumulated += value
        if accumulated >= target:
            return key


def push_trait(traits: dict, trait: str, dots: int = 1, limit: int = 5) -> dict:
    result = dict(traits)
    while True:
        from_trait = random.choice(list(traits.keys()))
        if from_trait == trait or traits[from_trait] < 1:
            continue
        result[from_trait] -= 1
        return add_trait(result, trait, dots, limit)


def reassign_profession(char: dict):
    profession = char["Profession"]
    profession_attributes = PROFESSION_ATTRIBUTES[profession]
    profession_skills = PROFESSION_SKILLS[profession]


def base_cod() -> dict:
    char = {
        "Name": fake.name(),
        "Attributes": base_attributes(),
        "Skills": base_skills(),
        "Virtue": random.choice(VIRTUES),
        "Vice": random.choice(VICES),
        "Merits": base_merits(),
        "Color": fake.safe_color_name().title(),
        "Profession": random.choice(PROFESSIONS),
        "Integrity": 7,
    }
    # char["Attributes"] = push_trait(char["Attributes"], char["Profession"])
    return char


def cod_spend_exp(char, exp):
    char = dict(char)
    return char


class DisplayFormat(Enum):
    yaml = "yaml"
    json = "json"


display_format = DisplayFormat.yaml
display_indent = 4


def display(char: dict):
    if display_format == "json":
        print(json.dumps(char, indent=4, sort_keys=False))
    elif display_format == "yaml":
        print(yaml.dump(char, indent=4, sort_keys=False))


app = typer.Typer()


@app.callback()
def app_callback(format: str = "yaml", indent: int = 2):
    global display_format, display_indent
    display_format = format
    display_indent = indent


@app.command()
def sleeper(exp: int = 0) -> dict:
    """Generate a random CoD Sleeper character."""

    assert exp >= 0
    char = base_cod()
    if exp:
        char = cod_spend_exp(char, exp)
    char["Skills"] = reassign_dense(char["Skills"], density=12)
    display(char)


@app.command()
def awakened() -> dict:
    """Generate a random CoD Awakened character."""

    resist = random.choice(RESISTANCE_ATTRIBUTES)
    char = base_cod()

    char["Attributes"] = add_trait(char["Attributes"], resist)
    char["Skills"] = push_trait(char["Skills"], "Occult")
    char["Skills"] = reassign_dense(char["Skills"], density=30, protect="Occult")
    char["Path"] = path = random.choice(PATHS)
    char["Order"] = weighted_choice(ORDER_CHANCE)
    char["Gnosis"] = 1
    char["Arcana"] = base_arcana(path)
    char["Wisdom"] = 7
    if "Integrity" in char:
        del char["Integrity"]
    display(char)


if __name__ == "__main__":
    app()
