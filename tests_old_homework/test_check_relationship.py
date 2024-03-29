import pytest

from tests_old_homework.old_homework.check_relationship import check_relationship


class TestCheckRelationship:

    @pytest.mark.parametrize(
        "courses,mentors,durations,expected_result", (
            [
                ["Java-разработчик с нуля",
                 "Fullstack-разработчик на Python",
                 "Python-разработчик с нуля",
                 "Frontend-разработчик с нуля"],
                [
                    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков",
                     "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев",
                     "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков",
                     "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен",
                     "Сергей Сердюк", "Павел Дерендяев"],
                    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов",
                     "Кирилл Табельский","Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев",
                     "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин",
                     "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
                    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский",
                     "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин",
                     "Максим Филипенко", "Елена Никитина","Азамат Искаков","Роман Гордиенко"],
                    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен",
                     "Александр Фитискин","Александр Шлейко", "Алена Батицкая", "Александр Беспоясов",
                     "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
                ],
                [14, 20, 12, 20],
                ["Связи нет", [2, 0, 1, 3], [2, 3, 1, 0]]
            ],
            [
                ["Java-разработчик с нуля",
                 "Fullstack-разработчик на Python",
                 "Python-разработчик с нуля",
                 "Frontend-разработчик с нуля"],
                [
                    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков",
                     "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев",
                     "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков",
                     "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен",
                     "Сергей Сердюк", "Павел Дерендяев"],
                    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов",
                     "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев",
                     "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин",
                     "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
                    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский",
                     "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин",
                     "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
                    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен",
                     "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов",
                     "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
                ],
                [14.2, "20 месяцев", 12, 20],
                "Длительность курса указана некорректно, длительность должна быть в виде целого числа"
            ],
            [
                ["Java-разработчик с нуля",
                 "Fullstack-разработчик на Python",
                 "Python-разработчик с нуля",
                 "Frontend-разработчик с нуля"],
                [
                    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков",
                     "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев",
                     "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков",
                     "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен",
                     "Сергей Сердюк", "Павел Дерендяев"],
                    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов",
                     "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев",
                     "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин",
                     "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
                    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский",
                     "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин",
                     "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"]
                ],
                [14, 20, 12, 20],
                "Длины списка курсов, списка имён и списка длительности курсов должны совпадать."
            ]
        )
    )
    def test_arrange_courses(self, courses, mentors, durations, expected_result):
        result = check_relationship(courses, mentors, durations)

        assert result == expected_result, f"Неверный результат: {result}"


if __name__ == '__main__':
    pytest.main()