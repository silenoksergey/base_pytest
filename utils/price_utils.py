import re


class PriceUtils:
    PRICE_PATTERN = (r'(\d{1,3}(?:[,.]\d{3})*(?:[,.]\d{1,2})?(?:\s*'
                     r'(?:руб|[a-zA-Z]{1,5}|[$€£¥₽]))|\b(?:Бесплатно|Free|Gratis)\b)')

    def extract_price(self, text):
        matches = re.findall(r'[\d\s]+[.,]?\d*', text.replace('\n', ' '))
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

    def parse_prices(self, prices):
        return [self.extract_price(price) for price in prices]

