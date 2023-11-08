from django.test import TestCase, Client, RequestFactory
from django.urls import resolve
from django.http import HttpResponse
from .views import top, snippet_new, snippet_edit, snippet_detail
from .models import Snippet
from django.contrib.auth import get_user_model

    
class TopPagaeTest(TestCase):
  def test_top_page_retruns_200_and_expected_title(self):
    response = self.client.get('/')
    self.assertContains(response, "Djangoスニペット", status_code=200)
    
  def test_top_uses_expected_template(self):
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'top.html')
  
    
#   def test_top_returns_expected_content(self):
#     request = HttpResponse()
#     response = top(request)
#     self.assertEqual(response.content, b"hello world")

# class TopPageTest(TestCase):
#   def test_top_returns_200(self):
#     response = self.client.get('/')
#     self.assertEqual(response.status_code, 200)
    
#   def test_top_returns_expected_content(self):
#     response = self.client.get('/')
#     self.assertEqual(response.content, b"hello world")

# class TopPageTest(TestCase):
#   def test_top_returns_200_and_expected_title(self):
#     response = self.client.get('/')
#     self.assertContains(response, "Django スニペット", status_code=200)
    
#   def test_top_returns_expected_template(self):
#     response = self.client.get('/')
#     self.assertTemplateUsed(response, "top.html")
    
UserModel = get_user_model()
class TopPageRenderSnippetTest(TestCase):
  def setUp(self):
    self.user = UserModel.objects.create(
      username = 'test_user',
      email = 'test@example.com',
      password = 'top_secret_pass0001',
    )
    self.snippet = Snippet.objects.create(
      title = 'title1',
      code = 'print(hello)',
      description = 'description1',
      created_by = self.user,
    )
    def test_should_retrun_snippet_title(self):
      request = RequestFactory().get("/")
      request.user = self.user
      response = top(request)
      self.assertContains(response, self.snippet.title)
      
    def test_should_return_username(self):
      request = RequestFactory().get("/")
      request.user = self.user
      response = top(request)
      self.assertContains(response, self.user.username)

class SnippetDetailTest(TestCase):
  def setUp(self):
    self.user = UserModel.objects.create(
      username = 'test_user',
      email = 'test@example.com',
      password = 'secret',
    )
    self.snippet = Snippet.objects.create(
      title = 'タイトル',
      code = 'コード',
      description = '練習',
      created_by = self.user,
    )
    def test_should_use_expected_template(self):
      response = self.client.get('/snippets/%s/' % self.snippet.id)
      self.assertTemplateUsed(response, 'snippet_detail.html')
      
    def test_top_page_returns_200_and_expected_heading(self):
      response = self.client.get('/snippets/%s/' % self.snippet.id)
      self.assertContains(response, self.snippet.title, status_code = 200)

class CreateSnippetTest(TestCase):
  def setUp(self):
    self.user = UserModel.objects.create(
      username = 'test_user',
      email = 'test_user@example.com',
      password = 'secret',
    )
    self.client.force_login(self.user)
    
    def test_render_creation_form(self):
      response = self.client.get('/snippets/new/')
      self.assertContains(response, 'スニペット登録', status_code=200)
    def test_create_snippet(self):
      data = {'title': 'タイトル', 'code': 'コード', 'description': '解説'}
      self.client.post('/snippets/new/', data)
      snippet = Snippet.objects.get(title = 'タイトル')
      self.assertEqual('コード', snippet.code)
      self.assertEqual('解説', snippet.description)
      
# class CreateSnippetTest(TestCase):
#   def test_should_resolve_snippet(self):
#     found = resolve('new/')
#     self.assertEqual(snippet_new, found.func)
    
# class SnippetDetailTest(TestCase):
#   def test_should_resolve_snippet(self):
#     found = resolve('1/')
#     self.assertEqual(snippet_detail, found.func)
    
# class EditSnippetTest(TestCase):
#   def test_should_resolve_snippet(self):
#     found = resolve('1/edit/')
#     self.assertEqual(snippet_edit, found.func)