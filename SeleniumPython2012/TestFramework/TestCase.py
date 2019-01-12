from TestFramework.BaseTestCase            import BaseTestCase
from TestFramework.Constants               import TT_Constants
from TestFramework.pages.ProductPage       import ProductPage
from TestFramework.pages.FacebookLoginPage import FacebookLoginPage



class TestCase(BaseTestCase):

  def setUp(self):
      super(TestCase, self).setUp()
      productPageURL = TT_Constants['Base_URL']+"store/p1/Leatherback_Turtle_Picture.html"
      self.navigate_to_page(productPageURL)
      product_page_obj = ProductPage(self.driver)
      product_page_obj.click_share_on_facebook_button()
      action = FacebookLoginPage(self.driver, 
                                 TT_Constants['Facebook_Username'],
                                 TT_Constants['Facebook_Password']
      )
      action.login()
      

  def tearDown(self):
  	  super(TestCase, self).tearDown()
