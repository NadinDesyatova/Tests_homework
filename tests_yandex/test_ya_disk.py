import unittest
import pytest
import requests

from tests_yandex.data import token


class TestYaDiskAPI_1(unittest.TestCase):
    def setUp(self):
        self.base_url_ya_disk = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers = {"Authorization": token}

    def test_create_folder(self):
        folder_name = "NewFolder"
        params = {"path": f"{folder_name}"}
        response = requests.put(self.base_url_ya_disk,
                                params=params,
                                headers=self.headers)

        self.assertEqual(response.status_code, 201)

    def test_create_existing_folder(self):
        folder_name = "OldFolder"
        params = {'path': f'{folder_name}'}
        response = requests.put(self.base_url_ya_disk,
                                params=params,
                                headers=self.headers)

        self.assertEqual(response.status_code, 409)

    def test_create_folder_without_auth(self):
        folder_name = "NextFolder"
        params = {'path': f'{folder_name}'}
        response = requests.put(self.base_url_ya_disk,
                                params=params)

        self.assertEqual(response.status_code, 401)

    def test_create_folder_with_incorrect_data(self):
        folder_name = ""
        params = {'path': f'{folder_name}'}
        response = requests.put(self.base_url_ya_disk,
                                params=params,
                                headers=self.headers)

        self.assertEqual(response.status_code, 400)


class TestYaDiskAPI_2:
    base_url_ya_disk = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {"Authorization": token}

    def test_create_folder_without_auth(self):
        folder_name = "NextFolder"
        params = {'path': f'{folder_name}'}
        response = requests.put(self.base_url_ya_disk,
                                params=params)

        assert response.status_code == 401

    @pytest.mark.parametrize(
        "name_folder,expected_status", (
            ["NewFolder_pytest", 201],
            ["OldFolder", 409],
            ["", 400]
        )
    )
    def test_create_folder(self, name_folder, expected_status):
        params = {"path": f"{name_folder}"}
        response = requests.put(self.base_url_ya_disk,
                                params=params,
                                headers=self.headers)

        assert response.status_code == expected_status


if __name__ == "__main__":
    # unittest.main()
    pytest.main()