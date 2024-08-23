import allure
from playwright.sync_api import Page


class RandomIntegerGeneratorPage:

    PAGE_URL = "https://www.random.org/widgets/integers/iframe"

    GENERATE_NUM_FIELD = "input[name='num']"

    MIN_NUM_FIELD = "(//input[@type='number'])[1]"

    MAX_NUM_FIELD = "(//input[@type='number'])[2]"

    GENERATE_BUTTON = "//input[@value='Generate']"

    RESULT_GENERATOR_VALUE = "//span[@style='font-size:100%;font-weight:bold;']"

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открыть страницу Генератор случайных целых чисел")
    def open_random_integer_page(self):
        self.page.goto(RandomIntegerGeneratorPage.PAGE_URL)

    @allure.step("Заполнить поля генерации чисел")
    def fill_fields(self, min_num: str, max_num: str):
        self.page.click(self.MIN_NUM_FIELD)
        self.page.fill(self.MIN_NUM_FIELD, min_num)
        self.page.fill(self.MAX_NUM_FIELD, max_num)

    @allure.step('Нажать кнопку Получение чисел')
    def click_get_numbers_button(self):
        self.page.click(self.GENERATE_BUTTON)

    @allure.step("Проверить результат генерации от 1 до 100")
    def check_result_generate_number_1_to_100(self):
        result = self.page.locator(self.RESULT_GENERATOR_VALUE).inner_text()
        number = int(result)
        assert 1 <= number <= 100, f"Number {number} is not within the range 1 to 100"

    @allure.step("Проверить результат генерации от 1 до 1")
    def check_result_generate_number_1_to_1(self):
        result = self.page.locator(self.RESULT_GENERATOR_VALUE).inner_text()
        number = int(result)
        assert number == 1, f"Number {number} is not equal to 1"

    @allure.step("Проверить результат генерации от 23 до 13")
    def check_result_generate_number_23_to_13(self):
        min_val = self.page.locator(self.MIN_NUM_FIELD).text_content()
        max_val = self.page.locator(self.MAX_NUM_FIELD).text_content()
        assert min_val == '13', f"Min value did not update correctly, expected '13' but got {min_val}"
        assert max_val == '23', f"Max value did not update correctly, expected '23' but got {max_val}"
        result = self.page.locator(self.RESULT_GENERATOR_VALUE).inner_text()
        number = int(result)
        assert 13 <= number <= 23, f"Number {number} is not within the range 13 to 23"
