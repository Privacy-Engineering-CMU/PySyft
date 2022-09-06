# stdlib
from secrets import randbelow

left_name = [
    "admiring",
    "adoring",
    "affectionate",
    "agitated",
    "amazing",
    "angry",
    "awesome",
    "beautiful",
    "blissful",
    "bold",
    "boring",
    "brave",
    "busy",
    "charming",
    "clever",
    "cool",
    "compassionate",
    "competent",
    "condescending",
    "confident",
    "cranky",
    "crazy",
    "dazzling",
    "determined",
    "distracted",
    "dreamy",
    "eager",
    "ecstatic",
    "elastic",
    "elated",
    "elegant",
    "eloquent",
    "epic",
    "exciting",
    "fervent",
    "festive",
    "flamboyant",
    "focused",
    "friendly",
    "frosty",
    "funny",
    "gallant",
    "gifted",
    "goofy",
    "gracious",
    "great",
    "happy",
    "hardcore",
    "heuristic",
    "hopeful",
    "hungry",
    "infallible",
    "inspiring",
    "interesting",
    "intelligent",
    "jolly",
    "jovial",
    "keen",
    "kellis",
    "kind",
    "laughing",
    "loving",
    "lucid",
    "magical",
    "mystifying",
    "modest",
    "musing",
    "naughty",
    "nervous",
    "nice",
    "nifty",
    "nostalgic",
    "objective",
    "optimistic",
    "peaceful",
    "pedantic",
    "pensive",
    "practical",
    "priceless",
    "quirky",
    "quizzical",
    "recursing",
    "relaxed",
    "reverent",
    "romantic",
    "sad",
    "serene",
    "sharp",
    "silly",
    "sleepy",
    "stoic",
    "strange",
    "stupefied",
    "suspicious",
    "sweet",
    "tender",
    "thirsty",
    "trusting",
    "unruffled",
    "upbeat",
    "vibrant",
    "vigilant",
    "vigorous",
    "wizardly",
    "wonderful",
    "xenodochial",
    "youthful",
    "zealous",
    "zen",
]

right_name = [
    "altman",
    "bach",
    "bengios",
    "bostrom",
    "botvinick",
    "brockman",
    "chintala",
    "chollet",
    "chomsky",
    "dean",
    "dolgov",
    "eckersley",
    "fridman",
    "gardner",
    "goertzel",
    "goodfellow",
    "hassabis",
    "he",
    "hinton",
    "hochreiter",
    "hotz",
    "howard",
    "hutter",
    "isbell",
    "kaliouby",
    "karp",
    "karpathy",
    "kearns",
    "kellis",
    "knuth",
    "koller",
    "krizhevsky",
    "larochelle",
    "lattner",
    "lecun",
    "li",
    "lim",
    "littman",
    "malik",
    "mironov",
    "ng",
    "norvig",
    "olah",
    "pearl",
    "pesenti",
    "russell",
    "salakhutdinov",
    "schmidhuber",
    "silver",
    "smola",
    "song",
    "sophia",
    "sutskever",
    "thomas",
    "thrun",
    "trask",
    "vapnik",
    "vaswani",
    "vinyals",
    "winston",
    "wolf",
    "wolfram",
]


def random_name() -> str:
    left_i = randbelow(len(left_name) - 1)
    right_i = randbelow(len(right_name) - 1)
    return f"{left_name[left_i].capitalize()} {right_name[right_i].capitalize()}"
