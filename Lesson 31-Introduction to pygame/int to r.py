class RomanConverter:
    ROMAN_MAPPING = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    def __init__(self, number: int):
        """Initializes the converter with a specific integer."""
        self.number = number

    def to_roman(self) -> str:
        """Converts the stored integer into a Roman numeral string."""
        if not isinstance(self.number, int) or self.number <= 0:
            raise ValueError(
                "Roman numerals only support positive integers greater than 0."
            )

        num = self.number
        roman_numeral = ""

        for value, symbol in self.ROMAN_MAPPING:
            while num >= value:
                roman_numeral += symbol
                num -= value

        return roman_numeral


if __name__ == "__main__":
    test_numbers = [3, 9, 58, 1994, 3999]

    print("Integer to Roman Numeral Conversion:")
    print("-" * 35)

    for num in test_numbers:
        converter = RomanConverter(num)
        print(f"Integer: {num:<6} -> Roman: {converter.to_roman()}")