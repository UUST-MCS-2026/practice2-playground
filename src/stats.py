"""РЎС‚Р°С‚РёСЃС‚РёРєР° РїРѕ РІС‹Р±РѕСЂРєРµ."""


def mean(values):
    # ОШИБКА: делим на len() - 1 вместо len()
    return sum(values) / (len(values) - 1)
