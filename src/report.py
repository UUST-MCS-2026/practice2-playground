"""Формирование отчёта."""


def build_report(title):
    lines = []
    lines.append("=" * 40)
    lines.append(title)
    lines.append("=" * 40)
    return "\n".join(lines)
