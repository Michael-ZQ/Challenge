from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Student


class StudentAPITests(APITestCase):
    def setUp(self):
        self.student_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'data_of_birth': '1990-01-01',
            'grade': 10,
            'phone': '1234567890',
            'email': 'johndoe@example.com'
        }
        self.student = Student.objects.create(**self.student_data)
        self.url = reverse('student-list')

    def test_get_all_students(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_student(self):
        response = self.client.get(reverse('student-detail', args=[self.student.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.student.first_name)

    def test_create_student(self):
        new_student_data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'data_of_birth': '1995-05-05',
            'grade': 12,
            'phone': '9876543210',
            'email': 'janesmith@example.com'
        }
        response = self.client.post(self.url, data=new_student_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 2)

    def test_update_student(self):
        updated_student_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'data_of_birth': '1990-01-01',
            'grade': 11,
            'phone': '1234567890',
            'email': 'johndoe@example.com'
        }
        response = self.client.put(reverse('student-detail', args=[self.student.id]), data=updated_student_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['grade'], updated_student_data['grade'])

    def test_delete_student(self):
        response = self.client.delete(reverse('student-detail', args=[self.student.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Student.objects.count(), 0)
