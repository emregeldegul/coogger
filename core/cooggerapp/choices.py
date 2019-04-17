LANGUAGES = [
        "english",
        "korean",
        "spanish",
        "turkish",
        "chinese",
        "arabic",
        "french",
        "indonesian",
        "korean",
        "polish",
        "portuguese",
        "german",
        "italian",
        "japanese",
        "romanian",
        "russian",
        "vietnamese ",
        "arabic",
        "azerbaijani",
]
FOLLOW = [
        "github",
        "linkedin",
        "instagram",
        "facebook",
        "youtube",
        "web site",
]
REPORTS = [
    "Fraud or Plagiarism",
    "Hate Speech or Internet Trolling",
    "Intentional miss-categorized content or Spam",
    "This content is not tutorial content",
    "Wrong list name",
    "I think this content should not be at coogger",
]
STATUS_CHAICES = [
    "shared",
    "rejected",
    "approved",
]
def make_choices(choice):
    from django.utils.text import slugify
    slugs = []
    for cho in choice:
        cho = str(cho).lower()
        slugs.append((slugify(cho),cho))
    return slugs
