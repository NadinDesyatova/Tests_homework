def count_similar_names(courses, mentors):
    if len(courses) == len(mentors):
        courses_namesakes = []

        courses_list = [
            {"title": course, "mentors": course_mentors}
            for course, course_mentors
            in zip(courses, mentors)
        ]

        for course in courses_list:
            mentors_names = [name.split()[0] for name in course['mentors']]
            unique_names = sorted(list(set(mentors_names)))

            same_name_list = []
            for name_unique in unique_names:
                if mentors_names.count(name_unique) > 1:
                    for full_name in course['mentors']:
                        if name_unique in full_name:
                            same_name_list.append(full_name)

            if len(same_name_list) > 0:
                courses_namesakes.append(
                    f'На курсе {course["title"]} есть тёзки: {", ".join(sorted(same_name_list))}'
                )

        return courses_namesakes

    return "Длины списка курсов и списка имён должны совпадать."
