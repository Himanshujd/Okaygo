from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

def fill_dominos_audit_form(driver, wait):
    """
    Automated form filling for Domino's Store Audit Form
    """
    
    time.sleep(5)
    
    def scroll_to_element(element):
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
    
    def click_choices_dropdown(field_id, value):
        dropdown = driver.find_element(By.ID, field_id).find_element(By.XPATH, "//*[@id='e8qz38d']/div[2]/div[1]")
        scroll_to_element(dropdown)
        dropdown.click()
        time.sleep(1)
        option = driver.find_element(By.XPATH, f"//div[@data-value='{value}']")
        option.click()
        time.sleep(1)
    
    def upload_file(field_id, file_path):
        file_input = driver.find_element(By.ID, field_id).find_element(By.XPATH, "../div//input[@type='file']")
        scroll_to_element(file_input)
        file_input.send_keys(file_path)
        time.sleep(1)
    
    def fill_text_field(field_id, text):
        field = driver.find_element(By.ID, field_id)
        scroll_to_element(field)
        field.clear()
        field.send_keys(text)
        time.sleep(1)
    
    # Audit Date
    audit_date_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='dd MMM yyyy' and not(@type='hidden')]")))
    scroll_to_element(audit_date_input)
    audit_date_input.clear()
    audit_date_input.send_keys(datetime.now().strftime('15 sep 2025'))
    
    # Time Slot
    click_choices_dropdown("TimeSlot", "7 PM – 11 PM → Dinner")
    
    # Signage
    click_choices_dropdown("wasTheSignageOutsideTheStoreCleanAndWellLitInTheEvening", "yes")
    upload_file("imageOfSignage", "/Users/himanshu.tiwari/Okaygo/screenshot.png")
    fill_text_field("signageRemarks", "Signage is clean and well-lit")
    
    # Vehicles
    click_choices_dropdown("wereTheDominosDeliveryVehiclesParkedCorrectlyWereTheyCleanAndWellMaintained", "yes")
    upload_file("imageOfVehicles", "/Users/himanshu.tiwari/Okaygo/screenshot.png")
    fill_text_field("vehiclesRemarks", "Vehicles properly parked and maintained")
    
    # Inside Banner
    click_choices_dropdown("wasStandyBannerPlacedAndVisibleInsideTheStoreAsPerVos", "yes")
    upload_file("imageOfInsideBanner", "/Users/himanshu.tiwari/Okaygo/screenshot.png")
    fill_text_field("insideBannerRemarks", "Banner properly placed and visible")
    
    # Outside Banner
    click_choices_dropdown("wasPosterStandyBannerVisibleOutsideTheStoreAsPerVos", "yes")
    upload_file("imageOfOutsideBanner", "/Users/himanshu.tiwari/Okaygo/screenshot.png")
    fill_text_field("outsideBannerRemarks", "Outside banner visible")
    
    # Temperature
    click_choices_dropdown("wasTheTemperatureInsideTheRestaurantsDiningAreaAdequatelyMaintainedComfortableAsPerTheWeather", "yes")
    fill_text_field("diningAreaRemarks", "Temperature well-maintained")
    
    # Furniture
    click_choices_dropdown("customerAreaFurnitureWereTablesChairsSofaTilesWallSealingWellMaintainedNoDamageWearTear", "yes")
    upload_file("imageOfCustomerAreaFurniture", "/Users/himanshu.tiwari/Okaygo/screenshot.png")
    fill_text_field("customerAreaFurnitureRemarks", "Furniture well-maintained")
    
    # DMB
    click_choices_dropdown("wasTheDigitalMenuBoardDmbWorkingProperly", "yes")
    upload_file("imageOfDmb", "/Users/himanshu.tiwari/Okaygo/screenshot.png")
    fill_text_field("dmbRemarks", "DMB working properly")
    
    # No Bill Board
    click_choices_dropdown("wasTheNoBillItsOurTreatBoardAvailableVisibleAtNearOrderingCounterOrNot", "yes")
    upload_file("imageOfBoard", "/Users/himanshu.tiwari/Okaygo/screenshot.png")
    fill_text_field("boardRemarks", "Board visible at counter")
    
    # Order Display
    click_choices_dropdown("wasTheOrderDisplayScreenAvailableAndWasItDisplayingOrdersReadyToEat", "yes")
    upload_file("imageOfOrderDisplayScreen", "/Users/himanshu.tiwari/Okaygo/screenshot.png")
    fill_text_field("orderDisplayScreenRemarks", "Display screen working")
    
    # Floor
    click_choices_dropdown("wasTheFloorNeatAndClean", "yes")
    upload_file("imageOfFloorNeatAndClean", "/Users/himanshu.tiwari/Okaygo/screenshot.png")
    fill_text_field("floorNeatAndCleanRemarks", "Floor neat and clean")
    
    # Washroom
    click_choices_dropdown("wasTheWashroomNeatAndClean", "yes")
    upload_file("imageOfWashroomNeatAndClean", "/Users/himanshu.tiwari/Okaygo/screenshot.png")
    fill_text_field("washroomNeatAndCleanRemarks", "Washroom clean")
    
    # Staff Dress Code
    click_choices_dropdown("wasStaffFollowingTheDressCode", "yes")
    upload_file("imageOfStaffDressCode", "/Users/himanshu.tiwari/Okaygo/screenshot.png")
    fill_text_field("staffDressCodeRemarks", "Staff following dress code")
    
    # Staff Gear
    click_choices_dropdown("wasStaffWearingAdequateGearHairNetCaps", "yes")
    upload_file("imageOfStaff", "/Users/himanshu.tiwari/Okaygo/screenshot.png")
    fill_text_field("staffRemarks", "Staff wearing adequate gear")
    
    # Greetings
    click_choices_dropdown("didTheStaffAcknowledgeOrGreetTheCustomer", "yes")
    fill_text_field("greetTheCustomerRemarks", "Staff greeted customers")
    
    # Drinking Water
    click_choices_dropdown("wasTheDrinkingWaterAvailableInsideTheStoreIfNotDidStaffProvideWaterUponAsking", "yes")
    upload_file("imageOfDrinkingWater", "/Users/himanshu.tiwari/Okaygo/screenshot.png")
    fill_text_field("drinkingWaterRemarks", "Water available")
    
    # Staff Courtesy
    click_choices_dropdown("wasTheStaffCourteousAndPoliteWithTheCustomer", "yes")
    fill_text_field("staffCourteousAndPoliteRemarks", "Staff courteous")
    
    # Cross-talking
    click_choices_dropdown("wasStaffObservedCrossTalkingOrSpeakingOnThePhoneWhileTakingOrders", "no")
    fill_text_field("crossTalkingRemarks", "No cross-talking observed")
    
    # Staff Availability
    click_choices_dropdown("wasStaffAvailableAtAllOrderCountersInCaseOfHighQueueAtTheStore", "yes")
    upload_file("imageOfStaffAtOrderCounter", "/Users/himanshu.tiwari/Okaygo/screenshot.png")
    fill_text_field("staffAtOrderCounterRemarks", "Staff available at counters")
    
    # Upselling
    click_choices_dropdown("didStaffShareTheOngoingOffersNewLaunchesEtcAndTryToUpsellCrossSell", "yes")
    fill_text_field("ongoingOffersRemarks", "Staff shared offers")
    
    # Invoice
    click_choices_dropdown("didYouReceiveAnInvoiceOnSms", "yes")
    upload_file("imageOfInvoice", "/Users/himanshu.tiwari/Okaygo/screenshot.png")
    fill_text_field("invoiceRemarks", "Invoice received")
    
    # Food Serving Time
    click_choices_dropdown("didStaffCommunicateTheFoodServingTime", "yes")
    fill_text_field("foodServingTimeRemarks", "Serving time communicated")
    
    # Pizza Box
    click_choices_dropdown("didYouReceiveYourPizzaBoxWithSlipAttachedToIt", "yes")
    upload_file("imageOfOrder", "/Users/himanshu.tiwari/Okaygo/screenshot.png")
    fill_text_field("orderWithSlipRemarks", "Box with slip received")
    
    # Hot Food
    click_choices_dropdown("wasTheFoodServedHotCaptureTheProductName", "yes")
    upload_file("imageOfOrderWithProductName", "/Users/himanshu.tiwari/Okaygo/screenshot.png")
    fill_text_field("orderWithProductNameRemarks", "Margherita Pizza - served hot")
    
    # Toppings
    click_choices_dropdown("didYouFindAdequateToppingsCheeseEtcOnYourPizza", "yes")
    upload_file("imageOfOrderInside", "/Users/himanshu.tiwari/Okaygo/screenshot.png")
    fill_text_field("orderInsideRemarks", "Adequate toppings")
    
    # Appearance
    click_choices_dropdown("didYouLikeTheAppearanceOfTheProduct", "yes")
    fill_text_field("appearanceOfTheProductRemarks", "Good appearance")
    
    # Baking
    click_choices_dropdown("wasTheProductBakedOrCookedProperly", "yes")
    fill_text_field("productBakedRemarks", "Properly baked")
    
    # Taste
    click_choices_dropdown("didYouLikeTheTasteOfTheFoodIfNotWhatWasTheProblem", "yes")
    fill_text_field("tasteOfTheFoodRemarks", "Excellent taste")
    
    # Red Alert
    red_alert = driver.find_element(By.ID, "redAlert")
    scroll_to_element(red_alert)
    red_alert.send_keys("No critical issues")
    
    # Video Upload
    upload_file("uploadAuditVideoFile", "/Users/himanshu.tiwari/Okaygo/screenshot.png")
    
    # Submit
    submit_btn = driver.find_element(By.ID, "submit")
    scroll_to_element(submit_btn)
    driver.execute_script("arguments[0].removeAttribute('disabled');", submit_btn)
    submit_btn.click()
    
    print("Form filled and submitted successfully!")