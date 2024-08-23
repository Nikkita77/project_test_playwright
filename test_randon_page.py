
import allure
import pytest


from integer_page import RandomIntegerGeneratorPage


@allure.suite('Проверки виджета генерации рандомных чисел')
class TestGenerateNumbers:

    @allure.title('Проверить генерацию числа от 1 до 100')
    def test_generate_number_1_to_100(self, playwright_setup):
        page = playwright_setup
        random_integer_generator_page = RandomIntegerGeneratorPage(page)

        random_integer_generator_page.open_random_integer_page()
        random_integer_generator_page.fill_fields(min_num="1", max_num="100")
        random_integer_generator_page.click_get_numbers_button()
        random_integer_generator_page.check_result_generate_number_1_to_100()

    @pytest.mark.flaky(reruns=3)
    @allure.title('Проверить генерацию числа от 1 до 1')
    def test_generate_number_1_to_1(self, playwright_setup):
        """
           Тест иногда будет падать, потому что проверка от 1 до 1 не возможна согласно заложенной логике.
           Максимальное значение порой автоматические меняется с 1 на 2
        """
        page = playwright_setup
        random_integer_generator_page = RandomIntegerGeneratorPage(page)

        random_integer_generator_page.open_random_integer_page()
        random_integer_generator_page.fill_fields(min_num="1", max_num="1")
        random_integer_generator_page.click_get_numbers_button()
        random_integer_generator_page.check_result_generate_number_1_to_1()

    @allure.title('Проверить генерацию числа от 23 до 13')
    def test_generate_number_23_to_13(self, playwright_setup):
        """
        Тест будет падать, потому что согласно заложенной логике значние ОТ должно быть меньше значения ДО.
        Логика второго поля автоматически вместо значения 13 меняет его на значение 24
        """
        page = playwright_setup
        random_integer_generator_page = RandomIntegerGeneratorPage(page)

        random_integer_generator_page.open_random_integer_page()
        random_integer_generator_page.fill_fields(min_num="23", max_num="13")
        random_integer_generator_page.click_get_numbers_button()
        random_integer_generator_page.check_result_generate_number_23_to_13()
