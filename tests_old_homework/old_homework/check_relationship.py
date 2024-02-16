def check_relationship(courses, mentors, durations):
    if len(courses) == len(mentors) and len(durations) == len(courses):
        courses_list = []
        for course, mentor, duration in zip(courses, mentors, durations):
            if str(duration).isdigit():
                course_dict = {"title": course, "mentors": mentor, "duration": duration}
                courses_list.append(course_dict)
            else:

                return "Длительность курса указана некорректно, длительность должна быть в виде целого числа"

        duration_index = []
        mcount_index = []

        for index, course in enumerate(courses_list):
            duration_index.append([course['duration'], index])
            mcount_index.append([len(course['mentors']), index])

        duration_index.sort()
        mcount_index.sort()

        indexes_d = []
        indexes_m = []

        for item in duration_index:
            indexes_d.append(item[1])

        for item in mcount_index:
            indexes_m.append(item[1])

        return ["Связь есть", indexes_d, indexes_m] \
            if indexes_d == indexes_m \
            else ["Связи нет", indexes_d, indexes_m]

    return "Длины списка курсов, списка имён и списка длительности курсов должны совпадать."
