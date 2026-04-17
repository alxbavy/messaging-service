import re


def clean_string(value) -> str | None:
    if value is None:
        return None
    result = str(value).strip()
    return result or None


def normalize_phone(value) -> str | None:
    raw = clean_string(value)
    if not raw:
        return None

    digits = re.sub(r"\D", "", raw)
    if len(digits) == 11 and digits.startswith("8"):
        digits = "7" + digits[1:]
    if len(digits) == 10:
        digits = "7" + digits

    if len(digits) != 11 or not digits.startswith("7"):
        raise ValueError(f"Некорректный телефон: {value}")

    return f"+{digits}"


def normalize_email(value) -> str | None:
    raw = clean_string(value)
    if not raw:
        return None

    result = raw.lower()
    if "@" not in result:
        raise ValueError(f"Некорректный email: {value}")
    return result


def normalize_telegram(value) -> str | None:
    raw = clean_string(value)
    if not raw:
        return None

    raw = raw.replace("https://t.me/", "")
    raw = raw.replace("https://telegram.me/", "")
    raw = raw.lstrip("@").strip("/")

    return raw.lower() or None


def normalize_handle(value) -> str | None:
    raw = clean_string(value)
    if not raw:
        return None
    return raw.lower()