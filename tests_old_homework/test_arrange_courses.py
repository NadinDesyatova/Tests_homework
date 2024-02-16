import pytest

from tests_old_homework.old_homework.arrange_courses import arrange_courses


class TestArrangeCourses:

    @pytest.mark.parametrize(
        "courses,durations,expected_result", (
            [
                ["Java-разработчик с нуля",
                 "Fullstack-разработчик на Python",
                 "Python-разработчик с нуля",
                 "Frontend-разработчик с нуля"],
                [14, 20, 12, 20],
                ["Python-разработчик с нуля - 12 месяцев",
                 "Java-разработчик с нуля - 14 месяцев",
                 "Fullstack-разработчик на Python - 20 месяцев",
                 "Frontend-разработчик с нуля - 20 месяцев"]
            ],
            [
                ["Java-разработчик с нуля",
                 "Fullstack-разработчик на Python",
                 "Python-разработчик с нуля",
                 "Frontend-разработчик с нуля"],
                [14.2, "20 месяцев", 12, 20],
                "Длительность курса указана некорректно, длительность должна быть в виде целого числа"
            ],
            [
                ["Java-разработчик с нуля",
                 "Fullstack-разработчик на Python",
                 "Python-разработчик с нуля",
                 "Frontend-разработчик с нуля"],
                [14, 20, 12],
                "Длины списка курсов и списка длительности курсов должны совпадать."
            ]
        )
    )
    def test_arrange_courses(self, courses, durations, expected_result):
        result = arrange_courses(courses, durations)

        assert result == expected_result, f"Неверный результат: {result}"


if __name__ == '__main__':
    pytest.main()