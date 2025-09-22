from playwright.sync_api import  expect

def test_empty_courses_list_new(chromium_page_with_state):

        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        #Заголовок “Courses” – наличие и текст.
        courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text('Courses')

        #Иконка пустого списка – наличие/видимость.
        empty_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_icon).to_be_visible()

        #Заголовок пустого блока “There is no results” – наличие и текст.
        no_results = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(no_results).to_be_visible()
        expect(no_results).to_have_text('There is no results')

        #Описание пустого блока “Results from the load test pipeline will be displayed here” – наличие и текст.
        description_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(description_text).to_be_visible()
        expect(description_text).to_have_text('Results from the load test pipeline will be displayed here')

        #page.wait_for_timeout(5000)