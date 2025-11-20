from selenium.webdriver.support import expected_conditions as EC, wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from selenium.webdriver.support.wait import WebDriverWait


class FillForm(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.base_url = "https://www.google.com/"
		self.verificationErrors = []
		self.accept_next_alert = True

	def scroll_into_view(self, driver, element):
		driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

	def safe_click(self, driver, locator, by="xpath"):
		if by == "id":
			element = driver.find_element(By.ID, locator)
		elif by == "xpath":
			element = driver.find_element(By.XPATH, locator)
		elif by == "link_text":
			element = driver.find_element(By.LINK_TEXT, locator)
		else:
			raise ValueError("Unsupported locator type")

		self.scroll_into_view(driver, element)
		element.click()
		return element

	def safe_type(self, driver, locator, text, by="id"):
		if by == "id":
			element = driver.find_element(By.ID, locator)
		elif by == "xpath":
			element = driver.find_element(By.XPATH, locator)
		else:
			raise ValueError("Unsupported locator type")

		self.scroll_into_view(driver, element)
		element.clear()
		element.send_keys(text)
		return element

	def safe_select(self, driver, locator, text):
		element = driver.find_element(By.ID, locator)
		self.scroll_into_view(driver, element)
		Select(element).select_by_visible_text(text)
		return element


	def test_fill_form(self):
		driver = self.driver
		self.safe_click(driver, "//div[@id='e00w65']/div/input[2]", by="xpath")
		self.safe_click(driver, "(.//*[normalize-space(text()) and normalize-space(.)='Sat'])[1]/following::span[15]",
		           by="xpath")

		self.safe_click(driver, "//div[@id='efrmq59']/div/div", by="xpath")
		self.safe_select(driver, "TimeSlot", "11 AM – 3 PM → Lunch")

		self.safe_click(driver, "//div[@id='e21hifj']/div/div", by="xpath")
		self.safe_select(driver, "wasTheSignageOutsideTheStoreCleanAndWellLitInTheEvening", "Yes")

		self.safe_click(driver, "//div[@id='epv20z']/div/div/div", by="xpath")
		self.safe_click(driver, "browse", by="link_text")

		self.safe_type(driver, "signageRemarks", "jkshds mksjdsl mksdklnsd")
		self.safe_select(driver, "wereTheDominosDeliveryVehiclesParkedCorrectlyWereTheyCleanAndWellMaintained", "No")

		self.safe_click(driver, "browse", by="link_text")
		self.safe_type(driver, "vehiclesRemarks", "jskjhd mskjhdkjsd klsjdkls")

		self.safe_select(driver, "wasStandyBannerPlacedAndVisibleInsideTheStoreAsPerVos", "NA")
		self.safe_type(driver, "insideBannerRemarks", "djfks mskdjhks skjhdks nkjsd")

		self.safe_click(driver, "e70d9du", by="id")
		self.safe_select(driver, "wasPosterStandyBannerVisibleOutsideTheStoreAsPerVos", "Yes")
		self.safe_type(driver, "outsideBannerRemarks", "sjhds sjkhds mshi skbdijs kjshds mkjsds")

		self.safe_select(driver, "wasTheTemperatureInsideTheRestaurantsDiningAreaAdequatelyMaintainedComfortableAsPerTheWeather",
		            "NA")
		self.safe_type(driver, "diningAreaRemarks", "djhfs sjhdjks ksjhd sdjshd sjdhs")

		self.safe_select(driver, "customerAreaFurnitureWereTablesChairsSofaTilesWallSealingWellMaintainedNoDamageWearTear", "No")
		self.safe_type(driver, "customerAreaFurnitureRemarks", "jshds nsjbhds djhsd sndjhshjdbs sjhds")

		self.safe_select(driver, "wasTheDigitalMenuBoardDmbWorkingProperly", "Yes")
		self.safe_type(driver, "dmbRemarks", "jsdhs sjhds nsjhds ndsjhdskbds")

		self.safe_select(driver, "wasTheNoBillItsOurTreatBoardAvailableVisibleAtNearOrderingCounterOrNot", "NA")
		self.safe_type(driver, "boardRemarks", "sjdhsn sjhdjsk sjdhjsdjsk sjhdjsd")

		self.safe_select(driver, "wasTheOrderDisplayScreenAvailableAndWasItDisplayingOrdersReadyToEat", "No")
		self.safe_type(driver, "orderDisplayScreenRemarks", "dshfsbv snbjdjsd jsbds djsbdjsd")

		self.safe_select(driver, "wasTheFloorNeatAndClean", "Yes")
		self.safe_type(driver, "floorNeatAndCleanRemarks", "djhsjhd sjhdjhs sjbhdjshb jsdjhkshd")

		self.safe_select(driver, "wasTheWashroomNeatAndClean", "No")
		self.safe_type(driver, "washroomNeatAndCleanRemarks", "shjdsjhg sjdhjhs jhsdjhs njhsjhgds")

		self.safe_select(driver, "wasStaffFollowingTheDressCode", "Yes")
		self.safe_type(driver, "staffDressCodeRemarks", "sjbhdsh nsjkhdskhj skjdjs skjdhksd")

		self.safe_select(driver, "wasStaffWearingAdequateGearHairNetCaps", "No")
		self.safe_type(driver, "staffRemarks", "shjbdjhs sjbhdjhsbdm jbshdb")

		self.safe_select(driver, "didTheStaffAcknowledgeOrGreetTheCustomer", "No")
		self.safe_type(driver, "greetTheCustomerRemarks", "sdjbsjhd sjhdhs")

		self.safe_select(driver, "wasTheDrinkingWaterAvailableInsideTheStoreIfNotDidStaffProvideWaterUponAsking", "Yes")
		self.safe_type(driver, "drinkingWaterRemarks", "sdjhbsh sjbdjhs sjbdjhshbds")

		self.safe_select(driver, "wasTheStaffCourteousAndPoliteWithTheCustomer", "Yes")
		self.safe_type(driver, "staffCourteousAndPoliteRemarks", "sjhdjshd nsjhdjhs sjdjbhs")

		self.safe_select(driver, "wasStaffObservedCrossTalkingOrSpeakingOnThePhoneWhileTakingOrders", "Yes")
		self.safe_type(driver, "crossTalkingRemarks", "sjhdshg sjhbdjhs nsjhbdjbs sjhdjbs")

		self.safe_select(driver, "wasStaffAvailableAtAllOrderCountersInCaseOfHighQueueAtTheStore", "No")
		self.safe_type(driver, "staffAtOrderCounterRemarks", "sdhjshg sjhbdjs sjhdjhgs sjhdjgs njhsgdjhs")

		self.safe_select(driver, "didStaffShareTheOngoingOffersNewLaunchesEtcAndTryToUpsellCrossSell", "NA")
		self.safe_type(driver, "ongoingOffersRemarks", "shjdgs skjhsajh nsdiuhas nsdaagdiugak aiuhdak")

		self.safe_select(driver, "didYouReceiveAnInvoiceOnSms", "Yes")
		self.safe_type(driver, "invoiceRemarks", "shjds sdjhsjhkd sdgjksm dsdksjd sjdgjskd")

		self.safe_select(driver, "didStaffCommunicateTheFoodServingTime", "Yes")
		self.safe_type(driver, "foodServingTimeRemarks", "sjbhdsj sjbhdjs djkshdjh")

		self.safe_select(driver, "didYouReceiveYourPizzaBoxWithSlipAttachedToIt", "No")
		self.safe_type(driver, "orderWithSlipRemarks", "sjbdsjbh sjhdjhs nsjbhdgs bnsbdjsb desjhbvdjhs")

		self.safe_select(driver, "wasTheFoodServedHotCaptureTheProductName", "NA")
		self.safe_type(driver, "orderWithProductNameRemarks", "sbhjdjs sjhdsi sjhdsihjd sjhdhjsbd sihudjsk")

		self.safe_select(driver, "didYouFindAdequateToppingsCheeseEtcOnYourPizza", "Yes")
		self.safe_type(driver, "orderInsideRemarks", "sjdhgs sjkdjiak akijda kabdkjaea mdjkb")

		self.safe_select(driver, "didYouLikeTheAppearanceOfTheProduct", "Yes")
		self.safe_type(driver, "appearanceOfTheProductRemarks", "skdjhsjgdasjbh sjkhdfkjsjdbs ihusidhskj")

		self.safe_select(driver, "wasTheProductBakedOrCookedProperly", "Yes")
		self.safe_type(driver, "productBakedRemarks", "ajkbsdjhgsjk skjhdjhks kjskjhdhksdhj")

		self.safe_select(driver, "didYouLikeTheTasteOfTheFoodIfNotWhatWasTheProblem", "No")
		self.safe_type(driver, "tasteOfTheFoodRemarks", "skjdsjb nsjhfdjshdks nsjbdjhshdjs jsjkdhs njsjdhshd sjhdsg")

		self.safe_type(driver, "redAlert", "sjhbdjhgshjgd nsjhdhjsj skjdhskdksj sjdhgsjjdkhs nsjkdgjshdjks djhsjdhs")

		self.safe_click(driver, "submit", by="id")

	def is_element_present(self, how, what):
		try:
			self.driver.find_element(by=how, value=what)
		except NoSuchElementException as e:
			return False
		return True

	def is_alert_present(self):
		try:
			self.driver.switch_to_alert()
		except NoAlertPresentException as e:
			return False
		return True

	def close_alert_and_get_its_text(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally:
			self.accept_next_alert = True

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
	unittest.main()
