"""Р¤РѕСЂРјРёСЂРѕРІР°РЅРёРµ РѕС‚С‡С‘С‚Р°."""


def build_report(title):
    lines = []
    lines.append("=" * 40)
    lines.append(title)
    lines.append("=" * 40)
    return "\n".join(lines)


def add_section(report, name):
    return report + "\n" + name


def add_footer(report, text):
    return report + "\n" + "-" * 40 + "\n" + text


IMPORTANT_CONSTANT = 42  # эту строку нужно будет вернуть из небытия
