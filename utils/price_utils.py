import re


class PriceUtils:
    compiled_pattern = re.compile(r'(\d{1,3}(?:[,.]\d{3})*(?:[,.]\d{1,2})?(?:\s*'
                                  r'(?:руб|[a-zA-Z]{1,5}|[$€£¥₽]))|\b(?:Бесплатно|Free|Gratis)\b)')

    @staticmethod
    def extract_price(text):
        matches = PriceUtils.compiled_pattern.findall(text.replace('\n', ' '))

        matches = [m for m in matches if m.strip()]
        if matches:
            num_str = matches[-1].replace(' ', '').replace(',', '.')
            try:
                return float(num_str)
            except ValueError:
                pass
        if any(word in text for word in ("Бесплатно", "Free", "Gratis")):
            return 0.0
        return 0.0

    @staticmethod
    def parse_prices(prices):
        return [PriceUtils.extract_price(price) for price in prices]
