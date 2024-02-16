def arrange_courses(courses, durations):
    if len(courses) == len(durations):
        courses_list = []
        for course, duration in zip(courses, durations):
            if str(duration).isdigit():
                course_dict = {"title": course, "duration": duration}
                courses_list.append(course_dict)
            else:

                return "Длительность курса указана некорректно, длительность должна быть в виде целого числа"

        durations_dict = {}

        for id, course in enumerate(courses_list):
            key = course['duration']
            if key in durations_dict:
                durations_dict[key].append(id)
            else:
                durations_dict[key] = [id]

        durations_dict = dict(sorted(durations_dict.items()))

        durations_list = []

        for key, value in durations_dict.items():
            for id in value:
                durations_list.append(f'{courses_list[id]["title"]} - {key} месяцев')

        return durations_list

    return "Длины списка курсов и списка длительности курсов должны совпадать."
